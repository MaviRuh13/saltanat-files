// Arat
PyObject * playerGetItemLink(PyObject * poSelf, PyObject * poArgs)

// Icinde Bul
		len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x",

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
		len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x:%x",
#else
		len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x",
#endif
// Arat
				pPlayerItem->alSockets[0], pPlayerItem->alSockets[1], pPlayerItem->alSockets[2]);

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
				pPlayerItem->alSockets[0], pPlayerItem->alSockets[1], pPlayerItem->alSockets[2], pPlayerItem->alSockets[3]);
#else
				pPlayerItem->alSockets[0], pPlayerItem->alSockets[1], pPlayerItem->alSockets[2]);
#endif