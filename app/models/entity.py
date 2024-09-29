from pydantic import BaseModel


class Entity(BaseModel):
	name: str

	level: int = 1

	current_hp: int = 100
	max_hp: int = 100

	attack: int = 10
	defense: int = 5

	is_defendig: bool = False
	
	def Attack(self, target):
		damageMitigation = (target.defense)/(target.defense + 5)
		extraMitigation = 0.3 if target.is_defendig else 0
		damage = self.attack * (1-damageMitigation) * (1-extraMitigation);
		target.current_hp -= damage;
		target.is_defendig = False
		return "{self.name} attacked {target.name} for {damage} damage"
	
	def Defend(self):
		self.is_defendig = True
		return "{self.name} is defending"

	def TakeTurn(self, target, action:int):
		if action == 1:
			return self.Attack(target)
		if action == 2:
			return self.Defend()
		return "Invalid action"
		

	class Config:
		schema_extra = {
			"example": {
				"id": 1,
				"name": "Goblin",
				"level": 1,
				"current_hp": 100,
				"max_hp": 100,
				"attack": 10,
				"defense": 5,
			}
		}