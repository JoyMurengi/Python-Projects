
# Hangman Game

A fun and interactive Hangman Game built with Python's Tkinter and Turtle libraries, showcasing GUI programming, event handling, and simple game logic.

---

## Overview
The Hangman Game is a Python project that challenges players to guess hidden words from different themes such as History, Computers, and Cars.  
It includes two playable versions:

1. **main.py** – A graphical version using Tkinter and Turtle.  
2. **hang_man.py** – A Turtle-only version that runs directly in the Turtle graphics window.  

Both versions rely entirely on Python’s built-in libraries and do not require any external installations.

---

## Features

### main.py (Tkinter + Turtle)
- Graphical interface built with Tkinter.  
- Theme selection menu (History, Computers, Cars).  
- Dynamic hangman drawing using Turtle graphics.  
- Real-time word display updates after each guess.  
- Input validation for single alphabet letters.  
- Pop-up messages for wins and losses.  
- Restart button for new game rounds.  

### hang_man.py (Turtle Only)
- Randomly selects a theme and word each game.  
- Step-by-step hangman drawing using Turtle.  
- Displays guessed letters and failed attempts.  
- Accepts input through Turtle’s text dialog box.  

---

## How to Play
1. A random word is chosen from the selected theme.  
2. Guess one letter at a time.  
3. Correct guesses reveal letters in the word.  
4. Each wrong guess draws part of the hangman.  
5. You have 6 total wrong attempts before losing.  
6. The game ends when you guess the full word or reach the attempt limit.  

---

## How to Run

### Tkinter GUI Version
```bash python main.py

## Purpose
This project was developed to strengthen my understanding of Python fundamentals, GUI development, and visualization using Turtle.  
It demonstrates logic handling, user input validation, and integration of multiple built-in Python modules.

---

## Key Concepts Demonstrated
- GUI programming with **Tkinter**
- Graphics and animation with **Turtle**
- Randomization and data structures (**lists**, **sets**, **dictionaries**)
- Control flow using loops and conditionals
- Event-driven programming and state management

---

## What I Learned
- How to combine Tkinter and Turtle within a single window.
- How to handle user input and feedback in a game setting.
- How to structure Python code for readability and reusability.
- The importance of step-by-step logic when building interactive applications.

---

## Future Improvements
- Add difficulty levels (easy, medium, hard).
- Include a hint or letter reveal system.
- Add score tracking and leaderboards.
- Refactor into an object-oriented design for scalability.

---

## Requirements
- **Python 3.8 or higher**
- Built-in libraries only:
  - `tkinter`
  - `turtle`
  - `random`

---

## License
This project is open-source and available under the **MIT License**.

---

## Author
**Joy Nduta**  
Python developer passionate about creative coding and beginner-friendly projects.




