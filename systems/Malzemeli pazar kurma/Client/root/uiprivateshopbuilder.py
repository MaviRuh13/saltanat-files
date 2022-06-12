"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                                                         AÇILIR: uiprivateshopbuilder.py                                                                   """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# EKLENIR:
#if app.ENABLE_KAYA_MULTI_PRICE:
import uiMaydanoz
import constInfo

# ARATILIR:

priceInputBoard = uiCommon.MoneyInputDialog()

# DEGISTIRILIR:
#if app.ENABLE_KAYA_MULTI_PRICE:
priceInputBoard = uiMaydanoz.NewMoneyInputDialog()

# ARATILIR:

def AcceptInputPrice(self):

# KOMPLE DEGISTIRILIR:
#if app.ENABLE_KAYA_MULTI_PRICE:
	def AcceptInputPrice(self):

		if not self.priceInputBoard:
			return TRUE

		text = self.priceInputBoard.GetText()
		text1 = self.priceInputBoard.GetText1()
		text2 = self.priceInputBoard.GetText2()
		text3 = self.priceInputBoard.GetText3()
		text4 = self.priceInputBoard.GetText4()
		text5 = self.priceInputBoard.GetText5()
		text6 = self.priceInputBoard.GetText6()
		text7 = self.priceInputBoard.GetText7()

		if not text:
			return TRUE

		if not text.isdigit():
			return TRUE

		if int(text) <= 0:
			return TRUE

		attachedInvenType = self.priceInputBoard.sourceWindowType
		sourceSlotPos = self.priceInputBoard.sourceSlotPos
		targetSlotPos = self.priceInputBoard.targetSlotPos

		for privatePos, (itemWindowType, itemSlotIndex) in self.itemStock.items():
			if itemWindowType == attachedInvenType and itemSlotIndex == sourceSlotPos:
				shop.DelPrivateShopItemStock(itemWindowType, itemSlotIndex)
				del self.itemStock[privatePos]

		price = int(self.priceInputBoard.GetText())

		if IsPrivateShopItemPriceList():
			SetPrivateShopItemPrice(self.priceInputBoard.itemVNum, price)

		shop.AddPrivateShopItemStock(attachedInvenType, sourceSlotPos, targetSlotPos, price) ## Bar ve su ile esya satma
		self.itemStock[targetSlotPos] = (attachedInvenType, sourceSlotPos)
		snd.PlaySound("sound/ui/drop.wav")
		import net
		net.SendChatPacket("/suileesyasat "+str(targetSlotPos)+" "+str(text1))
		net.SendChatPacket("/barileesyasat "+str(targetSlotPos)+" "+str(text2))
		net.SendChatPacket("/yesilotilesat "+str(targetSlotPos)+" "+str(text3))
		net.SendChatPacket("/kirmiziotilesat "+str(targetSlotPos)+" "+str(text4))
		net.SendChatPacket("/maviotilesat "+str(targetSlotPos)+" "+str(text5))
		net.SendChatPacket("/morotilesat "+str(targetSlotPos)+" "+str(text6))
		net.SendChatPacket("/ruhtasilesat "+str(targetSlotPos)+" "+str(text7))
		if targetSlotPos == 0:
			constInfo.sufiyat0 = int(text1)
		if targetSlotPos == 1:
			constInfo.sufiyat1 = int(text1)
		if targetSlotPos == 2:
			constInfo.sufiyat2 = int(text1)
		if targetSlotPos == 3:
			constInfo.sufiyat3 = int(text1)
		if targetSlotPos == 4:
			constInfo.sufiyat4 = int(text1)
		if targetSlotPos == 5:
			constInfo.sufiyat5 = int(text1)
		if targetSlotPos == 6:
			constInfo.sufiyat6 = int(text1)
		if targetSlotPos == 7:
			constInfo.sufiyat7 = int(text1)
		if targetSlotPos == 8:
			constInfo.sufiyat8 = int(text1)
		if targetSlotPos == 9:
			constInfo.sufiyat9 = int(text1)
		if targetSlotPos == 10:
			constInfo.sufiyat10 = int(text1)
		if targetSlotPos == 11:
			constInfo.sufiyat11 = int(text1)
		if targetSlotPos == 12:
			constInfo.sufiyat12 = int(text1)
		if targetSlotPos == 13:
			constInfo.sufiyat13 = int(text1)
		if targetSlotPos == 14:
			constInfo.sufiyat14 = int(text1)
		if targetSlotPos == 15:
			constInfo.sufiyat15 = int(text1)
		if targetSlotPos == 16:
			constInfo.sufiyat16 = int(text1)
		if targetSlotPos == 17:
			constInfo.sufiyat17 = int(text1)
		if targetSlotPos == 18:
			constInfo.sufiyat18 = int(text1)
		if targetSlotPos == 19:
			constInfo.sufiyat19 = int(text1)
		if targetSlotPos == 20:
			constInfo.sufiyat20 = int(text1)
		if targetSlotPos == 21:
			constInfo.sufiyat21 = int(text1)
		if targetSlotPos == 22:
			constInfo.sufiyat22 = int(text1)
		if targetSlotPos == 23:
			constInfo.sufiyat23 = int(text1)
		if targetSlotPos == 24:
			constInfo.sufiyat24 = int(text1)
		if targetSlotPos == 25:
			constInfo.sufiyat25 = int(text1)
		if targetSlotPos == 26:
			constInfo.sufiyat26 = int(text1)
		if targetSlotPos == 27:
			constInfo.sufiyat27 = int(text1)
		if targetSlotPos == 28:
			constInfo.sufiyat28 = int(text1)
		if targetSlotPos == 29:
			constInfo.sufiyat29 = int(text1)
		if targetSlotPos == 30:
			constInfo.sufiyat30 = int(text1)
		if targetSlotPos == 31:
			constInfo.sufiyat31 = int(text1)
		if targetSlotPos == 32:
			constInfo.sufiyat32 = int(text1)
		if targetSlotPos == 33:
			constInfo.sufiyat33 = int(text1)
		if targetSlotPos == 34:
			constInfo.sufiyat34 = int(text1)
		if targetSlotPos == 35:
			constInfo.sufiyat35 = int(text1)
		if targetSlotPos == 36:
			constInfo.sufiyat36 = int(text1)
		if targetSlotPos == 37:
			constInfo.sufiyat37 = int(text1)
		if targetSlotPos == 38:
			constInfo.sufiyat38 = int(text1)
		if targetSlotPos == 39:
			constInfo.sufiyat39 = int(text1)
		if targetSlotPos == 40:
			constInfo.sufiyat40 = int(text1)
		if targetSlotPos == 41:
			constInfo.sufiyat41 = int(text1)
		if targetSlotPos == 42:
			constInfo.sufiyat42 = int(text1)
		if targetSlotPos == 43:
			constInfo.sufiyat43 = int(text1)
		if targetSlotPos == 44:
			constInfo.sufiyat44 = int(text1)
		if targetSlotPos == 45:
			constInfo.sufiyat45 = int(text1)
		if targetSlotPos == 46:
			constInfo.sufiyat46 = int(text1)
		if targetSlotPos == 47:
			constInfo.sufiyat47 = int(text1)
		if targetSlotPos == 48:
			constInfo.sufiyat48 = int(text1)
		if targetSlotPos == 49:
			constInfo.sufiyat49 = int(text1)
		if targetSlotPos == 50:
			constInfo.sufiyat50 = int(text1)
		if targetSlotPos == 51:
			constInfo.sufiyat51 = int(text1)
		if targetSlotPos == 52:
			constInfo.sufiyat52 = int(text1)
		if targetSlotPos == 53:
			constInfo.sufiyat53 = int(text1)
		if targetSlotPos == 54:
			constInfo.sufiyat54 = int(text1)
		if targetSlotPos == 55:
			constInfo.sufiyat55 = int(text1)
		if targetSlotPos == 56:
			constInfo.sufiyat56 = int(text1)
		if targetSlotPos == 57:
			constInfo.sufiyat57 = int(text1)
		if targetSlotPos == 58:
			constInfo.sufiyat58 = int(text1)
		if targetSlotPos == 59:
			constInfo.sufiyat59 = int(text1)
		if targetSlotPos == 60:
			constInfo.sufiyat60 = int(text1)
		if targetSlotPos == 61:
			constInfo.sufiyat61 = int(text1)
		if targetSlotPos == 62:
			constInfo.sufiyat62 = int(text1)
		if targetSlotPos == 63:
			constInfo.sufiyat63 = int(text1)
		if targetSlotPos == 64:
			constInfo.sufiyat64 = int(text1)
		if targetSlotPos == 65:
			constInfo.sufiyat65 = int(text1)
		if targetSlotPos == 66:
			constInfo.sufiyat66 = int(text1)
		if targetSlotPos == 67:
			constInfo.sufiyat67 = int(text1)
		if targetSlotPos == 68:
			constInfo.sufiyat68 = int(text1)
		if targetSlotPos == 69:
			constInfo.sufiyat69 = int(text1)
		if targetSlotPos == 70:
			constInfo.sufiyat70 = int(text1)
		if targetSlotPos == 71:
			constInfo.sufiyat71 = int(text1)
		if targetSlotPos == 72:
			constInfo.sufiyat72 = int(text1)
		if targetSlotPos == 73:
			constInfo.sufiyat73 = int(text1)
		if targetSlotPos == 74:
			constInfo.sufiyat74 = int(text1)
		if targetSlotPos == 75:
			constInfo.sufiyat75 = int(text1)
		if targetSlotPos == 76:
			constInfo.sufiyat76 = int(text1)
		if targetSlotPos == 77:
			constInfo.sufiyat77 = int(text1)
		if targetSlotPos == 78:
			constInfo.sufiyat78 = int(text1)
		if targetSlotPos == 79:
			constInfo.sufiyat79 = int(text1)
		if targetSlotPos == 80:
			constInfo.sufiyat80 = int(text1)
		if targetSlotPos == 81:
			constInfo.sufiyat81 = int(text1)
		if targetSlotPos == 82:
			constInfo.sufiyat82 = int(text1)
		if targetSlotPos == 83:
			constInfo.sufiyat83 = int(text1)
		if targetSlotPos == 84:
			constInfo.sufiyat84 = int(text1)
		if targetSlotPos == 85:
			constInfo.sufiyat85 = int(text1)
		if targetSlotPos == 86:
			constInfo.sufiyat86 = int(text1)
		if targetSlotPos == 87:
			constInfo.sufiyat87 = int(text1)
		if targetSlotPos == 88:
			constInfo.sufiyat88 = int(text1)
		if targetSlotPos == 89:
			constInfo.sufiyat89 = int(text1)
		if targetSlotPos == 90:
			constInfo.sufiyat90 = int(text1)
		if targetSlotPos == 91:
			constInfo.sufiyat91 = int(text1)
		if targetSlotPos == 92:
			constInfo.sufiyat92 = int(text1)
		if targetSlotPos == 93:
			constInfo.sufiyat93 = int(text1)
		if targetSlotPos == 94:
			constInfo.sufiyat94 = int(text1)
		if targetSlotPos == 95:
			constInfo.sufiyat95 = int(text1)
		if targetSlotPos == 96:
			constInfo.sufiyat96 = int(text1)
		if targetSlotPos == 97:
			constInfo.sufiyat97 = int(text1)
		if targetSlotPos == 98:
			constInfo.sufiyat98 = int(text1)
		if targetSlotPos == 99:
			constInfo.sufiyat99 = int(text1)
		if targetSlotPos == 100:
			constInfo.sufiyat100 = int(text1)
			
		if targetSlotPos == 0:
			constInfo.barfiyat0 = int(text2)
		if targetSlotPos == 1:
			constInfo.barfiyat1 = int(text2)
		if targetSlotPos == 2:
			constInfo.barfiyat2 = int(text2)
		if targetSlotPos == 3:
			constInfo.barfiyat3 = int(text2)
		if targetSlotPos == 4:
			constInfo.barfiyat4 = int(text2)
		if targetSlotPos == 5:
			constInfo.barfiyat5 = int(text2)
		if targetSlotPos == 6:
			constInfo.barfiyat6 = int(text2)
		if targetSlotPos == 7:
			constInfo.barfiyat7 = int(text2)
		if targetSlotPos == 8:
			constInfo.barfiyat8 = int(text2)
		if targetSlotPos == 9:
			constInfo.barfiyat9 = int(text2)
		if targetSlotPos == 10:
			constInfo.barfiyat10 = int(text2)
		if targetSlotPos == 11:
			constInfo.barfiyat11 = int(text2)
		if targetSlotPos == 12:
			constInfo.barfiyat12 = int(text2)
		if targetSlotPos == 13:
			constInfo.barfiyat13 = int(text2)
		if targetSlotPos == 14:
			constInfo.barfiyat14 = int(text2)
		if targetSlotPos == 15:
			constInfo.barfiyat15 = int(text2)
		if targetSlotPos == 16:
			constInfo.barfiyat16 = int(text2)
		if targetSlotPos == 17:
			constInfo.barfiyat17 = int(text2)
		if targetSlotPos == 18:
			constInfo.barfiyat18 = int(text2)
		if targetSlotPos == 19:
			constInfo.barfiyat19 = int(text2)
		if targetSlotPos == 20:
			constInfo.barfiyat20 = int(text2)
		if targetSlotPos == 21:
			constInfo.barfiyat21 = int(text2)
		if targetSlotPos == 22:
			constInfo.barfiyat22 = int(text2)
		if targetSlotPos == 23:
			constInfo.barfiyat23 = int(text2)
		if targetSlotPos == 24:
			constInfo.barfiyat24 = int(text2)
		if targetSlotPos == 25:
			constInfo.barfiyat25 = int(text2)
		if targetSlotPos == 26:
			constInfo.barfiyat26 = int(text2)
		if targetSlotPos == 27:
			constInfo.barfiyat27 = int(text2)
		if targetSlotPos == 28:
			constInfo.barfiyat28 = int(text2)
		if targetSlotPos == 29:
			constInfo.barfiyat29 = int(text2)
		if targetSlotPos == 30:
			constInfo.barfiyat30 = int(text2)
		if targetSlotPos == 31:
			constInfo.barfiyat31 = int(text2)
		if targetSlotPos == 32:
			constInfo.barfiyat32 = int(text2)
		if targetSlotPos == 33:
			constInfo.barfiyat33 = int(text2)
		if targetSlotPos == 34:
			constInfo.barfiyat34 = int(text2)
		if targetSlotPos == 35:
			constInfo.barfiyat35 = int(text2)
		if targetSlotPos == 36:
			constInfo.barfiyat36 = int(text2)
		if targetSlotPos == 37:
			constInfo.barfiyat37 = int(text2)
		if targetSlotPos == 38:
			constInfo.barfiyat38 = int(text2)
		if targetSlotPos == 39:
			constInfo.barfiyat39 = int(text2)
		if targetSlotPos == 40:
			constInfo.barfiyat40 = int(text2)
		if targetSlotPos == 41:
			constInfo.barfiyat41 = int(text2)
		if targetSlotPos == 42:
			constInfo.barfiyat42 = int(text2)
		if targetSlotPos == 43:
			constInfo.barfiyat43 = int(text2)
		if targetSlotPos == 44:
			constInfo.barfiyat44 = int(text2)
		if targetSlotPos == 45:
			constInfo.barfiyat45 = int(text2)
		if targetSlotPos == 46:
			constInfo.barfiyat46 = int(text2)
		if targetSlotPos == 47:
			constInfo.barfiyat47 = int(text2)
		if targetSlotPos == 48:
			constInfo.barfiyat48 = int(text2)
		if targetSlotPos == 49:
			constInfo.barfiyat49 = int(text2)
		if targetSlotPos == 50:
			constInfo.barfiyat50 = int(text2)
		if targetSlotPos == 51:
			constInfo.barfiyat51 = int(text2)
		if targetSlotPos == 52:
			constInfo.barfiyat52 = int(text2)
		if targetSlotPos == 53:
			constInfo.barfiyat53 = int(text2)
		if targetSlotPos == 54:
			constInfo.barfiyat54 = int(text2)
		if targetSlotPos == 55:
			constInfo.barfiyat55 = int(text2)
		if targetSlotPos == 56:
			constInfo.barfiyat56 = int(text2)
		if targetSlotPos == 57:
			constInfo.barfiyat57 = int(text2)
		if targetSlotPos == 58:
			constInfo.barfiyat58 = int(text2)
		if targetSlotPos == 59:
			constInfo.barfiyat59 = int(text2)
		if targetSlotPos == 60:
			constInfo.barfiyat60 = int(text2)
		if targetSlotPos == 61:
			constInfo.barfiyat61 = int(text2)
		if targetSlotPos == 62:
			constInfo.barfiyat62 = int(text2)
		if targetSlotPos == 63:
			constInfo.barfiyat63 = int(text2)
		if targetSlotPos == 64:
			constInfo.barfiyat64 = int(text2)
		if targetSlotPos == 65:
			constInfo.barfiyat65 = int(text2)
		if targetSlotPos == 66:
			constInfo.barfiyat66 = int(text2)
		if targetSlotPos == 67:
			constInfo.barfiyat67 = int(text2)
		if targetSlotPos == 68:
			constInfo.barfiyat68 = int(text2)
		if targetSlotPos == 69:
			constInfo.barfiyat69 = int(text2)
		if targetSlotPos == 70:
			constInfo.barfiyat70 = int(text2)
		if targetSlotPos == 71:
			constInfo.barfiyat71 = int(text2)
		if targetSlotPos == 72:
			constInfo.barfiyat72 = int(text2)
		if targetSlotPos == 73:
			constInfo.barfiyat73 = int(text2)
		if targetSlotPos == 74:
			constInfo.barfiyat74 = int(text2)
		if targetSlotPos == 75:
			constInfo.barfiyat75 = int(text2)
		if targetSlotPos == 76:
			constInfo.barfiyat76 = int(text2)
		if targetSlotPos == 77:
			constInfo.barfiyat77 = int(text2)
		if targetSlotPos == 78:
			constInfo.barfiyat78 = int(text2)
		if targetSlotPos == 79:
			constInfo.barfiyat79 = int(text2)
		if targetSlotPos == 80:
			constInfo.barfiyat80 = int(text2)
		if targetSlotPos == 81:
			constInfo.barfiyat81 = int(text2)
		if targetSlotPos == 82:
			constInfo.barfiyat82 = int(text2)
		if targetSlotPos == 83:
			constInfo.barfiyat83 = int(text2)
		if targetSlotPos == 84:
			constInfo.barfiyat84 = int(text2)
		if targetSlotPos == 85:
			constInfo.barfiyat85 = int(text2)
		if targetSlotPos == 86:
			constInfo.barfiyat86 = int(text2)
		if targetSlotPos == 87:
			constInfo.barfiyat87 = int(text2)
		if targetSlotPos == 88:
			constInfo.barfiyat88 = int(text2)
		if targetSlotPos == 89:
			constInfo.barfiyat89 = int(text2)
		if targetSlotPos == 90:
			constInfo.barfiyat90 = int(text2)
		if targetSlotPos == 91:
			constInfo.barfiyat91 = int(text2)
		if targetSlotPos == 92:
			constInfo.barfiyat92 = int(text2)
		if targetSlotPos == 93:
			constInfo.barfiyat93 = int(text2)
		if targetSlotPos == 94:
			constInfo.barfiyat94 = int(text2)
		if targetSlotPos == 95:
			constInfo.barfiyat95 = int(text2)
		if targetSlotPos == 96:
			constInfo.barfiyat96 = int(text2)
		if targetSlotPos == 97:
			constInfo.barfiyat97 = int(text2)
		if targetSlotPos == 98:
			constInfo.barfiyat98 = int(text2)
		if targetSlotPos == 99:
			constInfo.barfiyat99 = int(text2)
		if targetSlotPos == 100:
			constInfo.barfiyat100 = int(text2)

		if targetSlotPos == 0:
			constInfo.yesilot0 = int(text3)
		if targetSlotPos == 1:
			constInfo.yesilot1 = int(text3)
		if targetSlotPos == 2:
			constInfo.yesilot2 = int(text3)
		if targetSlotPos == 3:
			constInfo.yesilot3 = int(text3)
		if targetSlotPos == 4:
			constInfo.yesilot4 = int(text3)
		if targetSlotPos == 5:
			constInfo.yesilot5 = int(text3)
		if targetSlotPos == 6:
			constInfo.yesilot6 = int(text3)
		if targetSlotPos == 7:
			constInfo.yesilot7 = int(text3)
		if targetSlotPos == 8:
			constInfo.yesilot8 = int(text3)
		if targetSlotPos == 9:
			constInfo.yesilot9 = int(text3)
		if targetSlotPos == 10:
			constInfo.yesilot10 = int(text3)
		if targetSlotPos == 11:
			constInfo.yesilot11 = int(text3)
		if targetSlotPos == 12:
			constInfo.yesilot12 = int(text3)
		if targetSlotPos == 13:
			constInfo.yesilot13 = int(text3)
		if targetSlotPos == 14:
			constInfo.yesilot14 = int(text3)
		if targetSlotPos == 15:
			constInfo.yesilot15 = int(text3)
		if targetSlotPos == 16:
			constInfo.yesilot16 = int(text3)
		if targetSlotPos == 17:
			constInfo.yesilot17 = int(text3)
		if targetSlotPos == 18:
			constInfo.yesilot18 = int(text3)
		if targetSlotPos == 19:
			constInfo.yesilot19 = int(text3)
		if targetSlotPos == 20:
			constInfo.yesilot20 = int(text3)
		if targetSlotPos == 21:
			constInfo.yesilot21 = int(text3)
		if targetSlotPos == 22:
			constInfo.yesilot22 = int(text3)
		if targetSlotPos == 23:
			constInfo.yesilot23 = int(text3)
		if targetSlotPos == 24:
			constInfo.yesilot24 = int(text3)
		if targetSlotPos == 25:
			constInfo.yesilot25 = int(text3)
		if targetSlotPos == 26:
			constInfo.yesilot26 = int(text3)
		if targetSlotPos == 27:
			constInfo.yesilot27 = int(text3)
		if targetSlotPos == 28:
			constInfo.yesilot28 = int(text3)
		if targetSlotPos == 29:
			constInfo.yesilot29 = int(text3)
		if targetSlotPos == 30:
			constInfo.yesilot30 = int(text3)
		if targetSlotPos == 31:
			constInfo.yesilot31 = int(text3)
		if targetSlotPos == 32:
			constInfo.yesilot32 = int(text3)
		if targetSlotPos == 33:
			constInfo.yesilot33 = int(text3)
		if targetSlotPos == 34:
			constInfo.yesilot34 = int(text3)
		if targetSlotPos == 35:
			constInfo.yesilot35 = int(text3)
		if targetSlotPos == 36:
			constInfo.yesilot36 = int(text3)
		if targetSlotPos == 37:
			constInfo.yesilot37 = int(text3)
		if targetSlotPos == 38:
			constInfo.yesilot38 = int(text3)
		if targetSlotPos == 39:
			constInfo.yesilot39 = int(text3)
		if targetSlotPos == 40:
			constInfo.yesilot40 = int(text3)
		if targetSlotPos == 41:
			constInfo.yesilot41 = int(text3)
		if targetSlotPos == 42:
			constInfo.yesilot42 = int(text3)
		if targetSlotPos == 43:
			constInfo.yesilot43 = int(text3)
		if targetSlotPos == 44:
			constInfo.yesilot44 = int(text3)
		if targetSlotPos == 45:
			constInfo.yesilot45 = int(text3)
		if targetSlotPos == 46:
			constInfo.yesilot46 = int(text3)
		if targetSlotPos == 47:
			constInfo.yesilot47 = int(text3)
		if targetSlotPos == 48:
			constInfo.yesilot48 = int(text3)
		if targetSlotPos == 49:
			constInfo.yesilot49 = int(text3)
		if targetSlotPos == 50:
			constInfo.yesilot50 = int(text3)
		if targetSlotPos == 51:
			constInfo.yesilot51 = int(text3)
		if targetSlotPos == 52:
			constInfo.yesilot52 = int(text3)
		if targetSlotPos == 53:
			constInfo.yesilot53 = int(text3)
		if targetSlotPos == 54:
			constInfo.yesilot54 = int(text3)
		if targetSlotPos == 55:
			constInfo.yesilot55 = int(text3)
		if targetSlotPos == 56:
			constInfo.yesilot56 = int(text3)
		if targetSlotPos == 57:
			constInfo.yesilot57 = int(text3)
		if targetSlotPos == 58:
			constInfo.yesilot58 = int(text3)
		if targetSlotPos == 59:
			constInfo.yesilot59 = int(text3)
		if targetSlotPos == 60:
			constInfo.yesilot60 = int(text3)
		if targetSlotPos == 61:
			constInfo.yesilot61 = int(text3)
		if targetSlotPos == 62:
			constInfo.yesilot62 = int(text3)
		if targetSlotPos == 63:
			constInfo.yesilot63 = int(text3)
		if targetSlotPos == 64:
			constInfo.yesilot64 = int(text3)
		if targetSlotPos == 65:
			constInfo.yesilot65 = int(text3)
		if targetSlotPos == 66:
			constInfo.yesilot66 = int(text3)
		if targetSlotPos == 67:
			constInfo.yesilot67 = int(text3)
		if targetSlotPos == 68:
			constInfo.yesilot68 = int(text3)
		if targetSlotPos == 69:
			constInfo.yesilot69 = int(text3)
		if targetSlotPos == 70:
			constInfo.yesilot70 = int(text3)
		if targetSlotPos == 71:
			constInfo.yesilot71 = int(text3)
		if targetSlotPos == 72:
			constInfo.yesilot72 = int(text3)
		if targetSlotPos == 73:
			constInfo.yesilot73 = int(text3)
		if targetSlotPos == 74:
			constInfo.yesilot74 = int(text3)
		if targetSlotPos == 75:
			constInfo.yesilot75 = int(text3)
		if targetSlotPos == 76:
			constInfo.yesilot76 = int(text3)
		if targetSlotPos == 77:
			constInfo.yesilot77 = int(text3)
		if targetSlotPos == 78:
			constInfo.yesilot78 = int(text3)
		if targetSlotPos == 79:
			constInfo.yesilot79 = int(text3)
		if targetSlotPos == 80:
			constInfo.yesilot80 = int(text3)
		if targetSlotPos == 81:
			constInfo.yesilot81 = int(text3)
		if targetSlotPos == 82:
			constInfo.yesilot82 = int(text3)
		if targetSlotPos == 83:
			constInfo.yesilot83 = int(text3)
		if targetSlotPos == 84:
			constInfo.yesilot84 = int(text3)
		if targetSlotPos == 85:
			constInfo.yesilot85 = int(text3)
		if targetSlotPos == 86:
			constInfo.yesilot86 = int(text3)
		if targetSlotPos == 87:
			constInfo.yesilot87 = int(text3)
		if targetSlotPos == 88:
			constInfo.yesilot88 = int(text3)
		if targetSlotPos == 89:
			constInfo.yesilot89 = int(text3)
		if targetSlotPos == 90:
			constInfo.yesilot90 = int(text3)
		if targetSlotPos == 91:
			constInfo.yesilot91 = int(text3)
		if targetSlotPos == 92:
			constInfo.yesilot92 = int(text3)
		if targetSlotPos == 93:
			constInfo.yesilot93 = int(text3)
		if targetSlotPos == 94:
			constInfo.yesilot94 = int(text3)
		if targetSlotPos == 95:
			constInfo.yesilot95 = int(text3)
		if targetSlotPos == 96:
			constInfo.yesilot96 = int(text3)
		if targetSlotPos == 97:
			constInfo.yesilot97 = int(text3)
		if targetSlotPos == 98:
			constInfo.yesilot98 = int(text3)
		if targetSlotPos == 99:
			constInfo.yesilot99 = int(text3)
		if targetSlotPos == 100:
			constInfo.yesilot100 = int(text3)
		if targetSlotPos == 0:
			constInfo.kirmiziot0 = int(text4)
		if targetSlotPos == 1:
			constInfo.kirmiziot1 = int(text4)
		if targetSlotPos == 2:
			constInfo.kirmiziot2 = int(text4)
		if targetSlotPos == 3:
			constInfo.kirmiziot3 = int(text4)
		if targetSlotPos == 4:
			constInfo.kirmiziot4 = int(text4)
		if targetSlotPos == 5:
			constInfo.kirmiziot5 = int(text4)
		if targetSlotPos == 6:
			constInfo.kirmiziot6 = int(text4)
		if targetSlotPos == 7:
			constInfo.kirmiziot7 = int(text4)
		if targetSlotPos == 8:
			constInfo.kirmiziot8 = int(text4)
		if targetSlotPos == 9:
			constInfo.kirmiziot9 = int(text4)
		if targetSlotPos == 10:
			constInfo.kirmiziot10 = int(text4)
		if targetSlotPos == 11:
			constInfo.kirmiziot11 = int(text4)
		if targetSlotPos == 12:
			constInfo.kirmiziot12 = int(text4)
		if targetSlotPos == 13:
			constInfo.kirmiziot13 = int(text4)
		if targetSlotPos == 14:
			constInfo.kirmiziot14 = int(text4)
		if targetSlotPos == 15:
			constInfo.kirmiziot15 = int(text4)
		if targetSlotPos == 16:
			constInfo.kirmiziot16 = int(text4)
		if targetSlotPos == 17:
			constInfo.kirmiziot17 = int(text4)
		if targetSlotPos == 18:
			constInfo.kirmiziot18 = int(text4)
		if targetSlotPos == 19:
			constInfo.kirmiziot19 = int(text4)
		if targetSlotPos == 20:
			constInfo.kirmiziot20 = int(text4)
		if targetSlotPos == 21:
			constInfo.kirmiziot21 = int(text4)
		if targetSlotPos == 22:
			constInfo.kirmiziot22 = int(text4)
		if targetSlotPos == 23:
			constInfo.kirmiziot23 = int(text4)
		if targetSlotPos == 24:
			constInfo.kirmiziot24 = int(text4)
		if targetSlotPos == 25:
			constInfo.kirmiziot25 = int(text4)
		if targetSlotPos == 26:
			constInfo.kirmiziot26 = int(text4)
		if targetSlotPos == 27:
			constInfo.kirmiziot27 = int(text4)
		if targetSlotPos == 28:
			constInfo.kirmiziot28 = int(text4)
		if targetSlotPos == 29:
			constInfo.kirmiziot29 = int(text4)
		if targetSlotPos == 30:
			constInfo.kirmiziot30 = int(text4)
		if targetSlotPos == 31:
			constInfo.kirmiziot31 = int(text4)
		if targetSlotPos == 32:
			constInfo.kirmiziot32 = int(text4)
		if targetSlotPos == 33:
			constInfo.kirmiziot33 = int(text4)
		if targetSlotPos == 34:
			constInfo.kirmiziot34 = int(text4)
		if targetSlotPos == 35:
			constInfo.kirmiziot35 = int(text4)
		if targetSlotPos == 36:
			constInfo.kirmiziot36 = int(text4)
		if targetSlotPos == 37:
			constInfo.kirmiziot37 = int(text4)
		if targetSlotPos == 38:
			constInfo.kirmiziot38 = int(text4)
		if targetSlotPos == 39:
			constInfo.kirmiziot39 = int(text4)
		if targetSlotPos == 40:
			constInfo.kirmiziot40 = int(text4)
		if targetSlotPos == 41:
			constInfo.kirmiziot41 = int(text4)
		if targetSlotPos == 42:
			constInfo.kirmiziot42 = int(text4)
		if targetSlotPos == 43:
			constInfo.kirmiziot43 = int(text4)
		if targetSlotPos == 44:
			constInfo.kirmiziot44 = int(text4)
		if targetSlotPos == 45:
			constInfo.kirmiziot45 = int(text4)
		if targetSlotPos == 46:
			constInfo.kirmiziot46 = int(text4)
		if targetSlotPos == 47:
			constInfo.kirmiziot47 = int(text4)
		if targetSlotPos == 48:
			constInfo.kirmiziot48 = int(text4)
		if targetSlotPos == 49:
			constInfo.kirmiziot49 = int(text4)
		if targetSlotPos == 50:
			constInfo.kirmiziot50 = int(text4)
		if targetSlotPos == 51:
			constInfo.kirmiziot51 = int(text4)
		if targetSlotPos == 52:
			constInfo.kirmiziot52 = int(text4)
		if targetSlotPos == 53:
			constInfo.kirmiziot53 = int(text4)
		if targetSlotPos == 54:
			constInfo.kirmiziot54 = int(text4)
		if targetSlotPos == 55:
			constInfo.kirmiziot55 = int(text4)
		if targetSlotPos == 56:
			constInfo.kirmiziot56 = int(text4)
		if targetSlotPos == 57:
			constInfo.kirmiziot57 = int(text4)
		if targetSlotPos == 58:
			constInfo.kirmiziot58 = int(text4)
		if targetSlotPos == 59:
			constInfo.kirmiziot59 = int(text4)
		if targetSlotPos == 60:
			constInfo.kirmiziot60 = int(text4)
		if targetSlotPos == 61:
			constInfo.kirmiziot61 = int(text4)
		if targetSlotPos == 62:
			constInfo.kirmiziot62 = int(text4)
		if targetSlotPos == 63:
			constInfo.kirmiziot63 = int(text4)
		if targetSlotPos == 64:
			constInfo.kirmiziot64 = int(text4)
		if targetSlotPos == 65:
			constInfo.kirmiziot65 = int(text4)
		if targetSlotPos == 66:
			constInfo.kirmiziot66 = int(text4)
		if targetSlotPos == 67:
			constInfo.kirmiziot67 = int(text4)
		if targetSlotPos == 68:
			constInfo.kirmiziot68 = int(text4)
		if targetSlotPos == 69:
			constInfo.kirmiziot69 = int(text4)
		if targetSlotPos == 70:
			constInfo.kirmiziot70 = int(text4)
		if targetSlotPos == 71:
			constInfo.kirmiziot71 = int(text4)
		if targetSlotPos == 72:
			constInfo.kirmiziot72 = int(text4)
		if targetSlotPos == 73:
			constInfo.kirmiziot73 = int(text4)
		if targetSlotPos == 74:
			constInfo.kirmiziot74 = int(text4)
		if targetSlotPos == 75:
			constInfo.kirmiziot75 = int(text4)
		if targetSlotPos == 76:
			constInfo.kirmiziot76 = int(text4)
		if targetSlotPos == 77:
			constInfo.kirmiziot77 = int(text4)
		if targetSlotPos == 78:
			constInfo.kirmiziot78 = int(text4)
		if targetSlotPos == 79:
			constInfo.kirmiziot79 = int(text4)
		if targetSlotPos == 80:
			constInfo.kirmiziot80 = int(text4)
		if targetSlotPos == 81:
			constInfo.kirmiziot81 = int(text4)
		if targetSlotPos == 82:
			constInfo.kirmiziot82 = int(text4)
		if targetSlotPos == 83:
			constInfo.kirmiziot83 = int(text4)
		if targetSlotPos == 84:
			constInfo.kirmiziot84 = int(text4)
		if targetSlotPos == 85:
			constInfo.kirmiziot85 = int(text4)
		if targetSlotPos == 86:
			constInfo.kirmiziot86 = int(text4)
		if targetSlotPos == 87:
			constInfo.kirmiziot87 = int(text4)
		if targetSlotPos == 88:
			constInfo.kirmiziot88 = int(text4)
		if targetSlotPos == 89:
			constInfo.kirmiziot89 = int(text4)
		if targetSlotPos == 90:
			constInfo.kirmiziot90 = int(text4)
		if targetSlotPos == 91:
			constInfo.kirmiziot91 = int(text4)
		if targetSlotPos == 92:
			constInfo.kirmiziot92 = int(text4)
		if targetSlotPos == 93:
			constInfo.kirmiziot93 = int(text4)
		if targetSlotPos == 94:
			constInfo.kirmiziot94 = int(text4)
		if targetSlotPos == 95:
			constInfo.kirmiziot95 = int(text4)
		if targetSlotPos == 96:
			constInfo.kirmiziot96 = int(text4)
		if targetSlotPos == 97:
			constInfo.kirmiziot97 = int(text4)
		if targetSlotPos == 98:
			constInfo.kirmiziot98 = int(text4)
		if targetSlotPos == 99:
			constInfo.kirmiziot99 = int(text4)
		if targetSlotPos == 100:
			constInfo.kirmiziot100 = int(text4)
		if targetSlotPos == 0:
			constInfo.maviot0 = int(text5)
		if targetSlotPos == 1:
			constInfo.maviot1 = int(text5)
		if targetSlotPos == 2:
			constInfo.maviot2 = int(text5)
		if targetSlotPos == 3:
			constInfo.maviot3 = int(text5)
		if targetSlotPos == 4:
			constInfo.maviot4 = int(text5)
		if targetSlotPos == 5:
			constInfo.maviot5 = int(text5)
		if targetSlotPos == 6:
			constInfo.maviot6 = int(text5)
		if targetSlotPos == 7:
			constInfo.maviot7 = int(text5)
		if targetSlotPos == 8:
			constInfo.maviot8 = int(text5)
		if targetSlotPos == 9:
			constInfo.maviot9 = int(text5)
		if targetSlotPos == 10:
			constInfo.maviot10 = int(text5)
		if targetSlotPos == 11:
			constInfo.maviot11 = int(text5)
		if targetSlotPos == 12:
			constInfo.maviot12 = int(text5)
		if targetSlotPos == 13:
			constInfo.maviot13 = int(text5)
		if targetSlotPos == 14:
			constInfo.maviot14 = int(text5)
		if targetSlotPos == 15:
			constInfo.maviot15 = int(text5)
		if targetSlotPos == 16:
			constInfo.maviot16 = int(text5)
		if targetSlotPos == 17:
			constInfo.maviot17 = int(text5)
		if targetSlotPos == 18:
			constInfo.maviot18 = int(text5)
		if targetSlotPos == 19:
			constInfo.maviot19 = int(text5)
		if targetSlotPos == 20:
			constInfo.maviot20 = int(text5)
		if targetSlotPos == 21:
			constInfo.maviot21 = int(text5)
		if targetSlotPos == 22:
			constInfo.maviot22 = int(text5)
		if targetSlotPos == 23:
			constInfo.maviot23 = int(text5)
		if targetSlotPos == 24:
			constInfo.maviot24 = int(text5)
		if targetSlotPos == 25:
			constInfo.maviot25 = int(text5)
		if targetSlotPos == 26:
			constInfo.maviot26 = int(text5)
		if targetSlotPos == 27:
			constInfo.maviot27 = int(text5)
		if targetSlotPos == 28:
			constInfo.maviot28 = int(text5)
		if targetSlotPos == 29:
			constInfo.maviot29 = int(text5)
		if targetSlotPos == 30:
			constInfo.maviot30 = int(text5)
		if targetSlotPos == 31:
			constInfo.maviot31 = int(text5)
		if targetSlotPos == 32:
			constInfo.maviot32 = int(text5)
		if targetSlotPos == 33:
			constInfo.maviot33 = int(text5)
		if targetSlotPos == 34:
			constInfo.maviot34 = int(text5)
		if targetSlotPos == 35:
			constInfo.maviot35 = int(text5)
		if targetSlotPos == 36:
			constInfo.maviot36 = int(text5)
		if targetSlotPos == 37:
			constInfo.maviot37 = int(text5)
		if targetSlotPos == 38:
			constInfo.maviot38 = int(text5)
		if targetSlotPos == 39:
			constInfo.maviot39 = int(text5)
		if targetSlotPos == 40:
			constInfo.maviot40 = int(text5)
		if targetSlotPos == 41:
			constInfo.maviot41 = int(text5)
		if targetSlotPos == 42:
			constInfo.maviot42 = int(text5)
		if targetSlotPos == 43:
			constInfo.maviot43 = int(text5)
		if targetSlotPos == 44:
			constInfo.maviot44 = int(text5)
		if targetSlotPos == 45:
			constInfo.maviot45 = int(text5)
		if targetSlotPos == 46:
			constInfo.maviot46 = int(text5)
		if targetSlotPos == 47:
			constInfo.maviot47 = int(text5)
		if targetSlotPos == 48:
			constInfo.maviot48 = int(text5)
		if targetSlotPos == 49:
			constInfo.maviot49 = int(text5)
		if targetSlotPos == 50:
			constInfo.maviot50 = int(text5)
		if targetSlotPos == 51:
			constInfo.maviot51 = int(text5)
		if targetSlotPos == 52:
			constInfo.maviot52 = int(text5)
		if targetSlotPos == 53:
			constInfo.maviot53 = int(text5)
		if targetSlotPos == 54:
			constInfo.maviot54 = int(text5)
		if targetSlotPos == 55:
			constInfo.maviot55 = int(text5)
		if targetSlotPos == 56:
			constInfo.maviot56 = int(text5)
		if targetSlotPos == 57:
			constInfo.maviot57 = int(text5)
		if targetSlotPos == 58:
			constInfo.maviot58 = int(text5)
		if targetSlotPos == 59:
			constInfo.maviot59 = int(text5)
		if targetSlotPos == 60:
			constInfo.maviot60 = int(text5)
		if targetSlotPos == 61:
			constInfo.maviot61 = int(text5)
		if targetSlotPos == 62:
			constInfo.maviot62 = int(text5)
		if targetSlotPos == 63:
			constInfo.maviot63 = int(text5)
		if targetSlotPos == 64:
			constInfo.maviot64 = int(text5)
		if targetSlotPos == 65:
			constInfo.maviot65 = int(text5)
		if targetSlotPos == 66:
			constInfo.maviot66 = int(text5)
		if targetSlotPos == 67:
			constInfo.maviot67 = int(text5)
		if targetSlotPos == 68:
			constInfo.maviot68 = int(text5)
		if targetSlotPos == 69:
			constInfo.maviot69 = int(text5)
		if targetSlotPos == 70:
			constInfo.maviot70 = int(text5)
		if targetSlotPos == 71:
			constInfo.maviot71 = int(text5)
		if targetSlotPos == 72:
			constInfo.maviot72 = int(text5)
		if targetSlotPos == 73:
			constInfo.maviot73 = int(text5)
		if targetSlotPos == 74:
			constInfo.maviot74 = int(text5)
		if targetSlotPos == 75:
			constInfo.maviot75 = int(text5)
		if targetSlotPos == 76:
			constInfo.maviot76 = int(text5)
		if targetSlotPos == 77:
			constInfo.maviot77 = int(text5)
		if targetSlotPos == 78:
			constInfo.maviot78 = int(text5)
		if targetSlotPos == 79:
			constInfo.maviot79 = int(text5)
		if targetSlotPos == 80:
			constInfo.maviot80 = int(text5)
		if targetSlotPos == 81:
			constInfo.maviot81 = int(text5)
		if targetSlotPos == 82:
			constInfo.maviot82 = int(text5)
		if targetSlotPos == 83:
			constInfo.maviot83 = int(text5)
		if targetSlotPos == 84:
			constInfo.maviot84 = int(text5)
		if targetSlotPos == 85:
			constInfo.maviot85 = int(text5)
		if targetSlotPos == 86:
			constInfo.maviot86 = int(text5)
		if targetSlotPos == 87:
			constInfo.maviot87 = int(text5)
		if targetSlotPos == 88:
			constInfo.maviot88 = int(text5)
		if targetSlotPos == 89:
			constInfo.maviot89 = int(text5)
		if targetSlotPos == 90:
			constInfo.maviot90 = int(text5)
		if targetSlotPos == 91:
			constInfo.maviot91 = int(text5)
		if targetSlotPos == 92:
			constInfo.maviot92 = int(text5)
		if targetSlotPos == 93:
			constInfo.maviot93 = int(text5)
		if targetSlotPos == 94:
			constInfo.maviot94 = int(text5)
		if targetSlotPos == 95:
			constInfo.maviot95 = int(text5)
		if targetSlotPos == 96:
			constInfo.maviot96 = int(text5)
		if targetSlotPos == 97:
			constInfo.maviot97 = int(text5)
		if targetSlotPos == 98:
			constInfo.maviot98 = int(text5)
		if targetSlotPos == 99:
			constInfo.maviot99 = int(text5)
		if targetSlotPos == 100:
			constInfo.maviot100 = int(text5)
		if targetSlotPos == 0:
			constInfo.morot0 = int(text6)
		if targetSlotPos == 1:
			constInfo.morot1 = int(text6)
		if targetSlotPos == 2:
			constInfo.morot2 = int(text6)
		if targetSlotPos == 3:
			constInfo.morot3 = int(text6)
		if targetSlotPos == 4:
			constInfo.morot4 = int(text6)
		if targetSlotPos == 5:
			constInfo.morot5 = int(text6)
		if targetSlotPos == 6:
			constInfo.morot6 = int(text6)
		if targetSlotPos == 7:
			constInfo.morot7 = int(text6)
		if targetSlotPos == 8:
			constInfo.morot8 = int(text6)
		if targetSlotPos == 9:
			constInfo.morot9 = int(text6)
		if targetSlotPos == 10:
			constInfo.morot10 = int(text6)
		if targetSlotPos == 11:
			constInfo.morot11 = int(text6)
		if targetSlotPos == 12:
			constInfo.morot12 = int(text6)
		if targetSlotPos == 13:
			constInfo.morot13 = int(text6)
		if targetSlotPos == 14:
			constInfo.morot14 = int(text6)
		if targetSlotPos == 15:
			constInfo.morot15 = int(text6)
		if targetSlotPos == 16:
			constInfo.morot16 = int(text6)
		if targetSlotPos == 17:
			constInfo.morot17 = int(text6)
		if targetSlotPos == 18:
			constInfo.morot18 = int(text6)
		if targetSlotPos == 19:
			constInfo.morot19 = int(text6)
		if targetSlotPos == 20:
			constInfo.morot20 = int(text6)
		if targetSlotPos == 21:
			constInfo.morot21 = int(text6)
		if targetSlotPos == 22:
			constInfo.morot22 = int(text6)
		if targetSlotPos == 23:
			constInfo.morot23 = int(text6)
		if targetSlotPos == 24:
			constInfo.morot24 = int(text6)
		if targetSlotPos == 25:
			constInfo.morot25 = int(text6)
		if targetSlotPos == 26:
			constInfo.morot26 = int(text6)
		if targetSlotPos == 27:
			constInfo.morot27 = int(text6)
		if targetSlotPos == 28:
			constInfo.morot28 = int(text6)
		if targetSlotPos == 29:
			constInfo.morot29 = int(text6)
		if targetSlotPos == 30:
			constInfo.morot30 = int(text6)
		if targetSlotPos == 31:
			constInfo.morot31 = int(text6)
		if targetSlotPos == 32:
			constInfo.morot32 = int(text6)
		if targetSlotPos == 33:
			constInfo.morot33 = int(text6)
		if targetSlotPos == 34:
			constInfo.morot34 = int(text6)
		if targetSlotPos == 35:
			constInfo.morot35 = int(text6)
		if targetSlotPos == 36:
			constInfo.morot36 = int(text6)
		if targetSlotPos == 37:
			constInfo.morot37 = int(text6)
		if targetSlotPos == 38:
			constInfo.morot38 = int(text6)
		if targetSlotPos == 39:
			constInfo.morot39 = int(text6)
		if targetSlotPos == 40:
			constInfo.morot40 = int(text6)
		if targetSlotPos == 41:
			constInfo.morot41 = int(text6)
		if targetSlotPos == 42:
			constInfo.morot42 = int(text6)
		if targetSlotPos == 43:
			constInfo.morot43 = int(text6)
		if targetSlotPos == 44:
			constInfo.morot44 = int(text6)
		if targetSlotPos == 45:
			constInfo.morot45 = int(text6)
		if targetSlotPos == 46:
			constInfo.morot46 = int(text6)
		if targetSlotPos == 47:
			constInfo.morot47 = int(text6)
		if targetSlotPos == 48:
			constInfo.morot48 = int(text6)
		if targetSlotPos == 49:
			constInfo.morot49 = int(text6)
		if targetSlotPos == 50:
			constInfo.morot50 = int(text6)
		if targetSlotPos == 51:
			constInfo.morot51 = int(text6)
		if targetSlotPos == 52:
			constInfo.morot52 = int(text6)
		if targetSlotPos == 53:
			constInfo.morot53 = int(text6)
		if targetSlotPos == 54:
			constInfo.morot54 = int(text6)
		if targetSlotPos == 55:
			constInfo.morot55 = int(text6)
		if targetSlotPos == 56:
			constInfo.morot56 = int(text6)
		if targetSlotPos == 57:
			constInfo.morot57 = int(text6)
		if targetSlotPos == 58:
			constInfo.morot58 = int(text6)
		if targetSlotPos == 59:
			constInfo.morot59 = int(text6)
		if targetSlotPos == 60:
			constInfo.morot60 = int(text6)
		if targetSlotPos == 61:
			constInfo.morot61 = int(text6)
		if targetSlotPos == 62:
			constInfo.morot62 = int(text6)
		if targetSlotPos == 63:
			constInfo.morot63 = int(text6)
		if targetSlotPos == 64:
			constInfo.morot64 = int(text6)
		if targetSlotPos == 65:
			constInfo.morot65 = int(text6)
		if targetSlotPos == 66:
			constInfo.morot66 = int(text6)
		if targetSlotPos == 67:
			constInfo.morot67 = int(text6)
		if targetSlotPos == 68:
			constInfo.morot68 = int(text6)
		if targetSlotPos == 69:
			constInfo.morot69 = int(text6)
		if targetSlotPos == 70:
			constInfo.morot70 = int(text6)
		if targetSlotPos == 71:
			constInfo.morot71 = int(text6)
		if targetSlotPos == 72:
			constInfo.morot72 = int(text6)
		if targetSlotPos == 73:
			constInfo.morot73 = int(text6)
		if targetSlotPos == 74:
			constInfo.morot74 = int(text6)
		if targetSlotPos == 75:
			constInfo.morot75 = int(text6)
		if targetSlotPos == 76:
			constInfo.morot76 = int(text6)
		if targetSlotPos == 77:
			constInfo.morot77 = int(text6)
		if targetSlotPos == 78:
			constInfo.morot78 = int(text6)
		if targetSlotPos == 79:
			constInfo.morot79 = int(text6)
		if targetSlotPos == 80:
			constInfo.morot80 = int(text6)
		if targetSlotPos == 81:
			constInfo.morot81 = int(text6)
		if targetSlotPos == 82:
			constInfo.morot82 = int(text6)
		if targetSlotPos == 83:
			constInfo.morot83 = int(text6)
		if targetSlotPos == 84:
			constInfo.morot84 = int(text6)
		if targetSlotPos == 85:
			constInfo.morot85 = int(text6)
		if targetSlotPos == 86:
			constInfo.morot86 = int(text6)
		if targetSlotPos == 87:
			constInfo.morot87 = int(text6)
		if targetSlotPos == 88:
			constInfo.morot88 = int(text6)
		if targetSlotPos == 89:
			constInfo.morot89 = int(text6)
		if targetSlotPos == 90:
			constInfo.morot90 = int(text6)
		if targetSlotPos == 91:
			constInfo.morot91 = int(text6)
		if targetSlotPos == 92:
			constInfo.morot92 = int(text6)
		if targetSlotPos == 93:
			constInfo.morot93 = int(text6)
		if targetSlotPos == 94:
			constInfo.morot94 = int(text6)
		if targetSlotPos == 95:
			constInfo.morot95 = int(text6)
		if targetSlotPos == 96:
			constInfo.morot96 = int(text6)
		if targetSlotPos == 97:
			constInfo.morot97 = int(text6)
		if targetSlotPos == 98:
			constInfo.morot98 = int(text6)
		if targetSlotPos == 99:
			constInfo.morot99 = int(text6)
		if targetSlotPos == 100:
			constInfo.morot100 = int(text6)
		if targetSlotPos == 0:
			constInfo.ruhtasi0 = int(text7)
		if targetSlotPos == 1:
			constInfo.ruhtasi1 = int(text7)
		if targetSlotPos == 2:
			constInfo.ruhtasi2 = int(text7)
		if targetSlotPos == 3:
			constInfo.ruhtasi3 = int(text7)
		if targetSlotPos == 4:
			constInfo.ruhtasi4 = int(text7)
		if targetSlotPos == 5:
			constInfo.ruhtasi5 = int(text7)
		if targetSlotPos == 6:
			constInfo.ruhtasi6 = int(text7)
		if targetSlotPos == 7:
			constInfo.ruhtasi7 = int(text7)
		if targetSlotPos == 8:
			constInfo.ruhtasi8 = int(text7)
		if targetSlotPos == 9:
			constInfo.ruhtasi9 = int(text7)
		if targetSlotPos == 10:
			constInfo.ruhtasi10 = int(text7)
		if targetSlotPos == 11:
			constInfo.ruhtasi11 = int(text7)
		if targetSlotPos == 12:
			constInfo.ruhtasi12 = int(text7)
		if targetSlotPos == 13:
			constInfo.ruhtasi13 = int(text7)
		if targetSlotPos == 14:
			constInfo.ruhtasi14 = int(text7)
		if targetSlotPos == 15:
			constInfo.ruhtasi15 = int(text7)
		if targetSlotPos == 16:
			constInfo.ruhtasi16 = int(text7)
		if targetSlotPos == 17:
			constInfo.ruhtasi17 = int(text7)
		if targetSlotPos == 18:
			constInfo.ruhtasi18 = int(text7)
		if targetSlotPos == 19:
			constInfo.ruhtasi19 = int(text7)
		if targetSlotPos == 20:
			constInfo.ruhtasi20 = int(text7)
		if targetSlotPos == 21:
			constInfo.ruhtasi21 = int(text7)
		if targetSlotPos == 22:
			constInfo.ruhtasi22 = int(text7)
		if targetSlotPos == 23:
			constInfo.ruhtasi23 = int(text7)
		if targetSlotPos == 24:
			constInfo.ruhtasi24 = int(text7)
		if targetSlotPos == 25:
			constInfo.ruhtasi25 = int(text7)
		if targetSlotPos == 26:
			constInfo.ruhtasi26 = int(text7)
		if targetSlotPos == 27:
			constInfo.ruhtasi27 = int(text7)
		if targetSlotPos == 28:
			constInfo.ruhtasi28 = int(text7)
		if targetSlotPos == 29:
			constInfo.ruhtasi29 = int(text7)
		if targetSlotPos == 30:
			constInfo.ruhtasi30 = int(text7)
		if targetSlotPos == 31:
			constInfo.ruhtasi31 = int(text7)
		if targetSlotPos == 32:
			constInfo.ruhtasi32 = int(text7)
		if targetSlotPos == 33:
			constInfo.ruhtasi33 = int(text7)
		if targetSlotPos == 34:
			constInfo.ruhtasi34 = int(text7)
		if targetSlotPos == 35:
			constInfo.ruhtasi35 = int(text7)
		if targetSlotPos == 36:
			constInfo.ruhtasi36 = int(text7)
		if targetSlotPos == 37:
			constInfo.ruhtasi37 = int(text7)
		if targetSlotPos == 38:
			constInfo.ruhtasi38 = int(text7)
		if targetSlotPos == 39:
			constInfo.ruhtasi39 = int(text7)
		if targetSlotPos == 40:
			constInfo.ruhtasi40 = int(text7)
		if targetSlotPos == 41:
			constInfo.ruhtasi41 = int(text7)
		if targetSlotPos == 42:
			constInfo.ruhtasi42 = int(text7)
		if targetSlotPos == 43:
			constInfo.ruhtasi43 = int(text7)
		if targetSlotPos == 44:
			constInfo.ruhtasi44 = int(text7)
		if targetSlotPos == 45:
			constInfo.ruhtasi45 = int(text7)
		if targetSlotPos == 46:
			constInfo.ruhtasi46 = int(text7)
		if targetSlotPos == 47:
			constInfo.ruhtasi47 = int(text7)
		if targetSlotPos == 48:
			constInfo.ruhtasi48 = int(text7)
		if targetSlotPos == 49:
			constInfo.ruhtasi49 = int(text7)
		if targetSlotPos == 50:
			constInfo.ruhtasi50 = int(text7)
		if targetSlotPos == 51:
			constInfo.ruhtasi51 = int(text7)
		if targetSlotPos == 52:
			constInfo.ruhtasi52 = int(text7)
		if targetSlotPos == 53:
			constInfo.ruhtasi53 = int(text7)
		if targetSlotPos == 54:
			constInfo.ruhtasi54 = int(text7)
		if targetSlotPos == 55:
			constInfo.ruhtasi55 = int(text7)
		if targetSlotPos == 56:
			constInfo.ruhtasi56 = int(text7)
		if targetSlotPos == 57:
			constInfo.ruhtasi57 = int(text7)
		if targetSlotPos == 58:
			constInfo.ruhtasi58 = int(text7)
		if targetSlotPos == 59:
			constInfo.ruhtasi59 = int(text7)
		if targetSlotPos == 60:
			constInfo.ruhtasi60 = int(text7)
		if targetSlotPos == 61:
			constInfo.ruhtasi61 = int(text7)
		if targetSlotPos == 62:
			constInfo.ruhtasi62 = int(text7)
		if targetSlotPos == 63:
			constInfo.ruhtasi63 = int(text7)
		if targetSlotPos == 64:
			constInfo.ruhtasi64 = int(text7)
		if targetSlotPos == 65:
			constInfo.ruhtasi65 = int(text7)
		if targetSlotPos == 66:
			constInfo.ruhtasi66 = int(text7)
		if targetSlotPos == 67:
			constInfo.ruhtasi67 = int(text7)
		if targetSlotPos == 68:
			constInfo.ruhtasi68 = int(text7)
		if targetSlotPos == 69:
			constInfo.ruhtasi69 = int(text7)
		if targetSlotPos == 70:
			constInfo.ruhtasi70 = int(text7)
		if targetSlotPos == 71:
			constInfo.ruhtasi71 = int(text7)
		if targetSlotPos == 72:
			constInfo.ruhtasi72 = int(text7)
		if targetSlotPos == 73:
			constInfo.ruhtasi73 = int(text7)
		if targetSlotPos == 74:
			constInfo.ruhtasi74 = int(text7)
		if targetSlotPos == 75:
			constInfo.ruhtasi75 = int(text7)
		if targetSlotPos == 76:
			constInfo.ruhtasi76 = int(text7)
		if targetSlotPos == 77:
			constInfo.ruhtasi77 = int(text7)
		if targetSlotPos == 78:
			constInfo.ruhtasi78 = int(text7)
		if targetSlotPos == 79:
			constInfo.ruhtasi79 = int(text7)
		if targetSlotPos == 80:
			constInfo.ruhtasi80 = int(text7)
		if targetSlotPos == 81:
			constInfo.ruhtasi81 = int(text7)
		if targetSlotPos == 82:
			constInfo.ruhtasi82 = int(text7)
		if targetSlotPos == 83:
			constInfo.ruhtasi83 = int(text7)
		if targetSlotPos == 84:
			constInfo.ruhtasi84 = int(text7)
		if targetSlotPos == 85:
			constInfo.ruhtasi85 = int(text7)
		if targetSlotPos == 86:
			constInfo.ruhtasi86 = int(text7)
		if targetSlotPos == 87:
			constInfo.ruhtasi87 = int(text7)
		if targetSlotPos == 88:
			constInfo.ruhtasi88 = int(text7)
		if targetSlotPos == 89:
			constInfo.ruhtasi89 = int(text7)
		if targetSlotPos == 90:
			constInfo.ruhtasi90 = int(text7)
		if targetSlotPos == 91:
			constInfo.ruhtasi91 = int(text7)
		if targetSlotPos == 92:
			constInfo.ruhtasi92 = int(text7)
		if targetSlotPos == 93:
			constInfo.ruhtasi93 = int(text7)
		if targetSlotPos == 94:
			constInfo.ruhtasi94 = int(text7)
		if targetSlotPos == 95:
			constInfo.ruhtasi95 = int(text7)
		if targetSlotPos == 96:
			constInfo.ruhtasi96 = int(text7)
		if targetSlotPos == 97:
			constInfo.ruhtasi97 = int(text7)
		if targetSlotPos == 98:
			constInfo.ruhtasi98 = int(text7)
		if targetSlotPos == 99:
			constInfo.ruhtasi99 = int(text7)
		if targetSlotPos == 100:
			constInfo.ruhtasi100 = int(text7)

		self.Refresh()		

		#####

		self.priceInputBoard = None
		return TRUE