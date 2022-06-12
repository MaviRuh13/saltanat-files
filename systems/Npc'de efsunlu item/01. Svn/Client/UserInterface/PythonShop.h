// Arat :
// } EShopCoinType;
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
typedef enum
{
	SHOP_TYPE_GOLD,	// DEFULT VALUE
	SHOP_TYPE_CASH,	// account.cash
	SHOP_TYPE_COINS,	// account.coins
	SHOP_TYPE_ALIGN,	// player.alignment
} EShopType;
#endif

// Arat :
// const char* GetTabName(BYTE tabIdx);
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		void SetShopName(const char* name);
		void SetPriceType(short price_type);
		const char* GetShopName();
		short GetPriceType();
#endif

// Arat :
// BYTE m_bTabCount;
// Üstüne Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		std::string			shop_name;
		short				sPrice_type;
#endif
