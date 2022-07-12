// Arat
	if (GetMyShop())	// 이미 샵이 열려 있으면 닫는다.
	{
		CloseMyShop();
		return;
	}

// Altina Ekle
#ifdef MAVIRUH_MULTI_PRICE
	int bosslot = 0;
	int gerekenbosluk = 100;
	for (int iCell = 0; iCell < INVENTORY_MAX_NUM; iCell++)
	{
	LPITEM item = GetInventoryItem(iCell);
	if (!item)
	bosslot += 1;
	continue;
	}
	if (bosslot < gerekenbosluk)
	{
	ChatPacket(CHAT_TYPE_INFO, "Pazar kurmak icin yeterli bos slota sahip degilsin. Gereken Slot : %d Sahip Oldugun : %d", gerekenbosluk, bosslot);
	return;
	}
#endif

// Arat
	if (!pkChrCauser)
	{
		sys_err("OnClick %s by NULL", GetName());
		return;
	}

// Altina Ekle
#ifdef MAVIRUH_MULTI_PRICE
	if (IsPC() && GetMyShop())
		pkChrCauser->ChatPacket(CHAT_TYPE_COMMAND, "pazarnasil 1");
	else
		pkChrCauser->ChatPacket(CHAT_TYPE_COMMAND, "pazarnasil 0");

	if (IsPC() && GetMyShop())
		pkChrCauser->SetQuestFlag("shop.shoptarz",1);
	else
		pkChrCauser->SetQuestFlag("shop.shoptarz",0);

	if (IsPC() && GetMyShop())
	{
		int slot = 0;
		int slot2 = 0;
		int fiyat = 0;
		int fiyat2 = 0;
		char buf[256];
		char buf2[256];
		while (slot < 100)
		{
			snprintf(buf, sizeof(buf), "pazar.pazarsuslot%d", slot);
			fiyat = GetQuestFlag(buf);
			pkChrCauser->ChatPacket(CHAT_TYPE_COMMAND, "sufiyatkac %d %d",slot,fiyat);
			slot++;
		}
		while (slot2 < 100)
		{
			snprintf(buf2, sizeof(buf2), "pazar.pazarbarslot%d", slot2);
			fiyat2 = GetQuestFlag(buf2);
			pkChrCauser->ChatPacket(CHAT_TYPE_COMMAND, "barfiyatkac %d %d",slot2,fiyat2);
			slot2++;
		}
	}
#endif