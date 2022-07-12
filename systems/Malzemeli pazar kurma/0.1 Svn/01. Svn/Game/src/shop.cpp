// Arat
int CShop::Buy(LPCHARACTER ch, BYTE pos)

// Komple Degistir
int CShop::Buy(LPCHARACTER ch, BYTE pos)
{
	if (pos >= m_itemVector.size())
	{
		sys_log(0, "Shop::Buy : invalid position %d : %s", pos, ch->GetName());
		return SHOP_SUBHEADER_GC_INVALID_POS;
	}

	sys_log(0, "Shop::Buy : name %s pos %d", ch->GetName(), pos);

	GuestMapType::iterator it = m_map_guest.find(ch);

	if (it == m_map_guest.end())
		return SHOP_SUBHEADER_GC_END;

	SHOP_ITEM& r_item = m_itemVector[pos];

//#ifdef YANG0_FIX
	if (r_item.price < 0)
	{
		LogManager::instance().HackLog("SHOP_BUY_GOLD_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}
//	#endif 
//#ifdef ENABLE_PAZAR_IKIKISIALMA_FIX
	LPITEM pkSelectedItem = ITEM_MANAGER::instance().Find(r_item.itemid);

	if (IsPCShop())
	{
		if (!pkSelectedItem)
		{
			sys_log(0, "Shop::Buy : Critical: This user seems to be a hacker : invalid pcshop item : BuyerPID:%d SellerPID:%d",
					ch->GetPlayerID(),
					m_pkPC->GetPlayerID());

			return SHOP_SUBHEADER_GC_SOLD_OUT; // @fixme132 false to SHOP_SUBHEADER_GC_SOLD_OUT
		}

		if ((pkSelectedItem->GetOwner() != m_pkPC))
		{
			sys_log(0, "Shop::Buy : Critical: This user seems to be a hacker : invalid pcshop item : BuyerPID:%d SellerPID:%d",
					ch->GetPlayerID(),
					m_pkPC->GetPlayerID());

			return SHOP_SUBHEADER_GC_SOLD_OUT; // @fixme132 false to SHOP_SUBHEADER_GC_SOLD_OUT
		}
	}
//#endif

	DWORD dwPrice = r_item.price;

	if (it->second)	// if other empire, price is triple
		dwPrice *= 3;

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

	LPITEM item;

	if (m_pkPC) // ??? ???? ?? ??? ?? ???? ?????? ??.
		item = r_item.pkItem;
	else
		item = ITEM_MANAGER::instance().CreateItem(r_item.vnum, r_item.count);

	if (!item)
		return SHOP_SUBHEADER_GC_SOLD_OUT;
#ifdef MAVIRUH_MULTI_PRICE
	int suprice = 0;
	int barprice = 0;

	if (ch->GetShopOwner()->IsPC() && ch->GetShopOwner())
	{
		//sys_err("267.satir");
		char bufff[256];
		char bufff2[256];
		snprintf(bufff, sizeof(bufff), "pazar.pazarsuslot%d", pos);
		snprintf(bufff2, sizeof(bufff2), "pazar.pazarbarslot%d", pos);
			

		//sys_err("272.satir");
		suprice = m_pkPC->GetQuestFlag(bufff);
		barprice = m_pkPC->GetQuestFlag(bufff2);
		//sys_err("275.satir");
		if (ch->CountSpecifyItem(90005) < suprice && ch->GetShopOwner()->IsPC() == true)
		{
			ch->ChatPacket(CHAT_TYPE_COMMAND, "sutasiyok");
			return SHOP_SUBHEADER_GC_END;
		}
		//sys_err("281.satir");

		if (ch->CountSpecifyItem(80007) < barprice && ch->GetShopOwner()->IsPC() == true)
		{
			ch->ChatPacket(CHAT_TYPE_COMMAND, "baryok");
			return SHOP_SUBHEADER_GC_END;
		}
	}
#endif
	int iEmptyPos;
	if (item->IsDragonSoul())
	{
		iEmptyPos = ch->GetEmptyDragonSoulInventory(item);
	}
	else
	{
		iEmptyPos = ch->GetEmptyInventory(item->GetSize());
	}

	if (iEmptyPos < 0)
	{
		if (m_pkPC)
		{
			sys_log(1, "Shop::Buy at PC Shop : Inventory full : %s size %d", ch->GetName(), item->GetSize());
			return SHOP_SUBHEADER_GC_INVENTORY_FULL;
		}
		else
		{
			sys_log(1, "Shop::Buy : Inventory full : %s size %d", ch->GetName(), item->GetSize());
			M2_DESTROY_ITEM(item);
			return SHOP_SUBHEADER_GC_INVENTORY_FULL;
		}
	}

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
	
	if (ch->GetShopOwner()->IsPC() == true && ch->GetShopOwner())
	{
#ifdef MAVIRUH_MULTI_PRICE
		if (ch->IsPC() == true && ch != m_pkPC)
		{
			ch->RemoveSpecifyItem(90005,suprice);
		}
		if (ch->IsPC() == true && ch != m_pkPC)
		{
			ch->RemoveSpecifyItem(80007,barprice);
		}
		int sumiktar = 0;
		int barmiktar = 0;
		//sys_err("364.satir");
		if (ch != m_pkPC)
		{
			while (sumiktar < suprice && ch->GetShopOwner()->IsPC() == true)
			{
				//m_pkPC->AutoGiveItem(80007,1);
				m_pkPC->AutoGiveItem(90005,1,0,false);
				sumiktar++;
			}
		}
		if (ch != m_pkPC)
		{
			while (barmiktar < barprice && ch->GetShopOwner()->IsPC() == true)
			{
				//m_pkPC->AutoGiveItem(50513,1);
				m_pkPC->AutoGiveItem(80007,1,0,false);
				barmiktar++;
			}
		}
	}
#endif
	//?? ??
	DWORD dwTax = 0;
	int iVal = 0;

	if (LC_IsYMIR() ||  LC_IsKorea())
	{
		if (0 < (iVal = quest::CQuestManager::instance().GetEventFlag("trade_tax")))
		{
			if (iVal > 100)
				iVal = 100;

			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;
		}
		else
		{
			iVal = 3;
			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;			
		}
	}
	else
	{
		iVal = quest::CQuestManager::instance().GetEventFlag("personal_shop");

		if (0 < iVal)
		{
			if (iVal > 100)
				iVal = 100;

			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;
		}
		else
		{
			iVal = 0;
			dwTax = 0;
		}
	}

	// ???? ??? ?? 5%
	// if (!m_pkPC) 
	// {
		// CMonarch::instance().SendtoDBAddMoney(dwTax, ch->GetEmpire(), ch);
	// }

	// ?? ??? : ?? ??
	if (m_pkPC)
	{
		m_pkPC->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 255);
			char buf[512];

			if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
			{
				snprintf(buf, sizeof(buf), "%s FROM: %u TO: %u PRICE: %u", item->GetName(), ch->GetPlayerID(), m_pkPC->GetPlayerID(), dwPrice);
				LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), SHOP_BUY, buf);
				LogManager::instance().GoldBarLog(m_pkPC->GetPlayerID(), item->GetID(), SHOP_SELL, buf);
			}
			
			item->RemoveFromCharacter();
			if (item->IsDragonSoul())
				item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
			else
				item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			ITEM_MANAGER::instance().FlushDelayedSave(item);
			

			snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", item->GetName(), m_pkPC->GetPlayerID(), m_pkPC->GetName(), dwPrice, item->GetCount());
			LogManager::instance().ItemLog(ch, item, "SHOP_BUY", buf);

			snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", item->GetName(), ch->GetPlayerID(), ch->GetName(), dwPrice, item->GetCount());
			LogManager::instance().ItemLog(m_pkPC, item, "SHOP_SELL", buf);

		r_item.pkItem = NULL;
		BroadcastUpdateItem(pos);

		m_pkPC->PointChange(POINT_GOLD, dwPrice, false);

		if (iVal > 0)
			m_pkPC->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("????? %d %% ? ???? ??????"), iVal);

	}
	else
	{
		if (item->IsDragonSoul())
			item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
		else
			item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
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
		ITEM_MANAGER::instance().FlushDelayedSave(item);
		LogManager::instance().ItemLog(ch, item, "BUY", item->GetName());

		if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
		{
			LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), PERSONAL_SHOP_BUY, "");
		}

		DBManager::instance().SendMoneyLog(MONEY_LOG_SHOP, item->GetVnum(), -dwPrice);
	}

	if (item)
		sys_log(0, "SHOP: BUY: name %s %s(x %d):%u price %u", ch->GetName(), item->GetName(), item->GetCount(), item->GetID(), dwPrice);

	ch->Save();

	return (SHOP_SUBHEADER_GC_OK);
}