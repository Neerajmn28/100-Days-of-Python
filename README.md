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




## Project Description: GUI Quiz Game
This project is a Python-based graphical user interface (GUI) quiz game built using the tkinter library. The quiz game fetches trivia questions from the Open Trivia Database API and displays them to the user in a user-friendly format. The user answers the questions by clicking either the 'True' or 'False' buttons, and their score is updated and displayed on the screen.

 Project Logic Breakdown:
Fetching Questions from API:

Uses the requests library to fetch trivia questions from the Open Trivia Database API.

Requests a set of 10 questions of type 'boolean' (True/False).

The received questions are stored in a list called question_data.

Question Model Class:

The Question class is used to model each question with two attributes:

text: The actual question text.

answer: The correct answer (either 'True' or 'False').

QuizBrain Class (Backend Logic):

Manages the quiz flow and scoring.

Tracks the current question, user’s score, and total questions.

Contains methods for:

Fetching the next question.

Checking the user’s answer.

Returning feedback based on the correctness of the answer.

Keeping track of the quiz progress.

QuizInterface Class (Frontend GUI):

Uses tkinter to create a window and display the quiz game.

Components:

A Label widget to show the current score.

A Canvas widget to display the question text.

Two Button widgets for 'True' and 'False' responses.

When a button is pressed, the answer is checked, and feedback is displayed by changing the canvas color.

After 1 second, the next question is automatically displayed.

User Interaction Handling:

User clicks either 'True' or 'False'.

The answer is validated, and the score is updated if correct.

Visual feedback is provided (green for correct, purple for incorrect).

Progresses to the next question after a delay.

Completion Handling:

When all questions are answered, the buttons are disabled, and a message indicating the end of the quiz is displayed.


![Image](https://github.com/user-attachments/assets/30b01a76-d9ae-4843-b670-2706d40a4260)
