import ui
import localeInfo
import app
import ime
import uiScriptLocale

class NewMoneyInputDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.moneyHeaderText = localeInfo.MONEY_INPUT_DIALOG_SELLPRICE
		self.__CreateDialog()
		self.SetMaxLength(10)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "newmoneyinputdialog.py")

		getObject = self.GetChild
		self.board = self.GetChild("board")
		self.acceptButton = getObject("AcceptButton")
		self.cancelButton = getObject("CancelButton")
		self.inputValue = getObject("InputValue")
		self.inputValue1 = getObject("InputValue1")
		self.inputValue2 = getObject("InputValue2")
		self.inputValue3 = getObject("InputValue3")
		self.inputValue4 = getObject("InputValue4")
		self.inputValue5 = getObject("InputValue5")
		self.inputValue6 = getObject("InputValue6")
		self.inputValue7 = getObject("InputValue7")
		self.inputValue.SetNumberMode()
		self.inputValue1.SetNumberMode()
		self.inputValue2.SetNumberMode()
		self.inputValue3.SetNumberMode()
		self.inputValue4.SetNumberMode()
		self.inputValue5.SetNumberMode()
		self.inputValue6.SetNumberMode()
		self.inputValue7.SetNumberMode()
		self.inputValue.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
		self.inputValue1.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate1)
		self.inputValue2.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate2)
		self.inputValue3.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate3)
		self.inputValue4.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate4)
		self.inputValue5.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate5)
		self.inputValue6.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate6)
		self.inputValue7.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate7)
		self.moneyText = getObject("MoneyValue")
		self.moneyText1 = getObject("MoneyValue1")
		self.moneyText2 = getObject("MoneyValue2")
		self.moneyText3 = getObject("MoneyValue3")
		self.moneyText4 = getObject("MoneyValue4")
		self.moneyText5 = getObject("MoneyValue5")
		self.moneyText6 = getObject("MoneyValue6")
		self.moneyText7 = getObject("MoneyValue7")

	def Open(self):
		self.inputValue.SetText("")
		self.inputValue.SetFocus()
		self.__OnValueUpdate()
		self.__OnValueUpdate1()
		self.__OnValueUpdate2()
		self.__OnValueUpdate3()
		self.__OnValueUpdate4()
		self.__OnValueUpdate5()
		self.__OnValueUpdate6()
		self.__OnValueUpdate7()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputValue = None
		self.Hide()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		length = min(10, length)
		self.inputValue.SetMax(length)

	def SetMoneyHeaderText(self, text):
		self.moneyHeaderText = text

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def SetValue(self, value):
		value=str(value)
		self.inputValue.SetText(value)
		self.__OnValueUpdate()
		self.__OnValueUpdate1()
		self.__OnValueUpdate2()
		self.__OnValueUpdate3()
		self.__OnValueUpdate4()
		self.__OnValueUpdate5()
		self.__OnValueUpdate6()
		self.__OnValueUpdate7()
		ime.SetCursorPosition(len(value))		

	def GetText(self):
		return self.inputValue.GetText()
	
	def GetText1(self):
		return self.inputValue1.GetText()
		
	def GetText2(self):
		return self.inputValue2.GetText()
		
	def GetText3(self):
		return self.inputValue3.GetText()
		
	def GetText4(self):
		return self.inputValue4.GetText()
		
	def GetText5(self):
		return self.inputValue5.GetText()
		
	def GetText6(self):
		return self.inputValue6.GetText()
		
	def GetText7(self):
		return self.inputValue7.GetText()
	def __OnValueUpdate(self):
		ui.EditLine.OnIMEUpdate(self.inputValue)

		text = self.inputValue.GetText()

		money = 0
		if text and text.isdigit():
			try:
				money = int(text)
			except ValueError:
				money = 299999999

		self.moneyText.SetText(self.moneyHeaderText + localeInfo.NumberToMoneyString(money))
		
	def __OnValueUpdate1(self):
		ui.EditLine.OnIMEUpdate(self.inputValue1)

		text = self.inputValue1.GetText()

		money = 0
		if text and text.isdigit():
			try:
				money = int(text)
			except ValueError:
				money = 299999999

		self.moneyText1.SetText("Satýþ Fiyatý:"+str(money)+" Su Taþý")
		
	def __OnValueUpdate2(self):
		ui.EditLine.OnIMEUpdate(self.inputValue2)

		text = self.inputValue2.GetText()

		money = 0
		if text and text.isdigit():
			try:
				money = int(text)
			except ValueError:
				money = 299999999

		self.moneyText2.SetText("Satýþ Fiyatý:"+str(money)+" Bar (400.Milyon.Yang)")
	def __OnValueUpdate3(self):
		ui.EditLine.OnIMEUpdate(self.inputValue3)

		text = self.inputValue3.GetText()

		money = 0
		if text and text.isdigit():
			try:
				money = int(text)
			except ValueError:
				money = 299999999

		self.moneyText3.SetText("Satýþ Fiyatý:"+str(money)+" Yesil ot")
	def __OnValueUpdate4(self):
		ui.EditLine.OnIMEUpdate(self.inputValue4)

		text = self.inputValue4.GetText()

		money = 0
		if text and text.isdigit():
			try:
				money = int(text)
			except ValueError:
				money = 299999999

		self.moneyText4.SetText("Satýþ Fiyatý:"+str(money)+" Kirmizi ot")
	def __OnValueUpdate5(self):
		ui.EditLine.OnIMEUpdate(self.inputValue5)

		text = self.inputValue5.GetText()

		money = 0
		if text and text.isdigit():
			try:
				money = int(text)
			except ValueError:
				money = 299999999

		self.moneyText5.SetText("Satýþ Fiyatý:"+str(money)+" Mavi ot")
	def __OnValueUpdate6(self):
		ui.EditLine.OnIMEUpdate(self.inputValue6)

		text = self.inputValue6.GetText()

		money = 0
		if text and text.isdigit():
			try:
				money = int(text)
			except ValueError:
				money = 299999999

		self.moneyText6.SetText("Satýþ Fiyatý:"+str(money)+" Mor ot")
	def __OnValueUpdate7(self):
		ui.EditLine.OnIMEUpdate(self.inputValue7)

		text = self.inputValue7.GetText()

		money = 0
		if text and text.isdigit():
			try:
				money = int(text)
			except ValueError:
				money = 299999999

		self.moneyText7.SetText("Satýþ Fiyatý:"+str(money)+" Ruh tasi")

