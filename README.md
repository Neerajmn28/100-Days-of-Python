# 100 Days of Python 🐍

Welcome to the **100 Days of Python** learning! 
🚀 This repository documents my journey to master Python, covering everything from the fundamentals to advanced concepts, projects, and real-world applications.


## FLASH CARD TO IMPROVE GERMAN VOCABS:
This project is a flashcard-based language learning app built using Python's Tkinter for the graphical user interface (GUI) and pandas for managing vocabulary data. The app helps users learn German vocabulary by showing them flashcards with the German word on one side and the English translation on the other. Users can interact with the flashcards by marking whether they know the word or not. The goal is to reinforce learning through repetition and active recall.


(HOW THIS WORKS)
* Data Loading:

When the app starts, it attempts to load the vocabulary data from a CSV file (words_to_learn.csv). If the file does not exist (for new users), it loads data from a fallback file (german words - Sheet1.csv).

* Displaying a Card:

The next_card function randomly selects a word from the vocabulary list (to_learn), updates the front of the card with the German word, and sets a timer to flip the card after 3 seconds to show the English translation.

* Flipping the Card:

After 3 seconds, the show_answer function is triggered, displaying the English translation and changing the background image to the back of the card.

* User Marking a Word as Known:

When the user clicks the "known" button, the word is removed from the to_learn list and the vocabulary data is saved back to the CSV file (words_to_learn.csv). This ensures the user only sees words they need to learn.

* UI Components:

The flashcards are displayed using a Canvas widget, and images are used for the front and back of the card.

Two buttons allow the user to interact with the flashcards, marking words as known or unknown.

* Persistent Data:

As the user marks words as "known," those words are removed from the vocabulary list, and the updated list is saved back to a CSV file. This allows the app to remember the progress across sessions

![Image](https://github.com/user-attachments/assets/bfcf78e8-6ebb-4c0c-ac1b-d357181e1298)



## Project Description
This project is a classic Snake Game built using Python’s Turtle module. The game features a moving snake that grows in length as it consumes food, with the goal of achieving the highest possible score without colliding with the walls or itself.

Features
* Snake Movement: The snake moves in four directions—up, down, left, and right—using keyboard controls.
* Food Generation: The game randomly places food on the screen, and the snake consumes it to grow.
* Scoreboard System: Displays the current score and keeps track of the highest score.
* Collision Detection: The game detects when the snake collides with the walls or its own body.
* Game Reset: The game resets when the player loses, updating the high score and restarting the snake.
* Smooth Animation: The game uses the screen.tracer(0) and screen.update() functions to create smooth animations.
![Image](https://github.com/user-attachments/assets/3addd781-fd45-40cf-9c82-636942827c06)
## Turtle Crossing Game
Description
This is a simple Turtle Crossing Game built using Python's turtle module. The player controls a turtle that must cross a road while avoiding moving cars. The game gets progressively harder as the player advances through levels.

Features
* Player Movement: Move the turtle upwards using the Up Arrow key.
* Obstacle Cars: Cars spawn randomly and move from right to left.
* Scoreboard: Displays the current level and updates upon successful crossings.
* Game Over Condition: The game ends if the turtle collides with a car.

![Image](https://github.com/user-attachments/assets/7c6c553f-6285-4973-ab65-79179eaa7df9)



## Pomodoro Timer
Project Overview: The Pomodoro Timer is a productivity tool designed to help users stay focused and manage their work and break intervals efficiently. Based on the popular Pomodoro Technique, this app divides work into 25-minute intervals (called Pomodoros) separated by short breaks. After completing four Pomodoros, users are rewarded with a longer break. The timer provides a visual countdown and checkmarks to track the number of completed work sessions.

Key Features:

* Start & Reset Functionality: Users can start and reset the timer with simple button clicks.
* Visual Timer: A dynamic countdown timer is displayed, showing minutes and seconds.
* Work & Break Sessions: The timer alternates between work and break intervals, with distinct colors to differentiate between the two (green for work, pink for short breaks, red for long breaks).
* Progress Tracker: Checkmarks appear after each completed work session to show the user their progress.
* Customizable Intervals: Users can modify work, short break, and long break durations based on their preference.
Technologies Used:

![Image](https://github.com/user-attachments/assets/14a6835b-0830-4b73-9831-8e4cfeec78f6)
