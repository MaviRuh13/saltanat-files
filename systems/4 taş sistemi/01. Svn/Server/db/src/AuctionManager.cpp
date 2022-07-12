// Arat
		"SELECT id,	owner_id, count, vnum, socket0, socket1, socket2,"

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
		"SELECT id, owner_id, count, vnum, socket0, socket1, socket2, socket3, "
#else
		"SELECT id, owner_id, count, vnum, socket0, socket1, socket2, "
#endif

// Arat
		str_to_number(item.alSockets[2], row[cur++]);

// Altina Ekle
#ifdef ENABLE_FOUR_STONE_SYSTEM
		str_to_number(item.alSockets[3], row[cur++]);
#endif