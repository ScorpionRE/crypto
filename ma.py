import gmpy2
import sympy


import math
#一元方程
# x = 5535722692962580764045545539105119140941061679289569420988353884209653851308860058948669740693107863231179565602072744542122031789184119031739723962825082929025825322421201364211726001366490949760887367407718763255964735567971493859197583624076478457865073449246835949075135223468616834636386958924709024763349115622062848212445867198457630368236782421195503713107838541903829979118327675371550868768159024260793541264335548489228744367609071659968450303895118817379316060805148754136917043160175570565717388336822960389664337656603584425629662613786203920234401824957121860225422901340950436355650311392398098947210940
# p = sympy.symbols('p')
# print(sympy.solve(2019*p**2 + 2020*p**3 + 2021*p**4-x,p))

#多元方程组

# x = sympy.Symbol('x')
# y = sympy.Symbol("y")
# z = sympy.Symbol("z")
# m = sympy.Symbol("m")
# # a = math.factorial(2020)
# # print(a)
# # print(hex(int(str(a)[:8])))
# #
# # x = pow(520,1314) + pow(2333,666)
# # print(x)
# # print(hex(int(str(x)[:8])))
#
# solved_value = sympy.solve([13627*x + 26183*y + 35897*z + 48119*m -347561292 ,
#                             23027*x + 38459*y + 40351*z + 19961*m -361760202,
#                             36013*x + 45589*y + 17029*z + 27823*m -397301762,
#                             43189*x + 12269*y + 21587*z + 33721*m -350830412], [x,y,z,m])
# print(solved_value)

#x**n = a mod p    #all_roots=False返回最小的值
# a =
# n =
# p =
#
# x = sympy.nthroot_mod(a,n,p,all_roots=True)

# a^b = x mod y
# in: a, x, y
# out: b

# a = 2
# x = 290707924192892686920253390955676600323331633814839708838347288502692494699485764473635783441705302268064111648851157070038783719749721994682837294625334517914882191486257362565066745587415388291939979195637720350919055988532145531805200483161599965215275808797976727969023747299578173497083532351976473770041800769265319548352841139802163279116490053292316399038329210043455932786945180855178341998049756983301499491011851026499269682821602212971062877270127451987836730083380463825717889123804613394241190839837791281657872259492589868751745327696030438893865069941066073554427558697972551085353027574529823439588670263047287131740802375738439636789806332323994866753085014446479034974063195632514803340511247735647970572837053148490258113394359072976858781060349776921428492973183958437965966963122069107876143476772436757554253049619918403996315720023020827394900507088006299225934263699192253079026440287311664705744424959801981503191480257138833694306501816837037995549817186335377411638035575004595417788588264823861850877111374085336446477943372458378834664678094751978400910288151519902977326995118727880223621964441498323865158898463327323193833062919619201107279964663654606753750042791368210261574897455830722232022689695292080269205470491791950839486861811469879413313773338916781857981641910031441448964144000585506870170898052132929034349451945051362244755750988705018897859238859476967568556992146975789444151432386692872801263000639711599152191790766776280
# y = 449703347709287328982446812318870158230369688625894307953604074502413258045265502496365998383562119915565080518077360839705004058211784369656486678307007348691991136610142919372779782779111507129101110674559235388392082113417306002050124215904803026894400155194275424834577942500150410440057660679460918645357376095613079720172148302097893734034788458122333816759162605888879531594217661921547293164281934920669935417080156833072528358511807757748554348615957977663784762124746554638152693469580761002437793837094101338408017407251986116589240523625340964025531357446706263871843489143068620501020284421781243879675292060268876353250854369189182926055204229002568224846436918153245720514450234433170717311083868591477186061896282790880850797471658321324127334704438430354844770131980049668516350774939625369909869906362174015628078258039638111064842324979997867746404806457329528690722757322373158670827203350590809390932986616805533168714686834174965211242863201076482127152571774960580915318022303418111346406295217571564155573765371519749325922145875128395909112254242027512400564855444101325427710643212690768272048881411988830011985059218048684311349415764441760364762942692722834850287985399559042457470942580456516395188637916303814055777357738894264037988945951468416861647204658893837753361851667573185920779272635885127149348845064478121843462789367112698673780005436144393573832498203659056909233757206537514290993810628872250841862059672570704733990716282248839
# b = sympy.discrete_log(y,x,a)
# print(b)

#素数
# sub_q = 168992529793593315757895995101430241994953638330919314800130536809801824971112039572562389449584350643924391984800978193707795909956472992631004290479273525116959461856227262232600089176950810729475058260332177626961286009876630340945093629959302803189668904123890991069113826241497783666995751391361028949651
# q1 = 103766439849465588084625049495793857634556517064563488433148224524638105971161051763127718438062862548184814747601299494052813662851459740127499557785398714481909461631996020048315790167967699932967974484481209879664173009585231469785141628982021847883945871201430155071257803163523612863113967495969578605521
# q2 = 151010734276916939790591461278981486442548035032350797306496105136358723586953123484087860176438629843688462671681777513652947555325607414858514566053513243083627810686084890261120641161987614435114887565491866120507844566210561620503961205851409386041194326728437073995372322433035153519757017396063066469743
# q = pow(sub_q,q2,q1)
# #q = sub_q ** q2 % q1
# print(sympy.nextprime(q))
#
# P = [0 for i in range(17)]
# P[9] = 206027926847308612719677572554991143421
# n = 206027926847308612719677572554991143421
# phi = 206027926847308612719677572554991143420
# c = 213671742765908980787116579976289600595864704574134469173111790965233629909513884704158446946409910475727584342641848597858942209151114627306286393390259700239698869487469080881267182803062488043469138252786381822646126962323295676431679988602406971858136496624861228526070581338082202663895710929460596143281673761666804565161435963957655012011051936180536581488499059517946308650135300428672486819645279969693519039407892941672784362868653243632727928279698588177694171797254644864554162848696210763681197279758130811723700154618280764123396312330032986093579531909363210692564988076206283296967165522152288770019720928264542910922693728918198338839
# for i in range(10,17):
#     P[i] = sympy.nextprime(P[i-1])
#     print(i, P[i])
#     n*= P[i]
#     phi *= P[i]-1
# for i in range(8,0,-1):
#     P[i] = sympy.prevprime(P[i+1])
#     print(i,P[i])
#     n *= P[i]
#     phi *= P[i]-1
# print(n)
# e = 65537
# d = gmpy2.invert(e,phi)
# p = pow(c,d,n)
# print(p)
# print(sympy.nextprime(p))
# p = 118153578345562250550767057731385782963063734586321112579869747650001448473633860305142281504862521928246520876300707405515141444727550839066835195905927281903880307860942630322499106164191736174201506457157272220802515607939618476716593888428832962374494147723577980992661629254713116923690067827155668889571
# q = 118975085954858660642562584152139261422493348532593400307960127317249511761542030451912561362687361053191375307180413931721355251895350936376781657674896801388806379750757264377396608174235075021854614328009897408824235800167369204203680938298803752964983358298299699273425596382268869237139724754214443556383
# factor2 = 2021 * p + 2020 * q
# if factor2 < 0:
#     factor2 = (-1) * factor2
# print(sympy.nextprime(factor2))

#中国剩余定理 CRT
from sympy import ln
from sympy.ntheory.modular import crt
#m模数列表,r余数列表
# m = [
#     20129615352491765499340112943188317180548761597861300847305827141510465619670536844634558246439230371658836928103063432870245707180355907194284861510906071265352409579441048101084995923962148527097370705452070577098780246282820065573711015664291991372085157016901209114191068574208680397710042842835940428451949500607613634682684113208766694028789275748528254287705759528498986306494267817198340658241873024800336013946294891687591013414935237821291805123285905335762719823771647853378892868896078424572232934360940672962436849523915563328779942134504499568866135266628078485232098208237036724121481835035731201383423,
#     31221650155627849964466413749414700613823841060149524451234901677160009099014018926581094879840097248543411980533066831976617023676225625067854003317018794041723612556008471579060428898117790587991055681380408263382761841625714415879087478072771968160384909919958010983669368360788505288855946124159513118847747998656422521414980295212646675850690937883764000571667574381419144372824211798018586804674824564606122592483286575800685232128273820087791811663878057827386379787882962763290066072231248814920468264741654086011072638211075445447843691049847262485759393290853117072868406861840793895816215956869523289231421,
#     29944537515397953361520922774124192605524711306753835303703478890414163510777460559798334313021216389356251874917792007638299225821018849648520673813786772452822809546571129816310207232883239771324122884804993418958309460009406342872173189008449237959577469114158991202433476710581356243815713762802478454390273808377430685157110095496727966308001254107517967559384019734279861840997239176254236069001453544559786063915970071130087811123912044312219535513880663913831358790376650439083660611831156205113873793106880255882114422025746986403355066996567909581710647746463994280444700922867397754748628425967488232530303,
#     25703437855600135215185778453583925446912731661604054184163883272265503323016295700357253105301146726667897497435532579974951478354570415554221401778536104737296154316056314039449116386494323668483749833147800557403368489542273169489080222009368903993658498263905567516798684211462607069796613434661148186901892016282065916190920443378756167250809872483501712225782004396969996983057423942607174314132598421269169722518224478248836881076484639837343079324636997145199835034833367743079935361276149990997875905313642775214486046381368619638551892292787783137622261433528915269333426768947358552919740901860982679180791]
# r = [
#     19131432661217908470262338421299691998526157790583544156741981238822158563988520225986915234570037383888112724408392918113942721994125505014727545946133307329781747600302829588248042922635714391033431930411180545085316438084317927348705241927570432757892985091396044950085462429575440060652967253845041398399648442340042970814415571904057667028157512971079384601724816308078631844480110201787343583073815186771790477712040051157180318804422120472007636722063989315320863580631330647116993819777750684150950416298085261478841177681677867236865666207391847046483954029213495373613490690687473081930148461830425717614569,
#     15341898433226638235160072029875733826956799982958107910250055958334922460202554924743144122170018355117452459472017133614642242411479849369061482860570279863692425621526056862808425135267608544855833358314071200687340442512856575278712986641573012456729402660597339609443771145347181268285050728925993518704899005416187250003304581230701444705157412790787027926810710998646191467130550713600765898234392350153965811595060656753711278308005193370936296124790772689433773414703645703910742193898471800081321469055211709339846392500706523670145259024267858368216902176489814789679472227343363035428541915118378163012031,
#     18715065071648040017967211297231106538139985087685358555650567057715550586464814763683688299037897182845007578571401359061213777645114414642903077003568155508465819628553747173244235936586812445440095450755154357646737087071605811984163416590278352605433362327949048243722556262979909488202442530307505819371594747936223835233586945423522256938701002370646382097846105014981763307729234675737702252155130837154876831885888669150418885088089324534892506199724486783446267336789872782137895552509353583305880144947714110009893134162185382309992604435664777436197587312317224862723813510974493087450281755452428746194446,
#     2282284561224858293138480447463319262474918847630148770112472703128549032592187797289965592615199709857879008271766433462032328498580340968871260189669707518557157836592424973257334362931639831072584824103123486522582531666152363874396482744561758133655406410364442174983227005501860927820871260711861008830120617056883514525798709601744088135999465598338635794275123149165498933580159945032363880613524921913023341209439657145962332213468573402863796920571812418200814817086234262280338221161622789516829363805084715652121739036183264026120868756523770196284142271849879003202190966150390061195469351716819539183797]
#
# a = crt(m,r)
# print(a[0])
# print(gmpy2.iroot(a[0],4)[0])
#
# a = [1]

# 极限
x = sympy.Symbol('x')
f = (x**2 -3*x + 2)/(x**2-4)
print(sympy.limit(f,x,2))

# 积分
f = sympy.exp(x)*(4+sympy.exp(x))**2
print(sympy.integrate(f,(x,0,sympy.ln(2))))

f2 = (1 + 5*sympy.ln(x))/x
print(sympy.integrate(f2,(x,1,sympy.exp(1))))

f3 = x*sympy.sin(x)
print(sympy.integrate(f3,(x,0,sympy.pi/2)))