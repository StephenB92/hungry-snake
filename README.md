# Hungry Snake

## Project Overview

Hungry Snake - The classic mobile game makes it's way to the Python Command Line Interface!! Control the snake to eat food and grow as big as you can to earn more points. The game is over if the snake runs into the edge of the screen or eats it's own tail!

## Project Goals and Target Audience

Hungry Snake is intended to be picked up and played by anyone! The aim of the game is to move the snake around the board and collect food. As the snake eats food, it becomes bigger and the user's score is increased. The game will end if the snake runs into the edge of the board or it it eats it's own tail. The game features multiple levels of difficulty to challenge players of all levels.

### User Stories

1. I want a game I can pick up and play that doesn't take too much time. Snake is perfect for when I have a few minutes to kill while I'm waiting to join a call and want to occupy myself that can be fun and challenging. 
2. I have played Snake before as a child on my old mobile phone and I am very used to how the game plays. Having the option of increasing the difficulty is very useful as I then have the option to make the game more difficult and engaging.

## Coding Languages Used

1. Python

## Wireframes

1. Please wireframe for the game on initialisation [here](assets/wireframes/start-of-game.png).

## Features

### Existing Features

1. Controlling the Snake. As soon as the game loads, the initial piece of food is created and users must use the directional buttons on their keyboard to steer the snake towards it.
2. Collision detection. As per the rules of the classic game, the game is over if the snake runs into the edge of the screen or into itself. The game has been coded to react to these instances when they occur and end the game when they do.
3. Pause button. The user can pause the game at any point by pressing the space key. 
4. Quit game. The user can quit the game and end the programme at any time by pressing the Escape key. This game is programmed to run as a "While Loop" that runs only while the key pressed by the user is NOT the escape key. Once pressed, the loop and game are closed.

### Future Features

1. Mongoose mode. In a future update, I would like to create an extra difficulty that includes a mongoose (an animal known for preying on snakes) that also appears on the map and which players also must avoid while collecting food.
2. User save data. In a future update, I would like to include a feature that can retain the user's high score even after the game has been closed.

## Testing

## Bugs and Fixes

### Fixed Bugs

1. I had been having a significant issue while developing this project in trying to program the snake to move automatically in the direction of the last directional button the user pressed, until the next direction is pressed. Of course, this is a fundamental aspect of the game. In the initial incarnation of the project, the snake could only be moved manually as the user presses directional keys, effectively removing any difficulty from the game as users could just control the snake space by space. This led to me having to overhaul the code and use a different template to start with. While this was not ideal due to the impending deadline, the change was successful and the base game now runs as intended. Credit to the tutorial from The AI Learner below.
2. After programming the "Quit Game" and "Pause Game" features, I noticed while testing these features that if a player pressed the escape key while the game is paused, the input from pressing the escape key would appear as "^[" in the middle of the game board and would remain there even when the game is resumed. This was fixed by adding "curses.noecho()" to my code which effectively stops player input from being echoed to appear in the game window.

### Unfixed Bugs

1. The CLI cursor can still be seen on the head of the snake. This did not appear to be an issue until I first attemped to deploy this project on Heroku. Initially, my code included the command "curses.curs_set(0)" which renders the users cursor invisible while the programme is running. However, this returned an error when deplying on Heroku.

## Deployment

## Credits

### Code Used
- Credit to YouTube user Indian Pythonista and their video [Creating Snake Game for Terminal | Intro to curses in Python (Part-3)](https://www.youtube.com/watch?v=BvbqI6eDh0c&list=WL&index=4) for the code and template used to create the game window, using the "curses" module.
- Credit to The AI Learner and the article [Snake Game using Python Curses](https://theailearner.com/2019/03/10/snake-game-using-python-curses/) for code used as a template for this project.
- Credit to [sanchitgangwar on Github](https://gist.github.com/sanchitgangwar/2158084), for code used for the pause game and quit game features. 