from .AbstractCharacter import AbstractCharacter

class Player(AbstractCharacter):
	
	id: int

	exp: int
	targetExp: int
	gold: int

	def __init__(self, name, id = 0, level = 1, hp = 100, maxHp = 100, exp = 0, targetExp = 10, gold = 0) -> None:
		super().__init__(name, level, hp, maxHp)
		self.id = id
		self.exp = exp
		self.targetExp = targetExp
		self.gold = gold

	def LevelUp(self) -> None:
		self.level += 1
		self.maxHp += 10
		self.hp = self._maxHp
		self._targetExp *= 0.1 
	
	def GainExp(self, exp: int) -> None:
		self.exp += exp
		if self.exp >= self._targetExp:
			self.LevelUp()
			self.exp = 0
	
	def Attack(self, target: AbstractCharacter) -> None:
		pass

	def Save(self):
		pass

	def Die(self) -> None:
		return super().Die()

	def GetId(self) -> int:
		return self._id
	def GetExp(self) -> int:
		return self._exp
	def GetTargetExp(self) -> int:
		return self._targetExp
	def GetGold(self) -> int:
		return self._gold



