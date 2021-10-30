import binascii
import codecs
import libnum

import gmpy2
n = 73069886771625642807435783661014062604264768481735145873508846925735521695159
p= 189239861511125143212536989589123569301
q= 386123125371923651191219869811293586459
#d =0x1806799bd44ce649122b78b43060c786f8b77fb1593e0842da063ba0d8728bf1
e = 65537
c =28767758880940662779934612526152562406674613203406706867456395986985664083182



#计算d
phi_n = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_n)
print("d:"+ str(d))

# #根据c求m
M = pow(c,d,p*q)
print("十进制M："+ str(M))
H = hex(M)
print("十六："+H)
flag = codecs.decode(H[2:], "hex")
print(flag)

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
# dp = 905074498052346904643025132879518330691925174573054004621877253318682675055421970943552016695528560364834446303196939207056642927148093290374440210503657
#
# def getd(n,e,dp):
#     for i in range(1,e):
#         if (dp * e - 1) % i == 0 and n % (((dp * e - 1) // i) + 1) == 0:
#             p=((dp*e-1)/i)+1
#             q=n / (((dp*e-1)//i)+1)
#             phi = (p-1)*(q-1)
#             d = gmpy2.invert(gmpy2.mpz(e),gmpy2.mpz(phi)) % phi
#             return d
# d = getd(n,e,dp)
# print("DP,d:"+str(d))

# 共模攻击
# e1 = 11187289
# e2 = 9647291
# c1 = 22322035275663237041646893770451933509324701913484303338076210603542612758956262869640822486470121149424485571361007421293675516338822195280313794991136048140918842471219840263536338886250492682739436410013436651161720725855484866690084788721349555662019879081501113222996123305533009325964377798892703161521852805956811219563883312896330156298621674684353919547558127920925706842808914762199011054955816534977675267395009575347820387073483928425066536361482774892370969520740304287456555508933372782327506569010772537497541764311429052216291198932092617792645253901478910801592878203564861118912045464959832566051361
# c2 = 18702010045187015556548691642394982835669262147230212731309938675226458555210425972429418449273410535387985931036711854265623905066805665751803269106880746769003478900791099590239513925449748814075904017471585572848473556490565450062664706449128415834787961947266259789785962922238701134079720414228414066193071495304612341052987455615930023536823801499269773357186087452747500840640419365011554421183037505653461286732740983702740822671148045619497667184586123657285604061875653909567822328914065337797733444640351518775487649819978262363617265797982843179630888729407238496650987720428708217115257989007867331698397
#
# gcd,s,t = gmpy2.gcdext(e1,e2)
# if s < 0:
#     s = -s
#     c1 = gmpy2.invert(c1,n)
# if t < 0:
#     t = -t
#     c2 = gmpy2.invert(c2,n)
#
# M = gmpy2.powmod(c1,s,n)*gmpy2.powmod(c2,t,n) % n
# m = hex(M)
# print(m)
# print(codecs.decode(m[2:],'hex'))


# 分行加密，解密
# m = ""
# with open("data.txt",'r') as f:
#     for c in f.readlines():
#         m += chr(pow(int(c), d, n))
# print(m)


# 小公钥指数攻击（一般e为3） 对K进行爆破，只要k满足 kn + C能够开e次方就可以得明文
# k = 0
# while 1:
#     res = gmpy2.iroot(c + k * n, e)
#     if res[1] == True:
#        print(libnum.n2s(int(res[0])))
#        break
#     k = k + 1


#爆破，给出e的范围
# for e in range(50000,70001):
#     if gmpy2.gcd(e,phi) == 1:
#             d = gmpy2.invert(e, phi)
#             m = pow(c, d, n)
#             flag = hex(m)[2:]
#             #不是偶数就要加0？？？但是libnum不可用？？？
#             if (len(str(flag)) % 2 == 1):
#                 flag = '0' + flag
#             print(codecs.decode(flag,'hex'))


#模不互素，n1,n2不互素,有e
# n1 = 13508774104460209743306714034546704137247627344981133461801953479736017021401725818808462898375994767375627749494839671944543822403059978073813122441407612530658168942987820256786583006947001711749230193542370570950705530167921702835627122401475251039000775017381633900222474727396823708695063136246115652622259769634591309421761269548260984426148824641285010730983215377509255011298737827621611158032976420011662547854515610597955628898073569684158225678333474543920326532893446849808112837476684390030976472053905069855522297850688026960701186543428139843783907624317274796926248829543413464754127208843070331063037
# n2 =12806210903061368369054309575159360374022344774547459345216907128193957592938071815865954073287532545947370671838372144806539753829484356064919357285623305209600680570975224639214396805124350862772159272362778768036844634760917612708721787320159318432456050806227784435091161119982613987303255995543165395426658059462110056431392517548717447898084915167661172362984251201688639469652283452307712821398857016487590794996544468826705600332208535201443322267298747117528882985955375246424812616478327182399461709978893464093245135530135430007842223389360212803439850867615121148050034887767584693608776323252233254261047
# c1 = 12641635617803746150332232646354596292707861480200207537199141183624438303757120570096741248020236666965755798009656547738616399025300123043766255518596149348930444599820675230046423373053051631932557230849083426859490183732303751744004874183062594856870318614289991675980063548316499486908923209627563871554875612702079100567018698992935818206109087568166097392314105717555482926141030505639571708876213167112187962584484065321545727594135175369233925922507794999607323536976824183162923385005669930403448853465141405846835919842908469787547341752365471892495204307644586161393228776042015534147913888338316244169120
#
#
# p1 = gmpy2.gcd(n1,n2)
# q1 = n1/p1



#已知m,c,n爆破求e



#多个n、c求
import libnum
n4 = 22822039733049388110936778173014765663663303811791283234361230649775805923902173438553927805407463106104699773994158375704033093471761387799852168337898526980521753614307899669015931387819927421875316304591521901592823814417756447695701045846773508629371397013053684553042185725059996791532391626429712416994990889693732805181947970071429309599614973772736556299404246424791660679253884940021728846906344198854779191951739719342908761330661910477119933428550774242910420952496929605686154799487839923424336353747442153571678064520763149793294360787821751703543288696726923909670396821551053048035619499706391118145067
c4 = 15406498580761780108625891878008526815145372096234083936681442225155097299264808624358826686906535594853622687379268969468433072388149786607395396424104318820879443743112358706546753935215756078345959375299650718555759698887852318017597503074317356745122514481807843745626429797861463012940172797612589031686718185390345389295851075279278516147076602270178540690147808314172798987497259330037810328523464851895621851859027823681655934104713689539848047163088666896473665500158179046196538210778897730209572708430067658411755959866033531700460551556380993982706171848970460224304996455600503982223448904878212849412357

p = gmpy2.mpz(132585806383798600305426957307612567604223562626764190211333136246643723811046149337852966828729052476725552361132437370521548707664977123165279305052971868012755509160408641100548744046621516877981864180076497524093201404558036301820216274968638825245150755772559259575544101918590311068466601618472464832499)

q = n4//p        #“//”  整除

phi = (p-1)*(q-1)

e = 65537
d = gmpy2.invert(e,phi)

m = pow(c4,d,n4)

#print(libnum.n2s(m))    # "n2s" (数值转字符串)
print(hex(m))
print(bytes.fromhex(hex(m)[2:]))



