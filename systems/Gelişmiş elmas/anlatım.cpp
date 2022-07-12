char_item.cpp açýlýr

case ITEM_AUTO_HP_RECOVERY_S: aratýlýr aþþaðýdaki kod bloðu üzerine eklenir.

						case item_kodu : //GELISMIS_ELMAS_AKIRAGAME
							//item_kodu yazan yere geliþmiþ elmas olmasý istediðiniz itemin kodunu yazýn.
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
										if (item2->GetSocketCount() == ITEM_SOCKET_MAX_NUM) // filesinizde 6 taþ varsa ve 4 taþa kadar eklesin istiyorsanýz ITEM_SOCKET_MAX_NUM yerine 4 yazýn
										{
											ChatPacket(CHAT_TYPE_INFO, "Bu iteme daha fazla soket ekleyemezsin.");
											return false;
										}
										item2->AddSocket();
										item2->UpdatePacket();
										item2->Save();
										ChatPacket(CHAT_TYPE_INFO, "Soket basarýyla eklendi.");
										item->SetCount(item->GetCount() - 1);
									}
									else
									{
										ChatPacket(CHAT_TYPE_INFO, "Bu iteme soket eklenmez.");
										break;
									}
								}
								break;

burda iþimiz bitti build edilebilir.

navicat açýlýr player>item_proto girilir char_item.cpp'de geliþmiþ elmas için girdiðiniz itemin kodu aratýlýp type 3 subtype 10 olarak ayarlanýr.

pack locale_xx açýlýr locale>xx>item_proto açýlýp char_item.cpp'de geliþmiþ elmas için girdiðiniz itemin kodu aratýlýp type 3 subtype 19 olarak ayarlanýr.

txt proto kullanýyorsanýz arttýrma kaðýdýný örnek alabilirsiniz. bknz.ITEM_USE	USE_ADD_ATTRIBUTE

Hayýrlý olsun bi teþekkürü çok görmeyin :)

Abdulkadir ÝSKAN (AkiraGame)

facebook.com/abdulkadir.iskan