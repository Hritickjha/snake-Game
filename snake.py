import tkinter as tk
import random

# Constants
TILE_SIZE = 10
ROWS = 50
COLS = 50

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

# Game window
window = tk.Tk()
window.title("Snake")
window.resizable(False, False)

# Canvas for drawing
canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black')
canvas.pack()

# Initial snake and food position
snake = [(25, 25)]
snake_direction = "Right"
food_position = (random.randint(0, COLS-1), random.randint(0, ROWS-1))

# Draw initial snake and food
def draw_tile(position, color):
    x, y = position
    canvas.create_rectangle(
        x * TILE_SIZE,
        y * TILE_SIZE,
        (x + 1) * TILE_SIZE,
        (y + 1) * TILE_SIZE,
        fill=color
    )

def draw_snake():
    for segment in snake:
        draw_tile(segment, 'green')

def draw_food():
    draw_tile(food_position, 'red')

# Move snake
def move_snake():
    global snake, food_position

    head_x, head_y = snake[0]

    if snake_direction == "Left":
        new_head = (head_x - 1, head_y)
    elif snake_direction == "Right":
        new_head = (head_x + 1, head_y)
    elif snake_direction == "Up":
        new_head = (head_x, head_y - 1)
    elif snake_direction == "Down":
        new_head = (head_x, head_y + 1)

    # Check if snake eats the food
    if new_head == food_position:
        food_position = (random.randint(0, COLS-1), random.randint(0, ROWS-1))
    else:
        snake.pop()

    # Add new head to the snake
    snake.insert(0, new_head)

    # Check for collisions
    if (new_head[0] < 0 or new_head[0] >= COLS or
        new_head[1] < 0 or new_head[1] >= ROWS or
        new_head in snake[1:]):
        game_over()
        return

    # Clear canvas and redraw snake and food
    canvas.delete(tk.ALL)
    draw_snake()
    draw_food()

    # Schedule next move
    window.after(100, move_snake)

def change_direction(new_direction):
    global snake_direction

    # Prevent the snake from reversing
    if (new_direction == "Left" and snake_direction != "Right" or
        new_direction == "Right" and snake_direction != "Left" or
        new_direction == "Up" and snake_direction != "Down" or
        new_direction == "Down" and snake_direction != "Up"):
        snake_direction = new_direction

def game_over():
    canvas.create_text(
        WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
        text="Game Over", fill="white", font=("Arial", 24)
    )

# Bind keys to change direction
window.bind("<Left>", lambda event: change_direction("Left"))
window.bind("<Right>", lambda event: change_direction("Right"))
window.bind("<Up>", lambda event: change_direction("Up"))
window.bind("<Down>", lambda event: change_direction("Down"))

# Start the game
draw_snake()
draw_food()
move_snake()

window.mainloop()
