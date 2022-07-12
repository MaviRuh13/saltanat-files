# Ekle
if app.MAVIRUH_MULTI_PRICE:
	import uiMaydanoz
	import constInfo

# Arat
			priceInputBoard = uiCommon.MoneyInputDialog()

# Degistir
			if app.MAVIRUH_MULTI_PRICE:
				priceInputBoard = uiMaydanoz.NewMoneyInputDialog()
			else:
				priceInputBoard = uiCommon.MoneyInputDialog()

# Arat
def AcceptInputPrice(self):

# Komple Degistir
	if app.MAVIRUH_MULTI_PRICE:
		def AcceptInputPrice(self):

			if not self.priceInputBoard:
				return TRUE

			text = self.priceInputBoard.GetText()
			text1 = self.priceInputBoard.GetText1()
			text2 = self.priceInputBoard.GetText2()

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

			self.Refresh()		

			#####

			self.priceInputBoard = None
			return TRUE
	else:
		def AcceptInputPrice(self):

			if not self.priceInputBoard:
				return True

			text = self.priceInputBoard.GetText()

			if not text:
				return True

			if not text.isdigit():
				return True

			if int(text) <= 0:
				return True

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

			shop.AddPrivateShopItemStock(attachedInvenType, sourceSlotPos, targetSlotPos, price)
			self.itemStock[targetSlotPos] = (attachedInvenType, sourceSlotPos)
			snd.PlaySound("sound/ui/drop.wav")

			self.Refresh()		

			#####

			self.priceInputBoard = None
			return True
