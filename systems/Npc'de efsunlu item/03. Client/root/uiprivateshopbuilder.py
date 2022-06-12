# Ekle :
import app

# Arat :
# pyScrLoader.LoadScriptFile(self, "UIScript/PrivateShopBuilder.py")
# Deðiþtir :

			if app.ENABLE_2TH_SHOPEX_SYSTEM:
				pyScrLoader.LoadScriptFile(self, "UIScript/PrivateShopExBuilder.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/PrivateShopBuilder.py")