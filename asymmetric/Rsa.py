import base64
import binascii
from cmath import sqrt
import codecs
import linecache
import random

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

# 已知m高位， 求低位,sage

# def High_m(high_m, n, c):
#     R.<x> = PolynomialRing(Zmod(n), implementation='NTL')
#     m = high_m + x
#     M = m((m^3 - c).small_roots()[0])
#     print(hex(int(M))[2:])
#
# n = 13112061820685643239663831166928327119579425830632458568801544406506769461279590962772340249183569437559394200635526183698604582385769381159563710823689417274479549627596095398621182995891454516953722025068926293512505383125227579169778946631369961753587856344582257683672313230378603324005337788913902434023431887061454368566100747618582590270385918204656156089053519709536001906964008635708510672550219546894006091483520355436091053866312718431318498783637712773878423777467316605865516248176248780637132615807886272029843770186833425792049108187487338237850806203728217374848799250419859646871057096297020670904211
# c = 15987554724003100295326076036413163634398600947695096857803937998969441763014731720375196104010794555868069024393647966040593258267888463732184495020709457560043050577198988363754703741636088089472488971050324654162166657678376557110492703712286306868843728466224887550827162442026262163340935333721705267432790268517
# high_m = 2519188594271759205757864486097605540135407501571078627238849443561219057751843170540261842677239681908736
# High_m(high_m,n,c)

# 已知p高位攻击,copper
# sage
# def High_p(high_p, pbits, n, c):
#     k = pbits - high_p.nbits()  # 注意有的p低位变0后，这里计算不一定准，可以直接手动改k
#     print(len)
#     high_p = high_p << k
#     R. < x > = PolynomialRing(Zmod(n))
#     p = high_p + x
#     x0 = p.small_roots(X=2 ^ k, beta=0.4)[0]
#
#     P = int(p(x0))
#     Q = n // P
#
#     assert n == P * Q
#     print(P)
#     print(Q)
#     d = inverse_mod(65537, (P - 1) * (Q - 1))
#     print(hex(power_mod(c, d, n)))
#
#
# n = 12784625729032789592766625203074018101354917751492952685083808825504221816847310910447532133616954262271205877651255598995305639194329607493047941212754523879402744065076183778452640602625242851184095546100200565113016690161053808950384458996881574266573992526357954507491397978278604102524731393059303476350167738237822647246425836482533150025923051544431330502522043833872580483142594571802189321599016725741260254170793393777293145010525686561904427613648184843619301241414264343057368192416551134404100386155751297424616254697041043851852081071306219462991969849123668248321130382231769250865190227630009181759219
# c = 627824086157119245056478875800598959553774250161670787506083253960788230737588761787385686125828765665617567887904228030839535317987589608761534500003128247164233774794784231518212804270056404565710426613938264302998015421153393879729263551292024543756422702956470022959537221269172084619081368498693930550456153543628170306324206266216348386707008661128717431426237486511309767286175518238620230507201952867261283880986868752676549613958785288914989429224582849218395471672295410036858881836363364885164276983237312235831591858044908369376855484127614933545955544787160352042318378588039587911741028067576722790778
# high_p = 97522826022187678545924975588711975512906538181361325096919121233043973599759518562689050415761485716705615149641768982838255403594331293651224395590747133152128042950062103156564440155088882592644046069208405360324372057140890317518802130081198060093576841538008960560391380395697098964411821716664506908672
#
# High_p(high_p, 1024, n, c)


# 已知d低位，sage
# def getFullP(low_p, kbits, n):
#     R. < x > = PolynomialRing(Zmod(n))
#     p = x * 2 ^ kbits + low_p
#     nbits = n.nbits()
#     root = (p - n).monic().small_roots(X=2 ^ (nbits // 2 - kbits), beta=0.3)
#     if root:
#         return p(root[0])
#     return None
#
#
# def Low_d(low_d, kbits, n, c):
#     maybe_p = []
#     for k in range(1, 4):
#         p = var('p')
#         p0 = solve_mod([3 * p * low_d == p + k * (n * p - p ^ 2 - n + p)], 2 ^ kbits)
#         maybe_p += [int(x[0]) for x in p0]
#     print(maybe_p)
#
#     for x in maybe_p:
#         P = getFullP(x, kbits, n)
#         if P: break
#
#     P = int(P)
#     Q = n // P
#
#     assert P * Q == n
#
#     d = inverse_mod(3, (P - 1) * (Q - 1))
#     print(hex(power_mod(c, d, n))[2:])
#
#
# n = 92896523979616431783569762645945918751162321185159790302085768095763248357146198882641160678623069857011832929179987623492267852304178894461486295864091871341339490870689110279720283415976342208476126414933914026436666789270209690168581379143120688241413470569887426810705898518783625903350928784794371176183
# c = 56164378185049402404287763972280630295410174183649054805947329504892979921131852321281317326306506444145699012788547718091371389698969718830761120076359634262880912417797038049510647237337251037070369278596191506725812511682495575589039521646062521091457438869068866365907962691742604895495670783101319608530
# low_d = 787673996295376297668171075170955852109814939442242049800811601753001897317556022653997651874897208487913321031340711138331360350633965420642045383644955
# kbits = 512
# # kbits = n.nbits() - low_d.nbits() - 1
# Low_d(low_d, kbits, n, c)

# Copper: Related Message Attack   M1 = f(M2) =  a*M2 + b
# n = 113604829563460357756722229849309932731534576966155520277171862442445354404910882358287832757024693652075211204635679309777620586814014894544893424988818766425089667672311645586528776360047956843961901352792631908859388801090108188344342619580661377758180391734771694803991493164412644148805229529911069578061
# c1 = 112992730284209629010217336632593897028023711212853788739137950706145189880318698604512926758021533447981943498594790549326550460216939216988828130624120379925895123186121819609415184887470233938291227816332249857236198616538782622327476603338806349004620909717360739157545735826670038169284252348037995399308
# c2 = 112992730284209629010217336632593897028023711212853788739137950706145189880318698604512926758021552486915464025361447529153776277710423467951041523831865232164370127602772602643378592695459331174613894578701940837730590029577336924367384969935652616989527416027725713616493815764725131271563545176286794438175
# e = 3
#
# # c1 = m^e
# # c2 = (m+1)^e
#
# R.<x> = PolynomialRing(Zmod(n))
# g1 = x^e - c1
# g2 = (x+1)^e - c2
#
# def myGcd(x, y):
#     if y == 0:
#         return x.monic()
#     return myGcd(y, x%y)
#
# v = myGcd(g2, g1)
# M = n - v.coefficients()[0]
#
# assert g1(M) == 0
# print(hex(M))

# related_message_attack： e=3的特殊情况
def related_message_attack(a,b,c1,c2):
    m2 = b/a * ((c1+2*pow(a,3)*c2-pow(b,3))/(c1-pow(a,3)*c2+2*pow(b,3)))
    m2 = gmpy2.mpz(m2)
    # print(gmpy2.mpz(m2))
    print(hex(m2))
    return m2

### boneh and Durfee, d < N^0.292(delta  LLL attack

# import time
#
# """
# Setting debug to true will display more informations
# about the lattice, the bounds, the vectors...
# """
# debug = True
#
# """
# Setting strict to true will stop the algorithm (and
# return (-1, -1)) if we don't have a correct
# upperbound on the determinant. Note that this
# doesn't necesseraly mean that no solutions
# will be found since the theoretical upperbound is
# usualy far away from actual results. That is why
# you should probably use `strict = False`
# """
# strict = False
#
# """
# This is experimental, but has provided remarkable results
# so far. It tries to reduce the lattice as much as it can
# while keeping its efficiency. I see no reason not to use
# this option, but if things don't work, you should try
# disabling it
# """
# helpful_only = True
# dimension_min = 7  # stop removing if lattice reaches that dimension
#
#
# ############################################
# # Functions
# ##########################################
#
# # display stats on helpful vectors
# def helpful_vectors(BB, modulus):
#     nothelpful = 0
#     for ii in range(BB.dimensions()[0]):
#         if BB[ii, ii] >= modulus:
#             nothelpful += 1
#
#     print(nothelpful, "/", BB.dimensions()[0], " vectors are not helpful")
#
#
# # display matrix picture with 0 and X
# def matrix_overview(BB, bound):
#     for ii in range(BB.dimensions()[0]):
#         a = ('%02d ' % ii)
#         for jj in range(BB.dimensions()[1]):
#             a += '0' if BB[ii, jj] == 0 else 'X'
#             if BB.dimensions()[0] < 60:
#                 a += ' '
#         if BB[ii, ii] >= bound:
#             a += '~'
#         print(a)
#
#
# # tries to remove unhelpful vectors
# # we start at current = n-1 (last vector)
# def remove_unhelpful(BB, monomials, bound, current):
#     # end of our recursive function
#     if current == -1 or BB.dimensions()[0] <= dimension_min:
#         return BB
#
#     # we start by checking from the end
#     for ii in range(current, -1, -1):
#         # if it is unhelpful:
#         if BB[ii, ii] >= bound:
#             affected_vectors = 0
#             affected_vector_index = 0
#             # let's check if it affects other vectors
#             for jj in range(ii + 1, BB.dimensions()[0]):
#                 # if another vector is affected:
#                 # we increase the count
#                 if BB[jj, ii] != 0:
#                     affected_vectors += 1
#                     affected_vector_index = jj
#
#             # level:0
#             # if no other vectors end up affected
#             # we remove it
#             if affected_vectors == 0:
#                 print("* removing unhelpful vector", ii)
#                 BB = BB.delete_columns([ii])
#                 BB = BB.delete_rows([ii])
#                 monomials.pop(ii)
#                 BB = remove_unhelpful(BB, monomials, bound, ii - 1)
#                 return BB
#
#             # level:1
#             # if just one was affected we check
#             # if it is affecting someone else
#             elif affected_vectors == 1:
#                 affected_deeper = True
#                 for kk in range(affected_vector_index + 1, BB.dimensions()[0]):
#                     # if it is affecting even one vector
#                     # we give up on this one
#                     if BB[kk, affected_vector_index] != 0:
#                         affected_deeper = False
#                 # remove both it if no other vector was affected and
#                 # this helpful vector is not helpful enough
#                 # compared to our unhelpful one
#                 if affected_deeper and abs(bound - BB[affected_vector_index, affected_vector_index]) < abs(
#                         bound - BB[ii, ii]):
#                     print("* removing unhelpful vectors", ii, "and", affected_vector_index)
#                     BB = BB.delete_columns([affected_vector_index, ii])
#                     BB = BB.delete_rows([affected_vector_index, ii])
#                     monomials.pop(affected_vector_index)
#                     monomials.pop(ii)
#                     BB = remove_unhelpful(BB, monomials, bound, ii - 1)
#                     return BB
#     # nothing happened
#     return BB
#
#
# """
# Returns:
# * 0,0   if it fails
# * -1,-1 if `strict=true`, and determinant doesn't bound
# * x0,y0 the solutions of `pol`
# """
#
#
# def boneh_durfee(pol, modulus, mm, tt, XX, YY):
#     """
#     Boneh and Durfee revisited by Herrmann and May
#
#     finds a solution if:
#     * d < N^delta
#     * |x| < e^delta
#     * |y| < e^0.5
#     whenever delta < 1 - sqrt(2)/2 ~ 0.292
#     """
#
#     # substitution (Herrman and May)
#     PR. < u, x, y > = PolynomialRing(ZZ)
#     Q = PR.quotient(x * y + 1 - u)  # u = xy + 1
#     polZ = Q(pol).lift()
#
#     UU = XX * YY + 1
#
#     # x-shifts
#     gg = []
#     for kk in range(mm + 1):
#         for ii in range(mm - kk + 1):
#             xshift = x ^ ii * modulus ^ (mm - kk) * polZ(u, x, y) ^ kk
#             gg.append(xshift)
#     gg.sort()
#
#     # x-shifts list of monomials
#     monomials = []
#     for polynomial in gg:
#         for monomial in polynomial.monomials():
#             if monomial not in monomials:
#                 monomials.append(monomial)
#     monomials.sort()
#
#     # y-shifts (selected by Herrman and May)
#     for jj in range(1, tt + 1):
#         for kk in range(floor(mm / tt) * jj, mm + 1):
#             yshift = y ^ jj * polZ(u, x, y) ^ kk * modulus ^ (mm - kk)
#             yshift = Q(yshift).lift()
#             gg.append(yshift)  # substitution
#
#     # y-shifts list of monomials
#     for jj in range(1, tt + 1):
#         for kk in range(floor(mm / tt) * jj, mm + 1):
#             monomials.append(u ^ kk * y ^ jj)
#
#     # construct lattice B
#     nn = len(monomials)
#     BB = Matrix(ZZ, nn)
#     for ii in range(nn):
#         BB[ii, 0] = gg[ii](0, 0, 0)
#         for jj in range(1, ii + 1):
#             if monomials[jj] in gg[ii].monomials():
#                 BB[ii, jj] = gg[ii].monomial_coefficient(monomials[jj]) * monomials[jj](UU, XX, YY)
#
#     # Prototype to reduce the lattice
#     if helpful_only:
#         # automatically remove
#         BB = remove_unhelpful(BB, monomials, modulus ^ mm, nn - 1)
#         # reset dimension
#         nn = BB.dimensions()[0]
#         if nn == 0:
#             print("failure")
#             return 0, 0
#
#     # check if vectors are helpful
#     if debug:
#         helpful_vectors(BB, modulus ^ mm)
#
#     # check if determinant is correctly bounded
#     det = BB.det()
#     bound = modulus ^ (mm * nn)
#     if det >= bound:
#         print("We do not have det < bound. Solutions might not be found.")
#         print("Try with highers m and t.")
#         if debug:
#             diff = (log(det) - log(bound)) / log(2)
#             print("size det(L) - size e^(m*n) = ", floor(diff))
#         if strict:
#             return -1, -1
#     else:
#         print("det(L) < e^(m*n) (good! If a solution exists < N^delta, it will be found)")
#
#     # display the lattice basis
#     if debug:
#         matrix_overview(BB, modulus ^ mm)
#
#     # LLL
#     if debug:
#         print("optimizing basis of the lattice via LLL, this can take a long time")
#
#     BB = BB.LLL()
#
#     if debug:
#         print("LLL is done!")
#
#     # transform vector i & j -> polynomials 1 & 2
#     if debug:
#         print("looking for independent vectors in the lattice")
#     found_polynomials = False
#
#     for pol1_idx in range(nn - 1):
#         for pol2_idx in range(pol1_idx + 1, nn):
#             # for i and j, create the two polynomials
#             PR. < w, z > = PolynomialRing(ZZ)
#             pol1 = pol2 = 0
#             for jj in range(nn):
#                 pol1 += monomials[jj](w * z + 1, w, z) * BB[pol1_idx, jj] / monomials[jj](UU, XX, YY)
#                 pol2 += monomials[jj](w * z + 1, w, z) * BB[pol2_idx, jj] / monomials[jj](UU, XX, YY)
#
#             # resultant
#             PR. < q > = PolynomialRing(ZZ)
#             rr = pol1.resultant(pol2)
#
#             # are these good polynomials?
#             if rr.is_zero() or rr.monomials() == [1]:
#                 continue
#             else:
#                 print("found them, using vectors", pol1_idx, "and", pol2_idx)
#                 found_polynomials = True
#                 break
#         if found_polynomials:
#             break
#
#     if not found_polynomials:
#         print("no independant vectors could be found. This should very rarely happen...")
#         return 0, 0
#
#     rr = rr(q, q)
#
#     # solutions
#     soly = rr.roots()
#
#     if len(soly) == 0:
#         print("Your prediction (delta) is too small")
#         return 0, 0
#
#     soly = soly[0][0]
#     ss = pol1(q, soly)
#     solx = ss.roots()[0][0]
#
#     #
#     return solx, soly
#
#
# def example():
#     ############################################
#     # How To Use This Script
#     ##########################################
#
#     #
#     # The problem to solve (edit the following values)
#     #
#
#     # the modulus
#     N = 0xbadd260d14ea665b62e7d2e634f20a6382ac369cd44017305b69cf3a2694667ee651acded7085e0757d169b090f29f3f86fec255746674ffa8a6a3e1c9e1861003eb39f82cf74d84cc18e345f60865f998b33fc182a1a4ffa71f5ae48a1b5cb4c5f154b0997dc9b001e441815ce59c6c825f064fdca678858758dc2cebbc4d27
#     # the public exponent
#     e = 0x11722b54dd6f3ad9ce81da6f6ecb0acaf2cbc3885841d08b32abc0672d1a7293f9856db8f9407dc05f6f373a2d9246752a7cc7b1b6923f1827adfaeefc811e6e5989cce9f00897cfc1fc57987cce4862b5343bc8e91ddf2bd9e23aea9316a69f28f407cfe324d546a7dde13eb0bd052f694aefe8ec0f5298800277dbab4a33bb
#
#     # the hypothesis on the private exponent (the theoretical maximum is 0.292)
#     delta = 0.280  # this means that d < N^delta
#
#     #
#     # Lattice (tweak those values)
#     #
#
#     # you should tweak this (after a first run), (e.g. increment it until a solution is found)
#     m = 4  # size of the lattice (bigger the better/slower)
#
#     # you need to be a lattice master to tweak these
#     t = int((1 - 2 * delta) * m)  # optimization from Herrmann and May
#     X = 2 * floor(N ^ delta)  # this _might_ be too much
#     Y = floor(N ^ (1 / 2))  # correct if p, q are ~ same size
#
#     #
#     # Don't touch anything below
#     #
#
#     # Problem put in equation
#     P. < x, y > = PolynomialRing(ZZ)
#     A = int((N + 1) / 2)
#     pol = 1 + x * (A + y)
#
#     #
#     # Find the solutions!
#     #
#
#     # Checking bounds
#     if debug:
#         print("=== checking values ===")
#         print("* delta:", delta)
#         print("* delta < 0.292", delta < 0.292)
#         print("* size of e:", int(log(e) / log(2)))
#         print("* size of N:", int(log(N) / log(2)))
#         print("* m:", m, ", t:", t)
#
#     # boneh_durfee
#     if debug:
#         print("=== running algorithm ===")
#         start_time = time.time()
#
#     solx, soly = boneh_durfee(pol, e, m, t, X, Y)
#
#     # found a solution?
#     if solx > 0:
#         print("=== solution found ===")
#         if False:
#             print("x:", solx)
#             print("y:", soly)
#
#         d = int(pol(solx, soly) / e)
#         print("private key found:", d)
#     else:
#         print("=== no solution was found ===")
#
#     if debug:
#         print("=== %s seconds ===" % (time.time() - start_time))
#
#
# if __name__ == "__main__":
#     example()

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
        if e%Q1 == 0 and Q1 != 1:
            return Q1
    print("not found")
    return 0

#d = wiener(e,n)



#wiener attack (owiener库
def owienerk(e,n):

    d = owiener.attack(e, n)

    if d is None:
        print("Failed")
    else:
        print("Hacked d={}".format(d))
        return d



# c = m^n mod n  Schmidt-Samoa
def schmit_samoa(N,d,c):
    pq = libnum.gcd(pow(2, d * N, N) - 2, N)

    m = pow(c, d, pq)
    print(n2s(m))

#已知e,p,q求d
def get_d(e,p,q):
    phi_n = (p - 1) * (q - 1)
    #若无法直接求逆元d
    #print(gmpy2.lcm(p - 1, q - 1))  # 最小公倍数
    #print(gmpy2.gcd(e,phi_n))
    d = gmpy2.invert(e, phi_n)
    print("d:"+ str(d))
    return d

#已知p+q为sum，p*q为n，求p和q
def get_pq(sum,n):
    p = (sum + sqrt(sum**2-4*n))/2
    q = (sum - sqrt(sum**2-4*n))/2
    print(p,q)
    return p,q
#已知e,d,n求p，q
# ed = 1 mod phi(n) = 1 + k*phi
# n = p*q   phi(n) = (p-1)*(q-1) = p*q - p - q + 1 = n - p - q + 1 = n - p - n/p + 1
# p 
def factorn(e,d,n):
    k = e * d - 1
    
    r = k
    t = 0
    while True:
        r = r // 2
        t += 1
        if r % 2 == 1:
            break
    
    success = False
    
    for i in range(1, 101):
        g = random.randint(0, n)
        y = pow(g, r, n)
        if y == 1 or y == n - 1:
            continue
    
        for j in range(1, t):
            x = pow(y, 2, n)
            if x == 1:
                success = True
                break
            elif x == n - 1:
                continue
            else:
                y = x
    
        if success:
            break
        else:
            continue
    
    if success:
        p = libnum.gcd(y - 1, n)
        q = n // p
        print ('P: ' + '%s' % p)
        print ('Q: ' + '%s' % q)
        return p,q
    else:
        print ('Cannot compute P and Q')





def decrypt(c, d, n):
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



