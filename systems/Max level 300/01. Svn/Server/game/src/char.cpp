// -----------------------------------------------Arat----------------------------------------------- //

void CHARACTER::SetLevel(BYTE level)

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
void CHARACTER::SetLevel(int level)
#else
void CHARACTER::SetLevel(BYTE level)
#endif
