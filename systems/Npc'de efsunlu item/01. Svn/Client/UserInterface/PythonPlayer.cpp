// Arat :
// DWORD CPythonPlayer::GetPlayTime()
// Alt�na Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
DWORD CPythonPlayer::GetDragonCoin()
{
	return m_dwDragonCoin;
}

DWORD CPythonPlayer::GetDragonMark()
{
	return m_dwDragonMark;
}

void CPythonPlayer::SetDragonCoin(DWORD amount)
{
	m_dwDragonCoin = amount;
}

void CPythonPlayer::SetDragonMark(DWORD amount)
{
	m_dwDragonMark = amount;
}
#endif

// Arat :
// m_dwPlayTime = 0;
// Alt�na Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	m_dwDragonCoin = 0;
	m_dwDragonMark = 0;
#endif