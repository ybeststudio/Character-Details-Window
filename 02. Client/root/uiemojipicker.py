# Ara:
import localeInfo
import ui

# Altina ekle:
import uiCharacterDetails


# EmojiSelectorWindow.__Build icinde ara:
		self.content.OnMouseWheel = ui.__mem_func__(self.OnMouseWheel)
		self.content.Show()

# Altina ekle:
		self.scrollBar = uiCharacterDetails.DetailsScrollBar()

