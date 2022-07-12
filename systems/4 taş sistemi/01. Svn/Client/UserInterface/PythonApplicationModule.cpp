// Arat
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

// Altina Ekle
#ifdef ENABLE_FOUR_STONE_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_FOUR_STONE_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_FOUR_STONE_SYSTEM", 0);
#endif