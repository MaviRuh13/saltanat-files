// Arat
#define __INC_METIN_II_LENGTH_H__

// Alt�na Ekle
#define ENABLE_2TH_SHOPEX_SYSTEM

// SHOP_HOST_ITEM_MAX_NUM  = 40,
// SHOP_GUEST_ITEM_MAX_NUM = 18,
// SHOP_PRICELIST_MAX_NUM  = 40,
// De�i�tir :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	SHOP_HOST_ITEM_MAX_NUM	= 100,	/* ȣ��Ʈ�� �ִ� ������ ���� */
	SHOP_GUEST_ITEM_MAX_NUM = 18,	/* �Խ�Ʈ�� �ִ� ������ ���� */

	SHOP_PRICELIST_MAX_NUM	= 100,	///< ���λ��� �������� ����Ʈ���� ������ ���������� �ִ� ����
#else
	SHOP_HOST_ITEM_MAX_NUM	= 40,	/* ȣ��Ʈ�� �ִ� ������ ���� */
	SHOP_GUEST_ITEM_MAX_NUM = 18,	/* �Խ�Ʈ�� �ִ� ������ ���� */

	SHOP_PRICELIST_MAX_NUM	= 40,	///< ���λ��� �������� ����Ʈ���� ������ ���������� �ִ� ����
#endif