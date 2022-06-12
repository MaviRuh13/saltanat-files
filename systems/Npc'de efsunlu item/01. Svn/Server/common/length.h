// Arat
#define __INC_METIN_II_LENGTH_H__

// Altýna Ekle
#define ENABLE_2TH_SHOPEX_SYSTEM

// SHOP_HOST_ITEM_MAX_NUM  = 40,
// SHOP_GUEST_ITEM_MAX_NUM = 18,
// SHOP_PRICELIST_MAX_NUM  = 40,
// Deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	SHOP_HOST_ITEM_MAX_NUM	= 100,	/* È£½ºÆ®ÀÇ ÃÖ´ë ¾ÆÀÌÅÛ °³¼ö */
	SHOP_GUEST_ITEM_MAX_NUM = 18,	/* °Ô½ºÆ®ÀÇ ÃÖ´ë ¾ÆÀÌÅÛ °³¼ö */

	SHOP_PRICELIST_MAX_NUM	= 100,	///< °³ÀÎ»óÁ¡ °¡°ÝÁ¤º¸ ¸®½ºÆ®¿¡¼­ À¯ÁöÇÒ °¡°ÝÁ¤º¸ÀÇ ÃÖ´ë °¹¼ö
#else
	SHOP_HOST_ITEM_MAX_NUM	= 40,	/* È£½ºÆ®ÀÇ ÃÖ´ë ¾ÆÀÌÅÛ °³¼ö */
	SHOP_GUEST_ITEM_MAX_NUM = 18,	/* °Ô½ºÆ®ÀÇ ÃÖ´ë ¾ÆÀÌÅÛ °³¼ö */

	SHOP_PRICELIST_MAX_NUM	= 40,	///< °³ÀÎ»óÁ¡ °¡°ÝÁ¤º¸ ¸®½ºÆ®¿¡¼­ À¯ÁöÇÒ °¡°ÝÁ¤º¸ÀÇ ÃÖ´ë °¹¼ö
#endif