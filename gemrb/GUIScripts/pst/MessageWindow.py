import GemRB

from GUICommonWindows import *

from FloatMenuWindow import *

from GUIJRNL import *
from GUIMA import *
from GUIMG import *
from GUIINV import *
from GUIOPT import *
from GUIPR import *
from GUIREC import *
from GUISTORE import *
from GUIWORLD import *


MessageWindow = 0
ActionsWindow = 0
PortraitWindow = 0
OptionsWindow = 0
CloseButton = 0
OpenButton = 0
MaxExpand = 1

def OnLoad():
	global MessageWindow, ActionsWindow, PortraitWindow, OptionsWindow, CloseButton
	GemRB.LoadWindowPack("GUIWORLD")
	GemRB.SetInfoTextColor(0,255,0,255)
	ActionsWindow = GemRB.LoadWindow(0)
	PortraitWindow = GemRB.LoadWindow(1)
	PopulatePortraitWindow ()
	OptionsWindow = GemRB.LoadWindow(2)
	MessageWindow = GemRB.LoadWindow(7)
	MessageTA = GemRB.GetControl(MessageWindow, 1)
	GemRB.SetTAAutoScroll(MessageWindow, MessageTA, 1)
	GemRB.SetVar("PortraitWindow", PortraitWindow)
	GemRB.SetVar("ActionsWindow", ActionsWindow)
	GemRB.SetVar("OptionsWindow", OptionsWindow)
	GemRB.SetVar("MessageWindow", -1)
	GemRB.SetVar("OtherWindow", -1)
	GemRB.SetVar("PortraitPosition", 1) #Bottom
	GemRB.SetVar("ActionsPosition", 1) #Bottom
	GemRB.SetVar("OptionsPosition", 1) #Bottom
	GemRB.SetVar("MessagePosition", 1) #Bottom
	GemRB.SetVar("OtherPosition", 0) #Left
	
	GemRB.SetVar("MessageTextArea", MessageTA)
	GemRB.SetVar("MessageWindowSize", 0)
	
	CloseButton= GemRB.GetControl(MessageWindow, 0)
	GemRB.SetText(MessageWindow, CloseButton, 28082)
	
	OpenButton = GemRB.GetControl(OptionsWindow, 10)
	GemRB.SetEvent(OptionsWindow, OpenButton, IE_GUI_BUTTON_ON_PRESS, "OnIncreaseSize")

	FormationButton = GemRB.GetControl(ActionsWindow, 4)
	GemRB.SetEvent(ActionsWindow, FormationButton, IE_GUI_BUTTON_ON_PRESS, "OpenFormationWindow")


	SetupMenuWindowControls (OptionsWindow)

	UpdateResizeButtons()
	
	GemRB.SetVisible(ActionsWindow, 1)
	GemRB.SetVisible(PortraitWindow, 1)
	GemRB.SetVisible(OptionsWindow, 1)
	GemRB.SetVisible(MessageWindow, 0)
	return
	
def OnIncreaseSize():
	global MessageWindow, PortraitWindow, ActionsWindow, OptionsWindow
	
	MessageTA = GemRB.GetVar("MessageTextArea")
	Expand = GemRB.GetVar("MessageWindowSize")
	
	if Expand == 1:
		return
		
	GemRB.HideGUI()
	
	if Expand == 0:
		GemRB.SetVar("MessageWindow", MessageWindow)
		GemRB.SetVar("PortraitWindow", -1)
		GemRB.SetVar("ActionsWindow", -1)
		GemRB.SetVar("OptionsWindow", -1)
		GemRB.SetVisible(MessageWindow, 1)
		GemRB.SetVisible(PortraitWindow, 0)
		GemRB.SetVisible(ActionsWindow, 0)
		GemRB.SetVisible(OptionsWindow, 0)
			
	Expand = 1
	
	GemRB.SetVar("MessageWindowSize", Expand)
	UpdateResizeButtons()
	GemRB.UnhideGUI()
	GemRB.SetControlStatus(MessageWindow,MessageTA,IE_GUI_CONTROL_FOCUSED);
	return
	
def OnDecreaseSize():
	global MessageWindow, PortraitWindow, ActionsWindow, OptionsWindow
	
	MessageTA = GemRB.GetVar("MessageTextArea")
	Expand = GemRB.GetVar("MessageWindowSize")
	
	if Expand == 0:
		return
		
	GemRB.HideGUI()
	
	if Expand == 1:
		GemRB.SetVar("MessageWindow", -1)
		GemRB.SetVar("PortraitWindow", PortraitWindow)
		GemRB.SetVar("ActionsWindow", ActionsWindow)
		GemRB.SetVar("OptionsWindow", OptionsWindow)
		GemRB.SetVisible(MessageWindow, 0)
		GemRB.SetVisible(PortraitWindow, 1)
		GemRB.SetVisible(ActionsWindow, 1)
		GemRB.SetVisible(OptionsWindow, 1)
			
	Expand = 0
	
	GemRB.SetVar("MessageWindowSize", Expand)
	UpdateResizeButtons()
	GemRB.UnhideGUI()
	if Expand:
		GemRB.SetControlStatus(MessageWindow,MessageTA,IE_GUI_CONTROL_FOCUSED);
	else:
		GemRB.SetControlStatus(0,0,IE_GUI_CONTROL_FOCUSED);
	return
	
def UpdateResizeButtons():
	global MessageWindow, CloseButton
	
	GemRB.SetEvent(MessageWindow, CloseButton, IE_GUI_BUTTON_ON_PRESS, "OnDecreaseSize")
	return

def PopulatePortraitWindow ():
	Window = PortraitWindow
	size = 6
	party_size = GemRB.GetPartySize ()

	for i in range (size):
		#actor = GemRB.PartyGetActor ()
		if i < party_size:
			pic = GemRB.ActorGetSmallPortrait (i)
			Button = GemRB.GetControl (Window, i)
			#GemRB.SetButtonSprites (Window, Button, pic, 0, 0, 1, 0, 0)
			GemRB.SetButtonBAM (Window, Button, pic, 0, 0, 0)
			GemRB.SetButtonFlags(Window, Button, IE_GUI_BUTTON_PICTURE, OP_SET)
		else:
			pass
