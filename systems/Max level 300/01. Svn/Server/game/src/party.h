// -----------------------------------------------Arat----------------------------------------------- //

#define __INC_METIN_II_GAME_PARTY_H__

// -----------------------------------------------Altina ekle----------------------------------------------- //

#define __MAX_LEVEL_300__

// -----------------------------------------------Arat----------------------------------------------- // (class CParty)

			BYTE	bLevel;

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
			int		bLevel;
#else
			BYTE	bLevel;
#endif

// -----------------------------------------------Arat----------------------------------------------- //

		BYTE		GetMemberMaxLevel();
		BYTE		GetMemberMinLevel();

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
		int			GetMemberMaxLevel();
		int			GetMemberMinLevel();
#else
		BYTE		GetMemberMaxLevel();
		BYTE		GetMemberMinLevel();
#endif

// -----------------------------------------------Arat----------------------------------------------- //

		void		RequestSetMemberLevel(DWORD pid, BYTE level);
		void		P2PSetMemberLevel(DWORD pid, BYTE level);

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
		void		RequestSetMemberLevel(DWORD pid, int level);
		void		P2PSetMemberLevel(DWORD pid, int level);
#else
		void		RequestSetMemberLevel(DWORD pid, BYTE level);
		void		P2PSetMemberLevel(DWORD pid, BYTE level);
#endif