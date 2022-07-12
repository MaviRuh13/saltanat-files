// -----------------------------------------------Arat----------------------------------------------- // (typedef struct SSimplePlayerInformation)

	BYTE                byLevel;

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
	int                 byLevel;
#else
	BYTE                byLevel;
#endif

// -----------------------------------------------Arat----------------------------------------------- // (typedef struct packet_guild_sub_member)

	BYTE byLevel;

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
	int byLevel;
#else
	BYTE byLevel;
#endif