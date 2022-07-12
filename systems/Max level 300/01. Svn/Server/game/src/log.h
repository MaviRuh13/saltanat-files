// -----------------------------------------------Arat----------------------------------------------- //

#define __INC_LOG_MANAGER_H__

// -----------------------------------------------Degistir----------------------------------------------- //

#define __MAX_LEVEL_300__

// -----------------------------------------------Arat----------------------------------------------- //

void		LoginLog(bool isLogin, DWORD dwAccountID, DWORD dwPID, BYTE bLevel, BYTE bJob, DWORD dwPlayTime);

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
void		LoginLog(bool isLogin, DWORD dwAccountID, DWORD dwPID, int bLevel, BYTE bJob, DWORD dwPlayTime);
#else
void		LoginLog(bool isLogin, DWORD dwAccountID, DWORD dwPID, BYTE bLevel, BYTE bJob, DWORD dwPlayTime);
#endif
