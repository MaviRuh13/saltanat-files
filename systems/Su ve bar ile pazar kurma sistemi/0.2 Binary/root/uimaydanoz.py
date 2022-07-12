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
		self.inputValue.SetNumberMode()
		self.inputValue1.SetNumberMode()
		self.inputValue2.SetNumberMode()
		self.inputValue.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
		self.inputValue1.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate1)
		self.inputValue2.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate2)
		self.moneyText = getObject("MoneyValue")
		self.moneyText1 = getObject("MoneyValue1")
		self.moneyText2 = getObject("MoneyValue2")

	def Open(self):
		self.inputValue.SetText("")
		self.inputValue.SetFocus()
		self.__OnValueUpdate()
		self.__OnValueUpdate1()
		self.__OnValueUpdate2()
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
		ime.SetCursorPosition(len(value))		


	def GetText(self):
		return self.inputValue.GetText()
	
	def GetText1(self):
		return self.inputValue1.GetText()
		
	def GetText2(self):
		return self.inputValue2.GetText()

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

