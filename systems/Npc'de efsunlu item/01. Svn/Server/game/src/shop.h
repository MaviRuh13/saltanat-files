// Arat
#define __INC_METIN_II_GAME_SHOP_H__

// Altýna Ekle
#define ENABLE_2TH_SHOPEX_SYSTEM

// Arat :
// typedef struct shop_item
// Ýçerisinde : int		itemid;
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
			long	alSockets[ITEM_SOCKET_MAX_NUM];
			TPlayerItemAttribute	aAttr[ITEM_ATTRIBUTE_MAX_NUM];
#endif

// Arat :
// shop_item()
// Ýçerisinde : itemid = 0;
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
				alSockets[0] = 0;
				alSockets[1] = 0;
				alSockets[2] = 0;
				aAttr[0].bType = 0;
				aAttr[0].sValue = 0;
				aAttr[1].bType = 0;
				aAttr[1].sValue = 0;
				aAttr[2].bType = 0;
				aAttr[2].sValue = 0;
				aAttr[3].bType = 0;
				aAttr[3].sValue = 0;
				aAttr[4].bType = 0;
				aAttr[4].sValue = 0;
				aAttr[5].bType = 0;
				aAttr[5].sValue = 0;
				aAttr[6].bType = 0;
				aAttr[6].sValue = 0;
#endif

// Arat :
// bool	Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pItemTable);
// Deðiþtir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		bool	Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pItemTable, short price_type, std::string shopname);
#else
		bool	Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pItemTable);
#endif

// Arat :
// DWORD				m_dwNPCVnum;
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		short				m_sPriceType;
		std::string			m_szShopName;
#endif