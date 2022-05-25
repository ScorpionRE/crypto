import base64
import binascii
import codecs
import linecache

import libnum
import owiener
import rsa
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2
import sympy


#dp，dq，c求m (RSA_CRT leaks)
# dp =6500795702216834621109042351193261530650043841056252930930949663358625016881832840728066026150264693076109354874099841380454881716097778307268116910582929
# dq =783472263673553449019532580386470672380574033551303889137911760438881683674556098098256795673512201963002175438762767516968043599582527539160811120550041
# def r_dpq(dp,dq):
#     invq = gmpy2.invert(q,p)
#     mp = pow(c,dp,p)
#     mq = pow(c,dq,q)
#     m = (((mp-mq)*invq) % p) * q + mq
#     m = hex(m)
#     print("m:"+ str(m))
#     print("n2s"+str(libnum.n2s(m)))
# r_dpq(dp,dq)

#n,dp,e求m dp泄露
from libnum import n2s


def dp_leak(dp,e,n):

    for i in range(1,e):
        if (dp * e - 1) % i == 0:
            p = gmpy2.mpz(((dp * e - 1) // i) + 1)
            if n % p == 0:
                q= n // p
                print(p)
                print(q)
                phi = gmpy2.mpz((p-1)*(q-1))
                d = gmpy2.invert(gmpy2.mpz(e),phi) % phi
                break



#共模攻击(使用相同的模数 N、不同的私钥时，加密同一明文消息时即存在共模攻击)
# e1 = 2303413961
# e2 = 2622163991
# c1 = 1754421169036191391717309256938035960912941109206872374826444526733030696056821731708193270151759843780894750696642659795452787547355043345348714129217723
# c2 = 1613454015951555289711148366977297613624544025937559371784736059448454437652633847111272619248126613500028992813732842041018588707201458398726700828844249
# n = 6807492006219935335233722232024809784434293293172317282814978688931711423939629682224374870233587969960713638310068784415474535033780772766171320461281579
# gcd,s,t = gmpy2.gcdext(e1,e2)
# if s < 0:
#     s = -s
#     c1 = gmpy2.invert(c1,n)
# if t < 0:
#     t = -t
#     c2 = gmpy2.invert(c2,n)
#
# M = gmpy2.powmod(c1,s,n)*gmpy2.powmod(c2,t,n) % n
# print("共模攻击" + str(M))
# m = hex(M)
# print(m)
# print(codecs.decode(m[2:],'hex'))
# m = m[2:]
# missing_padding = 4 - len(m) % 4
# if missing_padding:
#     m += '=' * missing_padding
# print(base64.b64decode(m))


# #多文件共模攻击，n相同，e不同

def multifile_come(filename1,filename2,n,e1,e2):
    with open(filename1,'rb') as f:
        c1 = gmpy2.mpz(f.read())
        print(c1)
    with open(filename2,'rb') as f:
        c2 = gmpy2.mpz(f.read())
        print(c2)
    gcd,s,t = gmpy2.gcdext(e1,e2)
    # c1 = libnum.s2n(c1)
    # c2 = libnum.s2n(c2)
    # print(c1)
    # print(c2)
    if s < 0:
        s = -s
        c1 = gmpy2.invert(c1,n)
    if t < 0:
        t = -t
        c2 = gmpy2.invert(c2,n)

    M = gmpy2.powmod(c1,s,n)*gmpy2.powmod(c2,t,n) % n
    # m = hex(M)
    # print(m)
    # print(codecs.decode(m[2:],'hex'))
    # m = m[2:]
    # m = codecs.decode(m[2:],'hex')
    # m = str(m).split("\\n")
    # # missing_padding = 4 - len(m) % 4
    # # if missing_padding:
    # #     m += '=' * missing_padding
    # for i in range(1,len(m)):
    #     print(m[i])
    #     missing_padding = 4 - len(m[i]) % 4
    #     if missing_padding:
    #         m[i] += '=' * missing_padding
    #     print(base64.b64decode(m[i]))
# #strip处理



# 小公钥指数攻击（一般e为3） 对K进行爆破，只要k满足 kn + C能够开e次方就可以得明文
def little_e(e,c,n):
    k = 0
    while 1:
        res = gmpy2.iroot(c + k * n, e)
        if res[1] == True:
            a = int(res[0])
            print(a)
            print(int(res[0]))

            print(libnum.n2s(int(res[0])))
            break
        k = k + 1


#多线程小公钥指数攻击
#def liitle_e_mulp(e,c,n):


#爆破，给出e的范围
def brute_e(c,d,n,p,q):
    phi = (p - 1) * (q - 1)
    for e in range(50000,70001):
        if gmpy2.gcd(e,phi) == 1:
                d = gmpy2.invert(e, phi)
                m = pow(c, d, n)
                flag = hex(m)[2:]
                #不是偶数就要加0？？？但是libnum不可用？？？
                if (len(str(flag)) % 2 == 1):
                    flag = '0' + flag
                print(codecs.decode(flag,'hex'))



#低解密指数广播攻击，多个n,c找n的公因数

# n1= p*q
# c1= 7395591129228876649030819616685821899204832684995757724924450812977470787822266387122334722132760470911599176362617225218345404468270014548817267727669872896838106451520392806497466576907063295603746660003188440170919490157250829308173310715318925771643105064882620746171266499859049038016902162599261409050907140823352990750298239508355767238575709803167676810456559665476121149766947851911064706646506705397091626648713684511780456955453552020460909638016134124590438425738826828694773960514221910109473941451471431637903182205738738109429736425025621308300895473186381826756650667842656050416299166317372707709596
#
# n2= p*127587319253436643569312142058559706815497211661083866592534217079310497260365307426095661281103710042392775453866174657404985539066741684196020137840472950102380232067786400322600902938984916355631714439668326671310160916766472897536055371474076089779472372913037040153356437528808922911484049460342088834871
# c2= 262739975753930281690942784321252339035906196846340713237510382364557685379543498765074448825799342194332681181129770046075018122033421983227887719610112028230603166527303021036386350781414447347150383783816869784006598225583375458609586450854602862569022571672049158809874763812834044257419199631217527367046624888837755311215081173386523806086783266198390289097231168172692326653657393522561741947951887577156666663584249108899327053951891486355179939770150550995812478327735917006194574412518819299303783243886962455399783601229227718787081785391010424030509937403600351414176138124705168002288620664809270046124
#
# n=[]
# c=[]
# for i in range(1,3):
#     n.append(eval('n'+str(i)))
#     c.append(eval('c'+str(i)))
#进制转换
#for i in range(len(n)):
#     n[i]=int(str(n[i]),5)
#     c[i]=int(str(c[i]),5)
#print(n)
# def CRT(data):
#     plian=0
#     m=1
#     for x in data:
#         m=m*x[1]
#     for z,n in data:
#         mi=m//n
#         mr=gmpy2.invert(mi,n)
#         plian=plian+z*(mr*mi)
#     return plian%m
#
# data=list(zip(c,n))
# f=CRT(data)
# for e in range(2,97):
#     m2,h=gmpy2.iroot(f,e)
#     if(h==1):
#         m2 = hex(m2)
#         print(m2)
#         print(codecs.decode(m2[2:],'hex'))

#模不互素，n1,n2不互素,有e
# n1 = 13508774104460209743306714034546704137247627344981133461801953479736017021401725818808462898375994767375627749494839671944543822403059978073813122441407612530658168942987820256786583006947001711749230193542370570950705530167921702835627122401475251039000775017381633900222474727396823708695063136246115652622259769634591309421761269548260984426148824641285010730983215377509255011298737827621611158032976420011662547854515610597955628898073569684158225678333474543920326532893446849808112837476684390030976472053905069855522297850688026960701186543428139843783907624317274796926248829543413464754127208843070331063037
# n2 =12806210903061368369054309575159360374022344774547459345216907128193957592938071815865954073287532545947370671838372144806539753829484356064919357285623305209600680570975224639214396805124350862772159272362778768036844634760917612708721787320159318432456050806227784435091161119982613987303255995543165395426658059462110056431392517548717447898084915167661172362984251201688639469652283452307712821398857016487590794996544468826705600332208535201443322267298747117528882985955375246424812616478327182399461709978893464093245135530135430007842223389360212803439850867615121148050034887767584693608776323252233254261047
# c1 = 12641635617803746150332232646354596292707861480200207537199141183624438303757120570096741248020236666965755798009656547738616399025300123043766255518596149348930444599820675230046423373053051631932557230849083426859490183732303751744004874183062594856870318614289991675980063548316499486908923209627563871554875612702079100567018698992935818206109087568166097392314105717555482926141030505639571708876213167112187962584484065321545727594135175369233925922507794999607323536976824183162923385005669930403448853465141405846835919842908469787547341752365471892495204307644586161393228776042015534147913888338316244169120
#
#
# p1 = gmpy2.gcd(n1,n2)
# q1 = n1/p1





#d泄露，遍历
#p,q是1024位的,因此两者相乘不低于2048位,通过运算可知ed-1为2064位,因此k一定小于16位
# e_d_1=e*d-1
# p=0
# q=0
# for k in range(pow(2,15),pow(2,16)):
#     if e_d_1%k==0:
#         p=sympy.prevprime(gmpy2.iroot(e_d_1//k,2)[0])
#         q=sympy.nextprime(p)
#         if (p-1)*(q-1)*k==e_d_1:
#             break
# n=p*q

#rsa的变形、n=p*q*r   威尔逊定理
# def get_pq(A,B):
#     tmp = 1
#     for i in range(B+1,A-1):
#         tmp *= i
#         tmp %= A
#     tmp_inv = gmpy2.invert(tmp,A)
#     return sympy.nextprime(tmp_inv)
#
# A1=21856963452461630437348278434191434000066076750419027493852463513469865262064340836613831066602300959772632397773487317560339056658299954464169264467234407
# B1=21856963452461630437348278434191434000066076750419027493852463513469865262064340836613831066602300959772632397773487317560339056658299954464169264467140596
#
# A2=16466113115839228119767887899308820025749260933863446888224167169857612178664139545726340867406790754560227516013796269941438076818194617030304851858418927
# B2=16466113115839228119767887899308820025749260933863446888224167169857612178664139545726340867406790754560227516013796269941438076818194617030304851858351026
#
# p = get_pq(A1,B1)
# q = get_pq(A2,B2)
# print(p)
# print(q)
# r = n//p//q
# phi = (p-1)*(q-1)*(r-1)
# d = gmpy2.invert(e, phi)
# print("d:"+ str(d))

#rabin，e=2,满足p,q = 3 (mod 4)的情况，直接利用Toelli-shanks算法的结论，不满足的方法？？？
def rabin(e,p,q,n,c):
    inv_p = gmpy2.invert(p, q)
    inv_q = gmpy2.invert(q, p)

    # 计算mp和mq
    mp = pow(c, (p + 1) // 4, p)
    mq = pow(c, (q + 1) // 4, q)

    # 计算a,b,c,d
    a = (inv_p * p * mq + inv_q * q * mp) % n
    b = n - int(a)
    c = (inv_p * p * mq - inv_q * q * mp) % n
    d = n - int(c)

    for i in (a, b, c, d):
        print(bin(i)[2:]) #输出二进制
        print(i)
        print(long_to_bytes(i))


#选择明文攻击
# c1 = 128509160179202
# c2 = 518818742414340
# c3 = 358553002064450
# n = gmpy2.gcd(pow(c1,2)-c2,pow(c1,3)-c3)
# #分解n
# n = n/2
# p = 18195301
# q = 28977097
# print(n)
# #离散对数求e
# e = 808723997
# c = 169169912654178


#wiener attack 连分数攻击
#求渐进分数
N1 = 1628
N2 = 321
#求连分数的项
def continuedfra(x,y):
    cf = []
    while y:
        cf += [x//y]
        x,y = y,x%y
    return cf
#得到分子和分母
def simplify(c):
    numrator = 0 #分子
    denominator = 1 #分母
    for x in c[::-1]: #倒序遍历？
        numrator,denominator = denominator,x * denominator + numrator
    return (numrator,denominator) #连分数生成分子和算出来的分母？

def getit(c):
    cf = []
    for i in range(len(c)):
        cf.append(simplify(c[:i]))
    return cf

def wiener(e,n):
    cf = []
    for (Q2,Q1) in getit(cf):
        if Q1 == 0:
            continue
        if N1%Q1 == 0 and Q1 != 1:
            return Q1
    print("not found")
    return 0

#Q1 = wiener(N1,N2)



#wiener attack (owiener库
def owienerk(e,n):

    d = owiener.attack(e, n)

    if d is None:
        print("Failed")
    else:
        print("Hacked d={}".format(d))
        return d

#给出具有相关性的一些式子，变形，然后求公因式，得到p/q
def g():
    com = gmpy2.gcd()
    return com

# c = m^n mod n  Schmidt-Samoa
def schmit_samoa(N,d,c):
    pq = libnum.gcd(pow(2, d * N, N) - 2, N)

    m = pow(c, d, pq)
    print(n2s(m))

#根据c求m
def get_d(e,p,q):
    phi_n = (p - 1) * (q - 1)
    #若无法直接求逆元d
    #print(gmpy2.lcm(p - 1, q - 1))  # 最小公倍数
    #print(gmpy2.gcd(e,phi_n))
    d = gmpy2.invert(e, phi_n)
    print("d:"+ str(d))
    return d

def decrypt(e, c, d, n):
    M = pow(c,d,n)

    #e不是素数，需要分解，变形后，m是之前的x次方
    #M = gmpy2.iroot(M,2)[0]

    print("十进制M："+ str(M))
    print(long_to_bytes(M))
    print(hex(M))
    #print(libnum.n2s(M))

    return M


#从公钥文件中获取n、e的值
def get_ne(filename):
    with open(filename,'rb') as f:
        pub = RSA.importKey(f.read())
        n = pub.n
        e = pub.e
        print(n,'\n',e)
        return n,e

# #解密文件
def decrypt_file1(n,e,d,p,q,filename):
    key_info = RSA.construct((n, e, int(d), p, q))
    key = RSA.importKey(key_info.exportKey())
    key = PKCS1_OAEP.new(key)
    f = open(filename, 'rb').read()
    #c = base64.b64decode(f)可以先自行查看具体什么编码
    flag = key.decrypt(f)
    print(flag)

#解密文件，不知道为什么可能某种方法无法使用
def decrypt_file2(n,e,d,p,q,filename):
    Rsa=rsa.PrivateKey(int(n), int(e), int(d), int(p), int(q))
    with open(filename,'rb') as f:
         cipher1=f.read()
         print(rsa.decrypt(cipher1, Rsa))



def main():
    p = 3
    q = 5
    n = 15
    e = 65537
    c = 123456
    decrypt()

if __name__ == main:
    main()



