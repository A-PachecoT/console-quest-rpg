from abc import ABC, abstractmethod

class Stats():
	strength: int
	agility: int
	intelligence: int
	vitality: int
	
	def __init__(self) -> None:
		self.strength = 1
		self.agility = 1
		self.intelligence = 1
		self.vitality = 1

class AbstractCharacter(ABC):
	name: str

	level: int
	hp: int
	maxHp: int

	stats: Stats

	def __init__(self, name, level = 1, hp = 100, maxHp = 100) -> None:
		self
		self.level = level
		self.hp = hp
		self.maxHp = maxHp
	
	@abstractmethod
	def Die(self) -> None:
		self.hp = 0

	@abstractmethod
	def Attack(self, target) -> None:
		pass

	def GetName(self) -> str:
		return self._name
	def GetLevel(self) -> int:
		return self._level
	def GetHp(self) -> int:
		return self._hp
	def GetMaxHp(self) -> int:
		return self._maxHp 
	


