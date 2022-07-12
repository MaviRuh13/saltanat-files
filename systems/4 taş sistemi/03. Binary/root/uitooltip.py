# Arat (def SetHyperlinkItem(self, tokens): icinde)
			metinSlot = [int(metin, 16) for metin in tokens[3:6]]
# Degistir
			if app.ENABLE_FOUR_STONE_SYSTEM:
				metinSlot = [int(metin, 16) for metin in tokens[3:7]]
			else:
				metinSlot = [int(metin, 16) for metin in tokens[3:6]]

# Arat (def SetHyperlinkItem(self, tokens): icinde)
			rests = tokens[6:]

# Degistir
			if app.ENABLE_FOUR_STONE_SYSTEM:
				rests = tokens[7:]
			else:
				rests = tokens[6:]