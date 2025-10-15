import turtle
import random
Themes = {"history": ["marco polo", "napoleon", "mesopotamia", "persia", "world war"],
    "computers": ["bus", "semiconductor", "keyboard", "vacuum tube", "nanometer"],
    "cars": ["dodge", "toyota", "daihatsu", "displacement", "stroke"]}
theme = random.choice(list(Themes.keys()))
word_to_guess = random.choice(Themes[theme]).lower()
display_word = ['_'if c.isalpha() 
                else c for c in word_to_guess]
guessed_letters = set()
max_attempts = 6
failed_attempts = 0
#set up turtle screen
screen = turtle.Screen()
screen.title("Hangman Game")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
#draw hangman step by step
def draw_hangman(stage):
    pen.penup()
    if stage == 1:
        pen.goto(-100, -150)
        pen.setheading(0)
        pen.pendown()
        pen.forward(200)
    elif stage == 2:
        pen.penup()
        pen.goto(0, -150)
        pen.setheading(90)
        pen.pendown()
        pen.forward(250)
    elif stage == 3:
        pen.setheading(0)
        pen.forward(100)
    elif stage == 4:
        pen.setheading(270)
        pen.forward(50)
    elif stage == 5:
        pen.circle(20)
    elif stage == 6:
        pen. penup()
        pen.goto(pen.xcor(), pen.ycor() - 40)
        pen. setheading(270)
        pen.pendown()
        pen.forward(60)
    #Display current game state
def show_word():
        pen.clear()
        pen.penup()
        pen.goto(-200, 180)
        pen.write(f"Theme:{theme.title()}", font=("Courier", 16, "bold"))
        pen.goto(-200, 140)
        pen.write("Word: " + " ".join(display_word), font=("Courier", 20, "normal"))
        pen.goto(-200, 100)
        pen.write(f"Wrong attempts: {failed_attempts} / {max_attempts}", font=("Courier", 16, "normal"))
        pen.goto(-200, 60)
        pen.write("Guessed letters: " + ", ".join(sorted(guessed_letters)), font=("Courier", 14, "normal"))

# Function to show final result
def end_game(win):
    pen.goto(-200, -20)
    if win:
        pen.write("You Won!", font=("Courier", 24, "bold"))
    else:
        pen.write(f"You Lost! Word was: {word_to_guess}", font=("Courier", 20, "bold"))

# Main game function
def play_game():
    global failed_attempts
    show_word()
    while failed_attempts < max_attempts and "_" in display_word:
        guess = screen.textinput("Your Guess", "Enter a letter: ")
        if not guess:
            continue
        guess = guess.lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            continue
        if guess in guessed_letters:
            continue
        guessed_letters.add(guess)
        if guess in word_to_guess:
            for i, c in enumerate(word_to_guess):
                if c == guess:
                    display_word[i] = guess
        else:
            failed_attempts += 1
            draw_hangman(failed_attempts)
        show_word()
    if "_" not in display_word:
        end_game(win=True)
    else:
        end_game(win=False)

play_game()
turtle.done()
        
        
        
        
