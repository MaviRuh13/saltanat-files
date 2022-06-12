// Arat :
// CPythonShop::Instance().SetItemData(iItemIndex, pShopStartPacket->items[iItemIndex]);
// } Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM				
				CPythonShop::Instance().SetShopName(pShopStartPacket->shop_name);
				CPythonShop::Instance().SetPriceType(pShopStartPacket->price_type);
#endif

// Arat :
// case SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX:
// break; Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		case SHOP_SUBHEADER_GC_NOT_ENOUGH_DRAGON_COIN:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_DRAGON_COIN"));
			break;

		case SHOP_SUBHEADER_GC_NOT_ENOUGH_DRAGON_MARK:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_DRAGON_MARK"));
			break;

		case SHOP_SUBHEADER_GC_NOT_ENOUGH_ALIGNMENT:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_ALIGNMENT"));
			break;
#endif		