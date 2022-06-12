# Arat :
# PythonScriptLoader.LoadScriptFile(self, "UIScript/shopdialog.py")
# Deðiþtir :

			if app.ENABLE_2TH_SHOPEX_SYSTEM:
				PythonScriptLoader.LoadScriptFile(self, "UIScript/shopexdialog.py")
			else:
				PythonScriptLoader.LoadScriptFile(self, "UIScript/shopdialog.py")
				
# Arat :
"""
			middleTab1 = GetObject("MiddleTab1")
			middleTab2 = GetObject("MiddleTab2")
			smallTab1 = GetObject("SmallTab1")
			smallTab2 = GetObject("SmallTab2")
			smallTab3 = GetObject("SmallTab3")
"""
# Deðiþtir :

			if not app.ENABLE_2TH_SHOPEX_SYSTEM:
				middleTab1 = GetObject("MiddleTab1")
				middleTab2 = GetObject("MiddleTab2")
				smallTab1 = GetObject("SmallTab1")
				smallTab2 = GetObject("SmallTab2")
				smallTab3 = GetObject("SmallTab3")
				
# Arat :
"""
			self.titleBar = GetObject("TitleBar")
"""
# Altýna Ekle :
			self.titleName = GetObject("TitleName")
# Arat :
"""
		self.smallRadioButtonGroup = ui.RadioButtonGroup.Create([[smallTab1, lambda : self.OnClickTabButton(0), None], [smallTab2, lambda : self.OnClickTabButton(1), None], [smallTab3, lambda : self.OnClickTabButton(2), None]])
		self.middleRadioButtonGroup = ui.RadioButtonGroup.Create([[middleTab1, lambda : self.OnClickTabButton(0), None], [middleTab2, lambda : self.OnClickTabButton(1), None]])

		self.__HideMiddleTabs()
		self.__HideSmallTabs()
"""
# Deðiþtir :

		if not app.ENABLE_2TH_SHOPEX_SYSTEM:
			self.smallRadioButtonGroup = ui.RadioButtonGroup.Create([[smallTab1, lambda : self.OnClickTabButton(0), None], [smallTab2, lambda : self.OnClickTabButton(1), None], [smallTab3, lambda : self.OnClickTabButton(2), None]])
			self.middleRadioButtonGroup = ui.RadioButtonGroup.Create([[middleTab1, lambda : self.OnClickTabButton(0), None], [middleTab2, lambda : self.OnClickTabButton(1), None]])

			self.__HideMiddleTabs()
			self.__HideSmallTabs()
			
# Arat :
"""
	def __ShowMiddleTabs(self):
		self.middleRadioButtonGroup.Show()
	
	def __ShowSmallTabs(self):
		self.smallRadioButtonGroup.Show()
"""
# Deðiþtir :

	if not app.ENABLE_2TH_SHOPEX_SYSTEM:
		def __ShowMiddleTabs(self):
			self.middleRadioButtonGroup.Show()
	
		def __ShowSmallTabs(self):
			self.smallRadioButtonGroup.Show()
			
# Arat :
"""
	def __HideMiddleTabs(self):
		self.middleRadioButtonGroup.Hide()
	
	def __HideSmallTabs(self):
		self.smallRadioButtonGroup.Hide()
		
	def __SetTabNames(self):
		if shop.GetTabCount() == 2:
			self.middleRadioButtonGroup.SetText(0, shop.GetTabName(0))
			self.middleRadioButtonGroup.SetText(1, shop.GetTabName(1))
		elif shop.GetTabCount() == 3:
			self.smallRadioButtonGroup.SetText(0, shop.GetTabName(0))
			self.smallRadioButtonGroup.SetText(1, shop.GetTabName(1))
			self.smallRadioButtonGroup.SetText(2, shop.GetTabName(2))
"""
# Deðiþtir :

	if not app.ENABLE_2TH_SHOPEX_SYSTEM:
		def __HideMiddleTabs(self):
			self.middleRadioButtonGroup.Hide()
	
		def __HideSmallTabs(self):
			self.smallRadioButtonGroup.Hide()
		
		def __SetTabNames(self):
			if shop.GetTabCount() == 2:
				self.middleRadioButtonGroup.SetText(0, shop.GetTabName(0))
				self.middleRadioButtonGroup.SetText(1, shop.GetTabName(1))
			elif shop.GetTabCount() == 3:
				self.smallRadioButtonGroup.SetText(0, shop.GetTabName(0))
				self.smallRadioButtonGroup.SetText(1, shop.GetTabName(1))
				self.smallRadioButtonGroup.SetText(2, shop.GetTabName(2))
				
# Arat :
# def Open(self, vid):
# Deðiþtir :

	def Open(self, vid):

		isPrivateShop = False
		isMainPlayerPrivateShop = False

		import chr
		if chr.IsNPC(vid):
			isPrivateShop = False
		else:
			isPrivateShop = True

		if player.IsMainCharacterIndex(vid):

			isMainPlayerPrivateShop = True

			self.btnBuy.Hide()
			self.btnSell.Hide()
			self.btnClose.Show()

		else:

			isMainPlayerPrivateShop = False

			self.btnBuy.Show()
			self.btnSell.Show()
			self.btnClose.Hide()

		shop.Open(isPrivateShop, isMainPlayerPrivateShop)

		self.tabIdx = 0

		if isPrivateShop:
			if not app.ENABLE_2TH_SHOPEX_SYSTEM:
				self.__HideMiddleTabs()
				self.__HideSmallTabs()
		else:
			if not app.ENABLE_2TH_SHOPEX_SYSTEM:
				if shop.GetTabCount() == 1:
					self.__ShowBuySellButton()
					self.__HideMiddleTabs()
					self.__HideSmallTabs()
				elif shop.GetTabCount() == 2:
					self.__HideBuySellButton()
					self.__ShowMiddleTabs()
					self.__HideSmallTabs()
					self.__SetTabNames()
					self.middleRadioButtonGroup.OnClick(0)
				elif shop.GetTabCount() == 3:
					self.__HideBuySellButton()
					self.__HideMiddleTabs()
					self.__ShowSmallTabs()
					self.__SetTabNames()
					self.middleRadioButtonGroup.OnClick(1)
			else:
				self.__ShowBuySellButton()
					
		if not isPrivateShop:
			if app.ENABLE_2TH_SHOPEX_SYSTEM:
				try:
					self.titleName.SetText(localeInfo.SHOP_NAME_DICT[shop.GetName()])
				except KeyError:
					self.titleName.SetText(localeInfo.SHOP_NAME_DICT["SHOPNAME_DEFAULT"])

		self.Refresh()
		self.SetTop()
			
		self.Show()

		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()
		
# Arat :
# itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
# Deðiþtir :

		if app.ENABLE_2TH_SHOPEX_SYSTEM:
			if shop.GetType() == shop.SHOP_TYPE_GOLD:
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
			elif shop.GetType() == shop.SHOP_TYPE_CASH:
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToDragonCoinString(itemPrice)))
			elif shop.GetType() == shop.SHOP_TYPE_COINS:
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToDragonMarkString(itemPrice)))
			elif shop.GetType() == shop.SHOP_TYPE_ALIGN:
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToAlignmentString(itemPrice)))
			else:
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
		else:
			itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
			
# Arat :
""" 
				if 0 != self.tooltipItem:
					if shop.SHOP_COIN_TYPE_GOLD == shop.GetTabCoinType(self.tabIdx):
						self.tooltipItem.SetShopItem(slotIndex)
					else: 
						self.tooltipItem.SetShopItemBySecondaryCoin(slotIndex)
"""
# Deðiþtir :

			if app.ENABLE_2TH_SHOPEX_SYSTEM:
				if 0 != self.tooltipItem:
					self.tooltipItem.SetShopExItem(slotIndex, shop.GetType())
			else:
				if 0 != self.tooltipItem:
					if shop.SHOP_COIN_TYPE_GOLD == shop.GetTabCoinType(self.tabIdx):
						self.tooltipItem.SetShopItem(slotIndex)
					else: 
						self.tooltipItem.SetShopItemBySecondaryCoin(slotIndex)