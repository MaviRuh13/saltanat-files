/*           AÇILIR: char.cpp       */

/** 

Aratýlýr:

**/

	if (GetMyShop())	// ÀÌ¹Ì ¼¥ÀÌ ¿­·Á ÀÖÀ¸¸é ´Ý´Â´Ù.
	{
		CloseMyShop();
		return;
	}

altýna eklenir 
#ifdef KAYA_MULTI_PRICE
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

aratýlýr


	if (!pkChrCauser)
	{
		sys_err("OnClick %s by NULL", GetName());
		return;
	}



/*

Altýna Eklenir:

*/
#ifdef KAYA_MULTI_PRICE

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
		int slot3 = 0;
		int slot4 = 0;
		int slot5 = 0;
		int slot6 = 0;
		int slot7 = 0;
		int fiyat = 0;
		int fiyat2 = 0;
		int fiyat3 = 0;
		int fiyat4 = 0;
		int fiyat5 = 0;
		int fiyat6 = 0;
		int fiyat7 = 0;
		char buf[256];
		char buf2[256];
		char buf3[256];
		char buf4[256];
		char buf5[256];
		char buf6[256];
		char buf7[256];
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
		while (slot3 < 100)
		{
			snprintf(buf3, sizeof(buf3), "pazar.pazaryesilslot%d", slot3);
			fiyat3 = GetQuestFlag(buf3);
			pkChrCauser->ChatPacket(CHAT_TYPE_COMMAND, "yesilfytkac %d %d",slot3,fiyat3);
			slot3++;
		}
		while (slot4 < 100)
		{
			snprintf(buf4, sizeof(buf4), "pazar.pazarkirmiziotslot%d", slot4);
			fiyat4 = GetQuestFlag(buf4);
			pkChrCauser->ChatPacket(CHAT_TYPE_COMMAND, "kirmizifytkac %d %d",slot4,fiyat4);
			slot4++;
		}
		while (slot5 < 100)
		{
			snprintf(buf5, sizeof(buf5), "pazar.pazarmaviotslot%d", slot5);
			fiyat5 = GetQuestFlag(buf5);
			pkChrCauser->ChatPacket(CHAT_TYPE_COMMAND, "mavifytkac %d %d",slot5,fiyat5);
			slot5++;
		}
		while (slot6 < 100)
		{
			snprintf(buf6, sizeof(buf6), "pazar.pazarmorotslot%d", slot6);
			fiyat6 = GetQuestFlag(buf6);
			pkChrCauser->ChatPacket(CHAT_TYPE_COMMAND, "morfytkac %d %d",slot6,fiyat6);
			slot6++;
		}
		while (slot7 < 100)
		{
			snprintf(buf7, sizeof(buf7), "pazar.pazaruhtasislot%d", slot7);
			fiyat7 = GetQuestFlag(buf7);
			pkChrCauser->ChatPacket(CHAT_TYPE_COMMAND, "ruhtasfytkac %d %d",slot7,fiyat7);
			slot7++;
		}
	}
#endif