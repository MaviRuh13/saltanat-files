// Arat :
// bool CClientManager::InitializeShopTable()
// Komple Deðiþtir :

bool CClientManager::InitializeShopTable()
{
	MYSQL_ROW	data;
	int		col;

	static const char * s_szQuery =
		"SELECT "
		"shop.vnum, "
#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		"shop.name, "
		"shop.npc_type, "
#endif
		"shop.npc_vnum, "
		"shop_item.item_vnum, "
		"shop_item.count "
#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		",shop_item.price "
		",shop_item.socket0 "
		",shop_item.socket1 "
		",shop_item.socket2 "
		",shop_item.attrtype0 "
		",shop_item.attrvalue0 "
		",shop_item.attrtype1 "
		",shop_item.attrvalue1 "
		",shop_item.attrtype2 "
		",shop_item.attrvalue2 "
		",shop_item.attrtype3 "
		",shop_item.attrvalue3 "
		",shop_item.attrtype4 "
		",shop_item.attrvalue4 "
		",shop_item.attrtype5 "
		",shop_item.attrvalue5 "
		",shop_item.attrtype6 "
		",shop_item.attrvalue6 "
#endif
		"FROM shop LEFT JOIN shop_item "
		"ON shop.vnum = shop_item.shop_vnum ORDER BY shop.vnum, shop_item.item_vnum";

	std::auto_ptr<SQLMsg> pkMsg2(CDBManager::instance().DirectQuery(s_szQuery));

	// shopÀÇ vnumÀº ÀÖ´Âµ¥ shop_item ÀÌ ¾øÀ»°æ¿ì... ½ÇÆÐ·Î Ã³¸®µÇ´Ï ÁÖÀÇ ¿ä¸Á.
	// °íÃ³¾ßÇÒºÎºÐ
	SQLResult * pRes2 = pkMsg2->Get();

	if (!pRes2->uiNumRows)
	{
		sys_err("InitializeShopTable : Table count is zero.");
		return false;
	}

	std::map<int, TShopTable *> map_shop;

	if (m_pShopTable)
	{
		delete [] (m_pShopTable);
		m_pShopTable = NULL;
	}

	TShopTable * shop_table = m_pShopTable;

	while ((data = mysql_fetch_row(pRes2->pSQLResult)))
	{
		col = 0;

		int iShopVnum = 0;
		str_to_number(iShopVnum, data[col++]);
#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		const char* name = data[col++];
		short price_type = 0;
		str_to_number(price_type, data[col++]);
#endif

		if (map_shop.end() == map_shop.find(iShopVnum))
		{
			shop_table = new TShopTable;
			memset(shop_table, 0, sizeof(TShopTable));
#ifdef ENABLE_2TH_SHOPEX_SYSTEM
			shop_table->price_type = price_type;
			strlcpy(shop_table->szShopName, name, sizeof(shop_table->szShopName));
#endif
			shop_table->dwVnum	= iShopVnum;

			map_shop[iShopVnum] = shop_table;
		}
		else
			shop_table = map_shop[iShopVnum];

		str_to_number(shop_table->dwNPCVnum, data[col++]);

		if (!data[col])	// ¾ÆÀÌÅÛÀÌ ÇÏ³ªµµ ¾øÀ¸¸é NULLÀÌ ¸®ÅÏ µÇ¹Ç·Î..
			continue;

		TShopItemTable * pItem = &shop_table->items[shop_table->byItemCount];

		str_to_number(pItem->vnum, data[col++]);
		str_to_number(pItem->count, data[col++]);
#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		str_to_number(pItem->price, data[col++]);
		str_to_number(pItem->alSockets[0], data[col++]);
		str_to_number(pItem->alSockets[1], data[col++]);
		str_to_number(pItem->alSockets[2], data[col++]);
		str_to_number(pItem->aAttr[0].bType, data[col++]);
		str_to_number(pItem->aAttr[0].sValue, data[col++]);
		str_to_number(pItem->aAttr[1].bType, data[col++]);
		str_to_number(pItem->aAttr[1].sValue, data[col++]);
		str_to_number(pItem->aAttr[2].bType, data[col++]);
		str_to_number(pItem->aAttr[2].sValue, data[col++]);
		str_to_number(pItem->aAttr[3].bType, data[col++]);
		str_to_number(pItem->aAttr[3].sValue, data[col++]);
		str_to_number(pItem->aAttr[4].bType, data[col++]);
		str_to_number(pItem->aAttr[4].sValue, data[col++]);
		str_to_number(pItem->aAttr[5].bType, data[col++]);
		str_to_number(pItem->aAttr[5].sValue, data[col++]);
		str_to_number(pItem->aAttr[6].bType, data[col++]);
		str_to_number(pItem->aAttr[6].sValue, data[col++]);
#endif

		++shop_table->byItemCount;
	}

	m_pShopTable = new TShopTable[map_shop.size()];
	m_iShopTableSize = map_shop.size();

	typeof(map_shop.begin()) it = map_shop.begin();

	int i = 0;

	while (it != map_shop.end())
	{
		thecore_memcpy((m_pShopTable + i), (it++)->second, sizeof(TShopTable));
		sys_log(0, "SHOP: #%d items: %d", (m_pShopTable + i)->dwVnum, (m_pShopTable + i)->byItemCount);
		++i;
	}

	return true;
}