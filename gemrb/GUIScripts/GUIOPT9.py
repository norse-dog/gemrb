#feedback
import GemRB

GamePlayWindow = 0
TextAreaControl = 0

def OnLoad():
	global GamePlayWindow, TextAreaControl
	GemRB.LoadWindowPack("GUIOPT")
	GamePlayWindow = GemRB.LoadWindow(9)

	S1 = GemRB.GetControl(GamePlayWindow, 30)
	S2 = GemRB.GetControl(GamePlayWindow, 31)

	B1 = GemRB.GetControl(GamePlayWindow, 32)
	B1B = GemRB.GetControl(GamePlayWindow, 10)

	B2 = GemRB.GetControl(GamePlayWindow, 33)
	B2B = GemRB.GetControl(GamePlayWindow, 11)

	B3 = GemRB.GetControl(GamePlayWindow, 34)
	B3B = GemRB.GetControl(GamePlayWindow, 12)

	B4 = GemRB.GetControl(GamePlayWindow, 35)
	B4B = GemRB.GetControl(GamePlayWindow, 13)

	B5 = GemRB.GetControl(GamePlayWindow, 36)
	B5B = GemRB.GetControl(GamePlayWindow, 14)

	B6 = GemRB.GetControl(GamePlayWindow, 37)
	B6B = GemRB.GetControl(GamePlayWindow, 15)
	OkButton = GemRB.GetControl(GamePlayWindow, 26)
	CancelButton = GemRB.GetControl(GamePlayWindow, 27)
	TextAreaControl = GemRB.GetControl(GamePlayWindow, 28)

        GemRB.SetText(GamePlayWindow, TextAreaControl, 18043)
        GemRB.SetText(GamePlayWindow, OkButton, 11973)
        GemRB.SetText(GamePlayWindow, CancelButton, 13727)
	
	GemRB.SetEvent(GamePlayWindow, S1, 0x00000000, "S1Press")
#	GemRB.SetEvent(GamePlayWindow, S1S, 0x00000000, "S1SChange")
	GemRB.SetEvent(GamePlayWindow, S2, 0x00000000, "S2Press")
#	GemRB.SetEvent(GamePlayWindow, S2S, 0x00000000, "S2SChange")

	GemRB.SetEvent(GamePlayWindow, B1, 0x00000000, "B1Press")
	GemRB.SetEvent(GamePlayWindow, B1B, 0x00000000, "B1BPress")
	GemRB.SetEvent(GamePlayWindow, B2, 0x00000000, "B2Press")
	GemRB.SetEvent(GamePlayWindow, B2B, 0x00000000, "B2BPress")
	GemRB.SetEvent(GamePlayWindow, B3, 0x00000000, "B3Press")
	GemRB.SetEvent(GamePlayWindow, B3B, 0x00000000, "B3BPress")
	GemRB.SetEvent(GamePlayWindow, B4, 0x00000000, "B4Press")
	GemRB.SetEvent(GamePlayWindow, B4B, 0x00000000, "B4BPress")
	GemRB.SetEvent(GamePlayWindow, B5, 0x00000000, "B5Press")
	GemRB.SetEvent(GamePlayWindow, B5B, 0x00000000, "B5BPress")
	GemRB.SetEvent(GamePlayWindow, B6, 0x00000000, "B6Press")
	GemRB.SetEvent(GamePlayWindow, B6B, 0x00000000, "B6BPress")
        GemRB.SetEvent(GamePlayWindow, OkButton, 0x00000000, "OkPress")
        GemRB.SetEvent(GamePlayWindow, CancelButton, 0x00000000, "CancelPress")
        GemRB.ShowModal(GamePlayWindow)
	return

def S1Press():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18024)
	return

def S1SChange():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18024)
#also handle slider1
	return

def S2Press():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18025)
	return

def S2SChange():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18025)
#also handle slider2
	return

def B1Press():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18026)
	return

def B1BPress():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18026)
#also handle to hit feedback
	return

def B2Press():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18027)
	return

def B2BPress():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18027)
#also handle combat info
	return

def B3Press():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18028)
	return

def B3BPress():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18028)
#also handle actions
	return

def B4Press():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18029)
	return

def B4BPress():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18029)
#also handle state changes
	return

def B5Press():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18030)
	return

def B5BPress():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18030)
#also handle selection
	return

def B6Press():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18031)
	return

def B6BPress():
        global GamePlayWindow, TextAreaControl
	GemRB.SetText(GamePlayWindow, TextAreaControl, 18031)
#also handle misc. feedback
	return

def OkPress():
        global GamePlayWindow, TextAreaControl
        GemRB.SetVisible(GamePlayWindow, 0)
        GemRB.UnloadWindow(GamePlayWindow)
        GemRB.SetNextScript("GUIOPT8")
        return

def CancelPress():
        global GamePlayWindow, TextAreaControl
        GemRB.SetVisible(GamePlayWindow, 0)
        GemRB.UnloadWindow(GamePlayWindow)
        GemRB.SetNextScript("GUIOPT8")
        return

