// -----------------------------------------------Arat----------------------------------------------- //
#define __INC_CLIENTMANAGER_H__

// --------------------------------------- -----Altina Ekle----------------------------------------------- //

#define __MAX_LEVEL_300__

// -----------------------------------------------Arat----------------------------------------------- //

	struct TPartyInfo
	{
	    BYTE bRole;
	    BYTE bLevel;

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
	struct TPartyInfo
	{
		BYTE bRole;
		int bLevel;
#else
	struct TPartyInfo
	{
	    BYTE bRole;
	    BYTE bLevel;
#endif
