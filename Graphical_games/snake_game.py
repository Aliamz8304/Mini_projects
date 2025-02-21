from tkinter import *
from random import randint
import sys
import os
#-------------------------------------------
class Snake:
    def __init__(self):
        self.bodysize = B0DY_SIZE
        self.coordinates = []
        self.squares = []
        
        for i in range(0, B0DY_SIZE):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y , x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if dirction == "down":
        y += SPACE_SIZE
    elif dirction == "up":
        y -= SPACE_SIZE
    elif dirction == "right":
        x += SPACE_SIZE
    elif dirction == "left":    
        x -= SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)    

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_game_over(snake):
        game_over()        

    else:
        window.after(SLOWNESS, next_turn, snake, food)


def change_dirction(new_dir):
    global dirction

    if new_dir == "down":
        if dirction != "up":
            dirction = new_dir
    elif new_dir == "up":
        if dirction != "down":
            dirction = new_dir
    elif new_dir == "right":
        if dirction != "left":
            dirction = new_dir
    elif new_dir == "left":
        if dirction != "right":
            dirction = new_dir


def check_game_over(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x > GAME_WIDTH - 30: # این منهای 30 بخاطر این که به محض برخورد گیم اور بشه
        return True
    if y < 0 or y > GAME_HEIGHT - 30: # این منهای 30 بخاطر این که به محض برخورد گیم اور بشه
        return True
    
    for sq in snake.coordinates[1:]:
        if x == sq[0] and y == sq[1]:
            return True
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text="GAME OVER!",
                       font=("terminal", 60), fill="#DF1A2F", tag="gameover")


def restart_game():
    path = sys.executable
    os.execl(path, path, *sys.argv)

def play_game():
    snake = Snake()
    food = Food()
    next_turn(snake, food)
# ------------------------------------------
GAME_WIDTH = 630
GAME_HEIGHT = 630 
SPACE_SIZE = 30
B0DY_SIZE = 2
SLOWNESS = 250
SNAKE_COLOR = "GREY"
FOOD_COLOR = "RED"
score = 0
dirction = "down"
#------------------------------------------
window = Tk()
window.title("SNAKE GAME")
window.resizable(False, False)

label = Label(window, text=f"Score: {score}", font=("Arial", 35))
label.pack()

canvas = Canvas(window, height=GAME_HEIGHT, width=GAME_WIDTH, bg="black")
canvas.pack()

restart = Button(window, text="RESTART", fg="black", command=restart_game)
restart.pack(side="right", padx=100)

exit = Button(window, text="EXIT", fg="black", command=window.quit)
exit.pack(side="left", padx=100)

play = Button(window, text="Play", fg="black", command=play_game)
play.place(x=300, y=692)

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_offset = (screen_width // 2) - (window_width // 2)
y_offset = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset - 50}") # این منهای 50 بخاطر اینکه نچسبه به پایین صفحه

window.bind("<Down>", lambda event: change_dirction("down"))
window.bind("<Up>", lambda event: change_dirction("up"))
window.bind("<Right>", lambda event: change_dirction("right"))
window.bind("<Left>", lambda event: change_dirction("left"))

window.mainloop()
