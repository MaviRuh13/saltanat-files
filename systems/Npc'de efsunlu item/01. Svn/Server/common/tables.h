// Arat
#define __INC_METIN_II_LENGTH_H__

// Alt�na Ekle
#define ENABLE_2TH_SHOPEX_SYSTEM

// Arat :
// typedef struct SShopItemTable
// ��erisinde : DWORD		price;
// Alt�na Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	long		alSockets[ITEM_SOCKET_MAX_NUM];
	TPlayerItemAttribute    aAttr[ITEM_ATTRIBUTE_MAX_NUM];
#endif

// Arat :
// typedef struct SShopTable
// ��erisinde : TShopItemTable	items[SHOP_HOST_ITEM_MAX_NUM];
// Alt�na Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	short		price_type;
	char		szShopName[SHOP_TAB_NAME_MAX];
#endif