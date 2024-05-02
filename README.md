Snake and Ladder
================

This Python script is a digital(Non GUI) version of the classic "Snake and Ladder" board game for multiple players. Players take turns rolling a virtual dice to move on the board. 

Initialization:
---------------

Players are prompted to enter their names, and the game begins with a set number of players.

Each player starts at position 0 on the board.

Game Mechanics:
--------------
Players take turns rolling a virtual dice (random number between 1 and 6).

Upon rolling the dice, players move forward on the board based on the dice result.

The game includes predefined "snakes" and "ladders" on certain board positions:
Landing on a snake position moves the player backward to a lower position.
Landing on a ladder position moves the player forward to a higher position.

Players cannot exceed position 100; if their roll would take them beyond 100, they must wait until their next turn.

Win Condition:
--------------
The game ends when a player reaches position 100, signifying completion of the board.

Upon completing the game, players are informed of their victory.

Instructions:
--------------
Players should roll a 1 to start the game.

The game continues in a loop until all players have completed the board.

Snakes move players down to lower positions, while ladders move players up to higher positions.

Ensure each player rolls the dice during their turn to progress through the game.

Key Features:
-------------

Warns about the snakes and ladders in next 6 steps from players current position.

Shows interesting messages, which makes the game interesting.
