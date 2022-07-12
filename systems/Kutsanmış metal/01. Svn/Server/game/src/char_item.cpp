// Arat
		case BLACKSMITH_MOB:
			if (item->GetRefinedVnum() && item->GetRefineSet() < 500)
			{
				return true;
			}
			else
			{
				return false;
			}

// Degistir
		case BLACKSMITH_MOB:
#ifdef ENABLE_BLESSED_METAL_SYSTEM
			if (item->GetRefineSet() >= 100 && item->GetRefineSet() < 500)
#else
			if (item->GetRefinedVnum() && item->GetRefineSet() < 500)
#endif
			{
				return true;
			}
			else
			{
				return false;
			}
#ifdef ENABLE_BLESSED_METAL_SYSTEM
		case MAVIRUH_BLESSED_METAL_NPC:
			if (item->GetRefineSet() >= 0 && item->GetRefineSet() < 100)
			{
				return true;
			}
			else
			{
				return false;
			}
#endif

// Arat
		case BLACKSMITH_MOB:
		case BLACKSMITH2_MOB:
		case BLACKSMITH_WEAPON_MOB:
		case BLACKSMITH_ARMOR_MOB:
		case BLACKSMITH_ACCESSORY_MOB:

// Altina Ekle
#ifdef ENABLE_BLESSED_METAL_SYSTEM
		case MAVIRUH_BLESSED_METAL_NPC:
#endif