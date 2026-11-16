# Ara:
	import uiSkillColor
if app.ENABLE_DETAILS_UI:

# Altina ekle:
	import uiCharacterDetails


# CharacterWindow.__ClickExpandButton icinde ara:
		def __ClickExpandButton(self):
			if not self.chDetailsWnd:

# Altina ekle:
				self.chDetailsWnd = uiCharacterDetails.CharacterDetailsUI(self)

