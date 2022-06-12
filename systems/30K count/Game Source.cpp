****************************************************************************************************************************

Açın \common\item_length.h


Aratın
ITEM_MAX_COUNT = 200,

Değiştirin
ITEM_MAX_COUNT = 500,

*****************************************************************************************************************************

Açın \common\tables.h


bu kodu aratın SShopItemTable
BYTE count;

böyle değiştirin.
short count;

bu kodu aratın SShopTable
BYTE byItemCount;

böyle değiştirin.
short byItemCount;

bu kodu aratın SRefineTable
BYTE material_count;

böyle değiştirin.
short material_count;

*****************************************************************************************************************************

Açın \game\char.cpp


Aratın
void CHARACTER::OpenMyShop(const char * c_pszSign, TShopItemTable * pTable, BYTE bItemCount)

Değiştirin
void CHARACTER::OpenMyShop(const char * c_pszSign, TShopItemTable * pTable, short bItemCount)

Aratın
for (BYTE i = 0; i < bItemCount; ++i)

Değiştirin
for (short i = 0; i < bItemCount; ++i)

*****************************************************************************************************************************

Açın \game\char.h


Aratın
bool            DropItem(TItemPos Cell,  BYTE bCount=0);

Değiştirin
bool            DropItem(TItemPos Cell,  short bCount=0);

Aratın
bool            MoveItem(TItemPos pos, TItemPos change_pos, BYTE num);

Değiştirin
bool            MoveItem(TItemPos pos, TItemPos change_pos, short num);

Aratın
LPITEM            AutoGiveItem(DWORD dwItemVnum, BYTE bCount=1, int iRarePct = -1, bool bMsg = true);
void            AutoGiveItem(LPITEM item, bool longOwnerShip = false);

Değiştirin
LPITEM            AutoGiveItem(DWORD dwItemVnum, short bCount=1, int iRarePct = -1, bool bMsg = true);
void            AutoGiveItem(LPITEM item, bool longOwnerShip = false);

Aratın
void            OpenMyShop(const char * c_pszSign, TShopItemTable * pTable, BYTE bItemCount);

Değiştirin
void            OpenMyShop(const char * c_pszSign, TShopItemTable * pTable, short bItemCount);

*****************************************************************************************************************************

Açın \game\char_item.cpp


Aratın
bool CHARACTER::DropItem(TItemPos Cell, BYTE bCount)

Değiştirin
bool CHARACTER::DropItem(TItemPos Cell, short bCount)

Aratın
bool CHARACTER::MoveItem(TItemPos Cell, TItemPos DestCell, BYTE count)

Değiştirin
bool CHARACTER::MoveItem(TItemPos Cell, TItemPos DestCell, short count)

Aratın
count = MIN(200 - item2->GetCount(), count);

Değiştirin
count = MIN(ITEM_MAX_COUNT - item2->GetCount(), count);

Aratın
BYTE bCount = item->GetCount();

Değiştirin
short bCount = item->GetCount();

Aratın
BYTE bCount2 = MIN(200 - item2->GetCount(), bCount);

Değiştirin
short bCount2 = MIN(ITEM_MAX_COUNT - item2->GetCount(), bCount);

Aratın
LPITEM CHARACTER::AutoGiveItem(DWORD dwItemVnum, BYTE bCount, int iRarePct, bool bMsg)

Değiştirin
LPITEM CHARACTER::AutoGiveItem(DWORD dwItemVnum, short bCount, int iRarePct, bool bMsg)

Aratın
BYTE bCount2 = MIN(200 - item->GetCount(), bCount);

Değiştirin
short bCount2 = MIN(ITEM_MAX_COUNT - item->GetCount(), bCount);

*****************************************************************************************************************************

Açın \game\input_main.cpp


Aratın
case SHOP_SUBHEADER_CG_SELL2:
    {
        if (uiBytes < sizeof(BYTE) + sizeof(BYTE))
            return -1;

        BYTE pos = *(c_pData++);
        BYTE count = *(c_pData);

        sys_log(0, "INPUT: %s SHOP: SELL2", ch->GetName());
        CShopManager::instance().Sell(ch, pos, count);
        return sizeof(BYTE) + sizeof(BYTE);
    }

Değiştirin
case SHOP_SUBHEADER_CG_SELL2:
    {
        if (uiBytes < sizeof(BYTE) + sizeof(short))
            return -1;

        BYTE pos = *(c_pData++);
        short count = *(c_pData);

        sys_log(0, "INPUT: %s SHOP: SELL2 pos: %d count: %d", ch->GetName(), pos, count);
        CShopManager::instance().Sell(ch, pos, count);
        return sizeof(BYTE) + sizeof(short);
    }

*****************************************************************************************************************************

Açın \game\item.cpp


Aratın
return MIN(m_dwCount, 200);

Değiştirin
return MIN(m_dwCount, ITEM_MAX_COUNT);

*****************************************************************************************************************************

Açın \game\OXEvent.cpp


Aratın
bool COXEventManager::GiveItemToAttender(DWORD dwItemVnum, BYTE count)

Değiştirin
bool COXEventManager::GiveItemToAttender(DWORD dwItemVnum, short count)

*****************************************************************************************************************************

Açın \game\OXEvent.h


Aratın
bool GiveItemToAttender(DWORD dwItemVnum, BYTE count);

Değiştirin
bool GiveItemToAttender(DWORD dwItemVnum, short count);

*****************************************************************************************************************************

Açın \game\packet.h


bu kodu aratın command_item_drop2
BYTE    count;

böyle değiştirin.
short    count;

bu kodu aratın command_item_move
BYTE    count;

böyle değiştirin.
short    count;

bu kodu aratın command_shop (TPacketCGShop)
BYTE    subheader;

böyle değiştirin.
short    subheader;

bu kodu aratın TPacketGCItemDelDeprecated
BYTE    count;

böyle değiştirin.
short    count;

bu kodu aratın packet_item_set
BYTE    count;

böyle değiştirin.
short    count;

bu kodu aratın packet_item_update
BYTE    count;

böyle değiştirin.
short    count;

bu kodu aratın packet_shop_item
BYTE    count;

böyle değiştirin.
short    count;

bu kodu aratın command_give_item
BYTE    byItemCount;

böyle değiştirin.
short    byItemCount;

bu kodu aratın SPacketCGMyShop
BYTE    bCount;

böyle değiştirin.
short    bCount;

bu kodu aratın SPacketGCRefineInformaion
BYTE    material_count;

böyle değiştirin.
short    material_count;

bu kodu aratın pakcet_view_equip
BYTE    count;

böyle değiştirin.
short    count;

*****************************************************************************************************************************

Açın \game\safebox.cpp


Aratın
bool CSafebox::MoveItem(BYTE bCell, BYTE bDestCell, BYTE count)

Değiştirin
bool CSafebox::MoveItem(BYTE bCell, BYTE bDestCell, short count)

Aratın
count = MIN(200 - item2->GetCount(), count);

Değiştirin
count = MIN(ITEM_MAX_COUNT - item2->GetCount(), count);

*****************************************************************************************************************************

Açın \game\safebox.h


Aratın
bool        MoveItem(BYTE bCell, BYTE bDestCell, BYTE count);

Değiştirin
bool        MoveItem(BYTE bCell, BYTE bDestCell, short count);

*****************************************************************************************************************************

Açın \game\shop.cpp


Aratın
BYTE bItemCount;

Değiştirin
short bItemCount;

Aratın
void CShop::SetShopItems(TShopItemTable * pTable, BYTE bItemCount)

Değiştirin
void CShop::SetShopItems(TShopItemTable * pTable, short bItemCount)

*****************************************************************************************************************************

Açın \game\shop.h


Aratın
BYTE    count

Değiştirin
short    count

Aratın
void    SetShopItems(TShopItemTable * pItemTable, BYTE bItemCount);

Değiştirin
void    SetShopItems(TShopItemTable * pItemTable, short bItemCount);

*****************************************************************************************************************************

Açın \game\shop_manager.cpp


Aratın
LPSHOP CShopManager::CreatePCShop(LPCHARACTER ch, TShopItemTable * pTable, BYTE bItemCount)

Değiştirin
LPSHOP CShopManager::CreatePCShop(LPCHARACTER ch, TShopItemTable * pTable, short bItemCount)

Aratın
void CShopManager::Sell(LPCHARACTER ch, BYTE bCell, BYTE bCount)

Değiştirin
void CShopManager::Sell(LPCHARACTER ch, BYTE bCell, short bCount)

*****************************************************************************************************************************

Açın \game\shop_manager.h


Aratın
void    Sell(LPCHARACTER ch, BYTE bCell, BYTE bCount=0);

Değiştirin
void    Sell(LPCHARACTER ch, BYTE bCell, short bCount=0);

Aratın
LPSHOP    CreatePCShop(LPCHARACTER ch, TShopItemTable * pTable, BYTE bItemCount);

Değiştirin
LPSHOP    CreatePCShop(LPCHARACTER ch, TShopItemTable * pTable, short bItemCount);

*****************************************************************************************************************************

FİX OLARAK

shop_item.sql
`count` smallint(4)unsigned NOT NULL DEFAULT '1',

item.sql
`count` smallint(3)unsigned NOT NULL DEFAULT '0',

safebox.sql
`size` smallint(3)unsigned NOT NULL DEFAULT '0',

içlerini değiştirin.