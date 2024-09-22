from .AbstractView import AbstractView
from .NewPlayerView import NewPlayerView
from ..data import globalInstance

class MainMenuView(AbstractView):
	
	@staticmethod
	def Show():
		print('\n\t\t--Bienvenido a Console Quest--\n\n')
		print('\t(1) Nueva Partida\n')
		print('\t(2) Cargar Partida\n')
		print('\t(0) Salir\n\n')

		decision = AbstractView.Decision(['0', '1', '2'])
		if(decision == '1'): #nueva partida
			globalInstance.SetView(NewPlayerView)
			return;

		elif(decision == '2'): #cargar_partida
			pass
			# lista = cargar_partida()
			# if(lista[1]!= 0):    
			# 	menu_juego(lista[0])

		elif(decision == '0'): #salir del juego
			print('\n\t¿Está seguro de salir del juego? (Y or N)')
			decision = AbstractView.Decision(['y', 'n'])
			if(decision == 'y'):
				exit();