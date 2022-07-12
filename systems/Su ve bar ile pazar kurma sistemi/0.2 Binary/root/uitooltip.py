# Ekle
import maviruhInfo

# Arat (eger npcde efsunlu tasli item sistemini kullanmiyorsan bir sonraki arat dedigim isleme gec)
	if app.ENABLE_2TH_SHOPEX_SYSTEM:
		def SetShopExItem(self, slotIndex, shopType):

# Komple Degistir
	if app.ENABLE_2TH_SHOPEX_SYSTEM:
		def SetShopExItem(self, slotIndex, shopType):
			itemVnum = shop.GetItemID(slotIndex)
			if 0 == itemVnum:
				return

			price = shop.GetItemPrice(slotIndex)
			suprices = 0
			barprices = 0
			
			if slotIndex == 0:
				suprices = constInfo.sufiyat0
				barprices = constInfo.barfiyat0
			if slotIndex == 1:
				suprices = constInfo.sufiyat1
				barprices = constInfo.barfiyat1
			if slotIndex == 2:
				suprices = constInfo.sufiyat2
				barprices = constInfo.barfiyat2
			if slotIndex == 3:
				suprices = constInfo.sufiyat3
				barprices = constInfo.barfiyat3
			if slotIndex == 4:
				suprices = constInfo.sufiyat4
				barprices = constInfo.barfiyat4
			if slotIndex == 5:
				suprices = constInfo.sufiyat5
				barprices = constInfo.barfiyat5
			if slotIndex == 6:
				suprices = constInfo.sufiyat6
				barprices = constInfo.barfiyat6
			if slotIndex == 7:
				suprices = constInfo.sufiyat7
				barprices = constInfo.barfiyat7
			if slotIndex == 8:
				suprices = constInfo.sufiyat8
				barprices = constInfo.barfiyat8
			if slotIndex == 9:
				suprices = constInfo.sufiyat9
				barprices = constInfo.barfiyat9
			if slotIndex == 10:
				suprices = constInfo.sufiyat10
				barprices = constInfo.barfiyat10
			if slotIndex == 11:
				suprices = constInfo.sufiyat11
				barprices = constInfo.barfiyat11
			if slotIndex == 12:
				suprices = constInfo.sufiyat12
				barprices = constInfo.barfiyat12
			if slotIndex == 13:
				suprices = constInfo.sufiyat13
				barprices = constInfo.barfiyat13
			if slotIndex == 14:
				suprices = constInfo.sufiyat14
				barprices = constInfo.barfiyat14
			if slotIndex == 15:
				suprices = constInfo.sufiyat15
				barprices = constInfo.barfiyat15
			if slotIndex == 16:
				suprices = constInfo.sufiyat16
				barprices = constInfo.barfiyat16
			if slotIndex == 17:
				suprices = constInfo.sufiyat17
				barprices = constInfo.barfiyat17
			if slotIndex == 18:
				suprices = constInfo.sufiyat18
				barprices = constInfo.barfiyat18
			if slotIndex == 19:
				suprices = constInfo.sufiyat19
				barprices = constInfo.barfiyat19
			if slotIndex == 20:
				suprices = constInfo.sufiyat20
				barprices = constInfo.barfiyat20
			if slotIndex == 21:
				suprices = constInfo.sufiyat21
				barprices = constInfo.barfiyat21
			if slotIndex == 22:
				suprices = constInfo.sufiyat22
				barprices = constInfo.barfiyat22
			if slotIndex == 23:
				suprices = constInfo.sufiyat23
				barprices = constInfo.barfiyat23
			if slotIndex == 24:
				suprices = constInfo.sufiyat24
				barprices = constInfo.barfiyat24
			if slotIndex == 25:
				suprices = constInfo.sufiyat25
				barprices = constInfo.barfiyat25
			if slotIndex == 26:
				suprices = constInfo.sufiyat26
				barprices = constInfo.barfiyat26
			if slotIndex == 27:
				suprices = constInfo.sufiyat27
				barprices = constInfo.barfiyat27
			if slotIndex == 28:
				suprices = constInfo.sufiyat28
				barprices = constInfo.barfiyat28
			if slotIndex == 29:
				suprices = constInfo.sufiyat29
				barprices = constInfo.barfiyat29
			if slotIndex == 30:
				suprices = constInfo.sufiyat30
				barprices = constInfo.barfiyat30
			if slotIndex == 31:
				suprices = constInfo.sufiyat31
				barprices = constInfo.barfiyat31
			if slotIndex == 32:
				suprices = constInfo.sufiyat32
				barprices = constInfo.barfiyat32
			if slotIndex == 33:
				suprices = constInfo.sufiyat33
				barprices = constInfo.barfiyat33
			if slotIndex == 34:
				suprices = constInfo.sufiyat34
				barprices = constInfo.barfiyat34
			if slotIndex == 35:
				suprices = constInfo.sufiyat35
				barprices = constInfo.barfiyat35
			if slotIndex == 36:
				suprices = constInfo.sufiyat36
				barprices = constInfo.barfiyat36
			if slotIndex == 37:
				suprices = constInfo.sufiyat37
				barprices = constInfo.barfiyat37
			if slotIndex == 38:
				suprices = constInfo.sufiyat38
				barprices = constInfo.barfiyat38
			if slotIndex == 39:
				suprices = constInfo.sufiyat39
				barprices = constInfo.barfiyat39
			if slotIndex == 40:
				suprices = constInfo.sufiyat40
				barprices = constInfo.barfiyat40
			if slotIndex == 41:
				suprices = constInfo.sufiyat41
				barprices = constInfo.barfiyat41
			if slotIndex == 42:
				suprices = constInfo.sufiyat42
				barprices = constInfo.barfiyat42
			if slotIndex == 43:
				suprices = constInfo.sufiyat43
				barprices = constInfo.barfiyat43
			if slotIndex == 44:
				suprices = constInfo.sufiyat44
				barprices = constInfo.barfiyat44
			if slotIndex == 45:
				suprices = constInfo.sufiyat45
				barprices = constInfo.barfiyat45
			if slotIndex == 46:
				suprices = constInfo.sufiyat46
				barprices = constInfo.barfiyat46
			if slotIndex == 47:
				suprices = constInfo.sufiyat47
				barprices = constInfo.barfiyat47
			if slotIndex == 48:
				suprices = constInfo.sufiyat48
				barprices = constInfo.barfiyat48
			if slotIndex == 49:
				suprices = constInfo.sufiyat49
				barprices = constInfo.barfiyat49
			if slotIndex == 50:
				suprices = constInfo.sufiyat50
				barprices = constInfo.barfiyat50
			if slotIndex == 51:
				suprices = constInfo.sufiyat51
				barprices = constInfo.barfiyat51
			if slotIndex == 52:
				suprices = constInfo.sufiyat52
				barprices = constInfo.barfiyat52
			if slotIndex == 53:
				suprices = constInfo.sufiyat53
				barprices = constInfo.barfiyat53
			if slotIndex == 54:
				suprices = constInfo.sufiyat54
				barprices = constInfo.barfiyat54
			if slotIndex == 55:
				suprices = constInfo.sufiyat55
				barprices = constInfo.barfiyat55
			if slotIndex == 56:
				suprices = constInfo.sufiyat56
				barprices = constInfo.barfiyat56
			if slotIndex == 57:
				suprices = constInfo.sufiyat57
				barprices = constInfo.barfiyat57
			if slotIndex == 58:
				suprices = constInfo.sufiyat58
				barprices = constInfo.barfiyat58
			if slotIndex == 59:
				suprices = constInfo.sufiyat59
				barprices = constInfo.barfiyat59
			if slotIndex == 60:
				suprices = constInfo.sufiyat60
				barprices = constInfo.barfiyat60
			if slotIndex == 61:
				suprices = constInfo.sufiyat61
				barprices = constInfo.barfiyat61
			if slotIndex == 62:
				suprices = constInfo.sufiyat62
				barprices = constInfo.barfiyat62
			if slotIndex == 63:
				suprices = constInfo.sufiyat63
				barprices = constInfo.barfiyat63
			if slotIndex == 64:
				suprices = constInfo.sufiyat64
				barprices = constInfo.barfiyat64
			if slotIndex == 65:
				suprices = constInfo.sufiyat65
				barprices = constInfo.barfiyat65
			if slotIndex == 66:
				suprices = constInfo.sufiyat66
				barprices = constInfo.barfiyat66
			if slotIndex == 67:
				suprices = constInfo.sufiyat67
				barprices = constInfo.barfiyat67
			if slotIndex == 68:
				suprices = constInfo.sufiyat68
				barprices = constInfo.barfiyat68
			if slotIndex == 69:
				suprices = constInfo.sufiyat69
				barprices = constInfo.barfiyat69
			if slotIndex == 70:
				suprices = constInfo.sufiyat70
				barprices = constInfo.barfiyat70
			if slotIndex == 71:
				suprices = constInfo.sufiyat71
				barprices = constInfo.barfiyat71
			if slotIndex == 72:
				suprices = constInfo.sufiyat72
				barprices = constInfo.barfiyat72
			if slotIndex == 73:
				suprices = constInfo.sufiyat73
				barprices = constInfo.barfiyat73
			if slotIndex == 74:
				suprices = constInfo.sufiyat74
				barprices = constInfo.barfiyat74
			if slotIndex == 75:
				suprices = constInfo.sufiyat75
				barprices = constInfo.barfiyat75
			if slotIndex == 76:
				suprices = constInfo.sufiyat76
				barprices = constInfo.barfiyat76
			if slotIndex == 77:
				suprices = constInfo.sufiyat77
				barprices = constInfo.barfiyat77
			if slotIndex == 78:
				suprices = constInfo.sufiyat78
				barprices = constInfo.barfiyat78
			if slotIndex == 79:
				suprices = constInfo.sufiyat79
				barprices = constInfo.barfiyat79
			if slotIndex == 80:
				suprices = constInfo.sufiyat80
				barprices = constInfo.barfiyat80
			if slotIndex == 81:
				suprices = constInfo.sufiyat81
				barprices = constInfo.barfiyat81
			if slotIndex == 82:
				suprices = constInfo.sufiyat82
				barprices = constInfo.barfiyat82
			if slotIndex == 83:
				suprices = constInfo.sufiyat83
				barprices = constInfo.barfiyat83
			if slotIndex == 84:
				suprices = constInfo.sufiyat84
				barprices = constInfo.barfiyat84
			if slotIndex == 85:
				suprices = constInfo.sufiyat85
				barprices = constInfo.barfiyat85
			if slotIndex == 86:
				suprices = constInfo.sufiyat86
				barprices = constInfo.barfiyat86
			if slotIndex == 87:
				suprices = constInfo.sufiyat87
				barprices = constInfo.barfiyat87
			if slotIndex == 88:
				suprices = constInfo.sufiyat88
				barprices = constInfo.barfiyat88
			if slotIndex == 89:
				suprices = constInfo.sufiyat89
				barprices = constInfo.barfiyat89
			if slotIndex == 90:
				suprices = constInfo.sufiyat90
				barprices = constInfo.barfiyat90
			if slotIndex == 91:
				suprices = constInfo.sufiyat91
				barprices = constInfo.barfiyat91
			if slotIndex == 92:
				suprices = constInfo.sufiyat92
				barprices = constInfo.barfiyat92
			if slotIndex == 93:
				suprices = constInfo.sufiyat93
				barprices = constInfo.barfiyat93
			if slotIndex == 94:
				suprices = constInfo.sufiyat94
				barprices = constInfo.barfiyat94
			if slotIndex == 95:
				suprices = constInfo.sufiyat95
				barprices = constInfo.barfiyat95
			if slotIndex == 96:
				suprices = constInfo.sufiyat96
				barprices = constInfo.barfiyat96
			if slotIndex == 97:
				suprices = constInfo.sufiyat97
				barprices = constInfo.barfiyat97
			if slotIndex == 98:
				suprices = constInfo.sufiyat98
				barprices = constInfo.barfiyat98
			if slotIndex == 99:
				suprices = constInfo.sufiyat99
				barprices = constInfo.barfiyat99
			if slotIndex == 100:
				suprices = constInfo.sufiyat100
				barprices = constInfo.barfiyat100
				
			suprice = suprices
			barprice = barprices
			self.ClearToolTip()
			self.isShopItem = True

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
				## Bar su ile item satma
				if shopType == shop.SHOP_TYPE_GOLD:
					self.AppendPrice(price)
				elif shopType == shop.SHOP_TYPE_CASH:
					self.AppendPriceByDragonCoin(price)
				elif shopType == shop.SHOP_TYPE_COINS:
					self.AppendPriceByDragonMark(price)
				elif shopType == shop.SHOP_TYPE_ALIGN:
					self.AppendPriceByAlignment(price)
				else:
					self.AppendPrice(price)
# Arat
def SetShopItem(self, slotIndex):

# Komple Degistir
	if app.MAVIRUH_MULTI_PRICE:
		def SetShopItem(self, slotIndex):
			itemVnum = shop.GetItemID(slotIndex)
			if 0 == itemVnum:
				return

			price = shop.GetItemPrice(slotIndex)
			suprices = 0
			barprices = 0
			
			if slotIndex == 0:
				suprices = constInfo.sufiyat0
				barprices = constInfo.barfiyat0
			if slotIndex == 1:
				suprices = constInfo.sufiyat1
				barprices = constInfo.barfiyat1
			if slotIndex == 2:
				suprices = constInfo.sufiyat2
				barprices = constInfo.barfiyat2
			if slotIndex == 3:
				suprices = constInfo.sufiyat3
				barprices = constInfo.barfiyat3
			if slotIndex == 4:
				suprices = constInfo.sufiyat4
				barprices = constInfo.barfiyat4
			if slotIndex == 5:
				suprices = constInfo.sufiyat5
				barprices = constInfo.barfiyat5
			if slotIndex == 6:
				suprices = constInfo.sufiyat6
				barprices = constInfo.barfiyat6
			if slotIndex == 7:
				suprices = constInfo.sufiyat7
				barprices = constInfo.barfiyat7
			if slotIndex == 8:
				suprices = constInfo.sufiyat8
				barprices = constInfo.barfiyat8
			if slotIndex == 9:
				suprices = constInfo.sufiyat9
				barprices = constInfo.barfiyat9
			if slotIndex == 10:
				suprices = constInfo.sufiyat10
				barprices = constInfo.barfiyat10
			if slotIndex == 11:
				suprices = constInfo.sufiyat11
				barprices = constInfo.barfiyat11
			if slotIndex == 12:
				suprices = constInfo.sufiyat12
				barprices = constInfo.barfiyat12
			if slotIndex == 13:
				suprices = constInfo.sufiyat13
				barprices = constInfo.barfiyat13
			if slotIndex == 14:
				suprices = constInfo.sufiyat14
				barprices = constInfo.barfiyat14
			if slotIndex == 15:
				suprices = constInfo.sufiyat15
				barprices = constInfo.barfiyat15
			if slotIndex == 16:
				suprices = constInfo.sufiyat16
				barprices = constInfo.barfiyat16
			if slotIndex == 17:
				suprices = constInfo.sufiyat17
				barprices = constInfo.barfiyat17
			if slotIndex == 18:
				suprices = constInfo.sufiyat18
				barprices = constInfo.barfiyat18
			if slotIndex == 19:
				suprices = constInfo.sufiyat19
				barprices = constInfo.barfiyat19
			if slotIndex == 20:
				suprices = constInfo.sufiyat20
				barprices = constInfo.barfiyat20
			if slotIndex == 21:
				suprices = constInfo.sufiyat21
				barprices = constInfo.barfiyat21
			if slotIndex == 22:
				suprices = constInfo.sufiyat22
				barprices = constInfo.barfiyat22
			if slotIndex == 23:
				suprices = constInfo.sufiyat23
				barprices = constInfo.barfiyat23
			if slotIndex == 24:
				suprices = constInfo.sufiyat24
				barprices = constInfo.barfiyat24
			if slotIndex == 25:
				suprices = constInfo.sufiyat25
				barprices = constInfo.barfiyat25
			if slotIndex == 26:
				suprices = constInfo.sufiyat26
				barprices = constInfo.barfiyat26
			if slotIndex == 27:
				suprices = constInfo.sufiyat27
				barprices = constInfo.barfiyat27
			if slotIndex == 28:
				suprices = constInfo.sufiyat28
				barprices = constInfo.barfiyat28
			if slotIndex == 29:
				suprices = constInfo.sufiyat29
				barprices = constInfo.barfiyat29
			if slotIndex == 30:
				suprices = constInfo.sufiyat30
				barprices = constInfo.barfiyat30
			if slotIndex == 31:
				suprices = constInfo.sufiyat31
				barprices = constInfo.barfiyat31
			if slotIndex == 32:
				suprices = constInfo.sufiyat32
				barprices = constInfo.barfiyat32
			if slotIndex == 33:
				suprices = constInfo.sufiyat33
				barprices = constInfo.barfiyat33
			if slotIndex == 34:
				suprices = constInfo.sufiyat34
				barprices = constInfo.barfiyat34
			if slotIndex == 35:
				suprices = constInfo.sufiyat35
				barprices = constInfo.barfiyat35
			if slotIndex == 36:
				suprices = constInfo.sufiyat36
				barprices = constInfo.barfiyat36
			if slotIndex == 37:
				suprices = constInfo.sufiyat37
				barprices = constInfo.barfiyat37
			if slotIndex == 38:
				suprices = constInfo.sufiyat38
				barprices = constInfo.barfiyat38
			if slotIndex == 39:
				suprices = constInfo.sufiyat39
				barprices = constInfo.barfiyat39
			if slotIndex == 40:
				suprices = constInfo.sufiyat40
				barprices = constInfo.barfiyat40
			if slotIndex == 41:
				suprices = constInfo.sufiyat41
				barprices = constInfo.barfiyat41
			if slotIndex == 42:
				suprices = constInfo.sufiyat42
				barprices = constInfo.barfiyat42
			if slotIndex == 43:
				suprices = constInfo.sufiyat43
				barprices = constInfo.barfiyat43
			if slotIndex == 44:
				suprices = constInfo.sufiyat44
				barprices = constInfo.barfiyat44
			if slotIndex == 45:
				suprices = constInfo.sufiyat45
				barprices = constInfo.barfiyat45
			if slotIndex == 46:
				suprices = constInfo.sufiyat46
				barprices = constInfo.barfiyat46
			if slotIndex == 47:
				suprices = constInfo.sufiyat47
				barprices = constInfo.barfiyat47
			if slotIndex == 48:
				suprices = constInfo.sufiyat48
				barprices = constInfo.barfiyat48
			if slotIndex == 49:
				suprices = constInfo.sufiyat49
				barprices = constInfo.barfiyat49
			if slotIndex == 50:
				suprices = constInfo.sufiyat50
				barprices = constInfo.barfiyat50
			if slotIndex == 51:
				suprices = constInfo.sufiyat51
				barprices = constInfo.barfiyat51
			if slotIndex == 52:
				suprices = constInfo.sufiyat52
				barprices = constInfo.barfiyat52
			if slotIndex == 53:
				suprices = constInfo.sufiyat53
				barprices = constInfo.barfiyat53
			if slotIndex == 54:
				suprices = constInfo.sufiyat54
				barprices = constInfo.barfiyat54
			if slotIndex == 55:
				suprices = constInfo.sufiyat55
				barprices = constInfo.barfiyat55
			if slotIndex == 56:
				suprices = constInfo.sufiyat56
				barprices = constInfo.barfiyat56
			if slotIndex == 57:
				suprices = constInfo.sufiyat57
				barprices = constInfo.barfiyat57
			if slotIndex == 58:
				suprices = constInfo.sufiyat58
				barprices = constInfo.barfiyat58
			if slotIndex == 59:
				suprices = constInfo.sufiyat59
				barprices = constInfo.barfiyat59
			if slotIndex == 60:
				suprices = constInfo.sufiyat60
				barprices = constInfo.barfiyat60
			if slotIndex == 61:
				suprices = constInfo.sufiyat61
				barprices = constInfo.barfiyat61
			if slotIndex == 62:
				suprices = constInfo.sufiyat62
				barprices = constInfo.barfiyat62
			if slotIndex == 63:
				suprices = constInfo.sufiyat63
				barprices = constInfo.barfiyat63
			if slotIndex == 64:
				suprices = constInfo.sufiyat64
				barprices = constInfo.barfiyat64
			if slotIndex == 65:
				suprices = constInfo.sufiyat65
				barprices = constInfo.barfiyat65
			if slotIndex == 66:
				suprices = constInfo.sufiyat66
				barprices = constInfo.barfiyat66
			if slotIndex == 67:
				suprices = constInfo.sufiyat67
				barprices = constInfo.barfiyat67
			if slotIndex == 68:
				suprices = constInfo.sufiyat68
				barprices = constInfo.barfiyat68
			if slotIndex == 69:
				suprices = constInfo.sufiyat69
				barprices = constInfo.barfiyat69
			if slotIndex == 70:
				suprices = constInfo.sufiyat70
				barprices = constInfo.barfiyat70
			if slotIndex == 71:
				suprices = constInfo.sufiyat71
				barprices = constInfo.barfiyat71
			if slotIndex == 72:
				suprices = constInfo.sufiyat72
				barprices = constInfo.barfiyat72
			if slotIndex == 73:
				suprices = constInfo.sufiyat73
				barprices = constInfo.barfiyat73
			if slotIndex == 74:
				suprices = constInfo.sufiyat74
				barprices = constInfo.barfiyat74
			if slotIndex == 75:
				suprices = constInfo.sufiyat75
				barprices = constInfo.barfiyat75
			if slotIndex == 76:
				suprices = constInfo.sufiyat76
				barprices = constInfo.barfiyat76
			if slotIndex == 77:
				suprices = constInfo.sufiyat77
				barprices = constInfo.barfiyat77
			if slotIndex == 78:
				suprices = constInfo.sufiyat78
				barprices = constInfo.barfiyat78
			if slotIndex == 79:
				suprices = constInfo.sufiyat79
				barprices = constInfo.barfiyat79
			if slotIndex == 80:
				suprices = constInfo.sufiyat80
				barprices = constInfo.barfiyat80
			if slotIndex == 81:
				suprices = constInfo.sufiyat81
				barprices = constInfo.barfiyat81
			if slotIndex == 82:
				suprices = constInfo.sufiyat82
				barprices = constInfo.barfiyat82
			if slotIndex == 83:
				suprices = constInfo.sufiyat83
				barprices = constInfo.barfiyat83
			if slotIndex == 84:
				suprices = constInfo.sufiyat84
				barprices = constInfo.barfiyat84
			if slotIndex == 85:
				suprices = constInfo.sufiyat85
				barprices = constInfo.barfiyat85
			if slotIndex == 86:
				suprices = constInfo.sufiyat86
				barprices = constInfo.barfiyat86
			if slotIndex == 87:
				suprices = constInfo.sufiyat87
				barprices = constInfo.barfiyat87
			if slotIndex == 88:
				suprices = constInfo.sufiyat88
				barprices = constInfo.barfiyat88
			if slotIndex == 89:
				suprices = constInfo.sufiyat89
				barprices = constInfo.barfiyat89
			if slotIndex == 90:
				suprices = constInfo.sufiyat90
				barprices = constInfo.barfiyat90
			if slotIndex == 91:
				suprices = constInfo.sufiyat91
				barprices = constInfo.barfiyat91
			if slotIndex == 92:
				suprices = constInfo.sufiyat92
				barprices = constInfo.barfiyat92
			if slotIndex == 93:
				suprices = constInfo.sufiyat93
				barprices = constInfo.barfiyat93
			if slotIndex == 94:
				suprices = constInfo.sufiyat94
				barprices = constInfo.barfiyat94
			if slotIndex == 95:
				suprices = constInfo.sufiyat95
				barprices = constInfo.barfiyat95
			if slotIndex == 96:
				suprices = constInfo.sufiyat96
				barprices = constInfo.barfiyat96
			if slotIndex == 97:
				suprices = constInfo.sufiyat97
				barprices = constInfo.barfiyat97
			if slotIndex == 98:
				suprices = constInfo.sufiyat98
				barprices = constInfo.barfiyat98
			if slotIndex == 99:
				suprices = constInfo.sufiyat99
				barprices = constInfo.barfiyat99
			if slotIndex == 100:
				suprices = constInfo.sufiyat100
				barprices = constInfo.barfiyat100
				
			suprice = suprices
			barprice = barprices
			
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
				## Bar su ile item satma
	else:
		def SetShopItem(self, slotIndex):
			itemVnum = shop.GetItemID(slotIndex)
			if 0 == itemVnum:
				return

			price = shop.GetItemPrice(slotIndex)
			self.ClearToolTip()
			self.isShopItem = True

			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(shop.GetItemMetinSocket(slotIndex, i))
			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append(shop.GetItemAttribute(slotIndex, i))

			self.AddItemData(itemVnum, metinSlot, attrSlot)
			self.AppendPrice(price)


# Arat
	def SetPrivateShopBuilderItem(self, invenType, invenPos, privateShopSlotIndex):

# Komple Degistir
	if app.MAVIRUH_MULTI_PRICE:
		def SetPrivateShopBuilderItem(self, invenType, invenPos, privateShopSlotIndex):
			itemVnum = player.GetItemIndex(invenType, invenPos)
			if 0 == itemVnum:
				return

			item.SelectItem(itemVnum)
			self.ClearToolTip()
			self.AppendSellingPrice(shop.GetPrivateShopItemPrice(invenType, invenPos))
			
			suprices = 0
			barprices = 0
			
			if privateShopSlotIndex == 0:
				suprices = constInfo.sufiyat0
				barprices = constInfo.barfiyat0
			if privateShopSlotIndex == 1:
				suprices = constInfo.sufiyat1
				barprices = constInfo.barfiyat1
			if privateShopSlotIndex == 2:
				suprices = constInfo.sufiyat2
				barprices = constInfo.barfiyat2
			if privateShopSlotIndex == 3:
				suprices = constInfo.sufiyat3
				barprices = constInfo.barfiyat3
			if privateShopSlotIndex == 4:
				suprices = constInfo.sufiyat4
				barprices = constInfo.barfiyat4
			if privateShopSlotIndex == 5:
				suprices = constInfo.sufiyat5
				barprices = constInfo.barfiyat5
			if privateShopSlotIndex == 6:
				suprices = constInfo.sufiyat6
				barprices = constInfo.barfiyat6
			if privateShopSlotIndex == 7:
				suprices = constInfo.sufiyat7
				barprices = constInfo.barfiyat7
			if privateShopSlotIndex == 8:
				suprices = constInfo.sufiyat8
				barprices = constInfo.barfiyat8
			if privateShopSlotIndex == 9:
				suprices = constInfo.sufiyat9
				barprices = constInfo.barfiyat9
			if privateShopSlotIndex == 10:
				suprices = constInfo.sufiyat10
				barprices = constInfo.barfiyat10
			if privateShopSlotIndex == 11:
				suprices = constInfo.sufiyat11
				barprices = constInfo.barfiyat11
			if privateShopSlotIndex == 12:
				suprices = constInfo.sufiyat12
				barprices = constInfo.barfiyat12
			if privateShopSlotIndex == 13:
				suprices = constInfo.sufiyat13
				barprices = constInfo.barfiyat13
			if privateShopSlotIndex == 14:
				suprices = constInfo.sufiyat14
				barprices = constInfo.barfiyat14
			if privateShopSlotIndex == 15:
				suprices = constInfo.sufiyat15
				barprices = constInfo.barfiyat15
			if privateShopSlotIndex == 16:
				suprices = constInfo.sufiyat16
				barprices = constInfo.barfiyat16
			if privateShopSlotIndex == 17:
				suprices = constInfo.sufiyat17
				barprices = constInfo.barfiyat17
			if privateShopSlotIndex == 18:
				suprices = constInfo.sufiyat18
				barprices = constInfo.barfiyat18
			if privateShopSlotIndex == 19:
				suprices = constInfo.sufiyat19
				barprices = constInfo.barfiyat19
			if privateShopSlotIndex == 20:
				suprices = constInfo.sufiyat20
				barprices = constInfo.barfiyat20
			if privateShopSlotIndex == 21:
				suprices = constInfo.sufiyat21
				barprices = constInfo.barfiyat21
			if privateShopSlotIndex == 22:
				suprices = constInfo.sufiyat22
				barprices = constInfo.barfiyat22
			if privateShopSlotIndex == 23:
				suprices = constInfo.sufiyat23
				barprices = constInfo.barfiyat23
			if privateShopSlotIndex == 24:
				suprices = constInfo.sufiyat24
				barprices = constInfo.barfiyat24
			if privateShopSlotIndex == 25:
				suprices = constInfo.sufiyat25
				barprices = constInfo.barfiyat25
			if privateShopSlotIndex == 26:
				suprices = constInfo.sufiyat26
				barprices = constInfo.barfiyat26
			if privateShopSlotIndex == 27:
				suprices = constInfo.sufiyat27
				barprices = constInfo.barfiyat27
			if privateShopSlotIndex == 28:
				suprices = constInfo.sufiyat28
				barprices = constInfo.barfiyat28
			if privateShopSlotIndex == 29:
				suprices = constInfo.sufiyat29
				barprices = constInfo.barfiyat29
			if privateShopSlotIndex == 30:
				suprices = constInfo.sufiyat30
				barprices = constInfo.barfiyat30
			if privateShopSlotIndex == 31:
				suprices = constInfo.sufiyat31
				barprices = constInfo.barfiyat31
			if privateShopSlotIndex == 32:
				suprices = constInfo.sufiyat32
				barprices = constInfo.barfiyat32
			if privateShopSlotIndex == 33:
				suprices = constInfo.sufiyat33
				barprices = constInfo.barfiyat33
			if privateShopSlotIndex == 34:
				suprices = constInfo.sufiyat34
				barprices = constInfo.barfiyat34
			if privateShopSlotIndex == 35:
				suprices = constInfo.sufiyat35
				barprices = constInfo.barfiyat35
			if privateShopSlotIndex == 36:
				suprices = constInfo.sufiyat36
				barprices = constInfo.barfiyat36
			if privateShopSlotIndex == 37:
				suprices = constInfo.sufiyat37
				barprices = constInfo.barfiyat37
			if privateShopSlotIndex == 38:
				suprices = constInfo.sufiyat38
				barprices = constInfo.barfiyat38
			if privateShopSlotIndex == 39:
				suprices = constInfo.sufiyat39
				barprices = constInfo.barfiyat39
			if privateShopSlotIndex == 40:
				suprices = constInfo.sufiyat40
				barprices = constInfo.barfiyat40
			if privateShopSlotIndex == 41:
				suprices = constInfo.sufiyat41
				barprices = constInfo.barfiyat41
			if privateShopSlotIndex == 42:
				suprices = constInfo.sufiyat42
				barprices = constInfo.barfiyat42
			if privateShopSlotIndex == 43:
				suprices = constInfo.sufiyat43
				barprices = constInfo.barfiyat43
			if privateShopSlotIndex == 44:
				suprices = constInfo.sufiyat44
				barprices = constInfo.barfiyat44
			if privateShopSlotIndex == 45:
				suprices = constInfo.sufiyat45
				barprices = constInfo.barfiyat45
			if privateShopSlotIndex == 46:
				suprices = constInfo.sufiyat46
				barprices = constInfo.barfiyat46
			if privateShopSlotIndex == 47:
				suprices = constInfo.sufiyat47
				barprices = constInfo.barfiyat47
			if privateShopSlotIndex == 48:
				suprices = constInfo.sufiyat48
				barprices = constInfo.barfiyat48
			if privateShopSlotIndex == 49:
				suprices = constInfo.sufiyat49
				barprices = constInfo.barfiyat49
			if privateShopSlotIndex == 50:
				suprices = constInfo.sufiyat50
				barprices = constInfo.barfiyat50
			if privateShopSlotIndex == 51:
				suprices = constInfo.sufiyat51
				barprices = constInfo.barfiyat51
			if privateShopSlotIndex == 52:
				suprices = constInfo.sufiyat52
				barprices = constInfo.barfiyat52
			if privateShopSlotIndex == 53:
				suprices = constInfo.sufiyat53
				barprices = constInfo.barfiyat53
			if privateShopSlotIndex == 54:
				suprices = constInfo.sufiyat54
				barprices = constInfo.barfiyat54
			if privateShopSlotIndex == 55:
				suprices = constInfo.sufiyat55
				barprices = constInfo.barfiyat55
			if privateShopSlotIndex == 56:
				suprices = constInfo.sufiyat56
				barprices = constInfo.barfiyat56
			if privateShopSlotIndex == 57:
				suprices = constInfo.sufiyat57
				barprices = constInfo.barfiyat57
			if privateShopSlotIndex == 58:
				suprices = constInfo.sufiyat58
				barprices = constInfo.barfiyat58
			if privateShopSlotIndex == 59:
				suprices = constInfo.sufiyat59
				barprices = constInfo.barfiyat59
			if privateShopSlotIndex == 60:
				suprices = constInfo.sufiyat60
				barprices = constInfo.barfiyat60
			if privateShopSlotIndex == 61:
				suprices = constInfo.sufiyat61
				barprices = constInfo.barfiyat61
			if privateShopSlotIndex == 62:
				suprices = constInfo.sufiyat62
				barprices = constInfo.barfiyat62
			if privateShopSlotIndex == 63:
				suprices = constInfo.sufiyat63
				barprices = constInfo.barfiyat63
			if privateShopSlotIndex == 64:
				suprices = constInfo.sufiyat64
				barprices = constInfo.barfiyat64
			if privateShopSlotIndex == 65:
				suprices = constInfo.sufiyat65
				barprices = constInfo.barfiyat65
			if privateShopSlotIndex == 66:
				suprices = constInfo.sufiyat66
				barprices = constInfo.barfiyat66
			if privateShopSlotIndex == 67:
				suprices = constInfo.sufiyat67
				barprices = constInfo.barfiyat67
			if privateShopSlotIndex == 68:
				suprices = constInfo.sufiyat68
				barprices = constInfo.barfiyat68
			if privateShopSlotIndex == 69:
				suprices = constInfo.sufiyat69
				barprices = constInfo.barfiyat69
			if privateShopSlotIndex == 70:
				suprices = constInfo.sufiyat70
				barprices = constInfo.barfiyat70
			if privateShopSlotIndex == 71:
				suprices = constInfo.sufiyat71
				barprices = constInfo.barfiyat71
			if privateShopSlotIndex == 72:
				suprices = constInfo.sufiyat72
				barprices = constInfo.barfiyat72
			if privateShopSlotIndex == 73:
				suprices = constInfo.sufiyat73
				barprices = constInfo.barfiyat73
			if privateShopSlotIndex == 74:
				suprices = constInfo.sufiyat74
				barprices = constInfo.barfiyat74
			if privateShopSlotIndex == 75:
				suprices = constInfo.sufiyat75
				barprices = constInfo.barfiyat75
			if privateShopSlotIndex == 76:
				suprices = constInfo.sufiyat76
				barprices = constInfo.barfiyat76
			if privateShopSlotIndex == 77:
				suprices = constInfo.sufiyat77
				barprices = constInfo.barfiyat77
			if privateShopSlotIndex == 78:
				suprices = constInfo.sufiyat78
				barprices = constInfo.barfiyat78
			if privateShopSlotIndex == 79:
				suprices = constInfo.sufiyat79
				barprices = constInfo.barfiyat79
			if privateShopSlotIndex == 80:
				suprices = constInfo.sufiyat80
				barprices = constInfo.barfiyat80
			if privateShopSlotIndex == 81:
				suprices = constInfo.sufiyat81
				barprices = constInfo.barfiyat81
			if privateShopSlotIndex == 82:
				suprices = constInfo.sufiyat82
				barprices = constInfo.barfiyat82
			if privateShopSlotIndex == 83:
				suprices = constInfo.sufiyat83
				barprices = constInfo.barfiyat83
			if privateShopSlotIndex == 84:
				suprices = constInfo.sufiyat84
				barprices = constInfo.barfiyat84
			if privateShopSlotIndex == 85:
				suprices = constInfo.sufiyat85
				barprices = constInfo.barfiyat85
			if privateShopSlotIndex == 86:
				suprices = constInfo.sufiyat86
				barprices = constInfo.barfiyat86
			if privateShopSlotIndex == 87:
				suprices = constInfo.sufiyat87
				barprices = constInfo.barfiyat87
			if privateShopSlotIndex == 88:
				suprices = constInfo.sufiyat88
				barprices = constInfo.barfiyat88
			if privateShopSlotIndex == 89:
				suprices = constInfo.sufiyat89
				barprices = constInfo.barfiyat89
			if privateShopSlotIndex == 90:
				suprices = constInfo.sufiyat90
				barprices = constInfo.barfiyat90
			if privateShopSlotIndex == 91:
				suprices = constInfo.sufiyat91
				barprices = constInfo.barfiyat91
			if privateShopSlotIndex == 92:
				suprices = constInfo.sufiyat92
				barprices = constInfo.barfiyat92
			if privateShopSlotIndex == 93:
				suprices = constInfo.sufiyat93
				barprices = constInfo.barfiyat93
			if privateShopSlotIndex == 94:
				suprices = constInfo.sufiyat94
				barprices = constInfo.barfiyat94
			if privateShopSlotIndex == 95:
				suprices = constInfo.sufiyat95
				barprices = constInfo.barfiyat95
			if privateShopSlotIndex == 96:
				suprices = constInfo.sufiyat96
				barprices = constInfo.barfiyat96
			if privateShopSlotIndex == 97:
				suprices = constInfo.sufiyat97
				barprices = constInfo.barfiyat97
			if privateShopSlotIndex == 98:
				suprices = constInfo.sufiyat98
				barprices = constInfo.barfiyat98
			if privateShopSlotIndex == 99:
				suprices = constInfo.sufiyat99
				barprices = constInfo.barfiyat99
			if privateShopSlotIndex == 100:
				suprices = constInfo.sufiyat100
				barprices = constInfo.barfiyat100
				
			suprice = suprices
			barprice = barprices
			
			self.AppendSellingsuprices(suprice)
			self.AppendSellingbarprices(barprice)

			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(player.GetItemMetinSocket(invenPos, i))
			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append(player.GetItemAttribute(invenPos, i))

				self.AddItemData(itemVnum, metinSlot, attrSlot)
	else:
		def SetPrivateShopBuilderItem(self, invenType, invenPos, privateShopSlotIndex):
			itemVnum = player.GetItemIndex(invenType, invenPos)
			if 0 == itemVnum:
				return

			item.SelectItem(itemVnum)
			self.ClearToolTip()
			self.AppendSellingPrice(shop.GetPrivateShopItemPrice(invenType, invenPos))

			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(player.GetItemMetinSocket(invenPos, i))
			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append(player.GetItemAttribute(invenPos, i))

			self.AddItemData(itemVnum, metinSlot, attrSlot)

# Arat
	def AppendPrice(self, price):

# Altina Ekle
	if app.MAVIRUH_MULTI_PRICE:
		def Appendsuprices(self, price):
			self.AppendSpace(5)
			self.AppendTextLine(maviruhInfo.SU_TASI_FIYATI+str(price)+maviruhInfo.SU_TASI, self.GetPriceColor(price))
		def Appendbarprices(self, price):
			self.AppendSpace(5)
			self.AppendTextLine(maviruhInfo.BAR_FIYATI+str(price)+maviruhInfo.BAR, self.GetPriceColor(price))

# Arat
	def AppendSellingPrice(self, price):

# Altina Ekle
	if app.MAVIRUH_MULTI_PRICE:
		def AppendSellingsuprices(self, price):
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
				return
			else:
				self.AppendTextLine(maviruhInfo.SU_TASI_FIYATI+str(price)+maviruhInfo.SU_TASI, self.GetPriceColor(price))
				self.AppendSpace(5)
		def AppendSellingbarprices(self, price):
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
				return
			else:
				self.AppendTextLine(maviruhInfo.BAR_FIYATI+str(price)+maviruhInfo.BAR, self.GetPriceColor(price))
				self.AppendSpace(5)
