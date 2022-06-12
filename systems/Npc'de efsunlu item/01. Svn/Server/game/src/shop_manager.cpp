// Arat :
// bool CShopManager::Initialize(TShopTable * table, int size)
// ��erisinde : if (!shop->Create(table->dwVnum, table->dwNPCVnum, table->items))
// De�i�tir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		if (!shop->Create(table->dwVnum, table->dwNPCVnum, table->items, table->price_type, table->szShopName))
#else
		if (!shop->Create(table->dwVnum, table->dwNPCVnum, table->items))
#endif

// Arat :
// CGrid grid = CGrid(5, 9);
// De�i�tir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	CGrid grid = CGrid(10, 10);
#else
	CGrid grid = CGrid(5, 9);
#endif