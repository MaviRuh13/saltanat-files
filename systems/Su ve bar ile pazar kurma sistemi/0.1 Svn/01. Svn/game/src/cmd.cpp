// Arat
struct command_info cmd_info[] =

// Ustune Ekle
#ifdef MAVIRUH_MULTI_PRICE
ACMD(do_suileesyasa);
ACMD(do_suileesyasat);
ACMD(do_barileesyasa);
ACMD(do_barileesyasat);
#endif

// Arat
	{ "\n",		NULL,			0,			POS_DEAD,	GM_IMPLEMENTOR	}

// Ustune Ekle
#ifdef MAVIRUH_MULTI_PRICE
	{ "suileesyasa",		do_suileesyasa,		0,			POS_DEAD,	GM_PLAYER	},
	{ "suileesyasat",		do_suileesyasat,		0,			POS_DEAD,	GM_PLAYER	},
	{ "barileesyasa",		do_barileesyasa,		0,			POS_DEAD,	GM_PLAYER	},
	{ "barileesyasat",		do_barileesyasat,		0,			POS_DEAD,	GM_PLAYER	},
#endif
