///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/*           AÇILIR: cmd_general.cpp       */


/**

ARATILIR: 

**/

ACMD(do_guildskillup)

/*

ÜSTÜNE EKLENIR:

*/
#ifdef KAYA_MULTI_PRICE
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
ACMD(do_yesilotilesat)
{
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	int slot3 = 0;
	int fiyat3 = 0;

	if (*arg1)
		str_to_number(slot3, arg1);
	
	if (*arg2)
		str_to_number(fiyat3, arg2);
	char buf3[256];  
	snprintf(buf3, sizeof(buf3), "pazar.pazaryesilslot%d", slot3);
	ch->SetQuestFlag(buf3,fiyat3);
}
ACMD(do_kirmiziotilesat)
{
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	int slot4 = 0;
	int fiyat4 = 0;

	if (*arg1)
		str_to_number(slot4, arg1);
	
	if (*arg2)
		str_to_number(fiyat4, arg2);
	char buf4[256];  
	snprintf(buf4, sizeof(buf4), "pazar.pazarkirmiziotslot%d", slot4);
	ch->SetQuestFlag(buf4,fiyat4);
}
ACMD(do_maviotilesat)
{
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	int slot5 = 0;
	int fiyat5 = 0;

	if (*arg1)
		str_to_number(slot5, arg1);
	
	if (*arg2)
		str_to_number(fiyat5, arg2);
	char buf5[256];  
	snprintf(buf5, sizeof(buf5), "pazar.pazarmaviotslot%d", slot5);
	ch->SetQuestFlag(buf5,fiyat5);
}
ACMD(do_morotilesat)
{
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	int slot6 = 0;
	int fiyat6 = 0;

	if (*arg1)
		str_to_number(slot6, arg1);
	
	if (*arg2)
		str_to_number(fiyat6, arg2);
	char buf6[256];  
	snprintf(buf6, sizeof(buf6), "pazar.pazarmorotslot%d", slot6);
	ch->SetQuestFlag(buf6,fiyat6);
}
ACMD(do_ruhtasilesat)
{
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	int slot7 = 0;
	int fiyat7 = 0;

	if (*arg1)
		str_to_number(slot7, arg1);
	
	if (*arg2)
		str_to_number(fiyat7, arg2);
	char buf7[256];  
	snprintf(buf7, sizeof(buf7), "pazar.pazaruhtasislot%d", slot7);
	ch->SetQuestFlag(buf7,fiyat7);
}
#endif