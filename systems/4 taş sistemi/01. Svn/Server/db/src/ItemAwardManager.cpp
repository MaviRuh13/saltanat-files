// Arat (void ItemAwardManager::RequestLoad() icinde)
	snprintf(szQuery, sizeof(szQuery), "SELECT id,login,vnum,count,socket0,socket1,socket2,mall,why FROM item_award WHERE taken_time IS NULL and id > %d", g_dwLastCachedItemAwardID);

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
	snprintf(szQuery, sizeof(szQuery), "SELECT id,login,vnum,count,socket0,socket1,socket2,socket3,mall,why FROM item_award WHERE taken_time IS NULL and id > %d", g_dwLastCachedItemAwardID);
#else
	snprintf(szQuery, sizeof(szQuery), "SELECT id,login,vnum,count,socket0,socket1,socket2,mall,why FROM item_award WHERE taken_time IS NULL and id > %d", g_dwLastCachedItemAwardID);
#endif

// Arat
		str_to_number(kData->dwSocket2, row[col++]);

// Altina Ekle
#ifdef ENABLE_FOUR_STONE_SYSTEM
		str_to_number(kData->dwSocket3, row[col++]);
#endif