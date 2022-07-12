/*
Discord ►	discord.gg/yz5xNNGM5C
Facebook ►	facebook.com/dirilis.maviruh
Date : 06.03.2022
*/
------------------------------------------------------------/* Game Source => Common -> Service.h */
// Ekle
#define MAVIRUH_WING_SLOT
------------------------------------------------------------/*Game Source => Common -> item_length.h */
// Arat
	ITEM_BELT,

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
	ITEM_WING,
#endif
------------------------------------------------------------/*Game Source => Common -> length.h */
// Arat
	WEAR_BELT,

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
	WEAR_WING,
#endif
------------------------------------------------------------/*Game Source => DB -> ProtoReader.cpp */
// Arat
		"ITEM_BELT",

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
		"ITEM_WING",
#endif
------------------------------------------------------------/*Game Source => Game -> char_item.cpp */
// Arat
		case ITEM_BELT:

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
		case ITEM_WING:
#endif
------------------------------------------------------------/*Game Source => Game -> item.cpp */
// Arat
&& ITEM_BELT != GetType()

// Sağına Ekle
&& ITEM_WING != GetType()

// Arat
	else if (GetType() == ITEM_BELT)
		return WEAR_BELT;

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
	else if (GetType() == ITEM_WING)
		return WEAR_WING;
#endif

// Arat
	case ITEM_BELT:

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
	case ITEM_WING:
#endif
------------------------------------------------------------/*Client Source => GameLib -> ItemData.h */
// Arat
			ITEM_TYPE_BELT,

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
			ITEM_TYPE_WING,
#endif
------------------------------------------------------------/*Client Source => UserInterface -> GameType.h */
// Arat
	const DWORD c_Equipment_Belt  = c_New_Equipment_Start + 2;;

// Değiştir
	const DWORD c_Equipment_Belt  = c_New_Equipment_Start + 2;
	#ifdef MAVIRUH_WING_SLOT
	const DWORD c_Equipment_Wing  = c_New_Equipment_Start + 3;;
	#endif
------------------------------------------------------------/*Client Source => UserInterface -> Locale_inc.h */
// Ekle
#define MAVIRUH_WING_SLOT
------------------------------------------------------------/*Client Source => UserInterface -> PythonItemModule.cpp */
// Arat
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	PyModule_AddIntConstant(poModule, "EQUIPMENT_RING1",			c_Equipment_Ring1);
	PyModule_AddIntConstant(poModule, "EQUIPMENT_RING2",			c_Equipment_Ring2);
	PyModule_AddIntConstant(poModule, "EQUIPMENT_BELT",				c_Equipment_Belt);
#endif

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
	PyModule_AddIntConstant(poModule, "EQUIPMENT_WING",			c_Equipment_Wing);
#endif

// Arat
	PyModule_AddIntConstant(poModule, "ITEM_TYPE_BELT",				CItemData::ITEM_TYPE_BELT);

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
	PyModule_AddIntConstant(poModule, "ITEM_TYPE_WING",			CItemData::ITEM_TYPE_WING);
#endif
------------------------------------------------------------/*Client Source => UserInterface -> PythonApplicationModule.cpp */
// Arat
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	0);
#endif

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
	PyModule_AddIntConstant(poModule, "MAVIRUH_WING_SLOT",	1);
#else
	PyModule_AddIntConstant(poModule, "MAVIRUH_WING_SLOT",	0);
#endif
------------------------------------------------------------/*Dump Proto => dump_proto -> ItemCSVReader.cpp */
// Arat
		"ITEM_BELT",

// Altına Ekle
#ifdef MAVIRUH_WING_SLOT
		"ITEM_WING",
#endif
------------------------------------------------------------/*Root => uitooltip.py */
// Arat
		elif item.ITEM_TYPE_BELT == itemType:
			self.__AppendLimitInformation()
			self.__AppendAffectInformation()
			self.__AppendAttributeInformation(attrSlot)
			self.AppendTextLine("Kullanilabilir Slot : %s " % extra_slot[item.GetValue(0)], self.SPECIAL_POSITIVE_COLOR)
			self.__AppendAccessoryMetinSlotInfo(metinSlot, constInfo.GET_BELT_MATERIAL_VNUM(itemVnum))

// Altına Ekle
		elif item.ITEM_TYPE_WING == itemType:
			self.__AppendLimitInformation()
			self.__AppendAffectInformation()
			self.__AppendAttributeInformation(attrSlot)
------------------------------------------------------------/*Root => uiinventory.py */
// Arat
class InventoryWindow(ui.ScriptWindow):

// İçinde Bul
	def Show(self):

// Altına Ekle
		self.RefreshNewSlotWing()

// Arat
			self.wndBelt.RefreshSlot()

// Altına Ekle
	def RefreshNewSlotWing(self):
		getWingVnum=player.GetItemIndex
		
		slot_wing = item.EQUIPMENT_WING
		for wing in xrange(slot_wing):
			slot_Wing = item.EQUIPMENT_WING + wing
			self.wndEquip.SetItemSlot(slot_Wing, getWingVnum(slot_Wing), 0)

// Arat
				print "ENABLE_NEW_EQUIPMENT_SYSTEM", slotNumber, itemCount, getItemVNum(slotNumber)

// Altına Ekle
		slot_wing = item.EQUIPMENT_WING
		for wing in xrange(slot_wing):
			slot_Wing = item.EQUIPMENT_WING + wing
			self.wndEquip.SetItemSlot(slot_Wing, getItemVNum(slot_Wing), 0)
------------------------------------------------------------/*Locale_tr => locale/tr/ui -> inventorywindow.py */
// Arat
				## Equipment Slot
				{
					"name" : "Equipment_Base",
					"type" : "image",

					"x" : 10,
					"y" : 33,

					"image" : "d:/ymir work/ui/equipment_bg_without_ring.tga",
// Değiştir
				## Equipment Slot
				{
					"name" : "Equipment_Base",
					"type" : "image",

					"x" : 10,
					"y" : 33,

					"image" : "d:/ymir work/ui/equipment_bg_with_ring_new.tga",

// Arat
										{"index":item.EQUIPMENT_BELT, "x":39, "y":106, "width":32, "height":32},

// Altına Ekle
										{"index":item.EQUIPMENT_WING, "x":2, "y":106, "width":32, "height":32},
------------------------------------------------------------>