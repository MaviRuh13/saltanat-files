// Arat :
// void	SetPlayTime(DWORD dwPlayTime);
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		// Mall
		DWORD	GetDragonCoin();
		DWORD	GetDragonMark();
		
		void	SetDragonCoin(DWORD amount);
		void	SetDragonMark(DWORD amount);
#endif

// Arat :
// DWORD					m_dwPlayTime;
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		DWORD					m_dwDragonCoin;
		DWORD					m_dwDragonMark;
#endif