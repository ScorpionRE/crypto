import binascii
import codecs
import libnum

import gmpy2
n = 21058339337354287847534107544613605305015441090508924094198816691219103399526800112802416383088995253908857460266726925615826895303377801614829364034624475195859997943146305588315939130777450485196290766249612340054354622516207681542973756257677388091926549655162490873849955783768663029138647079874278240867932127196686258800146911620730706734103611833179733264096475286491988063990431085380499075005629807702406676707841324660971173253100956362528346684752959937473852630145893796056675793646430793578265418255919376323796044588559726703858429311784705245069845938316802681575653653770883615525735690306674635167111
p= 189239861511125143212536989589123569301
q= 386123125371923651191219869811293586459
#d =0x1806799bd44ce649122b78b43060c786f8b77fb1593e0842da063ba0d8728bf1
e = 65537
c =28767758880940662779934612526152562406674613203406706867456395986985664083182




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
# e1 = 2767
# e2 = 3659
# c1 = 20152490165522401747723193966902181151098731763998057421967155300933719378216342043730801302534978403741086887969040721959533190058342762057359432663717825826365444996915469039056428416166173920958243044831404924113442512617599426876141184212121677500371236937127571802891321706587610393639446868836987170301813018218408886968263882123084155607494076330256934285171370758586535415136162861138898728910585138378884530819857478609791126971308624318454905992919405355751492789110009313138417265126117273710813843923143381276204802515910527468883224274829962479636527422350190210717694762908096944600267033351813929448599
# c2 = 11298697323140988812057735324285908480504721454145796535014418738959035245600679947297874517818928181509081545027056523790022598233918011261011973196386395689371526774785582326121959186195586069851592467637819366624044133661016373360885158956955263645614345881350494012328275215821306955212788282617812686548883151066866149060363482958708364726982908798340182288702101023393839781427386537230459436512613047311585875068008210818996941460156589314135010438362447522428206884944952639826677247819066812706835773107059567082822312300721049827013660418610265189288840247186598145741724084351633508492707755206886202876227
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

#多个n,c找n的公因数
# N1 = 331310324212000030020214312244232222400142410423413104441140203003243002104333214202031202212403400220031202142322434104143104244241214204444443323000244130122022422310201104411044030113302323014101331214303223312402430402404413033243132101010422240133122211400434023222214231402403403200012221023341333340042343122302113410210110221233241303024431330001303404020104442443120130000334110042432010203401440404010003442001223042211442001413004
# c1 = 310020004234033304244200421414413320341301002123030311202340222410301423440312412440240244110200112141140201224032402232131204213012303204422003300004011434102141321223311243242010014140422411342304322201241112402132203101131221223004022003120002110230023341143201404311340311134230140231412201333333142402423134333211302102413111111424430032440123340034044314223400401224111323000242234420441240411021023100222003123214343030122032301042243
#
# N2 = 302240000040421410144422133334143140011011044322223144412002220243001141141114123223331331304421113021231204322233120121444434210041232214144413244434424302311222143224402302432102242132244032010020113224011121043232143221203424243134044314022212024343100042342002432331144300214212414033414120004344211330224020301223033334324244031204240122301242232011303211220044222411134403012132420311110302442344021122101224411230002203344140143044114
# c2 = 112200203404013430330214124004404423210041321043000303233141423344144222343401042200334033203124030011440014210112103234440312134032123400444344144233020130110134042102220302002413321102022414130443041144240310121020100310104334204234412411424420321211112232031121330310333414423433343322024400121200333330432223421433344122023012440013041401423202210124024431040013414313121123433424113113414422043330422002314144111134142044333404112240344
#
# N3 = 332200324410041111434222123043121331442103233332422341041340412034230003314420311333101344231212130200312041044324431141033004333110021013020140020011222012300020041342040004002220210223122111314112124333211132230332124022423141214031303144444134403024420111423244424030030003340213032121303213343020401304243330001314023030121034113334404440421242240113103203013341231330004332040302440011324004130324034323430143102401440130242321424020323
# c3 = 10013444120141130322433204124002242224332334011124210012440241402342100410331131441303242011002101323040403311120421304422222200324402244243322422444414043342130111111330022213203030324422101133032212042042243101434342203204121042113212104212423330331134311311114143200011240002111312122234340003403312040401043021433112031334324322123304112340014030132021432101130211241134422413442312013042141212003102211300321404043012124332013240431242
# n = []
# c = []
# for i in range(1,3):
#     n.append(eval('N'+str(i)))
#     c.append(eval('c'+str(i)))
# data=list(zip(n,c))
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if gmpy2.gcd(n[i],n[j])!=1:
#             print (i,j)
#             p = gmpy2.gcd(n[i],n[j])
#             print("p:"+str(p))
#             break
# q = gmpy2.mpz(n[i]/p)
# phi = (p-1)*(q-1)











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
# n4 = 22822039733049388110936778173014765663663303811791283234361230649775805923902173438553927805407463106104699773994158375704033093471761387799852168337898526980521753614307899669015931387819927421875316304591521901592823814417756447695701045846773508629371397013053684553042185725059996791532391626429712416994990889693732805181947970071429309599614973772736556299404246424791660679253884940021728846906344198854779191951739719342908761330661910477119933428550774242910420952496929605686154799487839923424336353747442153571678064520763149793294360787821751703543288696726923909670396821551053048035619499706391118145067
# c4 = 15406498580761780108625891878008526815145372096234083936681442225155097299264808624358826686906535594853622687379268969468433072388149786607395396424104318820879443743112358706546753935215756078345959375299650718555759698887852318017597503074317356745122514481807843745626429797861463012940172797612589031686718185390345389295851075279278516147076602270178540690147808314172798987497259330037810328523464851895621851859027823681655934104713689539848047163088666896473665500158179046196538210778897730209572708430067658411755959866033531700460551556380993982706171848970460224304996455600503982223448904878212849412357
#
# p = gmpy2.mpz(132585806383798600305426957307612567604223562626764190211333136246643723811046149337852966828729052476725552361132437370521548707664977123165279305052971868012755509160408641100548744046621516877981864180076497524093201404558036301820216274968638825245150755772559259575544101918590311068466601618472464832499)
#
# q = n4//p        #“//”  整除
#
# phi = (p-1)*(q-1)
#
# e = 65537
# d = gmpy2.invert(e,phi)
#
# m = pow(c4,d,n4)
#
# #print(libnum.n2s(m))    # "n2s" (数值转字符串)
# print(hex(m))
# print(bytes.fromhex(hex(m)[2:]))


#低解密指数广播攻击，三个n、c，同一个e加密且e较小,且n均互素

n1= 331310324212000030020214312244232222400142410423413104441140203003243002104333214202031202212403400220031202142322434104143104244241214204444443323000244130122022422310201104411044030113302323014101331214303223312402430402404413033243132101010422240133122211400434023222214231402403403200012221023341333340042343122302113410210110221233241303024431330001303404020104442443120130000334110042432010203401440404010003442001223042211442001413004
c1= 310020004234033304244200421414413320341301002123030311202340222410301423440312412440240244110200112141140201224032402232131204213012303204422003300004011434102141321223311243242010014140422411342304322201241112402132203101131221223004022003120002110230023341143201404311340311134230140231412201333333142402423134333211302102413111111424430032440123340034044314223400401224111323000242234420441240411021023100222003123214343030122032301042243

n2= 302240000040421410144422133334143140011011044322223144412002220243001141141114123223331331304421113021231204322233120121444434210041232214144413244434424302311222143224402302432102242132244032010020113224011121043232143221203424243134044314022212024343100042342002432331144300214212414033414120004344211330224020301223033334324244031204240122301242232011303211220044222411134403012132420311110302442344021122101224411230002203344140143044114
c2= 112200203404013430330214124004404423210041321043000303233141423344144222343401042200334033203124030011440014210112103234440312134032123400444344144233020130110134042102220302002413321102022414130443041144240310121020100310104334204234412411424420321211112232031121330310333414423433343322024400121200333330432223421433344122023012440013041401423202210124024431040013414313121123433424113113414422043330422002314144111134142044333404112240344

n3= 332200324410041111434222123043121331442103233332422341041340412034230003314420311333101344231212130200312041044324431141033004333110021013020140020011222012300020041342040004002220210223122111314112124333211132230332124022423141214031303144444134403024420111423244424030030003340213032121303213343020401304243330001314023030121034113334404440421242240113103203013341231330004332040302440011324004130324034323430143102401440130242321424020323
c3= 10013444120141130322433204124002242224332334011124210012440241402342100410331131441303242011002101323040403311120421304422222200324402244243322422444414043342130111111330022213203030324422101133032212042042243101434342203204121042113212104212423330331134311311114143200011240002111312122234340003403312040401043021433112031334324322123304112340014030132021432101130211241134422413442312013042141212003102211300321404043012124332013240431242
n=[]
c=[]
for i in range(1,4):
	n.append(eval('n'+str(i)))
	c.append(eval('c'+str(i)))
for i in range(len(n)):
	n[i]=int(str(n[i]),5)
	c[i]=int(str(c[i]),5)
#print(n)
def CRT(data):
	plian=0
	m=1
	for x in data:
		m=m*x[1]
	for z,n in data:
		mi=m/n
		mr=gmpy2.invert(mi,n)
		plian=plian+z*(mr*mi)
	return plian%m
data=list(zip(c,n))
f=CRT(data)
for e in range(2,97):
	m2,h=gmpy2.iroot(f,e)
	if(h==1):
		print (m2)
		print (hex(m2)[2:].decode('hex'))



#计算d
phi_n = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_n)
print("d:"+ str(d))

# #根据c求m
M = pow(c[i],d,n[i])
print("十进制M："+ str(M))
H = hex(M)
print("十六："+H)
flag = codecs.decode(H[2:], "hex")
print(flag)