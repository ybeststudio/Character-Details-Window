# Ara:
import grp
import time

# Altina ekle:
import uiCharacterDetails


# WhisperMessenger.__Build icinde ara:
		self.listWindow.OnMouseWheel = ui.__mem_func__(self.__OnListWheel)
		self.listWindow.Show()

# Altina ekle:
		self.listScrollBar = uiCharacterDetails.DetailsScrollBar()


# WhisperMessenger.__Build icinde ara:
		self.chatWindow.OnMouseWheel = ui.__mem_func__(self.__OnChatWheel)
		self.chatWindow.Show()

# Altina ekle:
		self.chatScroll = uiCharacterDetails.DetailsScrollBar()

