// En Alta Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_2TH_SHOPEX_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_2TH_SHOPEX_SYSTEM", 0);
#endif

#ifdef ENABLE_CASH_INVENTORY_WINDOW
	PyModule_AddIntConstant(poModule, "ENABLE_CASH_INVENTORY_WINDOW", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_CASH_INVENTORY_WINDOW", 0);
#endif