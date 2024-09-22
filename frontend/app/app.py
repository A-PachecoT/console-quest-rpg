import time
from .data import globalInstance
from .views.MainMenuView import MainMenuView, AbstractView

def Update():
	AbstractView.Clear()
	time.sleep(0.5)
	globalInstance.GetView().Show()

def Start():
	globalInstance.SetView(MainMenuView)