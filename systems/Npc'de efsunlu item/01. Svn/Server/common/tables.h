// Arat
#define __INC_METIN_II_LENGTH_H__

// Altýna Ekle
#define ENABLE_2TH_SHOPEX_SYSTEM

// Arat :
// typedef struct SShopItemTable
// Ýçerisinde : DWORD		price;
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	long		alSockets[ITEM_SOCKET_MAX_NUM];
	TPlayerItemAttribute    aAttr[ITEM_ATTRIBUTE_MAX_NUM];
#endif

// Arat :
// typedef struct SShopTable
// Ýçerisinde : TShopItemTable	items[SHOP_HOST_ITEM_MAX_NUM];
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	short		price_type;
	char		szShopName[SHOP_TAB_NAME_MAX];
#endif