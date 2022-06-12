*****************************************************************************************************************************

Açın \UserInterface\AbstractPlayer.h


Aratın:
virtual void    SetItemCount(TItemPos itemPos, BYTE byCount) = 0;
Değiştirin:
virtual void    SetItemCount(TItemPos itemPos, short byCount) = 0;

*****************************************************************************************************************************

Açın \UserInterface\GameType.h


Dosya içerisinde aratın = packet_item

bu kodu aratın

BYTE        count;

böyle değiştirin.

short        count;

tekrar aynı dosya içerisinde aratın. packet_shop_item

bu kodu aratın

BYTE        count;

böyle değiştirin.

short        count;

*****************************************************************************************************************************

Açın \UserInterface\Packet.h


Dosya içerisinde command_item_drop2

bu kodu aratın

BYTE        count;

böyle değiştirin.

short        count;

tekrar aynı dosya içerisinde aratın command_item_move

bu kodu aratın

BYTE num;

böyle değiştirin.

short num;

tekrar aynı dosya içerisinde aratın command_shop

bu kodu aratın

BYTE subheader;

böyle değiştirin.

short subheader;

tekrar aynı dosya içerisinde aratın command_give_item

bu kodu aratın

BYTE byItemCount;

böyle değiştirin.

short byItemCount;

tekrar aynı dosya içerisinde aratın SShopItemTable

bu kodu aratın

BYTE count;

böyle değiştirin.

short count;

tekrar aynı dosya içerisinde aratın SPacketCGMyShop

bu kodu aratın

BYTE bCount;

böyle değiştirin.

short bCount;

tekrar aynı dosya içerisinde aratın TPacketGCItemDelDeprecate

bu kodu aratın

BYTE count;

böyle değiştirin.

short count;

tekrar aynı dosya içerisinde aratın 2 kez packet_set_item (TPacketGCItemSet)

bu kodu bulun 2 kez

BYTE count;

2 kez böyle değiştirin.

short count;

// eğer yukarda ki packet_set_item (TPacketGCItemSet) bulamassa
 sadece packet_set_item aratın //

tekrar aynı dosya içerisinde aratın packet_set_item2

bu kodu aratın

BYTE count;

böyle değiştirin.

short count;

tekrar aynı dosya içerisinde aratın packet_update_item

bu kodu aratın

BYTE count;

böyle değiştirin.

short count;

tekrar aynı dosya içerisinde aratın SRefineTable

bu kodu aratın

BYTE material_count;

böyle değiştirin.

short material_count;

tekrar aynı dosya içerisinde aratın SEquipmentItemSet

bu kodu aratın

BYTE count;

böyle değiştirin.

short count;

*****************************************************************************************************************************

Açın \UserInterface\PythonExchange.cpp


Aratın
void CPythonExchange::SetItemToTarget(DWORD pos, DWORD vnum, BYTE count)

Değiştirin
void CPythonExchange::SetItemToTarget(DWORD pos, DWORD vnum, short count)

Aratın
void CPythonExchange::SetItemToSelf(DWORD pos, DWORD vnum, BYTE count)

Değiştirin
void CPythonExchange::SetItemToSelf(DWORD pos, DWORD vnum, short count)

Aratın
BYTE CPythonExchange::GetItemCountFromTarget(BYTE pos)

Değiştirin
short CPythonExchange::GetItemCountFromTarget(BYTE pos)

Aratın
BYTE CPythonExchange::GetItemCountFromSelf(BYTE pos)

Değiştirin
short CPythonExchange::GetItemCountFromSelf(BYTE pos)

*****************************************************************************************************************************

Açın \UserInterface\PythonExchange.h


Aratın
BYTE                    item_count[EXCHANGE_ITEM_MAX_NUM];

Değiştirin
short                    item_count[EXCHANGE_ITEM_MAX_NUM];

Aratın
void            SetItemToTarget(DWORD pos, DWORD vnum, BYTE count);
void            SetItemToSelf(DWORD pos, DWORD vnum, BYTE count);

Değiştirin
void            SetItemToTarget(DWORD pos, DWORD vnum, short count);
void            SetItemToSelf(DWORD pos, DWORD vnum, short count);

Aratın
BYTE            GetItemCountFromTarget(BYTE pos);
BYTE            GetItemCountFromSelf(BYTE pos);

Değiştirin
short            GetItemCountFromTarget(BYTE pos);
short            GetItemCountFromSelf(BYTE pos);

*****************************************************************************************************************************

Açın \UserInterface\PythonNetworkStream.h


Aratın
bool SendItemMovePacket(TItemPos pos, TItemPos change_pos, BYTE num);

Değiştirin
bool SendItemMovePacket(TItemPos pos, TItemPos change_pos, short num);

Aratın
bool SendShopSellPacketNew(BYTE bySlot, BYTE byCount);

Değiştirin
bool SendShopSellPacketNew(BYTE bySlot, short byCount);

Aratın
bool SendSafeBoxItemMovePacket(BYTE bySourcePos, BYTE byTargetPos, BYTE byCount);

Değiştirin
bool SendSafeBoxItemMovePacket(BYTE bySourcePos, BYTE byTargetPos, short byCount);

*****************************************************************************************************************************

Açın \UserInterface\PythonNetworkStreamModule.cpp


Aratın
rkNetStream.SendItemMovePacket(Cell, ChangeCell, (BYTE) num);

Değiştirin
rkNetStream.SendItemMovePacket(Cell, ChangeCell, (short) num);

*****************************************************************************************************************************

Açın \UserInterface\PythonNetworkStreamPhaseGame.cpp


Aratın
CPythonExchange::Instance().SetItemToSelf(iSlotIndex, exchange_packet.arg1, (BYTE) exchange_packet.arg3);

Değiştirin
CPythonExchange::Instance().SetItemToSelf(iSlotIndex, exchange_packet.arg1, (short) exchange_packet.arg3);

Aratın
CPythonExchange::Instance().SetItemToTarget(iSlotIndex, exchange_packet.arg1, (BYTE) exchange_packet.arg3);

Değiştirin
CPythonExchange::Instance().SetItemToTarget(iSlotIndex, exchange_packet.arg1, (short) exchange_packet.arg3);

Aratın
CPythonExchange::Instance().DelItemOfSelf((BYTE) exchange_packet.arg1);

Değiştirin
CPythonExchange::Instance().DelItemOfSelf((short) exchange_packet.arg1);

Aratın
CPythonExchange::Instance().DelItemOfTarget((BYTE) exchange_packet.arg1);

Değiştirin
CPythonExchange::Instance().DelItemOfTarget((short) exchange_packet.arg1);

*****************************************************************************************************************************

Açın \UserInterface\PythonNetworkStreamPhaseGameItem.cpp


Aratın
bool CPythonNetworkStream::SendSafeBoxItemMovePacket(BYTE bySourcePos, BYTE byTargetPos, BYTE byCount)

Değiştirin
bool CPythonNetworkStream::SendSafeBoxItemMovePacket(BYTE bySourcePos, BYTE byTargetPos, short byCount)

Aratın
bool CPythonNetworkStream::SendShopSellPacketNew(BYTE bySlot, BYTE byCount)

Değiştirin
bool CPythonNetworkStream::SendShopSellPacketNew(BYTE bySlot, short byCount)

Aratın
if (!Send(sizeof(BYTE), &byCount))

Değiştirin
if (!Send(sizeof(short), &byCount))

Aratın
bool CPythonNetworkStream::SendItemMovePacket(TItemPos pos, TItemPos change_pos, BYTE num)

Değiştirin
bool CPythonNetworkStream::SendItemMovePacket(TItemPos pos, TItemPos change_pos, short num)

*****************************************************************************************************************************

Açın \UserInterface\PythonPlayer.cpp


Aratın
void CPythonPlayer::SetItemCount(TItemPos Cell, BYTE byCount)

Değiştirin
void CPythonPlayer::SetItemCount(TItemPos Cell, short byCount)

*****************************************************************************************************************************

Açın \UserInterface\PythonPlayer.h


Aratın
void    SetItemCount(TItemPos Cell, BYTE byCount);

Değiştirin
void    SetItemCount(TItemPos Cell, short byCount);

*****************************************************************************************************************************

Açın \UserInterface\PythonPlayerModule.cpp


Aratın 2 kere
BYTE bCount;

Değiştirin 2 kere
short bCount;

*****************************************************************************************************************************

Açın \ScriptLib\PythonUtils.cpp


Herhangi bir yere ekleyin

bool PyTuple_GetInteger(PyObject* poArgs, int pos, short* ret)
{
    int val;
    bool result = PyTuple_GetInteger(poArgs,pos,&val);
    *ret = short(val);
    return result;
}

*****************************************************************************************************************************

Açın \ScriptLib\PythonUtils.h


Herhangi bir yere ekleyin

bool PyTuple_GetInteger(PyObject* poArgs, int pos, short* ret);

*****************************************************************************************************************************

FİX OLARAK

shop_item.sql
`count` smallint(4)unsigned NOT NULL DEFAULT '1',

item.sql
`count` smallint(3)unsigned NOT NULL DEFAULT '0',

safebox.sql
`size` smallint(3)unsigned NOT NULL DEFAULT '0',

içlerini değiştirin.