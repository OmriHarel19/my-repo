import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint

# constants:
WINDOW_W = 600
WINDOW_H = 620

MOVE_INCREMENT = 20
moves_per_second = 15
GAME_SPEED = 1000 // moves_per_second

DIRECTIONS = ("Right", "Left", "Up", "Down")
OPPOSITES = ({"Right", "Left"}, {"Up", "Down"})


class Snake(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, width=WINDOW_W, height=WINDOW_H, background="black", highlightthickness=0)

        #       --class properties--

        # snake and food img
        self.snake_body_image, self.snake_body, self.food_image, self.food = None, None, None, None
        # snake body: composed of many square body image, each square has a side of 20px
        #                           head      ....        tail
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        # food:
        self.food_position = (200, 100)
        self.score = 0
        self.direction = "Right"

        # bind the canvas to "Key" event - any key press that occurs
        self.bind_all("<Key>", self.on_key_press)

        self.load_assets()  # load images from assets
        self.create_objects()  # create all elements in the canvas

        self.after(GAME_SPEED, self.perform_actions)

    def load_assets(self):
        # load images from assets dir
        try:
            self.snake_body_image = Image.open("./assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("./assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)
        # if failed print err and close app
        except IOError as error:
            print(error)
            root.destroy()

    def create_objects(self):
        # create score text:
        self.create_text(
            100, 12,
            text=f" Score {self.score} (speed: {moves_per_second})",
            tag="score",
            fill="#fff",
            font=("TkDefaultFont", 14)
        )
        # create snake
        for x_pos, y_pos in self.snake_positions:
            self.create_image(x_pos, y_pos, image=self.snake_body, tag="snake")

        # create food:      destructuring
        self.create_image(*self.food_position, image=self.food, tag="food")

        # create board border:x1,y1,x2,y2
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    # updates snake position
    def move_snake(self):
        # get current head pos:
        head_x_pos, head_y_pos = self.snake_positions[0]  # destructuring
        # create new head according to direction:
        if self.direction == "Left":
            new_head_pos = (head_x_pos - MOVE_INCREMENT, head_y_pos)
        elif self.direction == "Right":
            new_head_pos = (head_x_pos + MOVE_INCREMENT, head_y_pos)
        elif self.direction == "Down":
            new_head_pos = (head_x_pos, head_y_pos + MOVE_INCREMENT)
        elif self.direction == "Up":
            new_head_pos = (head_x_pos, head_y_pos - MOVE_INCREMENT)

        # add new head at the starts and remove tail from the end:
        self.snake_positions = [new_head_pos] + self.snake_positions[:-1]
        # update snake positions: run on all elements using the tag property
        #   body_elem, pos_tuple    zip - creates a tuple
        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)  # coords: moves segment pos to 'position'

    # performs snake moves
    def perform_actions(self):
        # check collision:
        if self.check_collisions():
            self.game_over()
            return

        # check food collision:
        self.check_food_collision()

        self.move_snake()
        self.after(GAME_SPEED, self.perform_actions)

    def check_collisions(self):
        # get current head pos:
        head_x_pos, head_y_pos = self.snake_positions[0]  # destructuring

        # check collisions:
        return (
            head_x_pos in (0, WINDOW_W)  # check collision on x axis
            or head_y_pos in (0, WINDOW_H)  # check collision on y axis
            or (head_x_pos, head_y_pos) in self.snake_positions[1:]  # check collision with snake body
        )

    def on_key_press(self, key_press):
        # keysym - gives the pressed key symbol (for key arrows: Left, Right, Down, Up)
        new_direction = key_press.keysym

        # update direction: check for valid direction and not opposite to current one
        if new_direction in DIRECTIONS and {self.direction, new_direction} not in OPPOSITES:
            self.direction = new_direction

    def check_food_collision(self):
        # get current head pos:
        head_x_pos, head_y_pos = self.snake_positions[0]  # destructuring
        # get current food pos:
        food_x_pos, food_y_pos = self.food_position

        # check collision:
        if (head_x_pos, head_y_pos) == (food_x_pos, food_y_pos):
            # update score:
            self.score += 1
            score = self.find_withtag("score")

            # increase game speed every five points:
            if self.score % 5 == 0:
                global moves_per_second
                moves_per_second += 1

            self.itemconfigure(
                score,
                text=f" Score {self.score} (speed: {moves_per_second})",
                tag="score"
            )

            # update snake: duplicate the tail, so next move it is going to stay there and therefore add a block
            self.snake_positions.append(self.snake_positions[-1])  # dup tail
            # create the new img:
            self.create_image(
                *self.snake_positions[-1],
                image=self.snake_body,
                tag="snake"
            )

            # update food pos:
            self.food_position = self.set_new_food_position()
            food = self.find_withtag("food")
            self.coords(food, self.food_position)

    def set_new_food_position(self):
        # create rand pos:
        while True:
            new_x_pos = randint(1, 28) * MOVE_INCREMENT
            new_y_pos = randint(3, 30) * MOVE_INCREMENT
            # check if not on snake body
            if (new_x_pos, new_y_pos) not in self.snake_positions:
                return new_x_pos, new_y_pos

    def game_over(self):
        self.delete(tk.ALL)  # del all elements from the canvas
        # create game over text:
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game over! You scored {self.score}!",
            fill="#fff",
            font=("TkDefaultFont", 14)
        )


root = tk.Tk()
root.title("Snake")
root.resizable(False, False)

board = Snake(root)
board.pack()

root.mainloop()
