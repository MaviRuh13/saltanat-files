// -----------------------------------------------Arat----------------------------------------------- //

			pkPeer->Encode(&it_member->second.bLevel, sizeof(BYTE));

// -----------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
			pkPeer->Encode(&it_member->second.bLevel, sizeof(int));
#else
			pkPeer->Encode(&it_member->second.bLevel, sizeof(BYTE));
#endif
