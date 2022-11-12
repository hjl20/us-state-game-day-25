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
    num_correct = 0
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < len(data):
        answer = screen.textinput(title=f"{num_correct}/50 states correct", prompt="Guess the name of a state").title()
        if answer == "Exit":
            for state in guessed_states:
                all_states.remove(state)
            break
        elif answer in all_states and answer not in guessed_states:
            guessed_states.append(answer)
            show_state(answer)

    df = pandas.DataFrame(all_states)
    df.to_csv("states_to_learn.csv")
    screen.exitonclick()


us_states_game()
