import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
t = turtle.Turtle()


def show_state(answer):
    t.penup()
    x_cord = int(data[data.state == answer].x)
    y_cord = int(data[data.state == answer].y)
    t.goto(x_cord, y_cord)
    t.write(answer)


def us_states_game():
    in_game = True
    num_correct = 0
    guessed_states = []

    while in_game:
        answer = screen.textinput(title=f"{num_correct}/50 states correct", prompt="Guess the name of a state").title()
        if answer in data.state.values and answer not in guessed_states:
            guessed_states.append(answer)
            num_correct += 1
            show_state(answer)
        if num_correct == len(data):
            in_game = False

    screen.exitonclick()


us_states_game()
