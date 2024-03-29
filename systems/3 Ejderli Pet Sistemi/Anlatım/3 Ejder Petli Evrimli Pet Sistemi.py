##########################################################################################
Date = 19.06.2017 Hour = 23:14
Sistem Rixus Saltanat Files'inden Sökülmüştür.
Anlatım Mavi Ruh'a Aittir.
##########################################################################################

--------------------------------------------------------------------------
[ROOT]>game.py Açılır.


#Aratılır

self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())

#Altına Eklenir

## PET SYSTEM
		ExpBar = ui.AniImageBox() 
		ExpBar.AddFlag("not_pick") 
		ExpBar.SetDelay(6) 
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_1.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_1.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_1.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_1.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_1.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_1.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_1.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_2.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_3.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_4.tga")
		ExpBar.AppendImage("d:/ymir work/ui/bar/blue_bar_5.tga")
		self.ExpBar = ExpBar 
		self.ExpBar.SetPosition(100, 156)
		
		self.Boardx = ui.ImageBox() 
		self.Boardx.SetParent(self) 
		self.Boardx.LoadImage("d:/ymir work/ui/board.tga") 
		self.Boardx.SetPosition(0, 100)
		self.Boardx.SetSize(225, 155) 
		self.Boardx.Hide()

		self.PetImg = ui.ImageBox() 
		self.PetImg.SetParent(self) 
		self.PetImg.OnMouseLeftButtonUp = ui.__mem_func__(self.__Pet_Click) 
		self.PetImg.SetSize(0, 100) 
		self.PetImg.Hide() 
		
		self.BonusB = ui.ImageBox() 
		self.BonusB.SetParent(self) 
		self.BonusB.LoadImage("") 
		self.BonusB.OnMouseLeftButtonUp = ui.__mem_func__(self.__BonusB) 
		self.BonusB.SetPosition(wndMgr.GetScreenWidth() - 225+63, 190+76) 
		self.BonusB.Hide() 

		self.info1 = ui.TextLine() 
		self.info1.SetFontName("Arial:12") 
		self.info1.SetText("Beceri Puani ") 
		self.info1.SetPosition(102, 143)
		self.info1.SetFeather() 
		self.info1.SetOutline() 
		self.info1.Hide()
		
		self.Pokasz = ui.TextLine() 
		self.Pokasz.SetFontName("Arial:12") 
		self.Pokasz.SetText("")
		self.Pokasz.SetPosition(0, 0)
		self.Pokasz.SetFeather() 
		self.Pokasz.SetOutline() 
		self.Pokasz.Hide()		
		
		self.abi = ui.TextLine() 
		self.abi.SetFontName("Arial:12") 
		self.abi.SetHorizontalAlignLeft() 
		self.abi.SetPosition(172, 143)
		self.abi.SetFeather() 
		self.abi.SetOutline() 
		self.abi.Hide() 

		self.info2 = ui.TextLine() 
		self.info2.SetFontName("Arial:12") 
		self.info2.SetText("Exp: ") 
		self.info2.SetPosition(102, 165)
		self.info2.SetFeather() 
		self.info2.SetOutline() 
		self.info2.Hide() 

		self.exp = ui.TextLine() 
		self.exp.SetFontName("Arial:12") 
		self.exp.SetHorizontalAlignRight() 
		self.exp.SetPosition(179, 165)
		self.exp.SetFeather() 
		self.exp.SetOutline() 
		self.exp.Hide() 

		self.nextExp = ui.TextLine() 
		self.nextExp.SetFontName("Arial:12") 
		self.nextExp.SetHorizontalAlignLeft()	
		self.nextExp.SetFeather() 
		self.nextExp.SetOutline() 
		self.nextExp.Hide() 

		self.nome = ui.TextLine() 
		self.nome.SetFontName(localeInfo.UI_DEF_FONT_LARGE) 
		self.nome.SetPosition(128, 126)
		self.nome.SetFeather() 
		self.nome.SetOutline() 
		self.nome.Hide() 

		self.livello = ui.TextLine() 
		self.livello.SetFontName("Arial:12") 
		self.livello.SetPosition(100, 143)
		self.livello.SetFeather() 
		self.livello.SetOutline() 
		self.livello.Hide() 
		
		self.Bonus1 = ui.TextLine() 
		self.Bonus1.SetFontName("Arial:12") 
		self.Bonus1.SetHorizontalAlignLeft() 
		self.Bonus1.SetPosition(wndMgr.GetScreenWidth() - 154, 265) 
		self.Bonus1.SetFeather() 
		self.Bonus1.SetOutline() 
		self.Bonus1.Hide() 
		
		self.Bonus2 = ui.TextLine() 
		self.Bonus2.SetFontName("Arial:12") 
		self.Bonus2.SetHorizontalAlignLeft() 
		self.Bonus2.SetPosition(wndMgr.GetScreenWidth() - 154, 276) 
		self.Bonus2.SetFeather() 
		self.Bonus2.SetOutline() 
		self.Bonus2.Hide() 
		
		self.Bonus3 = ui.TextLine() 
		self.Bonus3.SetFontName("Arial:12") 
		self.Bonus3.SetHorizontalAlignLeft() 
		self.Bonus3.SetPosition(wndMgr.GetScreenWidth() - 154, 287) 
		self.Bonus3.SetFeather() 
		self.Bonus3.SetOutline() 
		self.Bonus3.Hide() 
		
		self.Bonus4 = ui.TextLine() 
		self.Bonus4.SetFontName("Arial:12") 
		self.Bonus4.SetHorizontalAlignLeft() 
		self.Bonus4.SetPosition(wndMgr.GetScreenWidth() - 154, 298) 
		self.Bonus4.SetFeather() 
		self.Bonus4.SetOutline() 
		self.Bonus4.Hide() 
		
		self.Bonus5 = ui.TextLine() 
		self.Bonus5.SetFontName("Arial:12") 
		self.Bonus5.SetHorizontalAlignLeft() 
		self.Bonus5.SetPosition(wndMgr.GetScreenWidth() - 154, 309) 
		self.Bonus5.SetFeather() 
		self.Bonus5.SetOutline() 
		self.Bonus5.Hide()		
		

#Aratılır

def __ServerCommand_Build(self):
		serverCommandList={

#Altına Eklenir

"PetPokaz"				: self.__OpenBoardx, 
			"PetZamnkij"			: self.__CloseBoardx, 
			"PetUpdate"				: self.__UpdateBoardx, 
			"PetBonus"				: self.__Bonusy,			

#En Alta Eklenir

## PET SYSTEM
	def __OpenBoardx(self, index, livello, ExpPet, nextExpPet, lock, abi): 

		from array import array 
		pets = ("     Kurt","    Aslan","   Kaplan","Yavru Azrail","   Ceylan"," Yeşil Anka","Buz Ankası","Sevimli Bıdık","Sarı Anka","Yavru Ejder","Ejder","Zırhlı Ejder")
		petimage = ("it","aslan","kaplan","catacomb","rengeyigi","yesilanka","buzankasi","bidik","sarianka","ejder","ejder","ejder") 
		self.PetImg.SetPosition(22, 116) # Pet icon
		if int(index) == 4:
			self.PetImg.LoadImage("d:/ymir work/ui/catacomb.tga") 
			self.nome.SetText(pets[3]) 
		else:
			self.PetImg.LoadImage("d:/ymir work/ui/"+petimage[int(index)-1]+".tga") 
			self.nome.SetText(pets[int(index)-1])

		if int(index) == 5:
			self.PetImg.LoadImage("d:/ymir work/ui/rengeyigi.tga") 
			self.nome.SetText(pets[4]) 
		else:
			self.PetImg.LoadImage("d:/ymir work/ui/"+petimage[int(index)-1]+".tga") 
			self.nome.SetText(pets[int(index)-1])
			
		self.livello.SetText(livello)
		if len(livello) > 1:
			self.livello.SetPosition(69, 161)
		else:
			self.livello.SetPosition(69, 161)
		self.abi.SetText(abi)
		if int(nextExpPet) > 0: 
			self.ExpBar.SetPercentage(ExpPet, nextExpPet) 
		else: 
			pass 

		self.IsLock = int(lock) 
		if self.IsLock: 
			self.nextExp.SetText("Kapalı") 
			self.nextExp.SetPosition(160, 165)
			self.exp.Hide() 
		else: 
			self.exp.SetText(ExpPet+" / ") 
			self.nextExp.SetText(nextExpPet) 
			self.exp.Show() 
			self.nextExp.SetPosition(180, 165)

		self.info1.Show() 
		self.info2.Show() 
		self.abi.Show() 
		self.Boardx.Show() 
		self.nome.Show() 
		self.livello.Show() 
		self.nextExp.Show() 
		self.ExpBar.Show() 
		self.PetImg.Show() 
		self.Pokasz.Show()
		self.Bonus1.Hide()
		self.Bonus2.Hide()
		self.Bonus3.Hide()
		self.Bonus4.Hide()
		self.Bonus5.Hide()
		self.BonusB.LoadImage("")
		self.BonusB.Show()
		self.BonusIsClose = FALSE 
		self.PetIsClose = FALSE
		
	def __Bonusy(self, opcje, bonusy):
		if opcje == "1":
			self.Bonus1.SetText(bonusy.replace("_"," "))
		elif opcje == "2":
			self.Bonus2.SetText(bonusy.replace("_"," ")) 
		elif opcje == "3":
			self.Bonus3.SetText(bonusy.replace("_"," "))
		elif opcje == "4":
			self.Bonus4.SetText(bonusy.replace("_"," ")) 
		elif opcje == "5":	
			self.Bonus5.SetText(bonusy.replace("_"," "))

	def __UpdateBoardx(self, index, livello, ExpPet, nextExpPet, lock, abi): 
		self.livello.SetText(livello)
		self.abi.SetText(abi)
		if len(livello) > 1:
			self.livello.SetPosition(0, 100)
		else:
			self.livello.SetPosition(0, 100)
		if int(nextExpPet) > 0: 
			self.ExpBar.SetPercentage(ExpPet, nextExpPet) 
		else: 
			pass 

		self.IsLock = int(lock) 
		if self.IsLock: 
			self.nextExp.SetText("Kapalı") 
		else: 
			self.exp.SetText(ExpPet+" / ") 
			self.nextExp.SetText(nextExpPet) 

	def __Pet_Click(self): 
		if self.PetIsClose and self.IsLock: 
			self.Boardx.Show() 
			self.nome.Show() 
			self.livello.Show() 
			self.info1.Show() 
			self.info2.Show() 
			self.abi.Show() 
			self.exp.Hide() 
			self.nextExp.Show() 
			self.ExpBar.Show() 
			self.Pokasz.Show()
			self.PetImg.SetPosition(22, 116)
			self.PetImg.Show()
			self.BonusB.Show()
			self.PetIsClose = FALSE
			import chat
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<PET> Gizlenen Evcil Hayvan menüsü gösterildi. ")
		elif self.PetIsClose: 
			self.Boardx.Show() 
			self.nome.Show() 
			self.livello.Show() 
			self.info1.Show() 
			self.info2.Show() 
			self.exp.Show() 
			self.abi.Show() 
			self.nextExp.Show() 
			self.ExpBar.Show() 
			self.Pokasz.Show()
			self.PetImg.SetPosition(22, 116) 
			self.PetImg.Show() 
			self.BonusB.Show() 
			self.PetIsClose = FALSE
			import chat
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<PET> Gizlenen Evcil Hayvan menüsü gösterildi. ")
		else: 
			self.Boardx.Hide() 
			self.nome.Hide() 
			self.livello.Hide() 
			self.info1.Hide() 
			self.info2.Hide() 
			self.exp.Hide() 
			self.nextExp.Hide() 
			self.ExpBar.Hide() 
			self.Pokasz.Hide()
			self.PetImg.SetPosition(22, 116) 
			self.abi.Hide() 
			self.BonusB.Hide()
			self.Bonus1.Hide()
			self.Bonus2.Hide()
			self.Bonus3.Hide()
			self.Bonus4.Hide()
			self.Bonus5.Hide()	
			self.PetImg.Show() 
			self.PetIsClose = TRUE 
			self.BonusIsClose = FALSE
			import chat
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<PET> Evcil Hayvan menüsü gizlendi. ")

	def __CloseBoardx(self): 
		self.Boardx.Hide() 
		self.nome.Hide() 
		self.livello.Hide() 
		self.info1.Hide() 
		self.info2.Hide()
		self.abi.Hide()
		self.exp.Hide() 
		self.nextExp.Hide() 
		self.ExpBar.Hide() 
		self.BonusB.Hide() 
		self.PetImg.Hide()
		self.Pokasz.Hide()
		self.Bonus1.Hide()
		self.Bonus2.Hide()
		self.Bonus3.Hide()
		self.Bonus4.Hide()
		self.Bonus5.Hide()
		
	def __BonusB(self):
		if self.BonusIsClose:
			self.BonusB.LoadImage("")
			self.BonusIsClose = FALSE
			self.Bonus1.Hide()
			self.Bonus2.Hide()
			self.Bonus3.Hide()
			self.Bonus4.Hide()
			self.Bonus5.Hide()		
			self.Pokasz.Show()
		else:
			self.BonusB.LoadImage("")
			self.BonusIsClose = TRUE
			self.Bonus1.Show()
			self.Bonus2.Show()
			self.Bonus3.Show()
			self.Bonus4.Show()
			self.Bonus5.Show()	
			self.Pokasz.Hide()

--------------------------------------------------------------------------------------------------------------------------------
Phyton Bölümü Bitmiştir. Sıra Verilen Questi Filezilla Açılıp /usr/game/share/locale/turkey/quest Bölümüne Atılır.
Verilen Pet_Summon.quest /usr/game/share/locale/turkey/quest bölümüne atılır ve putty yardımıyla okutulur.
--------------------------------------------------------------------------------------------------------------------------------
#Questlib.lua Açılır En Alta Eklenir

dofile('locale/turkey/quest/AIMTIEvrimPet.lua')

Filezilla le Yapılacaklar Bitmiştir.
--------------------------------------------------------------------------------------------------------------------------------
Verilen ymir work Klasörünü Root'un içine Atılır.
`--------------------------------------------------------------------------------------------------------------------------------



                                            >>> Taskbar'a Pet Menüsü Eklemek İÇİN <<<                                                 

--------------------------------------------------------------------------------------------------------------------------------
[ROOT]>uitaskbar.py Açılır

# Aratılır

BUTTON_CHAT = 4

# Altına Eklenir

BUTTON_HORSEQUICK = 5

# Aratılır

toggleButtonDict[TaskBar.BUTTON_CHARACTER]=self.TaskBarLeft.GetChild("CharacterButton")

# Altına Eklenir

toggleButtonDict[TaskBar.BUTTON_HORSEQUICK]=self.GetChild("button_horse")
--------------------------------------------------------------------------------------------------------------------------------
[ROOT]>interfacemodule.py Açılır

# Aratılır

self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_CHARACTER, ui.__mem_func__(self.ToggleCharacterWindowStatusPage))

# Altına Eklenir

self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_HORSEQUICK, ui.__mem_func__(self.horse_button))

# Aratılır

def __IsChatOpen(self):
		return TRUE

# Altına Eklenir

def horse_button(self):
		import constInfo
		qid = constInfo.LOAD_QUEST_HORSE_BUTTON
		event.QuestButtonClick(qid)
--------------------------------------------------------------------------------------------------------------------------------
[ROOT]>constinfo.py Açılır

# Aratılır

PVPMODE_PROTECTED_LEVEL = 15

# Altına Eklenir

LOAD_QUEST_HORSE_BUTTON = 0
--------------------------------------------------------------------------------------------------------------------------------
[ROOT]>game.py Açılır

# Aratılır

"mall"			: self.__InGameShop_Show,

# Altına Eklenir

"horse_button" : self.__Horse_button,

# En Sona Eklenir

def __Horse_button(self, qid):
		constInfo.LOAD_QUEST_HORSE_BUTTON = int(qid)
--------------------------------------------------------------------------------------------------------------------------------
[LOCALE_TR]>taskbar.py Açılır

# Aratılır

{
			"name" : "CharacterButton",
			"type" : "button",
			

			"x" : SCREEN_WIDTH - 144,
			"y" : 3 + Y_ADD_POSITION,

			"tooltip_text" : uiScriptLocale.TASKBAR_CHARACTER,

			"default_image" : ROOT + "TaskBar/Character_Button_01.sub",
			"over_image" : ROOT + "TaskBar/Character_Button_02.sub",
			"down_image" : ROOT + "TaskBar/Character_Button_03.sub",
		},

# Altına Eklenir

{
			"name" : "button_horse",
			"type" : "button",

			"x" : SCREEN_WIDTH - 178,
			"y" : 3 + Y_ADD_POSITION,

			"tooltip_text" : "Pet Menusu"

			"default_image" : "d:/ymir work/ui/pet_up.tga",
			"over_image" : "d:/ymir work/ui/pet_over.tga",
			"down_image" : "d:/ymir work/ui/pet_down.tga",
		},
--------------------------------------------------------------------------------------------------------------------------------
                                             >>> 3 Ejder Pet'i Eklemek İçin <<<                                                 

[ROOT]>npc_list Açılır

# Eklenir

34030	dragon_pet
34031	taurios_dragon_pet3
34032	ridack_drag5
--------------------------------------------------------------------------------------------------------------------------------
[NAVICAT]>mob_proto Eklenir

INSERT INTO mob_proto VALUES ('34030', '?? ???', 0x506F726B69, '5', '1', '0', '1', '', '', '0', '', 'STUN,SLOW,CURSE,TERROR', '0', 'pig_young1', '2', '0', '0', '0', '0', '0', '0', '120', '3', '1', '0', '0', '10', '4', '100', '100', '0', '2000', '150', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');
INSERT INTO mob_proto VALUES ('34031', '?? ???', 0x506F726B69, '5', '1', '0', '1', '', '', '0', '', 'STUN,SLOW,CURSE,TERROR', '0', 'pig_young1', '2', '0', '0', '0', '0', '0', '0', '120', '3', '1', '0', '0', '10', '4', '100', '100', '0', '2000', '150', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');
INSERT INTO mob_proto VALUES ('34032', 'wslik_410', 0x456A64657220506574, '5', '1', '0', '1', '', '', '0', '', 'STUN,SLOW,CURSE,TERROR', '0', 'pig_young1', '2', '0', '0', '0', '0', '0', '0', '120', '3', '1', '0', '0', '10', '4', '100', '100', '0', '2000', '150', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');
--------------------------------------------------------------------------------------------------------------------------------

Pack'ları Ekleyin INDEX`e Pack İsmini Ekleyin... Reboot Atın Bitmiştir.