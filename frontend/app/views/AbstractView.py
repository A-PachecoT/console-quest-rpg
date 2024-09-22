from abc import ABC, abstractmethod
import os


class AbstractView(ABC):
	
	@staticmethod
	@abstractmethod
	def Show() -> None:
		pass

	@classmethod
	def Clear(cls) -> None:
		os.system('cls' if os.name == 'nt' else 'clear')


	@staticmethod
	def Decision(posibilites: list) -> str:
		while True:
			try:
				decision = int(input('\n\t\t'))
				if decision in posibilites:
					return decision
				else:
					print('\n\tPor favor, ingrese una opcion valida\n')
				break
			except ValueError:
				print('\n\tPor favor, ingrese una opcion valida\n')