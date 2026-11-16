# Ara:
import localeInfo
import uiCommon

# Altina ekle:
import uiCharacterDetails


# DropDown.__init__ icinde ara:
		self.scrollBar = None
		if self.hasScroll:

# Altina ekle:
			self.scrollBar = uiCharacterDetails.DetailsScrollBar()


# GuildApplicationWindow.__MakeMemberWindow icinde ara:
			row.Hide()
			self.guildRows.append(row)

# Altina ekle:
		self.listScrollBar = uiCharacterDetails.DetailsScrollBar()


# GuildApplicationWindow.__MakeLeaderWindow icinde ara:
			row.Hide()
			self.appRows.append(row)

# Altina ekle:
		self.appScrollBar = uiCharacterDetails.DetailsScrollBar()

