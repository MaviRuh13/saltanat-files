// -----------------------------------------------Arat----------------------------------------------- //

void LogManager::LoginLog(bool isLogin, DWORD dwAccountID, DWORD dwPID, BYTE bLevel, BYTE bJob, DWORD dwPlayTime)

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
void LogManager::LoginLog(bool isLogin, DWORD dwAccountID, DWORD dwPID, int bLevel, BYTE bJob, DWORD dwPlayTime)
#else
void LogManager::LoginLog(bool isLogin, DWORD dwAccountID, DWORD dwPID, BYTE bLevel, BYTE bJob, DWORD dwPlayTime)
#endif
