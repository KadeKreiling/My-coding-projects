import turtle
import pandas

screen = turtle.Screen()


image = "blank_states_img.gif"
screen.addshape(image)
screen.title("State Guessing Games")

turtle.shape(image)


guessed_states = []


states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
while len(guessed_states) < 50:
    correct_guesses = len(guessed_states)
    answer_state = screen.textinput(title= f"States guessed {correct_guesses}/50", prompt= "What is a state name").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)








