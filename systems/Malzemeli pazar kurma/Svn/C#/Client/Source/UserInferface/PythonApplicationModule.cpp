arat 

#ifdef ENABLE_DRAGON_SOUL_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_DRAGON_SOUL_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_DRAGON_SOUL_SYSTEM",	0);
#endif

altýna ekle 

#ifdef ENABLE_KAYA_MULTI_PRICE
	PyModule_AddIntConstant(poModule, "ENABLE_KAYA_MULTI_PRICE",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_KAYA_MULTI_PRICE",	0);
#endif