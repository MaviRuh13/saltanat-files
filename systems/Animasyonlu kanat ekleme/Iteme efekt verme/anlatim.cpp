/*
Discord ►	discord.gg/yz5xNNGM5C
Facebook ►	facebook.com/dirilis.maviruh
Date : 06.03.2022
*/
------------------------------------------------------------/* Game Source => Common -> Service.h */
// Ekle
#define MAVIRUH_WING_EFFECT
------------------------------------------------------------/*Game Source => Game -> affect.h */
// Arat
	AFFECT_QUEST_START_IDX = 1000

// Üstüne Ekle
#ifdef MAVIRUH_WING_EFFECT
	AFFECT_WING_1 = 703, AFFECT_WING_2 = 704, AFFECT_WING_3 = 705, AFFECT_WING_4 = 706,
#endif

// Arat
	AFF_BITS_MAX

// Üstüne Ekle
#ifdef MAVIRUH_WING_EFFECT
	AFF_WING1,AFF_WING2,AFF_WING3,AFF_WING4,
#endif
------------------------------------------------------------/*Game Source => Game -> char_affect.cpp */
// Arat
			if ( IS_NO_CLEAR_ON_DEATH_AFFECT(pkAff->dwType) || IS_NO_SAVE_AFFECT(pkAff->dwType) )
			{
				++it;
				continue;
			}

// Altına Ekle
#if defined MAVIRUH_WING_EFFECT
			if(pkAff->dwType==AFFECT_WING_1 || pkAff->dwType==AFFECT_WING_2 || pkAff->dwType==AFFECT_WING_3 || pkAff->dwType==AFFECT_WING_4){++it;continue;}
#endif
------------------------------------------------------------/*Game Source => Game -> item.cpp */
// Arat
	if (!ch)
	{
		sys_err("EquipTo: nil character");
		return false;
	}

// Altına Ekle
#if defined MAVIRUH_WING_EFFECT
	if (GetVnum() == WING_VNUM_1){if (!ch->IsAffectFlag(AFFECT_WING_1))ch->AddAffect(AFFECT_WING_1, POINT_NONE, 0,AFF_WING1, INFINITE_AFFECT_DURATION, 0, false);}
	if (GetVnum() == WING_VNUM_2){if (!ch->IsAffectFlag(AFFECT_WING_2))ch->AddAffect(AFFECT_WING_2, POINT_NONE, 0,AFF_WING2, INFINITE_AFFECT_DURATION, 0, false);}
	if (GetVnum() == WING_VNUM_3){if (!ch->IsAffectFlag(AFFECT_WING_3))ch->AddAffect(AFFECT_WING_3, POINT_NONE, 0,AFF_WING3, INFINITE_AFFECT_DURATION, 0, false);}
	if (GetVnum() == WING_VNUM_4){if (!ch->IsAffectFlag(AFFECT_WING_4))ch->AddAffect(AFFECT_WING_4, POINT_NONE, 0,AFF_WING4, INFINITE_AFFECT_DURATION, 0, false);}
#endif

// Arat
	if (IsRideItem())
		ClearMountAttributeAndAffect();

// Altına Ekle

#if defined MAVIRUH_WING_EFFECT
	if (GetVnum() == WING_VNUM_1){m_pOwner->RemoveAffect(AFFECT_WING_1);}
	if (GetVnum() == WING_VNUM_2){m_pOwner->RemoveAffect(AFFECT_WING_2);}
	if (GetVnum() == WING_VNUM_3){m_pOwner->RemoveAffect(AFFECT_WING_3);}
	if (GetVnum() == WING_VNUM_4){m_pOwner->RemoveAffect(AFFECT_WING_4);}
#endif

// Arat
	if (pkItem->GetValue(2) == 0)
	{
		if (pkItem->GetSocket(ITEM_SOCKET_UNIQUE_REMAIN_TIME) <= 1)
		{

// Altına Ekle
#if defined MAVIRUH_WING_EFFECT
			if (pkItem->GetVnum() == WING_VNUM_1){pkItem->GetOwner()->RemoveAffect(AFFECT_WING_1);}
			if (pkItem->GetVnum() == WING_VNUM_2){pkItem->GetOwner()->RemoveAffect(AFFECT_WING_2);}
			if (pkItem->GetVnum() == WING_VNUM_3){pkItem->GetOwner()->RemoveAffect(AFFECT_WING_3);}
			if (pkItem->GetVnum() == WING_VNUM_4){pkItem->GetOwner()->RemoveAffect(AFFECT_WING_4);}
#endif

// Arat
		if (pkItem->GetSocket(ITEM_SOCKET_UNIQUE_REMAIN_TIME) <= cur)
		{

// Altına Ekle
#if defined MAVIRUH_WING_EFFECT
			if (pkItem->GetVnum() == WING_VNUM_1){pkItem->GetOwner()->RemoveAffect(AFFECT_WING_1);}
			if (pkItem->GetVnum() == WING_VNUM_2){pkItem->GetOwner()->RemoveAffect(AFFECT_WING_2);}
			if (pkItem->GetVnum() == WING_VNUM_3){pkItem->GetOwner()->RemoveAffect(AFFECT_WING_3);}
			if (pkItem->GetVnum() == WING_VNUM_4){pkItem->GetOwner()->RemoveAffect(AFFECT_WING_4);}
#endif
------------------------------------------------------------/*Game Source => Game -> unique_item.h */
// Arat
	DRAGON_HEART_VNUM = 100000,

// Altına Ekle
#if defined MAVIRUH_WING_EFFECT
	WING_VNUM_1 = 72705, WING_VNUM_2 = 72706, WING_VNUM_3 = 72707, WING_VNUM_4 = 72708,
#endif
------------------------------------------------------------/*Client Source => UserInterface -> InstanceBase.h */
// Arat
			AFFECT_NUM = 64,

// Üstüne Ekle
#if defined MAVIRUH_WING_EFFECT
			AFFECT_WING1, AFFECT_WING2, AFFECT_WING3, AFFECT_WING4,
#endif
------------------------------------------------------------/*Client Source => UserInterface -> Locale_inc.h */
// Ekle
#define MAVIRUH_WING_EFFECT
------------------------------------------------------------/*Client Source => UserInterface -> PythonApplicationModule.cpp */
// Arat
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	0);
#endif

// Altına Ekle
#if defined MAVIRUH_WING_EFFECT
	PyModule_AddIntConstant(poModule, "MAVIRUH_WING_EFFECT",	1);
#else
	PyModule_AddIntConstant(poModule, "MAVIRUH_WING_EFFECT",	0);
#endif
------------------------------------------------------------/*Client Source => UserInterface -> PythonCharacterModule.cpp */
// Arat
	PyModule_AddIntConstant(poModule, "NEW_AFFECT_DRAGON_SOUL_QUALIFIED",		CInstanceBase::NEW_AFFECT_DRAGON_SOUL_QUALIFIED);

	PyModule_AddIntConstant(poModule, "NEW_AFFECT_DRAGON_SOUL_DECK1",		CInstanceBase::NEW_AFFECT_DRAGON_SOUL_DECK1);
	PyModule_AddIntConstant(poModule, "NEW_AFFECT_DRAGON_SOUL_DECK2",		CInstanceBase::NEW_AFFECT_DRAGON_SOUL_DECK2);

// Altına Ekle
#if defined MAVIRUH_WING_EFFECT
	PyModule_AddIntConstant(poModule, "AFFECT_WING1",						CInstanceBase::AFFECT_WING1);
	PyModule_AddIntConstant(poModule, "AFFECT_WING2",						CInstanceBase::AFFECT_WING2);
	PyModule_AddIntConstant(poModule, "AFFECT_WING3",						CInstanceBase::AFFECT_WING3);
	PyModule_AddIntConstant(poModule, "AFFECT_WING4",						CInstanceBase::AFFECT_WING4);
#endif
------------------------------------------------------------/*Root => playersettingmodule.py */
// Arat
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+1, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_7.mse")

// Üstüne Ekle
	if app.MAVIRUH_WING_EFFECT:
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+42, 'Bip01', 'd:/ymir work/effect/wing/maviruh/yesilkanat.mse')
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+43, 'Bip01', 'd:/ymir work/effect/wing/maviruh/mavikanat.mse')
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+44, 'Bip01', 'd:/ymir work/effect/wing/maviruh/kirmizikanat.mse')
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+45, 'Bip01', 'd:/ymir work/effect/wing/maviruh/bordokanat.mse')
------------------------------------------------------------>