from abc import ABC, abstractmethod
from pydantic import BaseModel, Field

class Stats(BaseModel):
	strength: int = Field(default=0, ge=0)
	agility: int = Field(default=0, ge=0)
	intelligence: int = Field(default=0, ge=0)
	vitality: int = Field(default=0, ge=0)

class AbstractCharacter(ABC, BaseModel):
	_id: int
	_name: str

	_level: int = Field(default=1, ge=1)

	_hp: int = Field(default=100, ge=0)
	_maxHp: int = Field(default=100, ge=0)

	_stats: Stats = Stats()

	def __init__(self, id, name, level, hp, maxHp) -> None:
		super().__init__()
		self._id = id
		self._name = name
		self._level = level
		self._hp = hp
		self._maxHp = maxHp
	
	@abstractmethod
	def Die(self) -> None:
		self._hp = 0

	def GetId(self) -> int:
		return self._id
	def GetName(self) -> str:
		return self._name
	def GetLevel(self) -> int:
		return self._level
	def GetHp(self) -> int:
		return self._hp
	def GetMaxHp(self) -> int:
		return self._maxHp 
	


