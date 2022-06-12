// Arat
#define __INC_PACKET_H__

// Altýna Ekle
#define ENABLE_2TH_SHOPEX_SYSTEM

// Arat :
// enum EPacketShopSubHeaders
// Ýçerisinde : SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX,
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	SHOP_SUBHEADER_GC_NOT_ENOUGH_DRAGON_COIN,
	SHOP_SUBHEADER_GC_NOT_ENOUGH_DRAGON_MARK,
	SHOP_SUBHEADER_GC_NOT_ENOUGH_ALIGNMENT,
#endif

// Arat :
// typedef struct packet_shop_start
// Ýçerisinde : struct packet_shop_item	items[SHOP_HOST_ITEM_MAX_NUM];
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	char shop_name[SHOP_TAB_NAME_MAX];
	short price_type;
#endif