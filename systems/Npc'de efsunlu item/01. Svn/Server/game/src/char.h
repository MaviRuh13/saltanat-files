// Arat
#define __INC_METIN_II_CHAR_H__

// Alt�na Ekle
#define ENABLE_2TH_SHOPEX_SYSTEM

// Arat :
// // End of Money
// Alt�na Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM	
		////////////////////////////////////////////////////////////////////////////////////////
		// Dragon Coin related
		DWORD			GetDragonCoin();
		DWORD			GetDragonMark();
		
		void			SetDragonCoin(DWORD amount);
		void			SetDragonMark(DWORD amount);
		
		void			RefreshDragonCoin();
		// End Of Dragon Coin
#endif