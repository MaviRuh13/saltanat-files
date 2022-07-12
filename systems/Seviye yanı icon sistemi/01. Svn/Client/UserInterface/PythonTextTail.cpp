// -----------------------------------------------Arat----------------------------------------------- //

		CGraphicTextInstance * pGuildNameInstance = pTextTail->pGuildNameTextInstance;

// -----------------------------------------------Altina Ekle----------------------------------------------- //

#ifdef ___SALTANAT_SEVIYEYE_GORE_IKON___
		CGraphicImageInstance * pSaltanat = pTextTail->pSaltanatFlagInstance;
#endif

// -----------------------------------------------Arat----------------------------------------------- //

		pTextTail->pTextInstance->SetColor(pTextTail->Color.r, pTextTail->Color.g, pTextTail->Color.b);

// -----------------------------------------------Ustune Ekle----------------------------------------------- //

#ifdef ___SALTANAT_SEVIYEYE_GORE_IKON___
		if (pSaltanat)
		{
			CGraphicTextInstance * pLevel = pTextTail->pLevelTextInstance;
			
			if (pLevel)
			{
				int iLevelWidth, iLevelHeight, iTitleWidth, iTitleHeight;
				pLevel->GetTextSize(&iLevelWidth, &iLevelHeight);
				if (pTitle)
				{
					pTitle->GetTextSize (&iTitleWidth, &iTitleHeight);
					pSaltanat->SetPosition (pTextTail->x - (iNameWidth / 2) - 4.0f - iTitleWidth - iLevelWidth - 15.0f- pSaltanat->GetWidth() / 2 + 8.5f, pTextTail->y - 12);
				}
				if (!pTitle)
					pSaltanat->SetPosition (pTextTail->x - (iNameWidth / 2) - 4.0f - iLevelWidth - 15.0f - pSaltanat->GetWidth() / 2 + 8.5f, pTextTail->y - 12);
			}
		}
#endif

// -----------------------------------------------Arat----------------------------------------------- //

		if (pTextTail->pTitleTextInstance)
		{
			pTextTail->pTitleTextInstance->Render();
		}

// -----------------------------------------------Altina Ekle----------------------------------------------- //

#ifdef ___SALTANAT_SEVIYEYE_GORE_IKON___
		if (pTextTail->pSaltanatFlagInstance)
		{
			pTextTail->pSaltanatFlagInstance->Render();
		}
#endif

// -----------------------------------------------Arat----------------------------------------------- //

	pTextTail->pLevelTextInstance=NULL;

// -----------------------------------------------Altina Ekle----------------------------------------------- //

#ifdef ___SALTANAT_SEVIYEYE_GORE_IKON___
	pTextTail->pSaltanatFlagInstance=NULL;
#endif

// -----------------------------------------------Arat----------------------------------------------- //

	m_CharacterTextTailMap.insert(TTextTailMap::value_type(dwVirtualID, pTextTail));

// -----------------------------------------------Ustune Ekle----------------------------------------------- //

#ifdef ___SALTANAT_SEVIYEYE_GORE_IKON___
	if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 250 &&  pCharacterInstance->GetLevel() <= 254)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/251.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 254 &&  pCharacterInstance->GetLevel() <= 259)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/255.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 259 &&  pCharacterInstance->GetLevel() <= 264)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/260.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 264 &&  pCharacterInstance->GetLevel() <= 269)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/265.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 269 &&  pCharacterInstance->GetLevel() <= 274)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/270.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 274 &&  pCharacterInstance->GetLevel() <= 279)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/275.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 279 &&  pCharacterInstance->GetLevel() <= 284)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/280.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 284 &&  pCharacterInstance->GetLevel() <= 289)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/285.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 289 &&  pCharacterInstance->GetLevel() <= 294)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/290.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 294 &&  pCharacterInstance->GetLevel() <= 299)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/295.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
	else if (pCharacterInstance->IsPC() && pCharacterInstance->GetLevel() > 299 &&  pCharacterInstance->GetLevel() <= 300)
	{
			pTextTail->pSaltanatFlagInstance = CGraphicImageInstance::New();
			char szPath[256];
			sprintf(szPath, "d:/ymir work/level_semboller/300.tga");
			pTextTail->pSaltanatFlagInstance->SetImagePointer((CGraphicImage*)CResourceManager::Instance().GetResourcePointer(szPath));
	}
#endif

// -----------------------------------------------Arat----------------------------------------------- //

	pTextTail->pLevelTextInstance = NULL;

// -----------------------------------------------Altina Ekle----------------------------------------------- //

#ifdef ___SALTANAT_SEVIYEYE_GORE_IKON___
	pTextTail->pSaltanatFlagInstance = NULL;
#endif

// -----------------------------------------------Arat----------------------------------------------- //

	if (pTextTail->pLevelTextInstance)
	{
		CGraphicTextInstance::Delete(pTextTail->pLevelTextInstance);
		pTextTail->pLevelTextInstance = NULL;
	}

// -----------------------------------------------Altina Ekle----------------------------------------------- //

#ifdef ___SALTANAT_SEVIYEYE_GORE_IKON___
	if (pTextTail->pSaltanatFlagInstance)
	{
		CGraphicImageInstance::Delete(pTextTail->pSaltanatFlagInstance);
		pTextTail->pSaltanatFlagInstance = NULL;
	}
#endif
