
class Global:
	def __init__(self) -> None:
		self.view = None
		self.CurrentPlayer = None

	def SetView(self, view):
		self.view = view
	def SetPlayer(self, player):
		self.CurrentPlayer = player

	def GetView(self):
		return self.view
	def GetPlayer(self):
		return self.CurrentPlayer

globalInstance = Global()