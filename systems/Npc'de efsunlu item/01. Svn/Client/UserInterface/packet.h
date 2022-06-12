// Arat :
// SHOP_HOST_ITEM_MAX_NUM = 40,
// De�i�tir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	SHOP_HOST_ITEM_MAX_NUM = 100,
#else
	SHOP_HOST_ITEM_MAX_NUM = 40,
#endif

// Arat :
// typedef struct SShopItemTable
// ��erisinde : DWORD		price;
// Alt�na Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	long		alSockets[ITEM_SOCKET_SLOT_MAX_NUM];
	TPlayerItemAttribute    aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
#endif

// Arat :
// typedef struct packet_shop_start
// ��erisinde : struct packet_shop_item		items[SHOP_HOST_ITEM_MAX_NUM];
// Alt�na Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	char shop_name[SHOP_TAB_NAME_MAX];
	short price_type;
#endif

// Arat :
// enum EPacketShopSubHeaders
// ��erisinde : SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX
// Alt�na Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	SHOP_SUBHEADER_GC_NOT_ENOUGH_DRAGON_COIN,
	SHOP_SUBHEADER_GC_NOT_ENOUGH_DRAGON_MARK,
	SHOP_SUBHEADER_GC_NOT_ENOUGH_ALIGNMENT,
#endif