char_item.cpp a��l�r

case ITEM_AUTO_HP_RECOVERY_S: arat�l�r a��a��daki kod blo�u �zerine eklenir.

						case item_kodu : //GELISMIS_ELMAS_AKIRAGAME
							//item_kodu yazan yere geli�mi� elmas olmas� istedi�iniz itemin kodunu yaz�n.
								{
									LPITEM item2;

									if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
										return false;

									if (item2->IsExchanging() == true)
										return false;

									if (item2->IsEquipped())
										return false;

									if ((item2->GetType() == ITEM_WEAPON) || (item2->GetType() == ITEM_ARMOR && item2->GetSubType() == ARMOR_BODY))
									{
										if (item2->GetSocketCount() == ITEM_SOCKET_MAX_NUM) // filesinizde 6 ta� varsa ve 4 ta�a kadar eklesin istiyorsan�z ITEM_SOCKET_MAX_NUM yerine 4 yaz�n
										{
											ChatPacket(CHAT_TYPE_INFO, "Bu iteme daha fazla soket ekleyemezsin.");
											return false;
										}
										item2->AddSocket();
										item2->UpdatePacket();
										item2->Save();
										ChatPacket(CHAT_TYPE_INFO, "Soket basar�yla eklendi.");
										item->SetCount(item->GetCount() - 1);
									}
									else
									{
										ChatPacket(CHAT_TYPE_INFO, "Bu iteme soket eklenmez.");
										break;
									}
								}
								break;

burda i�imiz bitti build edilebilir.

navicat a��l�r player>item_proto girilir char_item.cpp'de geli�mi� elmas i�in girdi�iniz itemin kodu arat�l�p type 3 subtype 10 olarak ayarlan�r.

pack locale_xx a��l�r locale>xx>item_proto a��l�p char_item.cpp'de geli�mi� elmas i�in girdi�iniz itemin kodu arat�l�p type 3 subtype 19 olarak ayarlan�r.

txt proto kullan�yorsan�z artt�rma ka��d�n� �rnek alabilirsiniz. bknz.ITEM_USE	USE_ADD_ATTRIBUTE

Hay�rl� olsun bi te�ekk�r� �ok g�rmeyin :)

Abdulkadir �SKAN (AkiraGame)

facebook.com/abdulkadir.iskan