// -----------------------------------------------Arat----------------------------------------------- //

void CParty::P2PSetMemberLevel(DWORD pid, BYTE level)

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
void CParty::P2PSetMemberLevel(DWORD pid, int level)
#else
void CParty::P2PSetMemberLevel(DWORD pid, BYTE level)
#endif

// -----------------------------------------------Arat----------------------------------------------- //

BYTE CParty::GetMemberMaxLevel()
{
	BYTE bMax = 0;

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
int CParty::GetMemberMaxLevel()
{
	int bMax = 0;
#else
BYTE CParty::GetMemberMaxLevel()
{
	BYTE bMax = 0;
#endif

// -----------------------------------------------Arat----------------------------------------------- //

BYTE CParty::GetMemberMinLevel()
{
	BYTE bMin = PLAYER_MAX_LEVEL_CONST;

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
int CParty::GetMemberMinLevel()
{
	int bMin = PLAYER_MAX_LEVEL_CONST;
#else
BYTE CParty::GetMemberMinLevel()
{
	BYTE bMin = PLAYER_MAX_LEVEL_CONST;
#endif

// -----------------------------------------------Arat----------------------------------------------- //

void CParty::RequestSetMemberLevel(DWORD pid, BYTE level)

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
void CParty::RequestSetMemberLevel(DWORD pid, int level)
#else
void CParty::RequestSetMemberLevel(DWORD pid, BYTE level)
#endif
