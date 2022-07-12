// Arat

#ifdef ENABLE_DRAGON_SOUL_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_DRAGON_SOUL_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_DRAGON_SOUL_SYSTEM",	0);
#endif

// Altina Ekle

#ifdef MAVIRUH_MULTI_PRICE
	PyModule_AddIntConstant(poModule, "MAVIRUH_MULTI_PRICE",	1);
#else
	PyModule_AddIntConstant(poModule, "MAVIRUH_MULTI_PRICE",	0);
#endif

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_2TH_SHOPEX_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_2TH_SHOPEX_SYSTEM", 0);
#endif