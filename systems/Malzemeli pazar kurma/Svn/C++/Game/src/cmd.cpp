///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/*           AÇILIR: cmd.cpp       */

/**

ARATILIR: 

**/

ACMD(do_kill);

/*

ALTINA EKLENIR:

*/
#ifdef KAYA_MULTI_PRICE

ACMD(do_suileesyasa);
ACMD(do_suileesyasat);
ACMD(do_barileesyasa);
ACMD(do_barileesyasat);
ACMD(do_yesilotilesat);
ACMD(do_kirmiziotilesat);
ACMD(do_maviotilesat);
ACMD(do_morotilesat);
ACMD(do_ruhtasilesat);
#endif
/**

ARATILIR: 

**/

{ "kill",		do_kill,		0,			POS_DEAD,	GM_HIGH_WIZARD	},

/*

ALTINA EKLENIR:

*/
#ifdef KAYA_MULTI_PRICE
	{ "suileesyasa",		do_suileesyasa,		0,			POS_DEAD,	GM_PLAYER	},
	{ "suileesyasat",		do_suileesyasat,		0,			POS_DEAD,	GM_PLAYER	},
	{ "barileesyasa",		do_barileesyasa,		0,			POS_DEAD,	GM_PLAYER	},
	{ "barileesyasat",		do_barileesyasat,		0,			POS_DEAD,	GM_PLAYER	},
	{ "yesilotilesat",		do_yesilotilesat,		0,			POS_DEAD,	GM_PLAYER	},
	{ "kirmiziotilesat",		do_kirmiziotilesat,		0,			POS_DEAD,	GM_PLAYER	},
	{ "maviotilesat",		do_maviotilesat,		0,			POS_DEAD,	GM_PLAYER	},
	{ "morotilesat",		do_morotilesat,		0,			POS_DEAD,	GM_PLAYER	},
	{ "ruhtasilesat",		do_ruhtasilesat,		0,			POS_DEAD,	GM_PLAYER	},
#endif
