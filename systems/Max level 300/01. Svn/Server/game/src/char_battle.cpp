// -----------------------------------------------Arat----------------------------------------------- //

	struct FPartyTotaler
	{
		int		total;

// -----------------------------------------------Degistir----------------------------------------------- //

	struct FPartyTotaler
	{
#ifdef __MAX_LEVEL_300__
		long	total;
#else
		int		total;
#endif

// -----------------------------------------------Arat----------------------------------------------- //

	struct FPartyDistributor
	{
		int		total;
		LPCHARACTER	c;
		int		x, y;
		DWORD		_iExp;
		int		m_iMode;
		int		m_iMemberCount;

		FPartyDistributor(LPCHARACTER center, int member_count, int total, DWORD iExp, int iMode) 

// -----------------------------------------------Degistir----------------------------------------------- //

	struct FPartyDistributor
	{
#ifdef __MAX_LEVEL_300__
		long	total;
#else
		int		total;
#endif
		LPCHARACTER	c;
		int		x, y;
		DWORD		_iExp;
		int		m_iMode;
		int		m_iMemberCount;
#ifdef __MAX_LEVEL_300__
		FPartyDistributor(LPCHARACTER center, int member_count, long total, DWORD iExp, int iMode) 
#else
		FPartyDistributor(LPCHARACTER center, int member_count, int total, DWORD iExp, int iMode) 
#endif
