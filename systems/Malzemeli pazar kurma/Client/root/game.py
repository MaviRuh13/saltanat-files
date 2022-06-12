"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                                                         AÇILIR: game.py                                                                     """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# ARATILIR: 

def BINARY_ServerCommand_Run(self, line):

# ÜSTÜNE EKLENIR:

#if app.ENABLE_KAYA_MULTI_PRICE:
	def sutasiyok(self):
		self.PopupMessage("Yeterli Su Yok")
		
	def wonyok(self):
		self.PopupMessage("Yeterli Bar Yok")

	def maviyok(self):
		self.PopupMessage("Yeterli Mavi ot Yok")

	def yesilyok(self):
		self.PopupMessage("Yeterli Yesil ot Yok")

	def kirmiziyok(self):
		self.PopupMessage("Yeterli Kirmizi ot Yok")

	def moryok(self):
		self.PopupMessage("Yeterli Mor ot Yok")

	def ruhtasiyok(self):
		self.PopupMessage("Yeterli Ruh tasi Yok")

	def sufiyatkac(self,slots,fiyats):
		import constInfo
		slot = int(slots)
		fiyat = int(fiyats)
		if slot == 0:
			constInfo.sufiyat0 = fiyat
		if slot == 1:
			constInfo.sufiyat1 = fiyat
		if slot == 2:
			constInfo.sufiyat2 = fiyat
		if slot == 3:
			constInfo.sufiyat3 = fiyat
		if slot == 4:
			constInfo.sufiyat4 = fiyat
		if slot == 5:
			constInfo.sufiyat5 = fiyat
		if slot == 6:
			constInfo.sufiyat6 = fiyat
		if slot == 7:
			constInfo.sufiyat7 = fiyat
		if slot == 8:
			constInfo.sufiyat8 = fiyat
		if slot == 9:
			constInfo.sufiyat9 = fiyat
		if slot == 10:
			constInfo.sufiyat10 = fiyat
		if slot == 11:
			constInfo.sufiyat11 = fiyat
		if slot == 12:
			constInfo.sufiyat12 = fiyat
		if slot == 13:
			constInfo.sufiyat13 = fiyat
		if slot == 14:
			constInfo.sufiyat14 = fiyat
		if slot == 15:
			constInfo.sufiyat15 = fiyat
		if slot == 16:
			constInfo.sufiyat16 = fiyat
		if slot == 17:
			constInfo.sufiyat17 = fiyat
		if slot == 18:
			constInfo.sufiyat18 = fiyat
		if slot == 19:
			constInfo.sufiyat19 = fiyat
		if slot == 20:
			constInfo.sufiyat20 = fiyat
		if slot == 21:
			constInfo.sufiyat21 = fiyat
		if slot == 22:
			constInfo.sufiyat22 = fiyat
		if slot == 23:
			constInfo.sufiyat23 = fiyat
		if slot == 24:
			constInfo.sufiyat24 = fiyat
		if slot == 25:
			constInfo.sufiyat25 = fiyat
		if slot == 26:
			constInfo.sufiyat26 = fiyat
		if slot == 27:
			constInfo.sufiyat27 = fiyat
		if slot == 28:
			constInfo.sufiyat28 = fiyat
		if slot == 29:
			constInfo.sufiyat29 = fiyat
		if slot == 30:
			constInfo.sufiyat30 = fiyat
		if slot == 31:
			constInfo.sufiyat31 = fiyat
		if slot == 32:
			constInfo.sufiyat32 = fiyat
		if slot == 33:
			constInfo.sufiyat33 = fiyat
		if slot == 34:
			constInfo.sufiyat34 = fiyat
		if slot == 35:
			constInfo.sufiyat35 = fiyat
		if slot == 36:
			constInfo.sufiyat36 = fiyat
		if slot == 37:
			constInfo.sufiyat37 = fiyat
		if slot == 38:
			constInfo.sufiyat38 = fiyat
		if slot == 39:
			constInfo.sufiyat39 = fiyat
		if slot == 40:
			constInfo.sufiyat40 = fiyat
		if slot == 41:
			constInfo.sufiyat41 = fiyat
		if slot == 42:
			constInfo.sufiyat42 = fiyat
		if slot == 43:
			constInfo.sufiyat43 = fiyat
		if slot == 44:
			constInfo.sufiyat44 = fiyat
		if slot == 45:
			constInfo.sufiyat45 = fiyat
		if slot == 46:
			constInfo.sufiyat46 = fiyat
		if slot == 47:
			constInfo.sufiyat47 = fiyat
		if slot == 48:
			constInfo.sufiyat48 = fiyat
		if slot == 49:
			constInfo.sufiyat49 = fiyat
		if slot == 50:
			constInfo.sufiyat50 = fiyat
		if slot == 51:
			constInfo.sufiyat51 = fiyat
		if slot == 52:
			constInfo.sufiyat52 = fiyat
		if slot == 53:
			constInfo.sufiyat53 = fiyat
		if slot == 54:
			constInfo.sufiyat54 = fiyat
		if slot == 55:
			constInfo.sufiyat55 = fiyat
		if slot == 56:
			constInfo.sufiyat56 = fiyat
		if slot == 57:
			constInfo.sufiyat57 = fiyat
		if slot == 58:
			constInfo.sufiyat58 = fiyat
		if slot == 59:
			constInfo.sufiyat59 = fiyat
		if slot == 60:
			constInfo.sufiyat60 = fiyat
		if slot == 61:
			constInfo.sufiyat61 = fiyat
		if slot == 62:
			constInfo.sufiyat62 = fiyat
		if slot == 63:
			constInfo.sufiyat63 = fiyat
		if slot == 64:
			constInfo.sufiyat64 = fiyat
		if slot == 65:
			constInfo.sufiyat65 = fiyat
		if slot == 66:
			constInfo.sufiyat66 = fiyat
		if slot == 67:
			constInfo.sufiyat67 = fiyat
		if slot == 68:
			constInfo.sufiyat68 = fiyat
		if slot == 69:
			constInfo.sufiyat69 = fiyat
		if slot == 70:
			constInfo.sufiyat70 = fiyat
		if slot == 71:
			constInfo.sufiyat71 = fiyat
		if slot == 72:
			constInfo.sufiyat72 = fiyat
		if slot == 73:
			constInfo.sufiyat73 = fiyat
		if slot == 74:
			constInfo.sufiyat74 = fiyat
		if slot == 75:
			constInfo.sufiyat75 = fiyat
		if slot == 76:
			constInfo.sufiyat76 = fiyat
		if slot == 77:
			constInfo.sufiyat77 = fiyat
		if slot == 78:
			constInfo.sufiyat78 = fiyat
		if slot == 79:
			constInfo.sufiyat79 = fiyat
		if slot == 80:
			constInfo.sufiyat80 = fiyat
		if slot == 81:
			constInfo.sufiyat81 = fiyat
		if slot == 82:
			constInfo.sufiyat82 = fiyat
		if slot == 83:
			constInfo.sufiyat83 = fiyat
		if slot == 84:
			constInfo.sufiyat84 = fiyat
		if slot == 85:
			constInfo.sufiyat85 = fiyat
		if slot == 86:
			constInfo.sufiyat86 = fiyat
		if slot == 87:
			constInfo.sufiyat87 = fiyat
		if slot == 88:
			constInfo.sufiyat88 = fiyat
		if slot == 89:
			constInfo.sufiyat89 = fiyat
		if slot == 90:
			constInfo.sufiyat90 = fiyat
		if slot == 91:
			constInfo.sufiyat91 = fiyat
		if slot == 92:
			constInfo.sufiyat92 = fiyat
		if slot == 93:
			constInfo.sufiyat93 = fiyat
		if slot == 94:
			constInfo.sufiyat94 = fiyat
		if slot == 95:
			constInfo.sufiyat95 = fiyat
		if slot == 96:
			constInfo.sufiyat96 = fiyat
		if slot == 97:
			constInfo.sufiyat97 = fiyat
		if slot == 98:
			constInfo.sufiyat98 = fiyat
		if slot == 99:
			constInfo.sufiyat99 = fiyat
		if slot == 100:
			constInfo.sufiyat100 = fiyat
			
	def barfiyatkac(self,slots,fiyats):
		import constInfo
		slot2 = int(slots)
		fiyat2 = int(fiyats)
		if slot2 == 0:
			constInfo.barfiyat0 = fiyat2
		if slot2 == 1:
			constInfo.barfiyat1 = fiyat2
		if slot2 == 2:
			constInfo.barfiyat2 = fiyat2
		if slot2 == 3:
			constInfo.barfiyat3 = fiyat2
		if slot2 == 4:
			constInfo.barfiyat4 = fiyat2
		if slot2 == 5:
			constInfo.barfiyat5 = fiyat2
		if slot2 == 6:
			constInfo.barfiyat6 = fiyat2
		if slot2 == 7:
			constInfo.barfiyat7 = fiyat2
		if slot2 == 8:
			constInfo.barfiyat8 = fiyat2
		if slot2 == 9:
			constInfo.barfiyat9 = fiyat2
		if slot2 == 10:
			constInfo.barfiyat10 = fiyat2
		if slot2 == 11:
			constInfo.barfiyat11 = fiyat2
		if slot2 == 12:
			constInfo.barfiyat12 = fiyat2
		if slot2 == 13:
			constInfo.barfiyat13 = fiyat2
		if slot2 == 14:
			constInfo.barfiyat14 = fiyat2
		if slot2 == 15:
			constInfo.barfiyat15 = fiyat2
		if slot2 == 16:
			constInfo.barfiyat16 = fiyat2
		if slot2 == 17:
			constInfo.barfiyat17 = fiyat2
		if slot2 == 18:
			constInfo.barfiyat18 = fiyat2
		if slot2 == 19:
			constInfo.barfiyat19 = fiyat2
		if slot2 == 20:
			constInfo.barfiyat20 = fiyat2
		if slot2 == 21:
			constInfo.barfiyat21 = fiyat2
		if slot2 == 22:
			constInfo.barfiyat22 = fiyat2
		if slot2 == 23:
			constInfo.barfiyat23 = fiyat2
		if slot2 == 24:
			constInfo.barfiyat24 = fiyat2
		if slot2 == 25:
			constInfo.barfiyat25 = fiyat2
		if slot2 == 26:
			constInfo.barfiyat26 = fiyat2
		if slot2 == 27:
			constInfo.barfiyat27 = fiyat2
		if slot2 == 28:
			constInfo.barfiyat28 = fiyat2
		if slot2 == 29:
			constInfo.barfiyat29 = fiyat2
		if slot2 == 30:
			constInfo.barfiyat30 = fiyat2
		if slot2 == 31:
			constInfo.barfiyat31 = fiyat2
		if slot2 == 32:
			constInfo.barfiyat32 = fiyat2
		if slot2 == 33:
			constInfo.barfiyat33 = fiyat2
		if slot2 == 34:
			constInfo.barfiyat34 = fiyat2
		if slot2 == 35:
			constInfo.barfiyat35 = fiyat2
		if slot2 == 36:
			constInfo.barfiyat36 = fiyat2
		if slot2 == 37:
			constInfo.barfiyat37 = fiyat2
		if slot2 == 38:
			constInfo.barfiyat38 = fiyat2
		if slot2 == 39:
			constInfo.barfiyat39 = fiyat2
		if slot2 == 40:
			constInfo.barfiyat40 = fiyat2
		if slot2 == 41:
			constInfo.barfiyat41 = fiyat2
		if slot2 == 42:
			constInfo.barfiyat42 = fiyat2
		if slot2 == 43:
			constInfo.barfiyat43 = fiyat2
		if slot2 == 44:
			constInfo.barfiyat44 = fiyat2
		if slot2 == 45:
			constInfo.barfiyat45 = fiyat2
		if slot2 == 46:
			constInfo.barfiyat46 = fiyat2
		if slot2 == 47:
			constInfo.barfiyat47 = fiyat2
		if slot2 == 48:
			constInfo.barfiyat48 = fiyat2
		if slot2 == 49:
			constInfo.barfiyat49 = fiyat2
		if slot2 == 50:
			constInfo.barfiyat50 = fiyat2
		if slot2 == 51:
			constInfo.barfiyat51 = fiyat2
		if slot2 == 52:
			constInfo.barfiyat52 = fiyat2
		if slot2 == 53:
			constInfo.barfiyat53 = fiyat2
		if slot2 == 54:
			constInfo.barfiyat54 = fiyat2
		if slot2 == 55:
			constInfo.barfiyat55 = fiyat2
		if slot2 == 56:
			constInfo.barfiyat56 = fiyat2
		if slot2 == 57:
			constInfo.barfiyat57 = fiyat2
		if slot2 == 58:
			constInfo.barfiyat58 = fiyat2
		if slot2 == 59:
			constInfo.barfiyat59 = fiyat2
		if slot2 == 60:
			constInfo.barfiyat60 = fiyat2
		if slot2 == 61:
			constInfo.barfiyat61 = fiyat2
		if slot2 == 62:
			constInfo.barfiyat62 = fiyat2
		if slot2 == 63:
			constInfo.barfiyat63 = fiyat2
		if slot2 == 64:
			constInfo.barfiyat64 = fiyat2
		if slot2 == 65:
			constInfo.barfiyat65 = fiyat2
		if slot2 == 66:
			constInfo.barfiyat66 = fiyat2
		if slot2 == 67:
			constInfo.barfiyat67 = fiyat2
		if slot2 == 68:
			constInfo.barfiyat68 = fiyat2
		if slot2 == 69:
			constInfo.barfiyat69 = fiyat2
		if slot2 == 70:
			constInfo.barfiyat70 = fiyat2
		if slot2 == 71:
			constInfo.barfiyat71 = fiyat2
		if slot2 == 72:
			constInfo.barfiyat72 = fiyat2
		if slot2 == 73:
			constInfo.barfiyat73 = fiyat2
		if slot2 == 74:
			constInfo.barfiyat74 = fiyat2
		if slot2 == 75:
			constInfo.barfiyat75 = fiyat2
		if slot2 == 76:
			constInfo.barfiyat76 = fiyat2
		if slot2 == 77:
			constInfo.barfiyat77 = fiyat2
		if slot2 == 78:
			constInfo.barfiyat78 = fiyat2
		if slot2 == 79:
			constInfo.barfiyat79 = fiyat2
		if slot2 == 80:
			constInfo.barfiyat80 = fiyat2
		if slot2 == 81:
			constInfo.barfiyat81 = fiyat2
		if slot2 == 82:
			constInfo.barfiyat82 = fiyat2
		if slot2 == 83:
			constInfo.barfiyat83 = fiyat2
		if slot2 == 84:
			constInfo.barfiyat84 = fiyat2
		if slot2 == 85:
			constInfo.barfiyat85 = fiyat2
		if slot2 == 86:
			constInfo.barfiyat86 = fiyat2
		if slot2 == 87:
			constInfo.barfiyat87 = fiyat2
		if slot2 == 88:
			constInfo.barfiyat88 = fiyat2
		if slot2 == 89:
			constInfo.barfiyat89 = fiyat2
		if slot2 == 90:
			constInfo.barfiyat90 = fiyat2
		if slot2 == 91:
			constInfo.barfiyat91 = fiyat2
		if slot2 == 92:
			constInfo.barfiyat92 = fiyat2
		if slot2 == 93:
			constInfo.barfiyat93 = fiyat2
		if slot2 == 94:
			constInfo.barfiyat94 = fiyat2
		if slot2 == 95:
			constInfo.barfiyat95 = fiyat2
		if slot2 == 96:
			constInfo.barfiyat96 = fiyat2
		if slot2 == 97:
			constInfo.barfiyat97 = fiyat2
		if slot2 == 98:
			constInfo.barfiyat98 = fiyat2
		if slot2 == 99:
			constInfo.barfiyat99 = fiyat2
		if slot2 == 100:
			constInfo.barfiyat100 = fiyat2

	def yesilfytkac(self,slots,fiyats):
		import constInfo
		slot3 = int(slots)
		fiyat3 = int(fiyats)
		if slot3 == 0:
			constInfo.yesilot0 = fiyat3
		if slot3 == 1:
			constInfo.yesilot1 = fiyat3
		if slot3 == 2:
			constInfo.yesilot2 = fiyat3
		if slot3 == 3:
			constInfo.yesilot3 = fiyat3
		if slot3 == 4:
			constInfo.yesilot4 = fiyat3
		if slot3 == 5:
			constInfo.yesilot5 = fiyat3
		if slot3 == 6:
			constInfo.yesilot6 = fiyat3
		if slot3 == 7:
			constInfo.yesilot7 = fiyat3
		if slot3 == 8:
			constInfo.yesilot8 = fiyat3
		if slot3 == 9:
			constInfo.yesilot9 = fiyat3
		if slot3 == 10:
			constInfo.yesilot10 = fiyat3
		if slot3 == 11:
			constInfo.yesilot11 = fiyat3
		if slot3 == 12:
			constInfo.yesilot12 = fiyat3
		if slot3 == 13:
			constInfo.yesilot13 = fiyat3
		if slot3 == 14:
			constInfo.yesilot14 = fiyat3
		if slot3 == 15:
			constInfo.yesilot15 = fiyat3
		if slot3 == 16:
			constInfo.yesilot16 = fiyat3
		if slot3 == 17:
			constInfo.yesilot17 = fiyat3
		if slot3 == 18:
			constInfo.yesilot18 = fiyat3
		if slot3 == 19:
			constInfo.yesilot19 = fiyat3
		if slot3 == 20:
			constInfo.yesilot20 = fiyat3
		if slot3 == 21:
			constInfo.yesilot21 = fiyat3
		if slot3 == 22:
			constInfo.yesilot22 = fiyat3
		if slot3 == 23:
			constInfo.yesilot23 = fiyat3
		if slot3 == 24:
			constInfo.yesilot24 = fiyat3
		if slot3 == 25:
			constInfo.yesilot25 = fiyat3
		if slot3 == 26:
			constInfo.yesilot26 = fiyat3
		if slot3 == 27:
			constInfo.yesilot27 = fiyat3
		if slot3 == 28:
			constInfo.yesilot28 = fiyat3
		if slot3 == 29:
			constInfo.yesilot29 = fiyat3
		if slot3 == 30:
			constInfo.yesilot30 = fiyat3
		if slot3 == 31:
			constInfo.yesilot31 = fiyat3
		if slot3 == 32:
			constInfo.yesilot32 = fiyat3
		if slot3 == 33:
			constInfo.yesilot33 = fiyat3
		if slot3 == 34:
			constInfo.yesilot34 = fiyat3
		if slot3 == 35:
			constInfo.yesilot35 = fiyat3
		if slot3 == 36:
			constInfo.yesilot36 = fiyat3
		if slot3 == 37:
			constInfo.yesilot37 = fiyat3
		if slot3 == 38:
			constInfo.yesilot38 = fiyat3
		if slot3 == 39:
			constInfo.yesilot39 = fiyat3
		if slot3 == 40:
			constInfo.yesilot40 = fiyat3
		if slot3 == 41:
			constInfo.yesilot41 = fiyat3
		if slot3 == 42:
			constInfo.yesilot42 = fiyat3
		if slot3 == 43:
			constInfo.yesilot43 = fiyat3
		if slot3 == 44:
			constInfo.yesilot44 = fiyat3
		if slot3 == 45:
			constInfo.yesilot45 = fiyat3
		if slot3 == 46:
			constInfo.yesilot46 = fiyat3
		if slot3 == 47:
			constInfo.yesilot47 = fiyat3
		if slot3 == 48:
			constInfo.yesilot48 = fiyat3
		if slot3 == 49:
			constInfo.yesilot49 = fiyat3
		if slot3 == 50:
			constInfo.yesilot50 = fiyat3
		if slot3 == 51:
			constInfo.yesilot51 = fiyat3
		if slot3 == 52:
			constInfo.yesilot52 = fiyat3
		if slot3 == 53:
			constInfo.yesilot53 = fiyat3
		if slot3 == 54:
			constInfo.yesilot54 = fiyat3
		if slot3 == 55:
			constInfo.yesilot55 = fiyat3
		if slot3 == 56:
			constInfo.yesilot56 = fiyat3
		if slot3 == 57:
			constInfo.yesilot57 = fiyat3
		if slot3 == 58:
			constInfo.yesilot58 = fiyat3
		if slot3 == 59:
			constInfo.yesilot59 = fiyat3
		if slot3 == 60:
			constInfo.yesilot60 = fiyat3
		if slot3 == 61:
			constInfo.yesilot61 = fiyat3
		if slot3 == 62:
			constInfo.yesilot62 = fiyat3
		if slot3 == 63:
			constInfo.yesilot63 = fiyat3
		if slot3 == 64:
			constInfo.yesilot64 = fiyat3
		if slot3 == 65:
			constInfo.yesilot65 = fiyat3
		if slot3 == 66:
			constInfo.yesilot66 = fiyat3
		if slot3 == 67:
			constInfo.yesilot67 = fiyat3
		if slot3 == 68:
			constInfo.yesilot68 = fiyat3
		if slot3 == 69:
			constInfo.yesilot69 = fiyat3
		if slot3 == 70:
			constInfo.yesilot70 = fiyat3
		if slot3 == 71:
			constInfo.yesilot71 = fiyat3
		if slot3 == 72:
			constInfo.yesilot72 = fiyat3
		if slot3 == 73:
			constInfo.yesilot73 = fiyat3
		if slot3 == 74:
			constInfo.yesilot74 = fiyat3
		if slot3 == 75:
			constInfo.yesilot75 = fiyat3
		if slot3 == 76:
			constInfo.yesilot76 = fiyat3
		if slot3 == 77:
			constInfo.yesilot77 = fiyat3
		if slot3 == 78:
			constInfo.yesilot78 = fiyat3
		if slot3 == 79:
			constInfo.yesilot79 = fiyat3
		if slot3 == 80:
			constInfo.yesilot80 = fiyat3
		if slot3 == 81:
			constInfo.yesilot81 = fiyat3
		if slot3 == 82:
			constInfo.yesilot82 = fiyat3
		if slot3 == 83:
			constInfo.yesilot83 = fiyat3
		if slot3 == 84:
			constInfo.yesilot84 = fiyat3
		if slot3 == 85:
			constInfo.yesilot85 = fiyat3
		if slot3 == 86:
			constInfo.yesilot86 = fiyat3
		if slot3 == 87:
			constInfo.yesilot87 = fiyat3
		if slot3 == 88:
			constInfo.yesilot88 = fiyat3
		if slot3 == 89:
			constInfo.yesilot89 = fiyat3
		if slot3 == 90:
			constInfo.yesilot90 = fiyat3
		if slot3 == 91:
			constInfo.yesilot91 = fiyat3
		if slot3 == 92:
			constInfo.yesilot92 = fiyat3
		if slot3 == 93:
			constInfo.yesilot93 = fiyat3
		if slot3 == 94:
			constInfo.yesilot94 = fiyat3
		if slot3 == 95:
			constInfo.yesilot95 = fiyat3
		if slot3 == 96:
			constInfo.yesilot96 = fiyat3
		if slot3 == 97:
			constInfo.yesilot97 = fiyat3
		if slot3 == 98:
			constInfo.yesilot98 = fiyat3
		if slot3 == 99:
			constInfo.yesilot99 = fiyat3
		if slot3 == 100:
			constInfo.yesilot100 = fiyat3

	def kirmizifytkac(self,slots,fiyats):
		import constInfo
		slot4 = int(slots)
		fiyat4 = int(fiyats)
		if slot4 == 0:
			constInfo.kirmiziot0 = fiyat4
		if slot4 == 1:
			constInfo.kirmiziot1 = fiyat4
		if slot4 == 2:
			constInfo.kirmiziot2 = fiyat4
		if slot4 == 3:
			constInfo.kirmiziot3 = fiyat4
		if slot4 == 4:
			constInfo.kirmiziot4 = fiyat4
		if slot4 == 5:
			constInfo.kirmiziot5 = fiyat4
		if slot4 == 6:
			constInfo.kirmiziot6 = fiyat4
		if slot4 == 7:
			constInfo.kirmiziot7 = fiyat4
		if slot4 == 8:
			constInfo.kirmiziot8 = fiyat4
		if slot4 == 9:
			constInfo.kirmiziot9 = fiyat4
		if slot4 == 10:
			constInfo.kirmiziot10 = fiyat4
		if slot4 == 11:
			constInfo.kirmiziot11 = fiyat4
		if slot4 == 12:
			constInfo.kirmiziot12 = fiyat4
		if slot4 == 13:
			constInfo.kirmiziot13 = fiyat4
		if slot4 == 14:
			constInfo.kirmiziot14 = fiyat4
		if slot4 == 15:
			constInfo.kirmiziot15 = fiyat4
		if slot4 == 16:
			constInfo.kirmiziot16 = fiyat4
		if slot4 == 17:
			constInfo.kirmiziot17 = fiyat4
		if slot4 == 18:
			constInfo.kirmiziot18 = fiyat4
		if slot4 == 19:
			constInfo.kirmiziot19 = fiyat4
		if slot4 == 20:
			constInfo.kirmiziot20 = fiyat4
		if slot4 == 21:
			constInfo.kirmiziot21 = fiyat4
		if slot4 == 22:
			constInfo.kirmiziot22 = fiyat4
		if slot4 == 23:
			constInfo.kirmiziot23 = fiyat4
		if slot4 == 24:
			constInfo.kirmiziot24 = fiyat4
		if slot4 == 25:
			constInfo.kirmiziot25 = fiyat4
		if slot4 == 26:
			constInfo.kirmiziot26 = fiyat4
		if slot4 == 27:
			constInfo.kirmiziot27 = fiyat4
		if slot4 == 28:
			constInfo.kirmiziot28 = fiyat4
		if slot4 == 29:
			constInfo.kirmiziot29 = fiyat4
		if slot4 == 30:
			constInfo.kirmiziot30 = fiyat4
		if slot4 == 31:
			constInfo.kirmiziot31 = fiyat4
		if slot4 == 32:
			constInfo.kirmiziot32 = fiyat4
		if slot4 == 33:
			constInfo.kirmiziot33 = fiyat4
		if slot4 == 34:
			constInfo.kirmiziot34 = fiyat4
		if slot4 == 35:
			constInfo.kirmiziot35 = fiyat4
		if slot4 == 36:
			constInfo.kirmiziot36 = fiyat4
		if slot4 == 37:
			constInfo.kirmiziot37 = fiyat4
		if slot4 == 38:
			constInfo.kirmiziot38 = fiyat4
		if slot4 == 39:
			constInfo.kirmiziot39 = fiyat4
		if slot4 == 40:
			constInfo.kirmiziot40 = fiyat4
		if slot4 == 41:
			constInfo.kirmiziot41 = fiyat4
		if slot4 == 42:
			constInfo.kirmiziot42 = fiyat4
		if slot4 == 43:
			constInfo.kirmiziot43 = fiyat4
		if slot4 == 44:
			constInfo.kirmiziot44 = fiyat4
		if slot4 == 45:
			constInfo.kirmiziot45 = fiyat4
		if slot4 == 46:
			constInfo.kirmiziot46 = fiyat4
		if slot4 == 47:
			constInfo.kirmiziot47 = fiyat4
		if slot4 == 48:
			constInfo.kirmiziot48 = fiyat4
		if slot4 == 49:
			constInfo.kirmiziot49 = fiyat4
		if slot4 == 50:
			constInfo.kirmiziot50 = fiyat4
		if slot4 == 51:
			constInfo.kirmiziot51 = fiyat4
		if slot4 == 52:
			constInfo.kirmiziot52 = fiyat4
		if slot4 == 53:
			constInfo.kirmiziot53 = fiyat4
		if slot4 == 54:
			constInfo.kirmiziot54 = fiyat4
		if slot4 == 55:
			constInfo.kirmiziot55 = fiyat4
		if slot4 == 56:
			constInfo.kirmiziot56 = fiyat4
		if slot4 == 57:
			constInfo.kirmiziot57 = fiyat4
		if slot4 == 58:
			constInfo.kirmiziot58 = fiyat4
		if slot4 == 59:
			constInfo.kirmiziot59 = fiyat4
		if slot4 == 60:
			constInfo.kirmiziot60 = fiyat4
		if slot4 == 61:
			constInfo.kirmiziot61 = fiyat4
		if slot4 == 62:
			constInfo.kirmiziot62 = fiyat4
		if slot4 == 63:
			constInfo.kirmiziot63 = fiyat4
		if slot4 == 64:
			constInfo.kirmiziot64 = fiyat4
		if slot4 == 65:
			constInfo.kirmiziot65 = fiyat4
		if slot4 == 66:
			constInfo.kirmiziot66 = fiyat4
		if slot4 == 67:
			constInfo.kirmiziot67 = fiyat4
		if slot4 == 68:
			constInfo.kirmiziot68 = fiyat4
		if slot4 == 69:
			constInfo.kirmiziot69 = fiyat4
		if slot4 == 70:
			constInfo.kirmiziot70 = fiyat4
		if slot4 == 71:
			constInfo.kirmiziot71 = fiyat4
		if slot4 == 72:
			constInfo.kirmiziot72 = fiyat4
		if slot4 == 73:
			constInfo.kirmiziot73 = fiyat4
		if slot4 == 74:
			constInfo.kirmiziot74 = fiyat4
		if slot4 == 75:
			constInfo.kirmiziot75 = fiyat4
		if slot4 == 76:
			constInfo.kirmiziot76 = fiyat4
		if slot4 == 77:
			constInfo.kirmiziot77 = fiyat4
		if slot4 == 78:
			constInfo.kirmiziot78 = fiyat4
		if slot4 == 79:
			constInfo.kirmiziot79 = fiyat4
		if slot4 == 80:
			constInfo.kirmiziot80 = fiyat4
		if slot4 == 81:
			constInfo.kirmiziot81 = fiyat4
		if slot4 == 82:
			constInfo.kirmiziot82 = fiyat4
		if slot4 == 83:
			constInfo.kirmiziot83 = fiyat4
		if slot4 == 84:
			constInfo.kirmiziot84 = fiyat4
		if slot4 == 85:
			constInfo.kirmiziot85 = fiyat4
		if slot4 == 86:
			constInfo.kirmiziot86 = fiyat4
		if slot4 == 87:
			constInfo.kirmiziot87 = fiyat4
		if slot4 == 88:
			constInfo.kirmiziot88 = fiyat4
		if slot4 == 89:
			constInfo.kirmiziot89 = fiyat4
		if slot4 == 90:
			constInfo.kirmiziot90 = fiyat4
		if slot4 == 91:
			constInfo.kirmiziot91 = fiyat4
		if slot4 == 92:
			constInfo.kirmiziot92 = fiyat4
		if slot4 == 93:
			constInfo.kirmiziot93 = fiyat4
		if slot4 == 94:
			constInfo.kirmiziot94 = fiyat4
		if slot4 == 95:
			constInfo.kirmiziot95 = fiyat4
		if slot4 == 96:
			constInfo.kirmiziot96 = fiyat4
		if slot4 == 97:
			constInfo.kirmiziot97 = fiyat4
		if slot4 == 98:
			constInfo.kirmiziot98 = fiyat4
		if slot4 == 99:
			constInfo.kirmiziot99 = fiyat4
		if slot4 == 100:
			constInfo.kirmiziot100 = fiyat4

	def mavifytkac(self,slots,fiyats):
		import constInfo
		slot5 = int(slots)
		fiyat5 = int(fiyats)
		if slot5 == 0:
			constInfo.maviot0 = fiyat5
		if slot5 == 1:
			constInfo.maviot1 = fiyat5
		if slot5 == 2:
			constInfo.maviot2 = fiyat5
		if slot5 == 3:
			constInfo.maviot3 = fiyat5
		if slot5 == 4:
			constInfo.maviot4 = fiyat5
		if slot5 == 5:
			constInfo.maviot5 = fiyat5
		if slot5 == 6:
			constInfo.maviot6 = fiyat5
		if slot5 == 7:
			constInfo.maviot7 = fiyat5
		if slot5 == 8:
			constInfo.maviot8 = fiyat5
		if slot5 == 9:
			constInfo.maviot9 = fiyat5
		if slot5 == 10:
			constInfo.maviot10 = fiyat5
		if slot5 == 11:
			constInfo.maviot11 = fiyat5
		if slot5 == 12:
			constInfo.maviot12 = fiyat5
		if slot5 == 13:
			constInfo.maviot13 = fiyat5
		if slot5 == 14:
			constInfo.maviot14 = fiyat5
		if slot5 == 15:
			constInfo.maviot15 = fiyat5
		if slot5 == 16:
			constInfo.maviot16 = fiyat5
		if slot5 == 17:
			constInfo.maviot17 = fiyat5
		if slot5 == 18:
			constInfo.maviot18 = fiyat5
		if slot5 == 19:
			constInfo.maviot19 = fiyat5
		if slot5 == 20:
			constInfo.maviot20 = fiyat5
		if slot5 == 21:
			constInfo.maviot21 = fiyat5
		if slot5 == 22:
			constInfo.maviot22 = fiyat5
		if slot5 == 23:
			constInfo.maviot23 = fiyat5
		if slot5 == 24:
			constInfo.maviot24 = fiyat5
		if slot5 == 25:
			constInfo.maviot25 = fiyat5
		if slot5 == 26:
			constInfo.maviot26 = fiyat5
		if slot5 == 27:
			constInfo.maviot27 = fiyat5
		if slot5 == 28:
			constInfo.maviot28 = fiyat5
		if slot5 == 29:
			constInfo.maviot29 = fiyat5
		if slot5 == 30:
			constInfo.maviot30 = fiyat5
		if slot5 == 31:
			constInfo.maviot31 = fiyat5
		if slot5 == 32:
			constInfo.maviot32 = fiyat5
		if slot5 == 33:
			constInfo.maviot33 = fiyat5
		if slot5 == 34:
			constInfo.maviot34 = fiyat5
		if slot5 == 35:
			constInfo.maviot35 = fiyat5
		if slot5 == 36:
			constInfo.maviot36 = fiyat5
		if slot5 == 37:
			constInfo.maviot37 = fiyat5
		if slot5 == 38:
			constInfo.maviot38 = fiyat5
		if slot5 == 39:
			constInfo.maviot39 = fiyat5
		if slot5 == 40:
			constInfo.maviot40 = fiyat5
		if slot5 == 41:
			constInfo.maviot41 = fiyat5
		if slot5 == 42:
			constInfo.maviot42 = fiyat5
		if slot5 == 43:
			constInfo.maviot43 = fiyat5
		if slot5 == 44:
			constInfo.maviot44 = fiyat5
		if slot5 == 45:
			constInfo.maviot45 = fiyat5
		if slot5 == 46:
			constInfo.maviot46 = fiyat5
		if slot5 == 47:
			constInfo.maviot47 = fiyat5
		if slot5 == 48:
			constInfo.maviot48 = fiyat5
		if slot5 == 49:
			constInfo.maviot49 = fiyat5
		if slot5 == 50:
			constInfo.maviot50 = fiyat5
		if slot5 == 51:
			constInfo.maviot51 = fiyat5
		if slot5 == 52:
			constInfo.maviot52 = fiyat5
		if slot5 == 53:
			constInfo.maviot53 = fiyat5
		if slot5 == 54:
			constInfo.maviot54 = fiyat5
		if slot5 == 55:
			constInfo.maviot55 = fiyat5
		if slot5 == 56:
			constInfo.maviot56 = fiyat5
		if slot5 == 57:
			constInfo.maviot57 = fiyat5
		if slot5 == 58:
			constInfo.maviot58 = fiyat5
		if slot5 == 59:
			constInfo.maviot59 = fiyat5
		if slot5 == 60:
			constInfo.maviot60 = fiyat5
		if slot5 == 61:
			constInfo.maviot61 = fiyat5
		if slot5 == 62:
			constInfo.maviot62 = fiyat5
		if slot5 == 63:
			constInfo.maviot63 = fiyat5
		if slot5 == 64:
			constInfo.maviot64 = fiyat5
		if slot5 == 65:
			constInfo.maviot65 = fiyat5
		if slot5 == 66:
			constInfo.maviot66 = fiyat5
		if slot5 == 67:
			constInfo.maviot67 = fiyat5
		if slot5 == 68:
			constInfo.maviot68 = fiyat5
		if slot5 == 69:
			constInfo.maviot69 = fiyat5
		if slot5 == 70:
			constInfo.maviot70 = fiyat5
		if slot5 == 71:
			constInfo.maviot71 = fiyat5
		if slot5 == 72:
			constInfo.maviot72 = fiyat5
		if slot5 == 73:
			constInfo.maviot73 = fiyat5
		if slot5 == 74:
			constInfo.maviot74 = fiyat5
		if slot5 == 75:
			constInfo.maviot75 = fiyat5
		if slot5 == 76:
			constInfo.maviot76 = fiyat5
		if slot5 == 77:
			constInfo.maviot77 = fiyat5
		if slot5 == 78:
			constInfo.maviot78 = fiyat5
		if slot5 == 79:
			constInfo.maviot79 = fiyat5
		if slot5 == 80:
			constInfo.maviot80 = fiyat5
		if slot5 == 81:
			constInfo.maviot81 = fiyat5
		if slot5 == 82:
			constInfo.maviot82 = fiyat5
		if slot5 == 83:
			constInfo.maviot83 = fiyat5
		if slot5 == 84:
			constInfo.maviot84 = fiyat5
		if slot5 == 85:
			constInfo.maviot85 = fiyat5
		if slot5 == 86:
			constInfo.maviot86 = fiyat5
		if slot5 == 87:
			constInfo.maviot87 = fiyat5
		if slot5 == 88:
			constInfo.maviot88 = fiyat5
		if slot5 == 89:
			constInfo.maviot89 = fiyat5
		if slot5 == 90:
			constInfo.maviot90 = fiyat5
		if slot5 == 91:
			constInfo.maviot91 = fiyat5
		if slot5 == 92:
			constInfo.maviot92 = fiyat5
		if slot5 == 93:
			constInfo.maviot93 = fiyat5
		if slot5 == 94:
			constInfo.maviot94 = fiyat5
		if slot5 == 95:
			constInfo.maviot95 = fiyat5
		if slot5 == 96:
			constInfo.maviot96 = fiyat5
		if slot5 == 97:
			constInfo.maviot97 = fiyat5
		if slot5 == 98:
			constInfo.maviot98 = fiyat5
		if slot5 == 99:
			constInfo.maviot99 = fiyat5
		if slot5 == 100:
			constInfo.maviot100 = fiyat5

	def morfytkac(self,slots,fiyats):
		import constInfo
		slot6 = int(slots)
		fiyat6 = int(fiyats)
		if slot6 == 0:
			constInfo.morot0 = fiyat6
		if slot6 == 1:
			constInfo.morot1 = fiyat6
		if slot6 == 2:
			constInfo.morot2 = fiyat6
		if slot6 == 3:
			constInfo.morot3 = fiyat6
		if slot6 == 4:
			constInfo.morot4 = fiyat6
		if slot6 == 5:
			constInfo.morot5 = fiyat6
		if slot6 == 6:
			constInfo.morot6 = fiyat6
		if slot6 == 7:
			constInfo.morot7 = fiyat6
		if slot6 == 8:
			constInfo.morot8 = fiyat6
		if slot6 == 9:
			constInfo.morot9 = fiyat6
		if slot6 == 10:
			constInfo.morot10 = fiyat6
		if slot6 == 11:
			constInfo.morot11 = fiyat6
		if slot6 == 12:
			constInfo.morot12 = fiyat6
		if slot6 == 13:
			constInfo.morot13 = fiyat6
		if slot6 == 14:
			constInfo.morot14 = fiyat6
		if slot6 == 15:
			constInfo.morot15 = fiyat6
		if slot6 == 16:
			constInfo.morot16 = fiyat6
		if slot6 == 17:
			constInfo.morot17 = fiyat6
		if slot6 == 18:
			constInfo.morot18 = fiyat6
		if slot6 == 19:
			constInfo.morot19 = fiyat6
		if slot6 == 20:
			constInfo.morot20 = fiyat6
		if slot6 == 21:
			constInfo.morot21 = fiyat6
		if slot6 == 22:
			constInfo.morot22 = fiyat6
		if slot6 == 23:
			constInfo.morot23 = fiyat6
		if slot6 == 24:
			constInfo.morot24 = fiyat6
		if slot6 == 25:
			constInfo.morot25 = fiyat6
		if slot6 == 26:
			constInfo.morot26 = fiyat6
		if slot6 == 27:
			constInfo.morot27 = fiyat6
		if slot6 == 28:
			constInfo.morot28 = fiyat6
		if slot6 == 29:
			constInfo.morot29 = fiyat6
		if slot6 == 30:
			constInfo.morot30 = fiyat6
		if slot6 == 31:
			constInfo.morot31 = fiyat6
		if slot6 == 32:
			constInfo.morot32 = fiyat6
		if slot6 == 33:
			constInfo.morot33 = fiyat6
		if slot6 == 34:
			constInfo.morot34 = fiyat6
		if slot6 == 35:
			constInfo.morot35 = fiyat6
		if slot6 == 36:
			constInfo.morot36 = fiyat6
		if slot6 == 37:
			constInfo.morot37 = fiyat6
		if slot6 == 38:
			constInfo.morot38 = fiyat6
		if slot6 == 39:
			constInfo.morot39 = fiyat6
		if slot6 == 40:
			constInfo.morot40 = fiyat6
		if slot6 == 41:
			constInfo.morot41 = fiyat6
		if slot6 == 42:
			constInfo.morot42 = fiyat6
		if slot6 == 43:
			constInfo.morot43 = fiyat6
		if slot6 == 44:
			constInfo.morot44 = fiyat6
		if slot6 == 45:
			constInfo.morot45 = fiyat6
		if slot6 == 46:
			constInfo.morot46 = fiyat6
		if slot6 == 47:
			constInfo.morot47 = fiyat6
		if slot6 == 48:
			constInfo.morot48 = fiyat6
		if slot6 == 49:
			constInfo.morot49 = fiyat6
		if slot6 == 50:
			constInfo.morot50 = fiyat6
		if slot6 == 51:
			constInfo.morot51 = fiyat6
		if slot6 == 52:
			constInfo.morot52 = fiyat6
		if slot6 == 53:
			constInfo.morot53 = fiyat6
		if slot6 == 54:
			constInfo.morot54 = fiyat6
		if slot6 == 55:
			constInfo.morot55 = fiyat6
		if slot6 == 56:
			constInfo.morot56 = fiyat6
		if slot6 == 57:
			constInfo.morot57 = fiyat6
		if slot6 == 58:
			constInfo.morot58 = fiyat6
		if slot6 == 59:
			constInfo.morot59 = fiyat6
		if slot6 == 60:
			constInfo.morot60 = fiyat6
		if slot6 == 61:
			constInfo.morot61 = fiyat6
		if slot6 == 62:
			constInfo.morot62 = fiyat6
		if slot6 == 63:
			constInfo.morot63 = fiyat6
		if slot6 == 64:
			constInfo.morot64 = fiyat6
		if slot6 == 65:
			constInfo.morot65 = fiyat6
		if slot6 == 66:
			constInfo.morot66 = fiyat6
		if slot6 == 67:
			constInfo.morot67 = fiyat6
		if slot6 == 68:
			constInfo.morot68 = fiyat6
		if slot6 == 69:
			constInfo.morot69 = fiyat6
		if slot6 == 70:
			constInfo.morot70 = fiyat6
		if slot6 == 71:
			constInfo.morot71 = fiyat6
		if slot6 == 72:
			constInfo.morot72 = fiyat6
		if slot6 == 73:
			constInfo.morot73 = fiyat6
		if slot6 == 74:
			constInfo.morot74 = fiyat6
		if slot6 == 75:
			constInfo.morot75 = fiyat6
		if slot6 == 76:
			constInfo.morot76 = fiyat6
		if slot6 == 77:
			constInfo.morot77 = fiyat6
		if slot6 == 78:
			constInfo.morot78 = fiyat6
		if slot6 == 79:
			constInfo.morot79 = fiyat6
		if slot6 == 80:
			constInfo.morot80 = fiyat6
		if slot6 == 81:
			constInfo.morot81 = fiyat6
		if slot6 == 82:
			constInfo.morot82 = fiyat6
		if slot6 == 83:
			constInfo.morot83 = fiyat6
		if slot6 == 84:
			constInfo.morot84 = fiyat6
		if slot6 == 85:
			constInfo.morot85 = fiyat6
		if slot6 == 86:
			constInfo.morot86 = fiyat6
		if slot6 == 87:
			constInfo.morot87 = fiyat6
		if slot6 == 88:
			constInfo.morot88 = fiyat6
		if slot6 == 89:
			constInfo.morot89 = fiyat6
		if slot6 == 90:
			constInfo.morot90 = fiyat6
		if slot6 == 91:
			constInfo.morot91 = fiyat6
		if slot6 == 92:
			constInfo.morot92 = fiyat6
		if slot6 == 93:
			constInfo.morot93 = fiyat6
		if slot6 == 94:
			constInfo.morot94 = fiyat6
		if slot6 == 95:
			constInfo.morot95 = fiyat6
		if slot6 == 96:
			constInfo.morot96 = fiyat6
		if slot6 == 97:
			constInfo.morot97 = fiyat6
		if slot6 == 98:
			constInfo.morot98 = fiyat6
		if slot6 == 99:
			constInfo.morot99 = fiyat6
		if slot6 == 100:
			constInfo.morot100 = fiyat6

	def ruhtasfytkac(self,slots,fiyats):
		import constInfo
		slot7 = int(slots)
		fiyat7 = int(fiyats)
		if slot7 == 0:
			constInfo.ruhtasi0 = fiyat7
		if slot7 == 1:
			constInfo.ruhtasi1 = fiyat7
		if slot7 == 2:
			constInfo.ruhtasi2 = fiyat7
		if slot7 == 3:
			constInfo.ruhtasi3 = fiyat7
		if slot7 == 4:
			constInfo.ruhtasi4 = fiyat7
		if slot7 == 5:
			constInfo.ruhtasi5 = fiyat7
		if slot7 == 6:
			constInfo.ruhtasi6 = fiyat7
		if slot7 == 7:
			constInfo.ruhtasi7 = fiyat7
		if slot7 == 8:
			constInfo.ruhtasi8 = fiyat7
		if slot7 == 9:
			constInfo.ruhtasi9 = fiyat7
		if slot7 == 10:
			constInfo.ruhtasi10 = fiyat7
		if slot7 == 11:
			constInfo.ruhtasi11 = fiyat7
		if slot7 == 12:
			constInfo.ruhtasi12 = fiyat7
		if slot7 == 13:
			constInfo.ruhtasi13 = fiyat7
		if slot7 == 14:
			constInfo.ruhtasi14 = fiyat7
		if slot7 == 15:
			constInfo.ruhtasi15 = fiyat7
		if slot7 == 16:
			constInfo.ruhtasi16 = fiyat7
		if slot7 == 17:
			constInfo.ruhtasi17 = fiyat7
		if slot7 == 18:
			constInfo.ruhtasi18 = fiyat7
		if slot7 == 19:
			constInfo.ruhtasi19 = fiyat7
		if slot7 == 20:
			constInfo.ruhtasi20 = fiyat7
		if slot7 == 21:
			constInfo.ruhtasi21 = fiyat7
		if slot7 == 22:
			constInfo.ruhtasi22 = fiyat7
		if slot7 == 23:
			constInfo.ruhtasi23 = fiyat7
		if slot7 == 24:
			constInfo.ruhtasi24 = fiyat7
		if slot7 == 25:
			constInfo.ruhtasi25 = fiyat7
		if slot7 == 26:
			constInfo.ruhtasi26 = fiyat7
		if slot7 == 27:
			constInfo.ruhtasi27 = fiyat7
		if slot7 == 28:
			constInfo.ruhtasi28 = fiyat7
		if slot7 == 29:
			constInfo.ruhtasi29 = fiyat7
		if slot7 == 30:
			constInfo.ruhtasi30 = fiyat7
		if slot7 == 31:
			constInfo.ruhtasi31 = fiyat7
		if slot7 == 32:
			constInfo.ruhtasi32 = fiyat7
		if slot7 == 33:
			constInfo.ruhtasi33 = fiyat7
		if slot7 == 34:
			constInfo.ruhtasi34 = fiyat7
		if slot7 == 35:
			constInfo.ruhtasi35 = fiyat7
		if slot7 == 36:
			constInfo.ruhtasi36 = fiyat7
		if slot7 == 37:
			constInfo.ruhtasi37 = fiyat7
		if slot7 == 38:
			constInfo.ruhtasi38 = fiyat7
		if slot7 == 39:
			constInfo.ruhtasi39 = fiyat7
		if slot7 == 40:
			constInfo.ruhtasi40 = fiyat7
		if slot7 == 41:
			constInfo.ruhtasi41 = fiyat7
		if slot7 == 42:
			constInfo.ruhtasi42 = fiyat7
		if slot7 == 43:
			constInfo.ruhtasi43 = fiyat7
		if slot7 == 44:
			constInfo.ruhtasi44 = fiyat7
		if slot7 == 45:
			constInfo.ruhtasi45 = fiyat7
		if slot7 == 46:
			constInfo.ruhtasi46 = fiyat7
		if slot7 == 47:
			constInfo.ruhtasi47 = fiyat7
		if slot7 == 48:
			constInfo.ruhtasi48 = fiyat7
		if slot7 == 49:
			constInfo.ruhtasi49 = fiyat7
		if slot7 == 50:
			constInfo.ruhtasi50 = fiyat7
		if slot7 == 51:
			constInfo.ruhtasi51 = fiyat7
		if slot7 == 52:
			constInfo.ruhtasi52 = fiyat7
		if slot7 == 53:
			constInfo.ruhtasi53 = fiyat7
		if slot7 == 54:
			constInfo.ruhtasi54 = fiyat7
		if slot7 == 55:
			constInfo.ruhtasi55 = fiyat7
		if slot7 == 56:
			constInfo.ruhtasi56 = fiyat7
		if slot7 == 57:
			constInfo.ruhtasi57 = fiyat7
		if slot7 == 58:
			constInfo.ruhtasi58 = fiyat7
		if slot7 == 59:
			constInfo.ruhtasi59 = fiyat7
		if slot7 == 60:
			constInfo.ruhtasi60 = fiyat7
		if slot7 == 61:
			constInfo.ruhtasi61 = fiyat7
		if slot7 == 62:
			constInfo.ruhtasi62 = fiyat7
		if slot7 == 63:
			constInfo.ruhtasi63 = fiyat7
		if slot7 == 64:
			constInfo.ruhtasi64 = fiyat7
		if slot7 == 65:
			constInfo.ruhtasi65 = fiyat7
		if slot7 == 66:
			constInfo.ruhtasi66 = fiyat7
		if slot7 == 67:
			constInfo.ruhtasi67 = fiyat7
		if slot7 == 68:
			constInfo.ruhtasi68 = fiyat7
		if slot7 == 69:
			constInfo.ruhtasi69 = fiyat7
		if slot7 == 70:
			constInfo.ruhtasi70 = fiyat7
		if slot7 == 71:
			constInfo.ruhtasi71 = fiyat7
		if slot7 == 72:
			constInfo.ruhtasi72 = fiyat7
		if slot7 == 73:
			constInfo.ruhtasi73 = fiyat7
		if slot7 == 74:
			constInfo.ruhtasi74 = fiyat7
		if slot7 == 75:
			constInfo.ruhtasi75 = fiyat7
		if slot7 == 76:
			constInfo.ruhtasi76 = fiyat7
		if slot7 == 77:
			constInfo.ruhtasi77 = fiyat7
		if slot7 == 78:
			constInfo.ruhtasi78 = fiyat7
		if slot7 == 79:
			constInfo.ruhtasi79 = fiyat7
		if slot7 == 80:
			constInfo.ruhtasi80 = fiyat7
		if slot7 == 81:
			constInfo.ruhtasi81 = fiyat7
		if slot7 == 82:
			constInfo.ruhtasi82 = fiyat7
		if slot7 == 83:
			constInfo.ruhtasi83 = fiyat7
		if slot7 == 84:
			constInfo.ruhtasi84 = fiyat7
		if slot7 == 85:
			constInfo.ruhtasi85 = fiyat7
		if slot7 == 86:
			constInfo.ruhtasi86 = fiyat7
		if slot7 == 87:
			constInfo.ruhtasi87 = fiyat7
		if slot7 == 88:
			constInfo.ruhtasi88 = fiyat7
		if slot7 == 89:
			constInfo.ruhtasi89 = fiyat7
		if slot7 == 90:
			constInfo.ruhtasi90 = fiyat7
		if slot7 == 91:
			constInfo.ruhtasi91 = fiyat7
		if slot7 == 92:
			constInfo.ruhtasi92 = fiyat7
		if slot7 == 93:
			constInfo.ruhtasi93 = fiyat7
		if slot7 == 94:
			constInfo.ruhtasi94 = fiyat7
		if slot7 == 95:
			constInfo.ruhtasi95 = fiyat7
		if slot7 == 96:
			constInfo.ruhtasi96 = fiyat7
		if slot7 == 97:
			constInfo.ruhtasi97 = fiyat7
		if slot7 == 98:
			constInfo.ruhtasi98 = fiyat7
		if slot7 == 99:
			constInfo.ruhtasi99 = fiyat7
		if slot7 == 100:
			constInfo.ruhtasi100 = fiyat7

	def pazarnasil(self,type):
		constInfo.pazarnasil = int(type)

# ARATILIR:

"MyShopPriceList"		: self.__PrivateShop_PriceList,

# ALTINA EKLENIR:
#if app.ENABLE_KAYA_MULTI_PRICE:
			"sufiyatkac"		: self.sufiyatkac,
			"barfiyatkac"		: self.barfiyatkac,
			"mavifytkac"		: self.mavifytkac,
			"yesilfytkac"		: self.yesilfytkac,
			"kirmizifytkac"		: self.kirmizifytkac,
			"morfytkac"			: self.morfytkac,
			"ruhtasfytkac"		: self.ruhtasfytkac,
			"pazarnasil"		: self.pazarnasil,
			"sutasiyok"			: self.sutasiyok,
			"wonyok"			: self.wonyok,
			"maviyok"			: self.maviyok,
			"yesilyok"			: self.yesilyok,
			"kirmiziyok"		: self.kirmiziyok,
			"moryok"			: self.moryok,
			"ruhtasiyok"		: self.ruhtasiyok,