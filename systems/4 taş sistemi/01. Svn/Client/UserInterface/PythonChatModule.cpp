// Arat
PyObject * chatGetLinkFromHyperlink(PyObject * poSelf, PyObject * poArgs)

// Icinde Bul
		if (results.size() < 6)

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
		if (results.size() < 7)
#else
		if (results.size() < 6)
#endif

// Arat
			len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x",

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
			len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x:%x",
#else
			len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x",
#endif

// Arat
					htoi(results[5].c_str()));

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
					htoi(results[5].c_str()),
					htoi(results[6].c_str()));
#else
					htoi(results[5].c_str()));
#endif

// Arat
			if (results.size() >= 8)
			{
				for (int i = 6; i < results.size(); i += 2)
				{
					len += snprintf(itemlink + len, sizeof(itemlink) - len, ":%x:%I64d", 

// Degistir
#ifdef ENABLE_FOUR_STONE_SYSTEM
			if (results.size() >= 9)
#else
			if (results.size() >= 8)
#endif
			{
#ifdef ENABLE_FOUR_STONE_SYSTEM
				for (int i = 7; i < results.size(); i += 2)
#else
				for (int i = 6; i < results.size(); i += 2)
#endif
				{
#ifdef ENABLE_FOUR_STONE_SYSTEM
					len += snprintf(itemlink + len, sizeof(itemlink) - len, ":%x:%d", //olur da hata olursa ":%x:%I64d", olarak kullan
#else
					len += snprintf(itemlink + len, sizeof(itemlink) - len, ":%x:%I64d", 
#endif