from .AbstractView import AbstractView

class NewPlayerView(AbstractView):
	
	@staticmethod
	def Show():
		print("\n\t\t--Nuevo Jugador--\n\n")
		name = input("\tNombre: ")