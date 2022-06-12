// Arat :
// CShop::CShop()
// Ýçerisinde : m_pkPC(NULL)
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	,m_sPriceType(0), m_szShopName("")
#endif

// Arat :
// m_pGrid = M2_NEW CGrid(5, 9);
// Deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	m_pGrid = M2_NEW CGrid(10, 10);
#else
	m_pGrid = M2_NEW CGrid(5, 9);
#endif

// Arat :
// bool CShop::Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pTable)
// Komple Deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
bool CShop::Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pTable, short price_type, std::string shopname)
#else
bool CShop::Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pTable)
#endif
{
	/*
	   if (NULL == CMobManager::instance().Get(dwNPCVnum))
	   {
	   sys_err("No such a npc by vnum %d", dwNPCVnum);
	   return false;
	   }
	 */
	sys_log(0, "SHOP #%d (Shopkeeper %d)", dwVnum, dwNPCVnum);

	m_dwVnum = dwVnum;
	m_dwNPCVnum = dwNPCVnum;
#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	m_sPriceType = price_type;
	m_szShopName = shopname;
#endif

	BYTE bItemCount;

	for (bItemCount = 0; bItemCount < SHOP_HOST_ITEM_MAX_NUM; ++bItemCount)
		if (0 == (pTable + bItemCount)->vnum)
			break;

	SetShopItems(pTable, bItemCount);
	return true;
}

// Arat :
// void CShop::SetShopItems(TShopItemTable * pTable, BYTE bItemCount)
// Ýçerisinde : item.vnum = pTable->vnum;
// else içerisindeki bloðu deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
			item.vnum = pTable->vnum;
			item.count = pTable->count;
			item.price = pTable->price;
			item.alSockets[0] = pTable->alSockets[0];
			item.alSockets[1] = pTable->alSockets[1];
			item.alSockets[2] = pTable->alSockets[2];
			item.aAttr[0].bType = pTable->aAttr[0].bType;
			item.aAttr[0].sValue = pTable->aAttr[0].sValue;
			item.aAttr[1].bType = pTable->aAttr[1].bType;
			item.aAttr[1].sValue = pTable->aAttr[1].sValue;
			item.aAttr[2].bType = pTable->aAttr[2].bType;
			item.aAttr[2].sValue = pTable->aAttr[2].sValue;
			item.aAttr[3].bType = pTable->aAttr[3].bType;
			item.aAttr[3].sValue = pTable->aAttr[3].sValue;
			item.aAttr[4].bType = pTable->aAttr[4].bType;
			item.aAttr[4].sValue = pTable->aAttr[4].sValue;
			item.aAttr[5].bType = pTable->aAttr[5].bType;
			item.aAttr[5].sValue = pTable->aAttr[5].sValue;
			item.aAttr[6].bType = pTable->aAttr[6].bType;
			item.aAttr[6].sValue = pTable->aAttr[6].sValue;
#else
			item.vnum = pTable->vnum;
			item.count = pTable->count;

			if (IS_SET(item_table->dwFlags, ITEM_FLAG_COUNT_PER_1GOLD))
			{
				if (item_table->dwGold == 0)
					item.price = item.count;
				else
					item.price = item.count / item_table->dwGold;
			}
			else
				item.price = item_table->dwGold * item.count;
#endif

// Arat :
// int CShop::Buy(LPCHARACTER ch, BYTE pos)
// Ýçerisinde : if (ch->GetGold() < (int) dwPrice)
// Deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	if (m_pkPC)
	{
		if (ch->GetGold() < (int) dwPrice)
		{
			sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), dwPrice);
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
		}
	}
	else
	{
		if (m_sPriceType == 0)
		{
			if (ch->GetGold() < (int) dwPrice)
			{
				sys_log(1, "Shop::Buy : Not enough money : %s has %lld, price %lld", ch->GetName(), ch->GetGold(), dwPrice);
				return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
			}			
		}
		else if (m_sPriceType == 1)
		{
			if (ch->GetDragonCoin() < (int) dwPrice)
			{
				sys_log(1, "Shop::Buy : Not enough dc : %s has %d, price %d", ch->GetName(), ch->GetDragonCoin(), dwPrice);
				return SHOP_SUBHEADER_GC_NOT_ENOUGH_DRAGON_COIN;
			}
		}
		else if (m_sPriceType == 2)
		{
			if (ch->GetDragonMark() < (int) dwPrice)
			{
				sys_log(1, "Shop::Buy : Not enough dm : %s has %d, price %d", ch->GetName(), ch->GetDragonMark(), dwPrice);
				return SHOP_SUBHEADER_GC_NOT_ENOUGH_DRAGON_MARK;
			}
		}
		else if (m_sPriceType == 3)
		{
			if (ch->GetAlignment() < (int) dwPrice*10)
			{
				sys_log(1, "Shop::Buy : Not enough alignment : %s has %d, price %d", ch->GetName(), ch->GetAlignment(), dwPrice*10);
				return SHOP_SUBHEADER_GC_NOT_ENOUGH_ALIGNMENT;
			}
		}		
	}
#else
	if (ch->GetGold() < (int) dwPrice)
	{
		sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), dwPrice);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}
#endif

// Arat :
// int CShop::Buy(LPCHARACTER ch, BYTE pos)
// Ýçerisinde : ch->PointChange(POINT_GOLD, -dwPrice, false);
// Deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	if (m_pkPC)
	{
		ch->PointChange(POINT_GOLD, -dwPrice, false);
	}
	else
	{
		if (m_sPriceType == 0)
		{
			ch->PointChange(POINT_GOLD, -dwPrice, false);
		}
		else if (m_sPriceType == 1)
		{
			ch->SetDragonCoin(ch->GetDragonCoin()-dwPrice);
			if (item->GetVnum() != 80014 || item->GetVnum() != 80015 || item->GetVnum() != 80016 || item->GetVnum() != 80017)
				ch->SetDragonMark(ch->GetDragonMark()+dwPrice);
		}
		else if (m_sPriceType == 2)
		{
			ch->SetDragonMark(ch->GetDragonMark()-dwPrice);
		}
		else if (m_sPriceType == 3)
		{
			ch->UpdateAlignment(-dwPrice*10);
		}
	}
#else
	ch->PointChange(POINT_GOLD, -dwPrice, false);
#endif

// Arat :
// int CShop::Buy(LPCHARACTER ch, BYTE pos)
// Ýçerisinde : item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
// ( 2. Arayýþta ) Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		if (r_item.alSockets[0] > 0)
			item->SetSocket(0, r_item.alSockets[0]);
		if (r_item.alSockets[1] > 0)
			item->SetSocket(1, r_item.alSockets[1]);
		if (r_item.alSockets[2] > 0)
			item->SetSocket(2, r_item.alSockets[2]);
		if (r_item.aAttr[0].bType > 0 && r_item.aAttr[0].sValue > 0)
			item->SetForceAttribute(0, r_item.aAttr[0].bType, r_item.aAttr[0].sValue);
		if (r_item.aAttr[1].bType > 0 && r_item.aAttr[1].sValue > 0)
			item->SetForceAttribute(1, r_item.aAttr[1].bType, r_item.aAttr[1].sValue);
		if (r_item.aAttr[2].bType > 0 && r_item.aAttr[2].sValue > 0)
			item->SetForceAttribute(2, r_item.aAttr[2].bType, r_item.aAttr[2].sValue);
		if (r_item.aAttr[3].bType > 0 && r_item.aAttr[3].sValue > 0)
			item->SetForceAttribute(3, r_item.aAttr[3].bType, r_item.aAttr[3].sValue);
		if (r_item.aAttr[4].bType > 0 && r_item.aAttr[4].sValue > 0)
			item->SetForceAttribute(4, r_item.aAttr[4].bType, r_item.aAttr[4].sValue);
		if (r_item.aAttr[5].bType > 0 && r_item.aAttr[5].sValue > 0)
			item->SetForceAttribute(5, r_item.aAttr[5].bType, r_item.aAttr[5].sValue);
		if (r_item.aAttr[6].bType > 0 && r_item.aAttr[6].sValue > 0)
			item->SetForceAttribute(6, r_item.aAttr[6].bType, r_item.aAttr[6].sValue);
#endif

// Arat :
// bool CShop::AddGuest(LPCHARACTER ch, DWORD owner_vid, bool bOtherEmpire)
// Ýçerisinde : pack2.owner_vid = owner_vid;
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	if (IsPCShop() || HasOwner())
	{
		strlcpy(pack2.shop_name, m_pkPC->GetName(), SHOP_TAB_NAME_MAX);
		pack2.price_type = 0;
	}
	else
	{
		pack2.price_type = m_sPriceType;
		strlcpy(pack2.shop_name, m_szShopName.c_str(), SHOP_TAB_NAME_MAX);
	}
#endif

// Arat :
// bool CShop::AddGuest(LPCHARACTER ch, DWORD owner_vid, bool bOtherEmpire)
// Ýçerisinde : thecore_memcpy(pack2.items[i].aAttr, item.pkItem->GetAttributes(), sizeof(pack2.items[i].aAttr));
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		else if (!m_pkPC)
		{
			thecore_memcpy(pack2.items[i].alSockets, item.alSockets, sizeof(pack2.items[i].alSockets));
			thecore_memcpy(pack2.items[i].aAttr, item.aAttr, sizeof(pack2.items[i].aAttr));
		}
#endif

// Arat :
// void CShop::BroadcastUpdateItem(BYTE pos)
// Ýçerisinde : memset(pack2.item.alSockets, 0, sizeof(pack2.item.alSockets));
// {} içerisini deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		{
			thecore_memcpy(pack2.item.alSockets, m_itemVector[pos].alSockets, sizeof(pack2.item.alSockets));
			thecore_memcpy(pack2.item.aAttr, m_itemVector[pos].aAttr, sizeof(pack2.item.aAttr));
		}
#else
		{
			memset(pack2.item.alSockets, 0, sizeof(pack2.item.alSockets));
			memset(pack2.item.aAttr, 0, sizeof(pack2.item.aAttr));
		}
#endif	

