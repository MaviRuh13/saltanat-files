// Arat :
// else if (!strcmpi(szCmd, "ObserverMode"))
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
	else if (!strcmpi(szCmd, "RefreshDragonCoin"))
	{
		if (2 != TokenVector.size())
		{
			TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
			return;
		}		
		
		UINT dragoncoin = atoi(TokenVector[1].c_str());
		
		IAbstractPlayer& rkPlayer=IAbstractPlayer::GetSingleton();
		rkPlayer.SetDragonCoin(dragoncoin);
#ifdef ENABLE_CASH_INVENTORY_WINDOW
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshStatus", Py_BuildValue("()"));
#endif
	}
	else if (!strcmpi(szCmd, "RefreshDragonMark"))
	{
		if (2 != TokenVector.size())
		{
			TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
			return;
		}
		
		UINT dragonmark = atoi(TokenVector[1].c_str());
		
		IAbstractPlayer& rkPlayer=IAbstractPlayer::GetSingleton();
		rkPlayer.SetDragonMark(dragonmark);
#ifdef ENABLE_CASH_INVENTORY_WINDOW
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshStatus", Py_BuildValue("()"));
#endif
	}
#endif