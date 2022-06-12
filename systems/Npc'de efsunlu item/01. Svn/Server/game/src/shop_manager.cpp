// Arat :
// bool CShopManager::Initialize(TShopTable * table, int size)
// Ýçerisinde : if (!shop->Create(table->dwVnum, table->dwNPCVnum, table->items))
// Deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		if (!shop->Create(table->dwVnum, table->dwNPCVnum, table->items, table->price_type, table->szShopName))
#else
		if (!shop->Create(table->dwVnum, table->dwNPCVnum, table->items))
#endif

// Arat :
// CGrid grid = CGrid(5, 9);
// Deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	CGrid grid = CGrid(10, 10);
#else
	CGrid grid = CGrid(5, 9);
#endif