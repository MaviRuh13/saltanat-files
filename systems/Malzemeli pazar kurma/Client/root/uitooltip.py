"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                                                         A�ILIR: uitooltip.py                                                                """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ARATILIR:

def SetShopItem(self, slotIndex):

# KOMPLE DEGISTIRILIR:
#if app.ENABLE_KAYA_MULTI_PRICE:
	def SetShopItem(self, slotIndex):
		itemVnum = shop.GetItemID(slotIndex)
		if 0 == itemVnum:
			return

		price = shop.GetItemPrice(slotIndex)
		suprices = 0
		barprices = 0
		yesilotprices = 0
		kirmiziotprices = 0
		maviotprices = 0
		morotprices = 0
		ruhtasiprices = 0
		
		if slotIndex == 0:
			suprices = constInfo.sufiyat0
			barprices = constInfo.barfiyat0
			yesilotprices = constInfo.yesilot0
			kirmiziotprices = constInfo.kirmiziot0
			maviotprices = constInfo.maviot0
			morotprices = constInfo.morot0
			ruhtasiprices = constInfo.ruhtasi0
		if slotIndex == 1:
			suprices = constInfo.sufiyat1
			barprices = constInfo.barfiyat1
			yesilotprices = constInfo.yesilot1
			kirmiziotprices = constInfo.kirmiziot1
			maviotprices = constInfo.maviot1
			morotprices = constInfo.morot1
			ruhtasiprices = constInfo.ruhtasi1
		if slotIndex == 2:
			suprices = constInfo.sufiyat2
			barprices = constInfo.barfiyat2
			yesilotprices = constInfo.yesilot2
			kirmiziotprices = constInfo.kirmiziot2
			maviotprices = constInfo.maviot2
			morotprices = constInfo.morot2
			ruhtasiprices = constInfo.ruhtasi2
		if slotIndex == 3:
			suprices = constInfo.sufiyat3
			barprices = constInfo.barfiyat3
			yesilotprices = constInfo.yesilot3
			kirmiziotprices = constInfo.kirmiziot3
			maviotprices = constInfo.maviot3
			morotprices = constInfo.morot3
			ruhtasiprices = constInfo.ruhtasi3
		if slotIndex == 4:
			suprices = constInfo.sufiyat4
			barprices = constInfo.barfiyat4
			yesilotprices = constInfo.yesilot4
			kirmiziotprices = constInfo.kirmiziot4
			maviotprices = constInfo.maviot4
			morotprices = constInfo.morot4
			ruhtasiprices = constInfo.ruhtasi4
		if slotIndex == 5:
			suprices = constInfo.sufiyat5
			barprices = constInfo.barfiyat5
			yesilotprices = constInfo.yesilot5
			kirmiziotprices = constInfo.kirmiziot5
			maviotprices = constInfo.maviot5
			morotprices = constInfo.morot5
			ruhtasiprices = constInfo.ruhtasi5
		if slotIndex == 6:
			suprices = constInfo.sufiyat6
			barprices = constInfo.barfiyat6
			yesilotprices = constInfo.yesilot6
			kirmiziotprices = constInfo.kirmiziot6
			maviotprices = constInfo.maviot6
			morotprices = constInfo.morot6
			ruhtasiprices = constInfo.ruhtasi6
		if slotIndex == 7:
			suprices = constInfo.sufiyat7
			barprices = constInfo.barfiyat7
			yesilotprices = constInfo.yesilot7
			kirmiziotprices = constInfo.kirmiziot7
			maviotprices = constInfo.maviot7
			morotprices = constInfo.morot7
			ruhtasiprices = constInfo.ruhtasi7
		if slotIndex == 8:
			suprices = constInfo.sufiyat8
			barprices = constInfo.barfiyat8
			yesilotprices = constInfo.yesilot8
			kirmiziotprices = constInfo.kirmiziot8
			maviotprices = constInfo.maviot8
			morotprices = constInfo.morot8
			ruhtasiprices = constInfo.ruhtasi8
		if slotIndex == 9:
			suprices = constInfo.sufiyat9
			barprices = constInfo.barfiyat9
			yesilotprices = constInfo.yesilot9
			kirmiziotprices = constInfo.kirmiziot9
			maviotprices = constInfo.maviot9
			morotprices = constInfo.morot9
			ruhtasiprices = constInfo.ruhtasi9
		if slotIndex == 10:
			suprices = constInfo.sufiyat10
			barprices = constInfo.barfiyat10
			yesilotprices = constInfo.yesilot10
			kirmiziotprices = constInfo.kirmiziot10
			maviotprices = constInfo.maviot10
			morotprices = constInfo.morot10
			ruhtasiprices = constInfo.ruhtasi10
		if slotIndex == 11:
			suprices = constInfo.sufiyat11
			barprices = constInfo.barfiyat11
			yesilotprices = constInfo.yesilot11
			kirmiziotprices = constInfo.kirmiziot11
			maviotprices = constInfo.maviot11
			morotprices = constInfo.morot11
			ruhtasiprices = constInfo.ruhtasi11
		if slotIndex == 12:
			suprices = constInfo.sufiyat12
			barprices = constInfo.barfiyat12
			yesilotprices = constInfo.yesilot12
			kirmiziotprices = constInfo.kirmiziot12
			maviotprices = constInfo.maviot12
			morotprices = constInfo.morot12
			ruhtasiprices = constInfo.ruhtasi12
		if slotIndex == 13:
			suprices = constInfo.sufiyat13
			barprices = constInfo.barfiyat13
			yesilotprices = constInfo.yesilot13
			kirmiziotprices = constInfo.kirmiziot13
			maviotprices = constInfo.maviot13
			morotprices = constInfo.morot13
			ruhtasiprices = constInfo.ruhtasi13
		if slotIndex == 14:
			suprices = constInfo.sufiyat14
			barprices = constInfo.barfiyat14
			yesilotprices = constInfo.yesilot14
			kirmiziotprices = constInfo.kirmiziot14
			maviotprices = constInfo.maviot14
			morotprices = constInfo.morot14
			ruhtasiprices = constInfo.ruhtasi14
		if slotIndex == 15:
			suprices = constInfo.sufiyat15
			barprices = constInfo.barfiyat15
			yesilotprices = constInfo.yesilot15
			kirmiziotprices = constInfo.kirmiziot15
			maviotprices = constInfo.maviot15
			morotprices = constInfo.morot15
			ruhtasiprices = constInfo.ruhtasi15
		if slotIndex == 16:
			suprices = constInfo.sufiyat16
			barprices = constInfo.barfiyat16
			yesilotprices = constInfo.yesilot16
			kirmiziotprices = constInfo.kirmiziot16
			maviotprices = constInfo.maviot16
			morotprices = constInfo.morot16
			ruhtasiprices = constInfo.ruhtasi16
		if slotIndex == 17:
			suprices = constInfo.sufiyat17
			barprices = constInfo.barfiyat17
			yesilotprices = constInfo.yesilot17
			kirmiziotprices = constInfo.kirmiziot17
			maviotprices = constInfo.maviot17
			morotprices = constInfo.morot17
			ruhtasiprices = constInfo.ruhtasi17
		if slotIndex == 18:
			suprices = constInfo.sufiyat18
			barprices = constInfo.barfiyat18
			yesilotprices = constInfo.yesilot18
			kirmiziotprices = constInfo.kirmiziot18
			maviotprices = constInfo.maviot18
			morotprices = constInfo.morot18
			ruhtasiprices = constInfo.ruhtasi18
		if slotIndex == 19:
			suprices = constInfo.sufiyat19
			barprices = constInfo.barfiyat19
			yesilotprices = constInfo.yesilot19
			kirmiziotprices = constInfo.kirmiziot19
			maviotprices = constInfo.maviot19
			morotprices = constInfo.morot19
			ruhtasiprices = constInfo.ruhtasi19
		if slotIndex == 20:
			suprices = constInfo.sufiyat20
			barprices = constInfo.barfiyat20
			yesilotprices = constInfo.yesilot20
			kirmiziotprices = constInfo.kirmiziot20
			maviotprices = constInfo.maviot20
			morotprices = constInfo.morot20
			ruhtasiprices = constInfo.ruhtasi20
		if slotIndex == 21:
			suprices = constInfo.sufiyat21
			barprices = constInfo.barfiyat21
			yesilotprices = constInfo.yesilot21
			kirmiziotprices = constInfo.kirmiziot21
			maviotprices = constInfo.maviot21
			morotprices = constInfo.morot21
			ruhtasiprices = constInfo.ruhtasi21
		if slotIndex == 22:
			suprices = constInfo.sufiyat22
			barprices = constInfo.barfiyat22
			yesilotprices = constInfo.yesilot22
			kirmiziotprices = constInfo.kirmiziot22
			maviotprices = constInfo.maviot22
			morotprices = constInfo.morot22
			ruhtasiprices = constInfo.ruhtasi22
		if slotIndex == 23:
			suprices = constInfo.sufiyat23
			barprices = constInfo.barfiyat23
			yesilotprices = constInfo.yesilot23
			kirmiziotprices = constInfo.kirmiziot23
			maviotprices = constInfo.maviot23
			morotprices = constInfo.morot23
			ruhtasiprices = constInfo.ruhtasi23
		if slotIndex == 24:
			suprices = constInfo.sufiyat24
			barprices = constInfo.barfiyat24
			yesilotprices = constInfo.yesilot24
			kirmiziotprices = constInfo.kirmiziot24
			maviotprices = constInfo.maviot24
			morotprices = constInfo.morot24
			ruhtasiprices = constInfo.ruhtasi24
		if slotIndex == 25:
			suprices = constInfo.sufiyat25
			barprices = constInfo.barfiyat25
			yesilotprices = constInfo.yesilot25
			kirmiziotprices = constInfo.kirmiziot25
			maviotprices = constInfo.maviot25
			morotprices = constInfo.morot25
			ruhtasiprices = constInfo.ruhtasi25
		if slotIndex == 26:
			suprices = constInfo.sufiyat26
			barprices = constInfo.barfiyat26
			yesilotprices = constInfo.yesilot26
			kirmiziotprices = constInfo.kirmiziot26
			maviotprices = constInfo.maviot26
			morotprices = constInfo.morot26
			ruhtasiprices = constInfo.ruhtasi26
		if slotIndex == 27:
			suprices = constInfo.sufiyat27
			barprices = constInfo.barfiyat27
			yesilotprices = constInfo.yesilot27
			kirmiziotprices = constInfo.kirmiziot27
			maviotprices = constInfo.maviot27
			morotprices = constInfo.morot27
			ruhtasiprices = constInfo.ruhtasi27
		if slotIndex == 28:
			suprices = constInfo.sufiyat28
			barprices = constInfo.barfiyat28
			yesilotprices = constInfo.yesilot28
			kirmiziotprices = constInfo.kirmiziot28
			maviotprices = constInfo.maviot28
			morotprices = constInfo.morot28
			ruhtasiprices = constInfo.ruhtasi28
		if slotIndex == 29:
			suprices = constInfo.sufiyat29
			barprices = constInfo.barfiyat29
			yesilotprices = constInfo.yesilot29
			kirmiziotprices = constInfo.kirmiziot29
			maviotprices = constInfo.maviot29
			morotprices = constInfo.morot29
			ruhtasiprices = constInfo.ruhtasi29
		if slotIndex == 30:
			suprices = constInfo.sufiyat30
			barprices = constInfo.barfiyat30
			yesilotprices = constInfo.yesilot30
			kirmiziotprices = constInfo.kirmiziot30
			maviotprices = constInfo.maviot30
			morotprices = constInfo.morot30
			ruhtasiprices = constInfo.ruhtasi30
		if slotIndex == 31:
			suprices = constInfo.sufiyat31
			barprices = constInfo.barfiyat31
			yesilotprices = constInfo.yesilot31
			kirmiziotprices = constInfo.kirmiziot31
			maviotprices = constInfo.maviot31
			morotprices = constInfo.morot31
			ruhtasiprices = constInfo.ruhtasi31
		if slotIndex == 32:
			suprices = constInfo.sufiyat32
			barprices = constInfo.barfiyat32
			yesilotprices = constInfo.yesilot32
			kirmiziotprices = constInfo.kirmiziot32
			maviotprices = constInfo.maviot32
			morotprices = constInfo.morot32
			ruhtasiprices = constInfo.ruhtasi32
		if slotIndex == 33:
			suprices = constInfo.sufiyat33
			barprices = constInfo.barfiyat33
			yesilotprices = constInfo.yesilot33
			kirmiziotprices = constInfo.kirmiziot33
			maviotprices = constInfo.maviot33
			morotprices = constInfo.morot33
			ruhtasiprices = constInfo.ruhtasi33
		if slotIndex == 34:
			suprices = constInfo.sufiyat34
			barprices = constInfo.barfiyat34
			yesilotprices = constInfo.yesilot34
			kirmiziotprices = constInfo.kirmiziot34
			maviotprices = constInfo.maviot34
			morotprices = constInfo.morot34
			ruhtasiprices = constInfo.ruhtasi34
		if slotIndex == 35:
			suprices = constInfo.sufiyat35
			barprices = constInfo.barfiyat35
			yesilotprices = constInfo.yesilot35
			kirmiziotprices = constInfo.kirmiziot35
			maviotprices = constInfo.maviot35
			morotprices = constInfo.morot35
			ruhtasiprices = constInfo.ruhtasi35
		if slotIndex == 36:
			suprices = constInfo.sufiyat36
			barprices = constInfo.barfiyat36
			yesilotprices = constInfo.yesilot36
			kirmiziotprices = constInfo.kirmiziot36
			maviotprices = constInfo.maviot36
			morotprices = constInfo.morot36
			ruhtasiprices = constInfo.ruhtasi36
		if slotIndex == 37:
			suprices = constInfo.sufiyat37
			barprices = constInfo.barfiyat37
			yesilotprices = constInfo.yesilot37
			kirmiziotprices = constInfo.kirmiziot37
			maviotprices = constInfo.maviot37
			morotprices = constInfo.morot37
			ruhtasiprices = constInfo.ruhtasi37
		if slotIndex == 38:
			suprices = constInfo.sufiyat38
			barprices = constInfo.barfiyat38
			yesilotprices = constInfo.yesilot38
			kirmiziotprices = constInfo.kirmiziot38
			maviotprices = constInfo.maviot38
			morotprices = constInfo.morot38
			ruhtasiprices = constInfo.ruhtasi38
		if slotIndex == 39:
			suprices = constInfo.sufiyat39
			barprices = constInfo.barfiyat39
			yesilotprices = constInfo.yesilot39
			kirmiziotprices = constInfo.kirmiziot39
			maviotprices = constInfo.maviot39
			morotprices = constInfo.morot39
			ruhtasiprices = constInfo.ruhtasi39
		if slotIndex == 40:
			suprices = constInfo.sufiyat40
			barprices = constInfo.barfiyat40
			yesilotprices = constInfo.yesilot40
			kirmiziotprices = constInfo.kirmiziot40
			maviotprices = constInfo.maviot40
			morotprices = constInfo.morot40
			ruhtasiprices = constInfo.ruhtasi40
		if slotIndex == 41:
			suprices = constInfo.sufiyat41
			barprices = constInfo.barfiyat41
			yesilotprices = constInfo.yesilot41
			kirmiziotprices = constInfo.kirmiziot41
			maviotprices = constInfo.maviot41
			morotprices = constInfo.morot41
			ruhtasiprices = constInfo.ruhtasi41
		if slotIndex == 42:
			suprices = constInfo.sufiyat42
			barprices = constInfo.barfiyat42
			yesilotprices = constInfo.yesilot42
			kirmiziotprices = constInfo.kirmiziot42
			maviotprices = constInfo.maviot42
			morotprices = constInfo.morot42
			ruhtasiprices = constInfo.ruhtasi42
		if slotIndex == 43:
			suprices = constInfo.sufiyat43
			barprices = constInfo.barfiyat43
			yesilotprices = constInfo.yesilot43
			kirmiziotprices = constInfo.kirmiziot43
			maviotprices = constInfo.maviot43
			morotprices = constInfo.morot43
			ruhtasiprices = constInfo.ruhtasi43
		if slotIndex == 44:
			suprices = constInfo.sufiyat44
			barprices = constInfo.barfiyat44
			yesilotprices = constInfo.yesilot44
			kirmiziotprices = constInfo.kirmiziot44
			maviotprices = constInfo.maviot44
			morotprices = constInfo.morot44
			ruhtasiprices = constInfo.ruhtasi44
		if slotIndex == 45:
			suprices = constInfo.sufiyat45
			barprices = constInfo.barfiyat45
			yesilotprices = constInfo.yesilot45
			kirmiziotprices = constInfo.kirmiziot45
			maviotprices = constInfo.maviot45
			morotprices = constInfo.morot45
			ruhtasiprices = constInfo.ruhtasi45
		if slotIndex == 46:
			suprices = constInfo.sufiyat46
			barprices = constInfo.barfiyat46
			yesilotprices = constInfo.yesilot46
			kirmiziotprices = constInfo.kirmiziot46
			maviotprices = constInfo.maviot46
			morotprices = constInfo.morot46
			ruhtasiprices = constInfo.ruhtasi46
		if slotIndex == 47:
			suprices = constInfo.sufiyat47
			barprices = constInfo.barfiyat47
			yesilotprices = constInfo.yesilot47
			kirmiziotprices = constInfo.kirmiziot47
			maviotprices = constInfo.maviot47
			morotprices = constInfo.morot47
			ruhtasiprices = constInfo.ruhtasi47
		if slotIndex == 48:
			suprices = constInfo.sufiyat48
			barprices = constInfo.barfiyat48
			yesilotprices = constInfo.yesilot48
			kirmiziotprices = constInfo.kirmiziot48
			maviotprices = constInfo.maviot48
			morotprices = constInfo.morot48
			ruhtasiprices = constInfo.ruhtasi48
		if slotIndex == 49:
			suprices = constInfo.sufiyat49
			barprices = constInfo.barfiyat49
			yesilotprices = constInfo.yesilot49
			kirmiziotprices = constInfo.kirmiziot49
			maviotprices = constInfo.maviot49
			morotprices = constInfo.morot49
			ruhtasiprices = constInfo.ruhtasi49
		if slotIndex == 50:
			suprices = constInfo.sufiyat50
			barprices = constInfo.barfiyat50
			yesilotprices = constInfo.yesilot50
			kirmiziotprices = constInfo.kirmiziot50
			maviotprices = constInfo.maviot50
			morotprices = constInfo.morot50
			ruhtasiprices = constInfo.ruhtasi50
		if slotIndex == 51:
			suprices = constInfo.sufiyat51
			barprices = constInfo.barfiyat51
			yesilotprices = constInfo.yesilot51
			kirmiziotprices = constInfo.kirmiziot51
			maviotprices = constInfo.maviot51
			morotprices = constInfo.morot51
			ruhtasiprices = constInfo.ruhtasi51
		if slotIndex == 52:
			suprices = constInfo.sufiyat52
			barprices = constInfo.barfiyat52
			yesilotprices = constInfo.yesilot52
			kirmiziotprices = constInfo.kirmiziot52
			maviotprices = constInfo.maviot52
			morotprices = constInfo.morot52
			ruhtasiprices = constInfo.ruhtasi52
		if slotIndex == 53:
			suprices = constInfo.sufiyat53
			barprices = constInfo.barfiyat53
			yesilotprices = constInfo.yesilot53
			kirmiziotprices = constInfo.kirmiziot53
			maviotprices = constInfo.maviot53
			morotprices = constInfo.morot53
			ruhtasiprices = constInfo.ruhtasi53
		if slotIndex == 54:
			suprices = constInfo.sufiyat54
			barprices = constInfo.barfiyat54
			yesilotprices = constInfo.yesilot54
			kirmiziotprices = constInfo.kirmiziot54
			maviotprices = constInfo.maviot54
			morotprices = constInfo.morot54
			ruhtasiprices = constInfo.ruhtasi54
		if slotIndex == 55:
			suprices = constInfo.sufiyat55
			barprices = constInfo.barfiyat55
			yesilotprices = constInfo.yesilot55
			kirmiziotprices = constInfo.kirmiziot55
			maviotprices = constInfo.maviot55
			morotprices = constInfo.morot55
			ruhtasiprices = constInfo.ruhtasi55
		if slotIndex == 56:
			suprices = constInfo.sufiyat56
			barprices = constInfo.barfiyat56
			yesilotprices = constInfo.yesilot56
			kirmiziotprices = constInfo.kirmiziot56
			maviotprices = constInfo.maviot56
			morotprices = constInfo.morot56
			ruhtasiprices = constInfo.ruhtasi56
		if slotIndex == 57:
			suprices = constInfo.sufiyat57
			barprices = constInfo.barfiyat57
			yesilotprices = constInfo.yesilot57
			kirmiziotprices = constInfo.kirmiziot57
			maviotprices = constInfo.maviot57
			morotprices = constInfo.morot57
			ruhtasiprices = constInfo.ruhtasi57
		if slotIndex == 58:
			suprices = constInfo.sufiyat58
			barprices = constInfo.barfiyat58
			yesilotprices = constInfo.yesilot58
			kirmiziotprices = constInfo.kirmiziot58
			maviotprices = constInfo.maviot58
			morotprices = constInfo.morot58
			ruhtasiprices = constInfo.ruhtasi58
		if slotIndex == 59:
			suprices = constInfo.sufiyat59
			barprices = constInfo.barfiyat59
			yesilotprices = constInfo.yesilot59
			kirmiziotprices = constInfo.kirmiziot59
			maviotprices = constInfo.maviot59
			morotprices = constInfo.morot59
			ruhtasiprices = constInfo.ruhtasi59
		if slotIndex == 60:
			suprices = constInfo.sufiyat60
			barprices = constInfo.barfiyat60
			yesilotprices = constInfo.yesilot60
			kirmiziotprices = constInfo.kirmiziot60
			maviotprices = constInfo.maviot60
			morotprices = constInfo.morot60
			ruhtasiprices = constInfo.ruhtasi60
		if slotIndex == 61:
			suprices = constInfo.sufiyat61
			barprices = constInfo.barfiyat61
			yesilotprices = constInfo.yesilot61
			kirmiziotprices = constInfo.kirmiziot61
			maviotprices = constInfo.maviot61
			morotprices = constInfo.morot61
			ruhtasiprices = constInfo.ruhtasi61
		if slotIndex == 62:
			suprices = constInfo.sufiyat62
			barprices = constInfo.barfiyat62
			yesilotprices = constInfo.yesilot62
			kirmiziotprices = constInfo.kirmiziot62
			maviotprices = constInfo.maviot62
			morotprices = constInfo.morot62
			ruhtasiprices = constInfo.ruhtasi62
		if slotIndex == 63:
			suprices = constInfo.sufiyat63
			barprices = constInfo.barfiyat63
			yesilotprices = constInfo.yesilot63
			kirmiziotprices = constInfo.kirmiziot63
			maviotprices = constInfo.maviot63
			morotprices = constInfo.morot63
			ruhtasiprices = constInfo.ruhtasi63
		if slotIndex == 64:
			suprices = constInfo.sufiyat64
			barprices = constInfo.barfiyat64
			yesilotprices = constInfo.yesilot64
			kirmiziotprices = constInfo.kirmiziot64
			maviotprices = constInfo.maviot64
			morotprices = constInfo.morot64
			ruhtasiprices = constInfo.ruhtasi64
		if slotIndex == 65:
			suprices = constInfo.sufiyat65
			barprices = constInfo.barfiyat65
			yesilotprices = constInfo.yesilot65
			kirmiziotprices = constInfo.kirmiziot65
			maviotprices = constInfo.maviot65
			morotprices = constInfo.morot65
			ruhtasiprices = constInfo.ruhtasi65
		if slotIndex == 66:
			suprices = constInfo.sufiyat66
			barprices = constInfo.barfiyat66
			yesilotprices = constInfo.yesilot66
			kirmiziotprices = constInfo.kirmiziot66
			maviotprices = constInfo.maviot66
			morotprices = constInfo.morot66
			ruhtasiprices = constInfo.ruhtasi66
		if slotIndex == 67:
			suprices = constInfo.sufiyat67
			barprices = constInfo.barfiyat67
			yesilotprices = constInfo.yesilot67
			kirmiziotprices = constInfo.kirmiziot67
			maviotprices = constInfo.maviot67
			morotprices = constInfo.morot67
			ruhtasiprices = constInfo.ruhtasi67
		if slotIndex == 68:
			suprices = constInfo.sufiyat68
			barprices = constInfo.barfiyat68
			yesilotprices = constInfo.yesilot68
			kirmiziotprices = constInfo.kirmiziot68
			maviotprices = constInfo.maviot68
			morotprices = constInfo.morot68
			ruhtasiprices = constInfo.ruhtasi68
		if slotIndex == 69:
			suprices = constInfo.sufiyat69
			barprices = constInfo.barfiyat69
			yesilotprices = constInfo.yesilot69
			kirmiziotprices = constInfo.kirmiziot69
			maviotprices = constInfo.maviot69
			morotprices = constInfo.morot69
			ruhtasiprices = constInfo.ruhtasi69
		if slotIndex == 70:
			suprices = constInfo.sufiyat70
			barprices = constInfo.barfiyat70
			yesilotprices = constInfo.yesilot70
			kirmiziotprices = constInfo.kirmiziot70
			maviotprices = constInfo.maviot70
			morotprices = constInfo.morot70
			ruhtasiprices = constInfo.ruhtasi70
		if slotIndex == 71:
			suprices = constInfo.sufiyat71
			barprices = constInfo.barfiyat71
			yesilotprices = constInfo.yesilot71
			kirmiziotprices = constInfo.kirmiziot71
			maviotprices = constInfo.maviot71
			morotprices = constInfo.morot71
			ruhtasiprices = constInfo.ruhtasi71
		if slotIndex == 72:
			suprices = constInfo.sufiyat72
			barprices = constInfo.barfiyat72
			yesilotprices = constInfo.yesilot72
			kirmiziotprices = constInfo.kirmiziot72
			maviotprices = constInfo.maviot72
			morotprices = constInfo.morot72
			ruhtasiprices = constInfo.ruhtasi72
		if slotIndex == 73:
			suprices = constInfo.sufiyat73
			barprices = constInfo.barfiyat73
			yesilotprices = constInfo.yesilot73
			kirmiziotprices = constInfo.kirmiziot73
			maviotprices = constInfo.maviot73
			morotprices = constInfo.morot73
			ruhtasiprices = constInfo.ruhtasi73
		if slotIndex == 74:
			suprices = constInfo.sufiyat74
			barprices = constInfo.barfiyat74
			yesilotprices = constInfo.yesilot74
			kirmiziotprices = constInfo.kirmiziot74
			maviotprices = constInfo.maviot74
			morotprices = constInfo.morot74
			ruhtasiprices = constInfo.ruhtasi74
		if slotIndex == 75:
			suprices = constInfo.sufiyat75
			barprices = constInfo.barfiyat75
			yesilotprices = constInfo.yesilot75
			kirmiziotprices = constInfo.kirmiziot75
			maviotprices = constInfo.maviot75
			morotprices = constInfo.morot75
			ruhtasiprices = constInfo.ruhtasi75
		if slotIndex == 76:
			suprices = constInfo.sufiyat76
			barprices = constInfo.barfiyat76
			yesilotprices = constInfo.yesilot76
			kirmiziotprices = constInfo.kirmiziot76
			maviotprices = constInfo.maviot76
			morotprices = constInfo.morot76
			ruhtasiprices = constInfo.ruhtasi76
		if slotIndex == 77:
			suprices = constInfo.sufiyat77
			barprices = constInfo.barfiyat77
			yesilotprices = constInfo.yesilot77
			kirmiziotprices = constInfo.kirmiziot77
			maviotprices = constInfo.maviot77
			morotprices = constInfo.morot77
			ruhtasiprices = constInfo.ruhtasi77
		if slotIndex == 78:
			suprices = constInfo.sufiyat78
			barprices = constInfo.barfiyat78
			yesilotprices = constInfo.yesilot78
			kirmiziotprices = constInfo.kirmiziot78
			maviotprices = constInfo.maviot78
			morotprices = constInfo.morot78
			ruhtasiprices = constInfo.ruhtasi78
		if slotIndex == 79:
			suprices = constInfo.sufiyat79
			barprices = constInfo.barfiyat79
			yesilotprices = constInfo.yesilot79
			kirmiziotprices = constInfo.kirmiziot79
			maviotprices = constInfo.maviot79
			morotprices = constInfo.morot79
			ruhtasiprices = constInfo.ruhtasi79
		if slotIndex == 80:
			suprices = constInfo.sufiyat80
			barprices = constInfo.barfiyat80
			yesilotprices = constInfo.yesilot80
			kirmiziotprices = constInfo.kirmiziot80
			maviotprices = constInfo.maviot80
			morotprices = constInfo.morot80
			ruhtasiprices = constInfo.ruhtasi80
		if slotIndex == 81:
			suprices = constInfo.sufiyat81
			barprices = constInfo.barfiyat81
			yesilotprices = constInfo.yesilot81
			kirmiziotprices = constInfo.kirmiziot81
			maviotprices = constInfo.maviot81
			morotprices = constInfo.morot81
			ruhtasiprices = constInfo.ruhtasi81
		if slotIndex == 82:
			suprices = constInfo.sufiyat82
			barprices = constInfo.barfiyat82
			yesilotprices = constInfo.yesilot82
			kirmiziotprices = constInfo.kirmiziot82
			maviotprices = constInfo.maviot82
			morotprices = constInfo.morot82
			ruhtasiprices = constInfo.ruhtasi82
		if slotIndex == 83:
			suprices = constInfo.sufiyat83
			barprices = constInfo.barfiyat83
			yesilotprices = constInfo.yesilot83
			kirmiziotprices = constInfo.kirmiziot83
			maviotprices = constInfo.maviot83
			morotprices = constInfo.morot83
			ruhtasiprices = constInfo.ruhtasi83
		if slotIndex == 84:
			suprices = constInfo.sufiyat84
			barprices = constInfo.barfiyat84
			yesilotprices = constInfo.yesilot84
			kirmiziotprices = constInfo.kirmiziot84
			maviotprices = constInfo.maviot84
			morotprices = constInfo.morot84
			ruhtasiprices = constInfo.ruhtasi84
		if slotIndex == 85:
			suprices = constInfo.sufiyat85
			barprices = constInfo.barfiyat85
			yesilotprices = constInfo.yesilot85
			kirmiziotprices = constInfo.kirmiziot85
			maviotprices = constInfo.maviot85
			morotprices = constInfo.morot85
			ruhtasiprices = constInfo.ruhtasi85
		if slotIndex == 86:
			suprices = constInfo.sufiyat86
			barprices = constInfo.barfiyat86
			yesilotprices = constInfo.yesilot86
			kirmiziotprices = constInfo.kirmiziot86
			maviotprices = constInfo.maviot86
			morotprices = constInfo.morot86
			ruhtasiprices = constInfo.ruhtasi86
		if slotIndex == 87:
			suprices = constInfo.sufiyat87
			barprices = constInfo.barfiyat87
			yesilotprices = constInfo.yesilot87
			kirmiziotprices = constInfo.kirmiziot87
			maviotprices = constInfo.maviot87
			morotprices = constInfo.morot87
			ruhtasiprices = constInfo.ruhtasi87
		if slotIndex == 88:
			suprices = constInfo.sufiyat88
			barprices = constInfo.barfiyat88
			yesilotprices = constInfo.yesilot88
			kirmiziotprices = constInfo.kirmiziot88
			maviotprices = constInfo.maviot88
			morotprices = constInfo.morot88
			ruhtasiprices = constInfo.ruhtasi88
		if slotIndex == 89:
			suprices = constInfo.sufiyat89
			barprices = constInfo.barfiyat89
			yesilotprices = constInfo.yesilot89
			kirmiziotprices = constInfo.kirmiziot89
			maviotprices = constInfo.maviot89
			morotprices = constInfo.morot89
			ruhtasiprices = constInfo.ruhtasi89
		if slotIndex == 90:
			suprices = constInfo.sufiyat90
			barprices = constInfo.barfiyat90
			yesilotprices = constInfo.yesilot90
			kirmiziotprices = constInfo.kirmiziot90
			maviotprices = constInfo.maviot90
			morotprices = constInfo.morot90
			ruhtasiprices = constInfo.ruhtasi90
		if slotIndex == 91:
			suprices = constInfo.sufiyat91
			barprices = constInfo.barfiyat91
			yesilotprices = constInfo.yesilot91
			kirmiziotprices = constInfo.kirmiziot91
			maviotprices = constInfo.maviot91
			morotprices = constInfo.morot91
			ruhtasiprices = constInfo.ruhtasi91
		if slotIndex == 92:
			suprices = constInfo.sufiyat92
			barprices = constInfo.barfiyat92
			yesilotprices = constInfo.yesilot92
			kirmiziotprices = constInfo.kirmiziot92
			maviotprices = constInfo.maviot92
			morotprices = constInfo.morot92
			ruhtasiprices = constInfo.ruhtasi92
		if slotIndex == 93:
			suprices = constInfo.sufiyat93
			barprices = constInfo.barfiyat93
			yesilotprices = constInfo.yesilot93
			kirmiziotprices = constInfo.kirmiziot93
			maviotprices = constInfo.maviot93
			morotprices = constInfo.morot93
			ruhtasiprices = constInfo.ruhtasi93
		if slotIndex == 94:
			suprices = constInfo.sufiyat94
			barprices = constInfo.barfiyat94
			yesilotprices = constInfo.yesilot94
			kirmiziotprices = constInfo.kirmiziot94
			maviotprices = constInfo.maviot94
			morotprices = constInfo.morot94
			ruhtasiprices = constInfo.ruhtasi94
		if slotIndex == 95:
			suprices = constInfo.sufiyat95
			barprices = constInfo.barfiyat95
			yesilotprices = constInfo.yesilot95
			kirmiziotprices = constInfo.kirmiziot95
			maviotprices = constInfo.maviot95
			morotprices = constInfo.morot95
			ruhtasiprices = constInfo.ruhtasi95
		if slotIndex == 96:
			suprices = constInfo.sufiyat96
			barprices = constInfo.barfiyat96
			yesilotprices = constInfo.yesilot96
			kirmiziotprices = constInfo.kirmiziot96
			maviotprices = constInfo.maviot96
			morotprices = constInfo.morot96
			ruhtasiprices = constInfo.ruhtasi96
		if slotIndex == 97:
			suprices = constInfo.sufiyat97
			barprices = constInfo.barfiyat97
			yesilotprices = constInfo.yesilot97
			kirmiziotprices = constInfo.kirmiziot97
			maviotprices = constInfo.maviot97
			morotprices = constInfo.morot97
			ruhtasiprices = constInfo.ruhtasi97
		if slotIndex == 98:
			suprices = constInfo.sufiyat98
			barprices = constInfo.barfiyat98
			yesilotprices = constInfo.yesilot98
			kirmiziotprices = constInfo.kirmiziot98
			maviotprices = constInfo.maviot98
			morotprices = constInfo.morot98
			ruhtasiprices = constInfo.ruhtasi98
		if slotIndex == 99:
			suprices = constInfo.sufiyat99
			barprices = constInfo.barfiyat99
			yesilotprices = constInfo.yesilot99
			kirmiziotprices = constInfo.kirmiziot99
			maviotprices = constInfo.maviot99
			morotprices = constInfo.morot99
			ruhtasiprices = constInfo.ruhtasi99
		if slotIndex == 100:
			suprices = constInfo.sufiyat100
			barprices = constInfo.barfiyat100
			yesilotprices = constInfo.yesilot100
			kirmiziotprices = constInfo.kirmiziot100
			maviotprices = constInfo.maviot100
			morotprices = constInfo.morot100
			ruhtasiprices = constInfo.ruhtasi100
			
		suprice = suprices
		barprice = barprices
		yesilotprice = yesilotprices
		kirmiziotprice = kirmiziotprices
		maviotprice = maviotprices
		morotprice = morotprices
		ruhtasiprice = ruhtasiprices
		
		self.ClearToolTip()
		self.isShopItem = TRUE

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(shop.GetItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(shop.GetItemAttribute(slotIndex, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)
		if constInfo.pazarnasil == 2:
			self.AppendEpPrice(price)
		else:
			## Bar su ile item satma
			self.AppendPrice(price)
			self.Appendsuprices(suprices)
			self.Appendbarprices(barprices)
			self.Appendyesilotprices(yesilotprices)
			self.Appendkirmiziotprices(kirmiziotprices)
			self.Appendmaviotprices(maviotprices)
			self.Appendmorotprices(morotprices)
			self.Appendmoruhtasiprices(ruhtasiprices)
			## Bar su ile item satma


# ARATILIR:

def SetPrivateShopBuilderItem(self, invenType, invenPos, privateShopSlotIndex):

# KOMPLE DEGISTIRILIR:
#if app.ENABLE_KAYA_MULTI_PRICE:
	def SetPrivateShopBuilderItem(self, invenType, invenPos, privateShopSlotIndex):
		itemVnum = player.GetItemIndex(invenType, invenPos)
		if 0 == itemVnum:
			return

		item.SelectItem(itemVnum)
		self.ClearToolTip()
		self.AppendSellingPrice(shop.GetPrivateShopItemPrice(invenType, invenPos))
		
		suprices = 0
		barprices = 0
		yesilotprices = 0
		kirmiziotprices = 0
		maviotprices = 0
		morotprices = 0
		ruhtasiprices = 0
		
		if privateShopSlotIndex == 0:
			suprices = constInfo.sufiyat0
			barprices = constInfo.barfiyat0
			yesilotprices = constInfo.yesilot0
			kirmiziotprices = constInfo.kirmiziot0
			maviotprices = constInfo.maviot0
			morotprices = constInfo.morot0
			ruhtasiprices = constInfo.ruhtasi0
		if privateShopSlotIndex == 1:
			suprices = constInfo.sufiyat1
			barprices = constInfo.barfiyat1
			yesilotprices = constInfo.yesilot1
			kirmiziotprices = constInfo.kirmiziot1
			maviotprices = constInfo.maviot1
			morotprices = constInfo.morot1
			ruhtasiprices = constInfo.ruhtasi1
		if privateShopSlotIndex == 2:
			suprices = constInfo.sufiyat2
			barprices = constInfo.barfiyat2
			yesilotprices = constInfo.yesilot2
			kirmiziotprices = constInfo.kirmiziot2
			maviotprices = constInfo.maviot2
			morotprices = constInfo.morot2
			ruhtasiprices = constInfo.ruhtasi2
		if privateShopSlotIndex == 3:
			suprices = constInfo.sufiyat3
			barprices = constInfo.barfiyat3
			yesilotprices = constInfo.yesilot3
			kirmiziotprices = constInfo.kirmiziot3
			maviotprices = constInfo.maviot3
			morotprices = constInfo.morot3
			ruhtasiprices = constInfo.ruhtasi3
		if privateShopSlotIndex == 4:
			suprices = constInfo.sufiyat4
			barprices = constInfo.barfiyat4
			yesilotprices = constInfo.yesilot4
			kirmiziotprices = constInfo.kirmiziot4
			maviotprices = constInfo.maviot4
			morotprices = constInfo.morot4
			ruhtasiprices = constInfo.ruhtasi4
		if privateShopSlotIndex == 5:
			suprices = constInfo.sufiyat5
			barprices = constInfo.barfiyat5
			yesilotprices = constInfo.yesilot5
			kirmiziotprices = constInfo.kirmiziot5
			maviotprices = constInfo.maviot5
			morotprices = constInfo.morot5
			ruhtasiprices = constInfo.ruhtasi5
		if privateShopSlotIndex == 6:
			suprices = constInfo.sufiyat6
			barprices = constInfo.barfiyat6
			yesilotprices = constInfo.yesilot6
			kirmiziotprices = constInfo.kirmiziot6
			maviotprices = constInfo.maviot6
			morotprices = constInfo.morot6
			ruhtasiprices = constInfo.ruhtasi6
		if privateShopSlotIndex == 7:
			suprices = constInfo.sufiyat7
			barprices = constInfo.barfiyat7
			yesilotprices = constInfo.yesilot7
			kirmiziotprices = constInfo.kirmiziot7
			maviotprices = constInfo.maviot7
			morotprices = constInfo.morot7
			ruhtasiprices = constInfo.ruhtasi7
		if privateShopSlotIndex == 8:
			suprices = constInfo.sufiyat8
			barprices = constInfo.barfiyat8
			yesilotprices = constInfo.yesilot8
			kirmiziotprices = constInfo.kirmiziot8
			maviotprices = constInfo.maviot8
			morotprices = constInfo.morot8
			ruhtasiprices = constInfo.ruhtasi8
		if privateShopSlotIndex == 9:
			suprices = constInfo.sufiyat9
			barprices = constInfo.barfiyat9
			yesilotprices = constInfo.yesilot9
			kirmiziotprices = constInfo.kirmiziot9
			maviotprices = constInfo.maviot9
			morotprices = constInfo.morot9
			ruhtasiprices = constInfo.ruhtasi9
		if privateShopSlotIndex == 10:
			suprices = constInfo.sufiyat10
			barprices = constInfo.barfiyat10
			yesilotprices = constInfo.yesilot10
			kirmiziotprices = constInfo.kirmiziot10
			maviotprices = constInfo.maviot10
			morotprices = constInfo.morot10
			ruhtasiprices = constInfo.ruhtasi10
		if privateShopSlotIndex == 11:
			suprices = constInfo.sufiyat11
			barprices = constInfo.barfiyat11
			yesilotprices = constInfo.yesilot11
			kirmiziotprices = constInfo.kirmiziot11
			maviotprices = constInfo.maviot11
			morotprices = constInfo.morot11
			ruhtasiprices = constInfo.ruhtasi11
		if privateShopSlotIndex == 12:
			suprices = constInfo.sufiyat12
			barprices = constInfo.barfiyat12
			yesilotprices = constInfo.yesilot12
			kirmiziotprices = constInfo.kirmiziot12
			maviotprices = constInfo.maviot12
			morotprices = constInfo.morot12
			ruhtasiprices = constInfo.ruhtasi12
		if privateShopSlotIndex == 13:
			suprices = constInfo.sufiyat13
			barprices = constInfo.barfiyat13
			yesilotprices = constInfo.yesilot13
			kirmiziotprices = constInfo.kirmiziot13
			maviotprices = constInfo.maviot13
			morotprices = constInfo.morot13
			ruhtasiprices = constInfo.ruhtasi13
		if privateShopSlotIndex == 14:
			suprices = constInfo.sufiyat14
			barprices = constInfo.barfiyat14
			yesilotprices = constInfo.yesilot14
			kirmiziotprices = constInfo.kirmiziot14
			maviotprices = constInfo.maviot14
			morotprices = constInfo.morot14
			ruhtasiprices = constInfo.ruhtasi14
		if privateShopSlotIndex == 15:
			suprices = constInfo.sufiyat15
			barprices = constInfo.barfiyat15
			yesilotprices = constInfo.yesilot15
			kirmiziotprices = constInfo.kirmiziot15
			maviotprices = constInfo.maviot15
			morotprices = constInfo.morot15
			ruhtasiprices = constInfo.ruhtasi15
		if privateShopSlotIndex == 16:
			suprices = constInfo.sufiyat16
			barprices = constInfo.barfiyat16
			yesilotprices = constInfo.yesilot16
			kirmiziotprices = constInfo.kirmiziot16
			maviotprices = constInfo.maviot16
			morotprices = constInfo.morot16
			ruhtasiprices = constInfo.ruhtasi16
		if privateShopSlotIndex == 17:
			suprices = constInfo.sufiyat17
			barprices = constInfo.barfiyat17
			yesilotprices = constInfo.yesilot17
			kirmiziotprices = constInfo.kirmiziot17
			maviotprices = constInfo.maviot17
			morotprices = constInfo.morot17
			ruhtasiprices = constInfo.ruhtasi17
		if privateShopSlotIndex == 18:
			suprices = constInfo.sufiyat18
			barprices = constInfo.barfiyat18
			yesilotprices = constInfo.yesilot18
			kirmiziotprices = constInfo.kirmiziot18
			maviotprices = constInfo.maviot18
			morotprices = constInfo.morot18
			ruhtasiprices = constInfo.ruhtasi18
		if privateShopSlotIndex == 19:
			suprices = constInfo.sufiyat19
			barprices = constInfo.barfiyat19
			yesilotprices = constInfo.yesilot19
			kirmiziotprices = constInfo.kirmiziot19
			maviotprices = constInfo.maviot19
			morotprices = constInfo.morot19
			ruhtasiprices = constInfo.ruhtasi19
		if privateShopSlotIndex == 20:
			suprices = constInfo.sufiyat20
			barprices = constInfo.barfiyat20
			yesilotprices = constInfo.yesilot20
			kirmiziotprices = constInfo.kirmiziot20
			maviotprices = constInfo.maviot20
			morotprices = constInfo.morot20
			ruhtasiprices = constInfo.ruhtasi20
		if privateShopSlotIndex == 21:
			suprices = constInfo.sufiyat21
			barprices = constInfo.barfiyat21
			yesilotprices = constInfo.yesilot21
			kirmiziotprices = constInfo.kirmiziot21
			maviotprices = constInfo.maviot21
			morotprices = constInfo.morot21
			ruhtasiprices = constInfo.ruhtasi21
		if privateShopSlotIndex == 22:
			suprices = constInfo.sufiyat22
			barprices = constInfo.barfiyat22
			yesilotprices = constInfo.yesilot22
			kirmiziotprices = constInfo.kirmiziot22
			maviotprices = constInfo.maviot22
			morotprices = constInfo.morot22
			ruhtasiprices = constInfo.ruhtasi22
		if privateShopSlotIndex == 23:
			suprices = constInfo.sufiyat23
			barprices = constInfo.barfiyat23
			yesilotprices = constInfo.yesilot23
			kirmiziotprices = constInfo.kirmiziot23
			maviotprices = constInfo.maviot23
			morotprices = constInfo.morot23
			ruhtasiprices = constInfo.ruhtasi23
		if privateShopSlotIndex == 24:
			suprices = constInfo.sufiyat24
			barprices = constInfo.barfiyat24
			yesilotprices = constInfo.yesilot24
			kirmiziotprices = constInfo.kirmiziot24
			maviotprices = constInfo.maviot24
			morotprices = constInfo.morot24
			ruhtasiprices = constInfo.ruhtasi24
		if privateShopSlotIndex == 25:
			suprices = constInfo.sufiyat25
			barprices = constInfo.barfiyat25
			yesilotprices = constInfo.yesilot25
			kirmiziotprices = constInfo.kirmiziot25
			maviotprices = constInfo.maviot25
			morotprices = constInfo.morot25
			ruhtasiprices = constInfo.ruhtasi25
		if privateShopSlotIndex == 26:
			suprices = constInfo.sufiyat26
			barprices = constInfo.barfiyat26
			yesilotprices = constInfo.yesilot26
			kirmiziotprices = constInfo.kirmiziot26
			maviotprices = constInfo.maviot26
			morotprices = constInfo.morot26
			ruhtasiprices = constInfo.ruhtasi26
		if privateShopSlotIndex == 27:
			suprices = constInfo.sufiyat27
			barprices = constInfo.barfiyat27
			yesilotprices = constInfo.yesilot27
			kirmiziotprices = constInfo.kirmiziot27
			maviotprices = constInfo.maviot27
			morotprices = constInfo.morot27
			ruhtasiprices = constInfo.ruhtasi27
		if privateShopSlotIndex == 28:
			suprices = constInfo.sufiyat28
			barprices = constInfo.barfiyat28
			yesilotprices = constInfo.yesilot28
			kirmiziotprices = constInfo.kirmiziot28
			maviotprices = constInfo.maviot28
			morotprices = constInfo.morot28
			ruhtasiprices = constInfo.ruhtasi28
		if privateShopSlotIndex == 29:
			suprices = constInfo.sufiyat29
			barprices = constInfo.barfiyat29
			yesilotprices = constInfo.yesilot29
			kirmiziotprices = constInfo.kirmiziot29
			maviotprices = constInfo.maviot29
			morotprices = constInfo.morot29
			ruhtasiprices = constInfo.ruhtasi29
		if privateShopSlotIndex == 30:
			suprices = constInfo.sufiyat30
			barprices = constInfo.barfiyat30
			yesilotprices = constInfo.yesilot30
			kirmiziotprices = constInfo.kirmiziot30
			maviotprices = constInfo.maviot30
			morotprices = constInfo.morot30
			ruhtasiprices = constInfo.ruhtasi30
		if privateShopSlotIndex == 31:
			suprices = constInfo.sufiyat31
			barprices = constInfo.barfiyat31
			yesilotprices = constInfo.yesilot31
			kirmiziotprices = constInfo.kirmiziot31
			maviotprices = constInfo.maviot31
			morotprices = constInfo.morot31
			ruhtasiprices = constInfo.ruhtasi31
		if privateShopSlotIndex == 32:
			suprices = constInfo.sufiyat32
			barprices = constInfo.barfiyat32
			yesilotprices = constInfo.yesilot32
			kirmiziotprices = constInfo.kirmiziot32
			maviotprices = constInfo.maviot32
			morotprices = constInfo.morot32
			ruhtasiprices = constInfo.ruhtasi32
		if privateShopSlotIndex == 33:
			suprices = constInfo.sufiyat33
			barprices = constInfo.barfiyat33
			yesilotprices = constInfo.yesilot33
			kirmiziotprices = constInfo.kirmiziot33
			maviotprices = constInfo.maviot33
			morotprices = constInfo.morot33
			ruhtasiprices = constInfo.ruhtasi33
		if privateShopSlotIndex == 34:
			suprices = constInfo.sufiyat34
			barprices = constInfo.barfiyat34
			yesilotprices = constInfo.yesilot34
			kirmiziotprices = constInfo.kirmiziot34
			maviotprices = constInfo.maviot34
			morotprices = constInfo.morot34
			ruhtasiprices = constInfo.ruhtasi34
		if privateShopSlotIndex == 35:
			suprices = constInfo.sufiyat35
			barprices = constInfo.barfiyat35
			yesilotprices = constInfo.yesilot35
			kirmiziotprices = constInfo.kirmiziot35
			maviotprices = constInfo.maviot35
			morotprices = constInfo.morot35
			ruhtasiprices = constInfo.ruhtasi35
		if privateShopSlotIndex == 36:
			suprices = constInfo.sufiyat36
			barprices = constInfo.barfiyat36
			yesilotprices = constInfo.yesilot36
			kirmiziotprices = constInfo.kirmiziot36
			maviotprices = constInfo.maviot36
			morotprices = constInfo.morot36
			ruhtasiprices = constInfo.ruhtasi36
		if privateShopSlotIndex == 37:
			suprices = constInfo.sufiyat37
			barprices = constInfo.barfiyat37
			yesilotprices = constInfo.yesilot37
			kirmiziotprices = constInfo.kirmiziot37
			maviotprices = constInfo.maviot37
			morotprices = constInfo.morot37
			ruhtasiprices = constInfo.ruhtasi37
		if privateShopSlotIndex == 38:
			suprices = constInfo.sufiyat38
			barprices = constInfo.barfiyat38
			yesilotprices = constInfo.yesilot38
			kirmiziotprices = constInfo.kirmiziot38
			maviotprices = constInfo.maviot38
			morotprices = constInfo.morot38
			ruhtasiprices = constInfo.ruhtasi38
		if privateShopSlotIndex == 39:
			suprices = constInfo.sufiyat39
			barprices = constInfo.barfiyat39
			yesilotprices = constInfo.yesilot39
			kirmiziotprices = constInfo.kirmiziot39
			maviotprices = constInfo.maviot39
			morotprices = constInfo.morot39
			ruhtasiprices = constInfo.ruhtasi39
		if privateShopSlotIndex == 40:
			suprices = constInfo.sufiyat40
			barprices = constInfo.barfiyat40
			yesilotprices = constInfo.yesilot40
			kirmiziotprices = constInfo.kirmiziot40
			maviotprices = constInfo.maviot40
			morotprices = constInfo.morot40
			ruhtasiprices = constInfo.ruhtasi40
		if privateShopSlotIndex == 41:
			suprices = constInfo.sufiyat41
			barprices = constInfo.barfiyat41
			yesilotprices = constInfo.yesilot41
			kirmiziotprices = constInfo.kirmiziot41
			maviotprices = constInfo.maviot41
			morotprices = constInfo.morot41
			ruhtasiprices = constInfo.ruhtasi41
		if privateShopSlotIndex == 42:
			suprices = constInfo.sufiyat42
			barprices = constInfo.barfiyat42
			yesilotprices = constInfo.yesilot42
			kirmiziotprices = constInfo.kirmiziot42
			maviotprices = constInfo.maviot42
			morotprices = constInfo.morot42
			ruhtasiprices = constInfo.ruhtasi42
		if privateShopSlotIndex == 43:
			suprices = constInfo.sufiyat43
			barprices = constInfo.barfiyat43
			yesilotprices = constInfo.yesilot43
			kirmiziotprices = constInfo.kirmiziot43
			maviotprices = constInfo.maviot43
			morotprices = constInfo.morot43
			ruhtasiprices = constInfo.ruhtasi43
		if privateShopSlotIndex == 44:
			suprices = constInfo.sufiyat44
			barprices = constInfo.barfiyat44		
			yesilotprices = constInfo.yesilot44
			kirmiziotprices = constInfo.kirmiziot44
			maviotprices = constInfo.maviot44
			morotprices = constInfo.morot44
			ruhtasiprices = constInfo.ruhtasi44
		if privateShopSlotIndex == 45:
			suprices = constInfo.sufiyat45
			barprices = constInfo.barfiyat45
			yesilotprices = constInfo.yesilot45
			kirmiziotprices = constInfo.kirmiziot45
			maviotprices = constInfo.maviot45
			morotprices = constInfo.morot45
			ruhtasiprices = constInfo.ruhtasi45
		if privateShopSlotIndex == 46:
			suprices = constInfo.sufiyat46
			barprices = constInfo.barfiyat46
			yesilotprices = constInfo.yesilot46
			kirmiziotprices = constInfo.kirmiziot46
			maviotprices = constInfo.maviot46
			morotprices = constInfo.morot46
			ruhtasiprices = constInfo.ruhtasi46
		if privateShopSlotIndex == 47:
			suprices = constInfo.sufiyat47
			barprices = constInfo.barfiyat47
			yesilotprices = constInfo.yesilot47
			kirmiziotprices = constInfo.kirmiziot47
			maviotprices = constInfo.maviot47
			morotprices = constInfo.morot47
			ruhtasiprices = constInfo.ruhtasi47
		if privateShopSlotIndex == 48:
			suprices = constInfo.sufiyat48
			barprices = constInfo.barfiyat48
			yesilotprices = constInfo.yesilot48
			kirmiziotprices = constInfo.kirmiziot48
			maviotprices = constInfo.maviot48
			morotprices = constInfo.morot48
			ruhtasiprices = constInfo.ruhtasi48
		if privateShopSlotIndex == 49:
			suprices = constInfo.sufiyat49
			barprices = constInfo.barfiyat49
			yesilotprices = constInfo.yesilot49
			kirmiziotprices = constInfo.kirmiziot49
			maviotprices = constInfo.maviot49
			morotprices = constInfo.morot49
			ruhtasiprices = constInfo.ruhtasi49
		if privateShopSlotIndex == 50:
			suprices = constInfo.sufiyat50
			barprices = constInfo.barfiyat50
			yesilotprices = constInfo.yesilot50
			kirmiziotprices = constInfo.kirmiziot50
			maviotprices = constInfo.maviot50
			morotprices = constInfo.morot50
			ruhtasiprices = constInfo.ruhtasi50
		if privateShopSlotIndex == 51:
			suprices = constInfo.sufiyat51
			barprices = constInfo.barfiyat51
			yesilotprices = constInfo.yesilot51
			kirmiziotprices = constInfo.kirmiziot51
			maviotprices = constInfo.maviot51
			morotprices = constInfo.morot51
			ruhtasiprices = constInfo.ruhtasi51
		if privateShopSlotIndex == 52:
			suprices = constInfo.sufiyat52
			barprices = constInfo.barfiyat52
			yesilotprices = constInfo.yesilot52
			kirmiziotprices = constInfo.kirmiziot52
			maviotprices = constInfo.maviot52
			morotprices = constInfo.morot52
			ruhtasiprices = constInfo.ruhtasi52
		if privateShopSlotIndex == 53:
			suprices = constInfo.sufiyat53
			barprices = constInfo.barfiyat53
			yesilotprices = constInfo.yesilot53
			kirmiziotprices = constInfo.kirmiziot53
			maviotprices = constInfo.maviot53
			morotprices = constInfo.morot53
			ruhtasiprices = constInfo.ruhtasi53
		if privateShopSlotIndex == 54:
			suprices = constInfo.sufiyat54
			barprices = constInfo.barfiyat54
			yesilotprices = constInfo.yesilot54
			kirmiziotprices = constInfo.kirmiziot54
			maviotprices = constInfo.maviot54
			morotprices = constInfo.morot54
			ruhtasiprices = constInfo.ruhtasi54
		if privateShopSlotIndex == 55:
			suprices = constInfo.sufiyat55
			barprices = constInfo.barfiyat55
			yesilotprices = constInfo.yesilot55
			kirmiziotprices = constInfo.kirmiziot55
			maviotprices = constInfo.maviot55
			morotprices = constInfo.morot55
			ruhtasiprices = constInfo.ruhtasi55
		if privateShopSlotIndex == 56:
			suprices = constInfo.sufiyat56
			barprices = constInfo.barfiyat56
			yesilotprices = constInfo.yesilot56
			kirmiziotprices = constInfo.kirmiziot56
			maviotprices = constInfo.maviot56
			morotprices = constInfo.morot56
			ruhtasiprices = constInfo.ruhtasi56
		if privateShopSlotIndex == 57:
			suprices = constInfo.sufiyat57
			barprices = constInfo.barfiyat57
			yesilotprices = constInfo.yesilot57
			kirmiziotprices = constInfo.kirmiziot57
			maviotprices = constInfo.maviot57
			morotprices = constInfo.morot57
			ruhtasiprices = constInfo.ruhtasi57
		if privateShopSlotIndex == 58:
			suprices = constInfo.sufiyat58
			barprices = constInfo.barfiyat58
			yesilotprices = constInfo.yesilot58
			kirmiziotprices = constInfo.kirmiziot58
			maviotprices = constInfo.maviot58
			morotprices = constInfo.morot58
			ruhtasiprices = constInfo.ruhtasi58
		if privateShopSlotIndex == 59:
			suprices = constInfo.sufiyat59
			barprices = constInfo.barfiyat59
			yesilotprices = constInfo.yesilot59
			kirmiziotprices = constInfo.kirmiziot59
			maviotprices = constInfo.maviot59
			morotprices = constInfo.morot59
			ruhtasiprices = constInfo.ruhtasi59
		if privateShopSlotIndex == 60:
			suprices = constInfo.sufiyat60
			barprices = constInfo.barfiyat60
			yesilotprices = constInfo.yesilot60
			kirmiziotprices = constInfo.kirmiziot60
			maviotprices = constInfo.maviot60
			morotprices = constInfo.morot60
			ruhtasiprices = constInfo.ruhtasi60
		if privateShopSlotIndex == 61:
			suprices = constInfo.sufiyat61
			barprices = constInfo.barfiyat61
			yesilotprices = constInfo.yesilot61
			kirmiziotprices = constInfo.kirmiziot61
			maviotprices = constInfo.maviot61
			morotprices = constInfo.morot61
			ruhtasiprices = constInfo.ruhtasi61
		if privateShopSlotIndex == 62:
			suprices = constInfo.sufiyat62
			barprices = constInfo.barfiyat62
			yesilotprices = constInfo.yesilot62
			kirmiziotprices = constInfo.kirmiziot62
			maviotprices = constInfo.maviot62
			morotprices = constInfo.morot62
			ruhtasiprices = constInfo.ruhtasi62
		if privateShopSlotIndex == 63:
			suprices = constInfo.sufiyat63
			barprices = constInfo.barfiyat63
			yesilotprices = constInfo.yesilot63
			kirmiziotprices = constInfo.kirmiziot63
			maviotprices = constInfo.maviot63
			morotprices = constInfo.morot63
			ruhtasiprices = constInfo.ruhtasi63
		if privateShopSlotIndex == 64:
			suprices = constInfo.sufiyat64
			barprices = constInfo.barfiyat64
			yesilotprices = constInfo.yesilot64
			kirmiziotprices = constInfo.kirmiziot64
			maviotprices = constInfo.maviot64
			morotprices = constInfo.morot64
			ruhtasiprices = constInfo.ruhtasi64
		if privateShopSlotIndex == 65:
			suprices = constInfo.sufiyat65
			barprices = constInfo.barfiyat65
			yesilotprices = constInfo.yesilot65
			kirmiziotprices = constInfo.kirmiziot65
			maviotprices = constInfo.maviot65
			morotprices = constInfo.morot65
			ruhtasiprices = constInfo.ruhtasi65
		if privateShopSlotIndex == 66:
			suprices = constInfo.sufiyat66
			barprices = constInfo.barfiyat66
			yesilotprices = constInfo.yesilot66
			kirmiziotprices = constInfo.kirmiziot66
			maviotprices = constInfo.maviot66
			morotprices = constInfo.morot66
			ruhtasiprices = constInfo.ruhtasi66
		if privateShopSlotIndex == 67:
			suprices = constInfo.sufiyat67
			barprices = constInfo.barfiyat67
			yesilotprices = constInfo.yesilot67
			kirmiziotprices = constInfo.kirmiziot67
			maviotprices = constInfo.maviot67
			morotprices = constInfo.morot67
			ruhtasiprices = constInfo.ruhtasi67
		if privateShopSlotIndex == 68:
			suprices = constInfo.sufiyat68
			barprices = constInfo.barfiyat68
			yesilotprices = constInfo.yesilot68
			kirmiziotprices = constInfo.kirmiziot68
			maviotprices = constInfo.maviot68
			morotprices = constInfo.morot68
			ruhtasiprices = constInfo.ruhtasi68
		if privateShopSlotIndex == 69:
			suprices = constInfo.sufiyat69
			barprices = constInfo.barfiyat69
			yesilotprices = constInfo.yesilot69
			kirmiziotprices = constInfo.kirmiziot69
			maviotprices = constInfo.maviot69
			morotprices = constInfo.morot69
			ruhtasiprices = constInfo.ruhtasi69
		if privateShopSlotIndex == 70:
			suprices = constInfo.sufiyat70
			barprices = constInfo.barfiyat70
			yesilotprices = constInfo.yesilot70
			kirmiziotprices = constInfo.kirmiziot70
			maviotprices = constInfo.maviot70
			morotprices = constInfo.morot70
			ruhtasiprices = constInfo.ruhtasi70
		if privateShopSlotIndex == 71:
			suprices = constInfo.sufiyat71
			barprices = constInfo.barfiyat71
			yesilotprices = constInfo.yesilot71
			kirmiziotprices = constInfo.kirmiziot71
			maviotprices = constInfo.maviot71
			morotprices = constInfo.morot71
			ruhtasiprices = constInfo.ruhtasi71
		if privateShopSlotIndex == 72:
			suprices = constInfo.sufiyat72
			barprices = constInfo.barfiyat72
			yesilotprices = constInfo.yesilot72
			kirmiziotprices = constInfo.kirmiziot72
			maviotprices = constInfo.maviot72
			morotprices = constInfo.morot72
			ruhtasiprices = constInfo.ruhtasi72
		if privateShopSlotIndex == 73:
			suprices = constInfo.sufiyat73
			barprices = constInfo.barfiyat73
			yesilotprices = constInfo.yesilot73
			kirmiziotprices = constInfo.kirmiziot73
			maviotprices = constInfo.maviot73
			morotprices = constInfo.morot73
			ruhtasiprices = constInfo.ruhtasi73
		if privateShopSlotIndex == 74:
			suprices = constInfo.sufiyat74
			barprices = constInfo.barfiyat74
			yesilotprices = constInfo.yesilot74
			kirmiziotprices = constInfo.kirmiziot74
			maviotprices = constInfo.maviot74
			morotprices = constInfo.morot74
			ruhtasiprices = constInfo.ruhtasi74
		if privateShopSlotIndex == 75:
			suprices = constInfo.sufiyat75
			barprices = constInfo.barfiyat75
			yesilotprices = constInfo.yesilot75
			kirmiziotprices = constInfo.kirmiziot75
			maviotprices = constInfo.maviot75
			morotprices = constInfo.morot75
			ruhtasiprices = constInfo.ruhtasi75
		if privateShopSlotIndex == 76:
			suprices = constInfo.sufiyat76
			barprices = constInfo.barfiyat76
			yesilotprices = constInfo.yesilot76
			kirmiziotprices = constInfo.kirmiziot76
			maviotprices = constInfo.maviot76
			morotprices = constInfo.morot76
			ruhtasiprices = constInfo.ruhtasi76
		if privateShopSlotIndex == 77:
			suprices = constInfo.sufiyat77
			barprices = constInfo.barfiyat77
			yesilotprices = constInfo.yesilot77
			kirmiziotprices = constInfo.kirmiziot77
			maviotprices = constInfo.maviot77
			morotprices = constInfo.morot77
			ruhtasiprices = constInfo.ruhtasi77
		if privateShopSlotIndex == 78:
			suprices = constInfo.sufiyat78
			barprices = constInfo.barfiyat78
			yesilotprices = constInfo.yesilot78
			kirmiziotprices = constInfo.kirmiziot78
			maviotprices = constInfo.maviot78
			morotprices = constInfo.morot78
			ruhtasiprices = constInfo.ruhtasi78
		if privateShopSlotIndex == 79:
			suprices = constInfo.sufiyat79
			barprices = constInfo.barfiyat79
			yesilotprices = constInfo.yesilot79
			kirmiziotprices = constInfo.kirmiziot79
			maviotprices = constInfo.maviot79
			morotprices = constInfo.morot79
			ruhtasiprices = constInfo.ruhtasi79
		if privateShopSlotIndex == 80:
			suprices = constInfo.sufiyat80
			barprices = constInfo.barfiyat80
			yesilotprices = constInfo.yesilot80
			kirmiziotprices = constInfo.kirmiziot80
			maviotprices = constInfo.maviot80
			morotprices = constInfo.morot80
			ruhtasiprices = constInfo.ruhtasi80
		if privateShopSlotIndex == 81:
			suprices = constInfo.sufiyat81
			barprices = constInfo.barfiyat81
			yesilotprices = constInfo.yesilot81
			kirmiziotprices = constInfo.kirmiziot81
			maviotprices = constInfo.maviot81
			morotprices = constInfo.morot81
			ruhtasiprices = constInfo.ruhtasi81
		if privateShopSlotIndex == 82:
			suprices = constInfo.sufiyat82
			barprices = constInfo.barfiyat82
			yesilotprices = constInfo.yesilot82
			kirmiziotprices = constInfo.kirmiziot82
			maviotprices = constInfo.maviot82
			morotprices = constInfo.morot82
			ruhtasiprices = constInfo.ruhtasi82
		if privateShopSlotIndex == 83:
			suprices = constInfo.sufiyat83
			barprices = constInfo.barfiyat83
			yesilotprices = constInfo.yesilot83
			kirmiziotprices = constInfo.kirmiziot83
			maviotprices = constInfo.maviot83
			morotprices = constInfo.morot83
			ruhtasiprices = constInfo.ruhtasi83
		if privateShopSlotIndex == 84:
			suprices = constInfo.sufiyat84
			barprices = constInfo.barfiyat84
			yesilotprices = constInfo.yesilot84
			kirmiziotprices = constInfo.kirmiziot84
			maviotprices = constInfo.maviot84
			morotprices = constInfo.morot84
			ruhtasiprices = constInfo.ruhtasi84
		if privateShopSlotIndex == 85:
			suprices = constInfo.sufiyat85
			barprices = constInfo.barfiyat85
			yesilotprices = constInfo.yesilot85
			kirmiziotprices = constInfo.kirmiziot85
			maviotprices = constInfo.maviot85
			morotprices = constInfo.morot85
			ruhtasiprices = constInfo.ruhtasi85
		if privateShopSlotIndex == 86:
			suprices = constInfo.sufiyat86
			barprices = constInfo.barfiyat86
			yesilotprices = constInfo.yesilot86
			kirmiziotprices = constInfo.kirmiziot86
			maviotprices = constInfo.maviot86
			morotprices = constInfo.morot86
			ruhtasiprices = constInfo.ruhtasi86
		if privateShopSlotIndex == 87:
			suprices = constInfo.sufiyat87
			barprices = constInfo.barfiyat87
			yesilotprices = constInfo.yesilot87
			kirmiziotprices = constInfo.kirmiziot87
			maviotprices = constInfo.maviot87
			morotprices = constInfo.morot87
			ruhtasiprices = constInfo.ruhtasi87
		if privateShopSlotIndex == 88:
			suprices = constInfo.sufiyat88
			barprices = constInfo.barfiyat88
			yesilotprices = constInfo.yesilot88
			kirmiziotprices = constInfo.kirmiziot88
			maviotprices = constInfo.maviot88
			morotprices = constInfo.morot88
			ruhtasiprices = constInfo.ruhtasi88
		if privateShopSlotIndex == 89:
			suprices = constInfo.sufiyat89
			barprices = constInfo.barfiyat89
			yesilotprices = constInfo.yesilot89
			kirmiziotprices = constInfo.kirmiziot89
			maviotprices = constInfo.maviot89
			morotprices = constInfo.morot89
			ruhtasiprices = constInfo.ruhtasi89
		if privateShopSlotIndex == 90:
			suprices = constInfo.sufiyat90
			barprices = constInfo.barfiyat90
			yesilotprices = constInfo.yesilot90
			kirmiziotprices = constInfo.kirmiziot90
			maviotprices = constInfo.maviot90
			morotprices = constInfo.morot90
			ruhtasiprices = constInfo.ruhtasi90
		if privateShopSlotIndex == 91:
			suprices = constInfo.sufiyat91
			barprices = constInfo.barfiyat91
			yesilotprices = constInfo.yesilot91
			kirmiziotprices = constInfo.kirmiziot91
			maviotprices = constInfo.maviot91
			morotprices = constInfo.morot91
			ruhtasiprices = constInfo.ruhtasi91
		if privateShopSlotIndex == 92:
			suprices = constInfo.sufiyat92
			barprices = constInfo.barfiyat92
			yesilotprices = constInfo.yesilot92
			kirmiziotprices = constInfo.kirmiziot92
			maviotprices = constInfo.maviot92
			morotprices = constInfo.morot92
			ruhtasiprices = constInfo.ruhtasi92
		if privateShopSlotIndex == 93:
			suprices = constInfo.sufiyat93
			barprices = constInfo.barfiyat93
			yesilotprices = constInfo.yesilot93
			kirmiziotprices = constInfo.kirmiziot93
			maviotprices = constInfo.maviot93
			morotprices = constInfo.morot93
			ruhtasiprices = constInfo.ruhtasi93
		if privateShopSlotIndex == 94:
			suprices = constInfo.sufiyat94
			barprices = constInfo.barfiyat94
			yesilotprices = constInfo.yesilot94
			kirmiziotprices = constInfo.kirmiziot94
			maviotprices = constInfo.maviot94
			morotprices = constInfo.morot94
			ruhtasiprices = constInfo.ruhtasi94
		if privateShopSlotIndex == 95:
			suprices = constInfo.sufiyat95
			barprices = constInfo.barfiyat95
			yesilotprices = constInfo.yesilot95
			kirmiziotprices = constInfo.kirmiziot95
			maviotprices = constInfo.maviot95
			morotprices = constInfo.morot95
			ruhtasiprices = constInfo.ruhtasi95
		if privateShopSlotIndex == 96:
			suprices = constInfo.sufiyat96
			barprices = constInfo.barfiyat96
			yesilotprices = constInfo.yesilot96
			kirmiziotprices = constInfo.kirmiziot96
			maviotprices = constInfo.maviot96
			morotprices = constInfo.morot96
			ruhtasiprices = constInfo.ruhtasi96
		if privateShopSlotIndex == 97:
			suprices = constInfo.sufiyat97
			barprices = constInfo.barfiyat97
			yesilotprices = constInfo.yesilot97
			kirmiziotprices = constInfo.kirmiziot97
			maviotprices = constInfo.maviot97
			morotprices = constInfo.morot97
			ruhtasiprices = constInfo.ruhtasi97
		if privateShopSlotIndex == 98:
			suprices = constInfo.sufiyat98
			barprices = constInfo.barfiyat98
			yesilotprices = constInfo.yesilot98
			kirmiziotprices = constInfo.kirmiziot98
			maviotprices = constInfo.maviot98
			morotprices = constInfo.morot98
			ruhtasiprices = constInfo.ruhtasi98
		if privateShopSlotIndex == 99:
			suprices = constInfo.sufiyat99
			barprices = constInfo.barfiyat99
			yesilotprices = constInfo.yesilot99
			kirmiziotprices = constInfo.kirmiziot99
			maviotprices = constInfo.maviot99
			morotprices = constInfo.morot99
			ruhtasiprices = constInfo.ruhtasi99
		if privateShopSlotIndex == 100:
			suprices = constInfo.sufiyat100
			barprices = constInfo.barfiyat100
			yesilotprices = constInfo.yesilot100
			kirmiziotprices = constInfo.kirmiziot100
			maviotprices = constInfo.maviot100
			morotprices = constInfo.morot100
			ruhtasiprices = constInfo.ruhtasi100
			
		suprice = suprices
		barprice = barprices
		yesilotprice = yesilotprices
		kirmiziotprice = kirmiziotprices
		maviotprice = maviotprices
		morotprice = morotprices
		ruhtasiprice = ruhtasiprices
		
		self.AppendSellingsuprices(suprice)
		self.AppendSellingbarprices(barprice)
		self.AppendSellingyesilotprices(yesilotprice)
		self.AppendSellingkirmiziotprices(kirmiziotprice)
		self.AppendSellingmaviotprices(maviotprice)
		self.AppendSellingmorotprices(morotprice)
		self.AppendSellingmoruhtasiprices(ruhtasiprice)

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(invenPos, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(player.GetItemAttribute(invenPos, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)

# ARATILIR:

def AppendPrice(self, price):

# ALTINA EKLENIR:
#if app.ENABLE_KAYA_MULTI_PRICE:
	def Appendsuprices(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine("|cffff6060Fiyati: "+str(price)+" Su", self.GetPriceColor(price))
	
	def AppendEpPrice(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine("Fiyati: "+str(price)+" EP", self.GetPriceColor(price))
		
	def Appendbarprices(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine("|cFFFFD700Fiyati: "+str(price)+" Bar(400m)", self.GetPriceColor(price))

	def Appendyesilotprices(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine("|cff00ff00Fiyati: "+str(price)+" Yesil ot", self.GetPriceColor(price))
	def Appendkirmiziotprices(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine("|cffff0000Fiyati: "+str(price)+" Kirmizi ot", self.GetPriceColor(price))
	def Appendmaviotprices(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine("|cff0000ffFiyati: "+str(price)+" Mavi ot", self.GetPriceColor(price))
	def Appendmorotprices(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine("|cffDA70D6Fiyati: "+str(price)+" Mor ot", self.GetPriceColor(price))
	def Appendmoruhtasiprices(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine("|cffffff00Fiyati: "+str(price)+" Ruh tasi", self.GetPriceColor(price))

# ARATILIR:

def AppendSellingPrice(self, price):

# ALTINA EKLENIR:
#if app.ENABLE_KAYA_MULTI_PRICE:
	def AppendSellingsuprices(self, price):
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
			return
		else:
			self.AppendTextLine("|cffff6060Fiyati: "+str(price)+" Su", self.GetPriceColor(price))
			self.AppendSpace(5)
		
	def AppendSellingbarprices(self, price):	
		# self.AppendSpace(5)
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
			return
		else:
			self.AppendTextLine("|cFFFFD700Fiyati: "+str(price)+" Yesil ot", self.GetPriceColor(price))
			self.AppendSpace(5)

	def AppendSellingyesilotprices(self, price):	
		# self.AppendSpace(5)
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
			return
		else:
			self.AppendTextLine("|cFFFFD700Fiyati: "+str(price)+" Bar(400m)", self.GetPriceColor(price))
			self.AppendSpace(5)
	def AppendSellingkirmiziotprices(self, price):	
		# self.AppendSpace(5)
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
			return
		else:
			self.AppendTextLine("|cffff0000Fiyati: "+str(price)+" Kirmizi ot", self.GetPriceColor(price))
			self.AppendSpace(5)
	def AppendSellingmaviotprices(self, price):	
		# self.AppendSpace(5)
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
			return
		else:
			self.AppendTextLine("|cff0000ffFiyati: "+str(price)+" Mavi ot", self.GetPriceColor(price))
			self.AppendSpace(5)
	def AppendSellingmorotprices(self, price):	
		# self.AppendSpace(5)
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
			return
		else:
			self.AppendTextLine("|cffDA70D6Fiyati: "+str(price)+" Mor ot", self.GetPriceColor(price))
			self.AppendSpace(5)
	def AppendSellingmoruhtasiprices(self, price):	
		# self.AppendSpace(5)
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
			return
		else:
			self.AppendTextLine("|cffffff00Fiyati: "+str(price)+" Ruh tasi", self.GetPriceColor(price))
			self.AppendSpace(5)