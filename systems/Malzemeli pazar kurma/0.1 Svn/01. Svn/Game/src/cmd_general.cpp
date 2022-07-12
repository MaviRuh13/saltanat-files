// Arat
ACMD(do_guildskillup)

// Ustune Ekle
#ifdef MAVIRUH_MULTI_PRICE
ACMD(do_suileesyasa)
{
	ch->ChatPacket(CHAT_TYPE_INFO, "Bu duzenleme mevcut degil.");
}
ACMD(do_suileesyasat)
{
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	int slot;
	int fiyat;

	if (*arg1)
		str_to_number(slot, arg1);

	if (*arg2)
		str_to_number(fiyat, arg2);
	char buf[256];  
	snprintf(buf, sizeof(buf), "pazar.pazarsuslot%d", slot);
	ch->SetQuestFlag(buf,fiyat);
}

ACMD(do_barileesyasa)
{
	ch->ChatPacket(CHAT_TYPE_INFO, "Bu duzenleme mevcut degil.");
}
ACMD(do_barileesyasat)
{
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	int slot2 = 0;
	int fiyat2 = 0;

	if (*arg1)
		str_to_number(slot2, arg1);
	
	if (*arg2)
		str_to_number(fiyat2, arg2);
	char buf2[256];  
	snprintf(buf2, sizeof(buf2), "pazar.pazarbarslot%d", slot2);
	ch->SetQuestFlag(buf2,fiyat2);
}
#endif