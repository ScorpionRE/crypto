

# This file was *autogenerated* from the file test.sage
from sage.all_cmdline import *   # import sage library

_sage_const_4 = Integer(4); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_431 = Integer(431); _sage_const_8 = Integer(8); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_129274519334082165644106292383763271862424981496822335330342328217347928093592453953990448827969549377883054831490973006383371688359344675312001881631556371220779971357039899721241880304156884612458373310254854821837978876725801047977081900824202659636258168216028784656056334358157381820784576207338479493823 = Integer(129274519334082165644106292383763271862424981496822335330342328217347928093592453953990448827969549377883054831490973006383371688359344675312001881631556371220779971357039899721241880304156884612458373310254854821837978876725801047977081900824202659636258168216028784656056334358157381820784576207338479493823); _sage_const_146694460234280339612721415368435987068740712812770728817136582256341063038147863645902264969297892447333024201649306207442798919845916187823646745721109151386096190207317810424580842120750075213595282979568495342617919336417068886973047979116994072272482630372638964064972815256237040541007947708358680368391 = Integer(146694460234280339612721415368435987068740712812770728817136582256341063038147863645902264969297892447333024201649306207442798919845916187823646745721109151386096190207317810424580842120750075213595282979568495342617919336417068886973047979116994072272482630372638964064972815256237040541007947708358680368391); _sage_const_8140023566779187828652447593867705813386781164538611122714708931585587727699213769519135028841126072130625547328311301696554048174772606261707345115571968105138543476580875347239912760797035694220505996377127309341770427102697008350472060971360460756799310951343070384766137332401117333917901167639276168214 = Integer(8140023566779187828652447593867705813386781164538611122714708931585587727699213769519135028841126072130625547328311301696554048174772606261707345115571968105138543476580875347239912760797035694220505996377127309341770427102697008350472060971360460756799310951343070384766137332401117333917901167639276168214); _sage_const_65031485534704406281490718325237831433086480239135617407356760819741796565231283220528137697949585150709734732370203390254643835828984376427852793969716489016520923272675090536677771074867975287284694860155903327351119710765174437247599498342292671117884858621418276613385329637307269711179183430246951756029 = Integer(65031485534704406281490718325237831433086480239135617407356760819741796565231283220528137697949585150709734732370203390254643835828984376427852793969716489016520923272675090536677771074867975287284694860155903327351119710765174437247599498342292671117884858621418276613385329637307269711179183430246951756029); _sage_const_25434511525127530194830986592289179576070740435049947678930286998924519588985583799757299734846614343604661534391991096353170465467791358514448923161460366596251448937540153262731348684727026598527904328268639060306102090278287818149679940661579357649191023269947102746200467430583428889484549034314463114080 = Integer(25434511525127530194830986592289179576070740435049947678930286998924519588985583799757299734846614343604661534391991096353170465467791358514448923161460366596251448937540153262731348684727026598527904328268639060306102090278287818149679940661579357649191023269947102746200467430583428889484549034314463114080); _sage_const_126172075578367446151297289668746433680600889845504078949758568698284471307000358407453139846282095477016675769468273204536898117467559575203458221600341760844973676129445394999861380625435418853474246813202182316736885441120197888145039130477114127079444939102267586634051045795627433724810346460217871661901 = Integer(126172075578367446151297289668746433680600889845504078949758568698284471307000358407453139846282095477016675769468273204536898117467559575203458221600341760844973676129445394999861380625435418853474246813202182316736885441120197888145039130477114127079444939102267586634051045795627433724810346460217871661901); _sage_const_9435583236354598287661880148272717764447540972316605192855157484524753847806158586224733743434644389385148450722945845355791145016665856388503878165725148745517696840251674049929524448078129458846254866804153080766917319923905682824180976106679633180818527967145571143203594244851742143986040226240019541346 = Integer(9435583236354598287661880148272717764447540972316605192855157484524753847806158586224733743434644389385148450722945845355791145016665856388503878165725148745517696840251674049929524448078129458846254866804153080766917319923905682824180976106679633180818527967145571143203594244851742143986040226240019541346); _sage_const_75691424835079457343374072990750986689075078863640186724151061449621926239051140991748483370587430224317778303489124525034113533087612981452189061743589227565099659070008017454957304620495920813121234552401715857719372861565651204968408267740732475458128601061676264465241188491988485848198323410127587280471 = Integer(75691424835079457343374072990750986689075078863640186724151061449621926239051140991748483370587430224317778303489124525034113533087612981452189061743589227565099659070008017454957304620495920813121234552401715857719372861565651204968408267740732475458128601061676264465241188491988485848198323410127587280471); _sage_const_20 = Integer(20)#Sage
#e=3, padding: m²+(3^431)k
#m经 k次非线性padding处理后，分别用 k组 (Ni,ei)加密后得 k组 c
def linearPaddingHastads(cArray,nArray,aArray,bArray,eArray,eps):
	if(len(cArray) == len(nArray) == len(aArray) == len(bArray) == len(eArray)):
		for i in range(_sage_const_4 ):
			cArray[i] = Integer(cArray[i])
			nArray[i] = Integer(nArray[i])
			aArray[i] = Integer(aArray[i])
			bArray[i] = Integer(bArray[i])
			eArray[i] = Integer(eArray[i])
		TArray = [-_sage_const_1 ]*_sage_const_4 
		for i in range(_sage_const_4 ):
			arrayToCRT = [_sage_const_0 ]*_sage_const_4 
			arrayToCRT[i] = _sage_const_1 
			TArray[i] = crt(arrayToCRT,nArray)
		P = PolynomialRing(Zmod(prod(nArray)), names=('x',)); (x,) = P._first_ngens(1)
		gArray = [-_sage_const_1 ]*_sage_const_4 
		for i in range(_sage_const_4 ):
			gArray[i] = TArray[i]*(pow(aArray[i]*x**_sage_const_2  + bArray[i],eArray[i]) - cArray[i])
		g = sum(gArray)
		g = g.monic()
		roots = g.small_roots(epsilon=eps)
		if(len(roots)== _sage_const_0 ):
			print("No Solutions found!")
			return -_sage_const_1 
		return roots
	else:
		print("Input error!")

def nonLinearPadding():
    eArr = [_sage_const_3  for i in range(_sage_const_4 )]
    nArr = []
    cArr = []
    aArr = [_sage_const_1  for i in range(_sage_const_4 )]
    bArr = [i * _sage_const_3  ** _sage_const_431  for i in [_sage_const_3 ,_sage_const_8 ,_sage_const_10 ,_sage_const_11 ]]  #e=3的第几组
    C = [[_sage_const_129274519334082165644106292383763271862424981496822335330342328217347928093592453953990448827969549377883054831490973006383371688359344675312001881631556371220779971357039899721241880304156884612458373310254854821837978876725801047977081900824202659636258168216028784656056334358157381820784576207338479493823 , _sage_const_3 , _sage_const_146694460234280339612721415368435987068740712812770728817136582256341063038147863645902264969297892447333024201649306207442798919845916187823646745721109151386096190207317810424580842120750075213595282979568495342617919336417068886973047979116994072272482630372638964064972815256237040541007947708358680368391 , _sage_const_3 ], [_sage_const_8140023566779187828652447593867705813386781164538611122714708931585587727699213769519135028841126072130625547328311301696554048174772606261707345115571968105138543476580875347239912760797035694220505996377127309341770427102697008350472060971360460756799310951343070384766137332401117333917901167639276168214 , _sage_const_3 , _sage_const_65031485534704406281490718325237831433086480239135617407356760819741796565231283220528137697949585150709734732370203390254643835828984376427852793969716489016520923272675090536677771074867975287284694860155903327351119710765174437247599498342292671117884858621418276613385329637307269711179183430246951756029 , _sage_const_8 ], [_sage_const_25434511525127530194830986592289179576070740435049947678930286998924519588985583799757299734846614343604661534391991096353170465467791358514448923161460366596251448937540153262731348684727026598527904328268639060306102090278287818149679940661579357649191023269947102746200467430583428889484549034314463114080 , _sage_const_3 , _sage_const_126172075578367446151297289668746433680600889845504078949758568698284471307000358407453139846282095477016675769468273204536898117467559575203458221600341760844973676129445394999861380625435418853474246813202182316736885441120197888145039130477114127079444939102267586634051045795627433724810346460217871661901 , _sage_const_10 ], [_sage_const_9435583236354598287661880148272717764447540972316605192855157484524753847806158586224733743434644389385148450722945845355791145016665856388503878165725148745517696840251674049929524448078129458846254866804153080766917319923905682824180976106679633180818527967145571143203594244851742143986040226240019541346 , _sage_const_3 , _sage_const_75691424835079457343374072990750986689075078863640186724151061449621926239051140991748483370587430224317778303489124525034113533087612981452189061743589227565099659070008017454957304620495920813121234552401715857719372861565651204968408267740732475458128601061676264465241188491988485848198323410127587280471 , _sage_const_11 ]]
    for c in C:
        nArr.append(c[_sage_const_2 ])
        cArr.append(c[_sage_const_0 ])
        #bArr.append(c[3])
    msg = linearPaddingHastads(cArr,nArr,aArr,bArr,eArr,eps=_sage_const_1 /_sage_const_20 )
    for i in msg:
        print(bytes.fromhex(hex(i)[_sage_const_2 :]))
	
if __name__ == '__main__':
	nonLinearPadding()


