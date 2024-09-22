
class Global:
	def __init__(self) -> None:
		self.view = None

	def ChangeView(self, view):
		self.view = view

	def GetView(self):
		return self.view


globalInstance = Global()