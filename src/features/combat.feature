Feature: Combat
	As a player
  	I need to  combat
  	So that I can fight against enemies
	
	Scenario: Player start the combat
		Given a player not in combat
		When the player start the combat
		Then the player is in combat
	
	Scenario: Player attack enemy
		Given a player in combat and the enemy with 50 HP
		When the player attacks
		Then the enemy should have less than 50 HP
	
	Scenario: Player defend
		Given a player with 1 enemies
		When the player defend
		Then the player should be defending