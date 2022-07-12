// -----------------------------------------------Arat----------------------------------------------- //

#define __INC_LOG_MANAGER_H__

// --------------------------------------------Altina Ekle----------------------------------------------- //

#define __MAX_LEVEL_300__

// -----------------------------------------------Arat----------------------------------------------- //

typedef struct SGuildMemberPacketData
{   
	DWORD pid;
	BYTE grade;
	BYTE is_general;
	BYTE job;
	BYTE level;
	DWORD offer;
	BYTE name_flag;
	char name[CHARACTER_NAME_MAX_LEN+1];
} TGuildMemberPacketData;

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
typedef struct SGuildMemberPacketData
{
	DWORD pid;
	BYTE byGrade;
	BYTE byIsGeneral;
	BYTE byJob;
	int	 byLevel;
	DWORD dwOffer;
	BYTE byNameFlag;
} TGuildMemberPacketData;
#else
typedef struct SGuildMemberPacketData
{   
	DWORD pid;
	BYTE grade;
	BYTE is_general;
	BYTE job;
	BYTE level;
	DWORD offer;
	BYTE name_flag;
	char name[CHARACTER_NAME_MAX_LEN+1];
} TGuildMemberPacketData;
#endif

// -----------------------------------------------Arat----------------------------------------------- //

		void		ChangeMemberData(DWORD pid, DWORD offer, BYTE level, BYTE grade);

// --------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
		void		ChangeMemberData(DWORD pid, DWORD offer, int level, BYTE grade);
#else
		void		ChangeMemberData(DWORD pid, DWORD offer, BYTE level, BYTE grade);
#endif

// -----------------------------------------------Arat----------------------------------------------- //

	SGuildMember(DWORD pid, BYTE grade, BYTE is_general, BYTE job, BYTE level, DWORD offer_exp, char* name);

// --------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
	SGuildMember(DWORD pid, BYTE grade, BYTE is_general, BYTE job, int level, DWORD offer_exp, char* name);
#else
	SGuildMember(DWORD pid, BYTE grade, BYTE is_general, BYTE job, BYTE level, DWORD offer_exp, char* name);
#endif

// -----------------------------------------------Arat----------------------------------------------- //

typedef struct SGuildMember
{
	DWORD pid; // player 테이블의 id; primary key
	BYTE grade; // 길드상의 플레이어의 계급 1 to 15 (1이 짱)
	BYTE is_general;
	BYTE job;
	int level;
	DWORD offer_exp; // 공헌한 경험치
	BYTE _dummy;

	std::string name;

	SGuildMember(LPCHARACTER ch, BYTE grade, DWORD offer_exp);
	SGuildMember(DWORD pid, BYTE grade, BYTE is_general, BYTE job, int level, DWORD offer_exp, char* name);

} TGuildMember;

// --------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
	DWORD pid; // player 테이블의 id; primary key
	BYTE grade; // 길드상의 플레이어의 계급 1 to 15 (1이 짱)
	BYTE is_general;
	BYTE job;
	int level;
	DWORD offer_exp; // 공헌한 경험치
	BYTE _dummy;
#else
typedef struct SGuildMember
{
	DWORD pid; // player 테이블의 id; primary key
	BYTE grade; // 길드상의 플레이어의 계급 1 to 15 (1이 짱)
	BYTE is_general;
	BYTE job;
	int level;
	DWORD offer_exp; // 공헌한 경험치
	BYTE _dummy;

	std::string name;

	SGuildMember(LPCHARACTER ch, BYTE grade, DWORD offer_exp);
	SGuildMember(DWORD pid, BYTE grade, BYTE is_general, BYTE job, int level, DWORD offer_exp, char* name);

} TGuildMember;
#endif


// -----------------------------------------------Arat----------------------------------------------- //

		void		LevelChange(DWORD pid, BYTE level);

// --------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
		void		LevelChange(DWORD pid, int level);
#else
		void		LevelChange(DWORD pid, BYTE level);
#endif

