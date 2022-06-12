# Arat :
# def SetShopItem(self, slotIndex):
# Altýna Ekle :

	if app.ENABLE_2TH_SHOPEX_SYSTEM:
		def SetShopExItem(self, slotIndex, shopType):
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
			if shopType == shop.SHOP_TYPE_GOLD:
				self.AppendPrice(0, price, 0, 0, 0)
			elif shopType == shop.SHOP_TYPE_CASH:
				self.AppendPriceByDragonCoin(price)
			elif shopType == shop.SHOP_TYPE_COINS:
				self.AppendPriceByDragonMark(price)
			elif shopType == shop.SHOP_TYPE_ALIGN:
				self.AppendPriceByAlignment(price)
			else:
				self.AppendPrice(price)
				
# Arat :
# def AppendPrice(self, price):
# Altýna Ekle :

	if app.ENABLE_2TH_SHOPEX_SYSTEM:
		def AppendPriceByDragonCoin(self, price):
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToDragonCoinString(price)), self.GetPriceColor(price))		
			
		def AppendPriceByDragonMark(self, price):
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToDragonMarkString(price)), self.GetPriceColor(price))
		
		def AppendPriceByAlignment(self, price):
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToAlignmentString(price)), self.GetPriceColor(price))