import tkinter as tk 
from  tkinter import  messagebox
import turtle
import random
Themes  = {"history": ["marco polo", "napoleon", "mesopotamia", "persia", "world war"],
    "computers": ["bus", "semiconductor", "keyboard", "vacuum tube", "nanometer"],
    "cars": ["dodge", "toyota", "daihatsu", "displacement", "stroke"]}
 
word_to_guess = "" 
word_display = []
guessed_letters = set()
failed_attempts = 0
max_attempts = 6

root = tk.Tk()
root.title("Hangman Game ")
#canvas and turtle for drawing hangman
canvas = tk.Canvas(root,width = 400,height = 400)
canvas.pack()
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")
drawer = turtle.RawTurtle(screen)
drawer.hideturtle()
drawer.speed(0)
#GUI widgets
theme_var = tk.StringVar(value="history") #tracks which theme is selected
theme_menu = tk.OptionMenu(root, theme_var, *Themes.keys())
theme_menu.pack(pady=5)

word_label = tk.Label(root, text="", font=("Courier", 28))
word_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Arial", 14))#player types a single letter
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", font=("Arial", 12))
guess_button.pack(pady=5)

restart_button = tk.Button(root, text="Restart Game", font=("Arial", 12))
restart_button.pack(pady=10)
restart_button.config(state="disabled")
#Turtle drawing functions
def reset_turtle(): #clears the canvas and resets the turtle before new game starts
    drawer.clear()
    drawer.penup()
    drawer.home()
def draw_hangman(stage): # each wrong guess draws one body part
    steps = {
        1: lambda: drawer.goto(-100, -150) or drawer.setheading(0) or drawer.pendown() or drawer.forward(200),
        2: lambda: drawer.penup() or drawer.goto(0, -150) or drawer.setheading(90) or drawer.pendown() or drawer.forward(250),
        3: lambda: drawer.setheading(0) or drawer.forward(100),
        4: lambda: drawer.setheading(270) or drawer.forward(50),
        5: lambda: drawer.circle(20),
        6: lambda: drawer.penup() or drawer.goto(drawer.xcor(), drawer.ycor() - 40) or drawer.setheading(270) or drawer.pendown() or drawer.forward(60)}
    if stage in steps :
        steps[stage]()
# game logic
def update_display():
    word_label.config(text = ' '.join(word_display))
def end_game(win):
    guess_entry.config(state= "disabled")
    guess_button.config(state= "disabled")
    restart_button.config(state= "normal")
    if win:
        messagebox.showinfo("You Won!", f"You guessed the word: {word_to_guess}")
    else:
        messagebox.showerror("You Lost", f"The word was: {word_to_guess}\nThe monster ate you!")
def check_guess():
     global failed_attempts
     guess = guess_entry.get().lower().strip()
     guess_entry.delete(0, tk.END)

     if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single alphabet letter.")
        return
     if guess in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'")
        return

     guessed_letters.add(guess)

     if guess in word_to_guess:
        for i, c in enumerate(word_to_guess):
            if c == guess:
                word_display[i] = guess
        update_display()
        if "_" not in word_display:
            end_game(win=True)
     else:
        failed_attempts += 1
        draw_hangman(failed_attempts)
        if failed_attempts >= max_attempts:
            end_game(win=False)
#Restarting the game
def start_game():
    global word_to_guess, word_display, guessed_letters, failed_attempts
    chosen_theme = theme_var.get()
    word_to_guess = random.choice(Themes[chosen_theme]).lower()
    word_display = ['_' if c.isalpha() else c for c in word_to_guess]
    guessed_letters = set()
    failed_attempts = 0

    update_display()
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    restart_button.config(state="disabled")
    reset_turtle()
#Button function
guess_button.config(command= check_guess)
restart_button.config(command=start_game)

start_game()
root.mainloop()
    
    
    
    