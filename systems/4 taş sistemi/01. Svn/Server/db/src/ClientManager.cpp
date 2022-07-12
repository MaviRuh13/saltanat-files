// Arat
					DWORD dwSocket2 = 0;

					if (pItemTable->bType == ITEM_UNIQUE)
					{
						if (pItemAward->dwSocket2 != 0)
							dwSocket2 = pItemAward->dwSocket2;
						else
							dwSocket2 = pItemTable->alValues[0];
					}

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
					DWORD dwSocket3 = 0;

					if (pItemTable->bType == ITEM_UNIQUE)
					{
						if (pItemAward->dwSocket3 != 0)
							dwSocket3 = pItemAward->dwSocket3;
						else
							dwSocket3 = pItemTable->alValues[0];
					}
#else
					DWORD dwSocket2 = 0;

					if (pItemTable->bType == ITEM_UNIQUE)
					{
						if (pItemAward->dwSocket2 != 0)
							dwSocket2 = pItemAward->dwSocket2;
						else
							dwSocket2 = pItemTable->alValues[0];
					}
#endif

// Arat
								if (pItemAward->dwSocket2 == 0)
								{
									dwSocket2 = pItemTable->alValues[0];
								}
								else
								{
									dwSocket2 = pItemAward->dwSocket2;
								}
								break;

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
								if (pItemAward->dwSocket3 == 0)
								{
									dwSocket3 = pItemTable->alValues[0];
								}
								else
								{
									dwSocket3 = pItemAward->dwSocket3;
								}
								break;
#else
								if (pItemAward->dwSocket2 == 0)
								{
									dwSocket2 = pItemTable->alValues[0];
								}
								else
								{
									dwSocket2 = pItemAward->dwSocket2;
								}
								break;
#endif

// Arat
		pi->pSafebox = pSafebox;

		char szQuery[512];
		snprintf(szQuery, sizeof(szQuery), 
				"SELECT id, window+0, pos, count, vnum, socket0, socket1, socket2, "

// Degistir
		pi->pSafebox = pSafebox;

		char szQuery[512];
		snprintf(szQuery, sizeof(szQuery), 
#ifdef ENABLE_FOUR_STONE_SYSTEM
				"SELECT id, window+0, pos, count, vnum, socket0, socket1, socket2,socket3, "
#else
				"SELECT id, window+0, pos, count, vnum, socket0, socket1, socket2, "
#endif

// Arat
						snprintf(szQuery, sizeof(szQuery), 
								"INSERT INTO item%s (id, owner_id, window, pos, vnum, count, socket0, socket1, socket2) "
								"VALUES(%u, %u, '%s', %d, %u, %u, %u, %u, %u)",
								GetTablePostfix(),
								GainItemID(),
								pi->account_id,
								pi->ip[0] == 0 ? "SAFEBOX" : "MALL",
								iPos,
								pItemAward->dwVnum, pItemAward->dwCount, pItemAward->dwSocket0, pItemAward->dwSocket1, dwSocket2);
					}

// Degistir
						snprintf(szQuery, sizeof(szQuery), 
#ifdef ENABLE_FOUR_STONE_SYSTEM
								"INSERT INTO item%s (id, owner_id, window, pos, vnum, count, socket0, socket1, socket2, socket3) "
								"VALUES(%u, %u, '%s', %d, %u, %u, %u, %u, %u, %u)",
#else
								"INSERT INTO item%s (id, owner_id, window, pos, vnum, count, socket0, socket1, socket2) "
								"VALUES(%u, %u, '%s', %d, %u, %u, %u, %u, %u)",
#endif
								GetTablePostfix(),
								GainItemID(),
								pi->account_id,
								pi->ip[0] == 0 ? "SAFEBOX" : "MALL",
								iPos,
#ifdef ENABLE_FOUR_STONE_SYSTEM
								pItemAward->dwVnum, pItemAward->dwCount, pItemAward->dwSocket0, pItemAward->dwSocket1, pItemAward->dwSocket2, dwSocket3);
#else
								pItemAward->dwVnum, pItemAward->dwCount, pItemAward->dwSocket0, pItemAward->dwSocket1, dwSocket2);
#endif
					}

// Arat
					item.alSockets[2] = dwSocket2;

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
					item.alSockets[2] = pItemAward->dwSocket2;
					item.alSockets[3] = dwSocket3;
#else
					item.alSockets[2] = dwSocket2;
#endif

// Arat
void CClientManager::QUERY_ITEM_SAVE(CPeer * pkPeer, const char * c_pData)

// Icinde Bul
			"REPLACE INTO item%s (id, owner_id, window, pos, count, vnum, socket0, socket1, socket2, "

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
			"REPLACE INTO item%s (id, owner_id, window, pos, count, vnum, socket0, socket1, socket2, socket3, "
#else
			"REPLACE INTO item%s (id, owner_id, window, pos, count, vnum, socket0, socket1, socket2, "
#endif

// Arat
			"VALUES(%u, %u, %d, %d, %u, %u, %ld, %ld, %ld, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)",

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
			"VALUES(%u, %u, %d, %d, %u, %u, %ld, %ld, %ld, %ld, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)",
#else
			"VALUES(%u, %u, %d, %d, %u, %u, %ld, %ld, %ld, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)",
#endif

// Arat
			p->alSockets[2],

// Altina Ekle
#ifdef ENABLE_FOUR_STONE_SYSTEM
			p->alSockets[3],
#endif