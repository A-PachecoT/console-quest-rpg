from .AbstractView import AbstractView

class EnterDungeonView(AbstractView):
	
	@staticmethod
	def Show():
		print('\n\t\t--Bienvenido a la Mazmorra--\n\n')
		print('\t(1) Combate\n')
		print('\t(2) Ver Jugador\n')
		print('\t(0) Salir\n\n')

		decision = AbstractView.Decision(['1', '2', '0'])
		if(decision == '1'): #explorar
			pass
			# explorar()
		elif(decision == '2'): #ver inventario
			pass
			# ver_inventario()
		elif(decision == '0'): #salir
			pass
			# salir()