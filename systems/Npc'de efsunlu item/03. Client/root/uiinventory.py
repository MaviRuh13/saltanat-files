# Arat :
# self.costumeButton = self.GetChild2("CostumeButton")
# Alt�na Ekle :

			if app.ENABLE_CASH_INVENTORY_WINDOW:
				self.wndDragonCoin = self.GetChild("DragonCoin")
				self.wndDragonCoinSlot = self.GetChild("DragonCoin_Slot")
				
# Arat :
# self.wndMoneySlot = 0
# Alt�na Ekle :

		if app.ENABLE_CASH_INVENTORY_WINDOW:
			self.wndDragonCoin = 0
			self.wndDragonCoinSlot = 0
			
# Arat :
# self.wndMoney.SetText(localeInfo.NumberToMoneyString(money))
# Alt�na Ekle :

		if app.ENABLE_CASH_INVENTORY_WINDOW:
			dragoncoin = player.GetDragonCoin()
			self.wndDragonCoin.SetText(localeInfo.NumberToDragonCoinString(dragoncoin))