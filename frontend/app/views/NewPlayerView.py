from ..models import Player
from ..data import globalInstance
from .AbstractView import AbstractView
from .EnterDungeonView import EnterDungeonView

class NewPlayerView(AbstractView):
	
	@staticmethod
	def Show():
		print("\n\t\t--Nuevo Jugador--\n\n")
		name = input("\tNombre: ")
		print(f'\n\tEstá seguro de usar el nombre {name}? (Y or N)')
		decision = AbstractView.Decision(['y', 'n'])
		if(decision == 'y'):
			print(f'\n\t¡Bienvenido {name}!\n')
			player = NewPlayerView.CreatePlayer(name)
			globalInstance.SetPlayer(player)
			globalInstance.SetView(EnterDungeonView)
			return;

	@staticmethod
	def CreatePlayer(name):
		player = Player(name)
		player.Save()
		return player