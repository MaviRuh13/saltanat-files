// Arat :
// BOOL CPythonShop::IsMainPlayerPrivateShop()
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
void CPythonShop::SetPriceType(short price_type)
{
	sPrice_type = price_type;
}

short CPythonShop::GetPriceType()
{
	return sPrice_type;
}

void CPythonShop::SetShopName(const char* name)
{
	shop_name = name;
}

const char* CPythonShop::GetShopName()
{
	return shop_name.c_str();
}
#endif

// Arat :
// PyObject * shopGetTabCoinType(PyObject * poSelf, PyObject * poArgs)
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
PyObject * shopGetName(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("s", CPythonShop::instance().GetShopName());
}

PyObject * shopGetType(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonShop::instance().GetPriceType());
}
#endif

// Arat :
// { "BuildPrivateShop",			shopBuildPrivateShop,			METH_VARARGS },
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		// ShopEx
		{ "GetName",					shopGetName,					METH_VARARGS },
		{ "GetType",					shopGetType,					METH_VARARGS },
#endif

// Arat :
// PyModule_AddIntConstant(poModule, "SHOP_COIN_TYPE_SECONDARY_COIN", SHOP_COIN_TYPE_SECONDARY_COIN);
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	PyModule_AddIntConstant(poModule, "SHOP_TYPE_GOLD", SHOP_TYPE_GOLD);
	PyModule_AddIntConstant(poModule, "SHOP_TYPE_CASH", SHOP_TYPE_CASH);
	PyModule_AddIntConstant(poModule, "SHOP_TYPE_COINS", SHOP_TYPE_COINS);
	PyModule_AddIntConstant(poModule, "SHOP_TYPE_ALIGN", SHOP_TYPE_ALIGN);
#endif