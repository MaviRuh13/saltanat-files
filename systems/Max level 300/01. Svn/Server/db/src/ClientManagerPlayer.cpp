// -----------------------------------------------Arat----------------------------------------------- //

				if (pTab->level >= m_iPlayerDeleteLevelLimit)
				{
					sys_log(0, "PLAYER_DELETE FAILED LEVEL %u >= DELETE LIMIT %d", pTab->level, m_iPlayerDeleteLevelLimit);

// -----------------------------------------------Degistir----------------------------------------------- //

				if (pTab->level >= m_iPlayerDeleteLevelLimit)
				{
#ifdef __MAX_LEVEL_300__
					sys_log(0, "PLAYER_DELETE FAILED LEVEL %d >= DELETE LIMIT %d", pTab->level, m_iPlayerDeleteLevelLimit);
#else
					sys_log(0, "PLAYER_DELETE FAILED LEVEL %u >= DELETE LIMIT %d", pTab->level, m_iPlayerDeleteLevelLimit);
#endif

// -----------------------------------------------Arat----------------------------------------------- //

		if (deletedLevelLimit >= m_iPlayerDeleteLevelLimit && !IsChinaEventServer())
		{
			sys_log(0, "PLAYER_DELETE FAILED LEVEL %u >= DELETE LIMIT %d", deletedLevelLimit, m_iPlayerDeleteLevelLimit);

// -----------------------------------------------Degistir----------------------------------------------- //

		if (deletedLevelLimit >= m_iPlayerDeleteLevelLimit && !IsChinaEventServer())
		{
#ifdef __MAX_LEVEL_300__
			sys_log(0, "PLAYER_DELETE FAILED LEVEL %d >= DELETE LIMIT %d", deletedLevelLimit, m_iPlayerDeleteLevelLimit);
#else
			sys_log(0, "PLAYER_DELETE FAILED LEVEL %u >= DELETE LIMIT %d", deletedLevelLimit, m_iPlayerDeleteLevelLimit);
#endif
