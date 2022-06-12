///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/*           AÇILIR: shop.cpp       */

/**

ARATILIR: 

**/

int CShop::Buy(LPCHARACTER ch, BYTE pos)

/*

Fonksiyon komple deðiþtirilir:

*/

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

	if (ch->GetGold() < (int) dwPrice)
	{
		sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), dwPrice);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}

	LPITEM item;

	if (m_pkPC) // ??? ???? ?? ??? ?? ???? ?????? ??.
		item = r_item.pkItem;
	else
		item = ITEM_MANAGER::instance().CreateItem(r_item.vnum, r_item.count);

	if (!item)
		return SHOP_SUBHEADER_GC_SOLD_OUT;
#ifdef KAYA_MULTI_PRICE
	int suprice = 0;
	int wonprice = 0;
	int yesilotprices = 0;
	int kirmiziotprices = 0;
	int maviotprices = 0;
	int morotprices = 0;
	int ruhtasiprices = 0;

	if (ch->GetShopOwner()->IsPC() && ch->GetShopOwner())
	{
		//sys_err("267.satir");
		char bufff[256];
		char bufff2[256];
		char bufff3[256];
		char bufff4[256];
		char bufff5[256];
		char bufff6[256];
		char bufff7[256];
		snprintf(bufff, sizeof(bufff), "pazar.pazarsuslot%d", pos);
		snprintf(bufff2, sizeof(bufff2), "pazar.pazarbarslot%d", pos);
		snprintf(bufff3, sizeof(bufff2), "pazar.pazaryesilslot%d", pos);
		snprintf(bufff4, sizeof(bufff2), "pazar.pazarkirmiziotslot%d", pos);
		snprintf(bufff5, sizeof(bufff2), "pazar.pazarmaviotslot%d", pos);
		snprintf(bufff6, sizeof(bufff2), "pazar.pazarmorotslot%d", pos);
		snprintf(bufff7, sizeof(bufff2), "pazar.pazaruhtasislot%d", pos);
			

		//sys_err("272.satir");
		suprice = m_pkPC->GetQuestFlag(bufff);
		wonprice = m_pkPC->GetQuestFlag(bufff2);
		yesilotprices = m_pkPC->GetQuestFlag(bufff3);
		kirmiziotprices = m_pkPC->GetQuestFlag(bufff4);
		maviotprices = m_pkPC->GetQuestFlag(bufff5);
		morotprices = m_pkPC->GetQuestFlag(bufff6);
		ruhtasiprices = m_pkPC->GetQuestFlag(bufff7);
		//sys_err("275.satir");
		if (ch->CountSpecifyItem(27991) < suprice && ch->GetShopOwner()->IsPC() == true)
		{
			ch->ChatPacket(CHAT_TYPE_COMMAND, "sutasiyok");
			return SHOP_SUBHEADER_GC_END;
		}
		//sys_err("281.satir");

		if (ch->CountSpecifyItem(80007) < wonprice && ch->GetShopOwner()->IsPC() == true)
		{
			ch->ChatPacket(CHAT_TYPE_COMMAND, "wonyok");
			return SHOP_SUBHEADER_GC_END;
		}
		if (ch->CountSpecifyItem(70253) < yesilotprices && ch->GetShopOwner()->IsPC() == true)
		{
			ch->ChatPacket(CHAT_TYPE_COMMAND, "yesilyok");
			return SHOP_SUBHEADER_GC_END;
		}
		if (ch->CountSpecifyItem(70251) < kirmiziotprices && ch->GetShopOwner()->IsPC() == true)
		{
			ch->ChatPacket(CHAT_TYPE_COMMAND, "kirmiziyok");
			return SHOP_SUBHEADER_GC_END;
		}
		if (ch->CountSpecifyItem(70252) < maviotprices && ch->GetShopOwner()->IsPC() == true)
		{
			ch->ChatPacket(CHAT_TYPE_COMMAND, "maviyok");
			return SHOP_SUBHEADER_GC_END;
		}
		if (ch->CountSpecifyItem(70254) < morotprices && ch->GetShopOwner()->IsPC() == true)
		{
			ch->ChatPacket(CHAT_TYPE_COMMAND, "moryok");
			return SHOP_SUBHEADER_GC_END;
		}
		if (ch->CountSpecifyItem(50513) < ruhtasiprices && ch->GetShopOwner()->IsPC() == true)
		{
			ch->ChatPacket(CHAT_TYPE_COMMAND, "ruhtasiyok");
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

	ch->PointChange(POINT_GOLD, -dwPrice, false);
	
	if (ch->GetShopOwner()->IsPC() == true && ch->GetShopOwner())
	{
#ifdef KAYA_MULTI_PRICE
		if (ch->IsPC() == true && ch != m_pkPC)
		{
			ch->RemoveSpecifyItem(27991,suprice);
		}
		if (ch->IsPC() == true && ch != m_pkPC)
		{
			ch->RemoveSpecifyItem(80007,wonprice);
		}
		if (ch->IsPC() == true && ch != m_pkPC)
		{
			ch->RemoveSpecifyItem(70253,yesilotprices);
		}
		if (ch->IsPC() == true && ch != m_pkPC)
		{
			ch->RemoveSpecifyItem(70251,kirmiziotprices);
		}
		if (ch->IsPC() == true && ch != m_pkPC)
		{
			ch->RemoveSpecifyItem(70252,maviotprices);
		}
		if (ch->IsPC() == true && ch != m_pkPC)
		{
			ch->RemoveSpecifyItem(70254,morotprices);
		}
		if (ch->IsPC() == true && ch != m_pkPC)
		{
			ch->RemoveSpecifyItem(50513,ruhtasiprices);
		}
		int sumiktar = 0;
		int barmiktar = 0;
		int yesilmiktar = 0;
		int kirmizimiktar = 0;
		int mavimiktar = 0;
		int mormiktar = 0;
		int ruhtasmiktar = 0;
		//sys_err("364.satir");
		if (ch != m_pkPC)
		{
			while (sumiktar < suprice && ch->GetShopOwner()->IsPC() == true)
			{
				//m_pkPC->AutoGiveItem(80007,1);
				m_pkPC->AutoGiveItem(27991,1,0,false);
				sumiktar++;
			}
		}
		if (ch != m_pkPC)
		{
			while (barmiktar < wonprice && ch->GetShopOwner()->IsPC() == true)
			{
				//m_pkPC->AutoGiveItem(50513,1);
				m_pkPC->AutoGiveItem(80007,1,0,false);
				barmiktar++;
			}
		}
		if (ch != m_pkPC)
		{
			while (yesilmiktar < yesilotprices && ch->GetShopOwner()->IsPC() == true)
			{
				//m_pkPC->AutoGiveItem(50513,1);
				m_pkPC->AutoGiveItem(70253,1,0,false);
				yesilmiktar++;
			}
		}
		if (ch != m_pkPC)
		{
			while (kirmizimiktar < kirmiziotprices && ch->GetShopOwner()->IsPC() == true)
			{
				//m_pkPC->AutoGiveItem(50513,1);
				m_pkPC->AutoGiveItem(70251,1,0,false);
				kirmizimiktar++;
			}
		}
		if (ch != m_pkPC)
		{
			while (mavimiktar < maviotprices && ch->GetShopOwner()->IsPC() == true)
			{
				//m_pkPC->AutoGiveItem(50513,1);
				m_pkPC->AutoGiveItem(70252,1,0,false);
				mavimiktar++;
			}
		}
		if (ch != m_pkPC)
		{
			while (mormiktar < morotprices && ch->GetShopOwner()->IsPC() == true)
			{
				//m_pkPC->AutoGiveItem(50513,1);
				m_pkPC->AutoGiveItem(70254,1,0,false);
				mormiktar++;
			}
		}
		if (ch != m_pkPC)
		{
			while (ruhtasmiktar < ruhtasiprices && ch->GetShopOwner()->IsPC() == true)
			{
				//m_pkPC->AutoGiveItem(50513,1);
				m_pkPC->AutoGiveItem(50513,1,0,false);
				ruhtasmiktar++;
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
	if (!m_pkPC) 
	{
		CMonarch::instance().SendtoDBAddMoney(dwTax, ch->GetEmpire(), ch);
	}

	// ?? ??? : ?? ??
	if (m_pkPC)
	{
		m_pkPC->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 255);

		if (item->GetVnum() == 90008 || item->GetVnum() == 90009) // VCARD
		{
			VCardUse(m_pkPC, ch, item);
			item = NULL;
		}
		else
		{
			char buf[512];

			if (item->GetVnum() >= 27991 && item->GetVnum() <= 80007 && item->GetVnum() <= 70253 && item->GetVnum() <= 70251 && item->GetVnum() <= 70252 && item->GetVnum() <= 70254 && item->GetVnum() <= 50513)
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
		}

		r_item.pkItem = NULL;
		BroadcastUpdateItem(pos);

		m_pkPC->PointChange(POINT_GOLD, dwPrice, false);

		if (iVal > 0)
			m_pkPC->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("????? %d %% ? ???? ??????"), iVal);

		CMonarch::instance().SendtoDBAddMoney(dwTax, m_pkPC->GetEmpire(), m_pkPC);
	}
	else
	{
		if (item->IsDragonSoul())
			item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
		else
			item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		ITEM_MANAGER::instance().FlushDelayedSave(item);
		LogManager::instance().ItemLog(ch, item, "BUY", item->GetName());

		if (item->GetVnum() >= 27991 && item->GetVnum() <= 80007 && item->GetVnum() <= 70253 && item->GetVnum() <= 70251 && item->GetVnum() <= 70252 && item->GetVnum() <= 70254 && item->GetVnum() <= 50513)
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