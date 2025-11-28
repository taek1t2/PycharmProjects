import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:

    state_answer = screen.textinput(title= f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    map_data = pandas.read_csv("50_states.csv")
    all_states = map_data.state.to_list()

    if state_answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn")
        break
    if state_answer in all_states:
        guessed_states.append(state_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = map_data[map_data.state == state_answer]
        t.goto(data.x.item(), data.y.item())
        t.write(state_answer)




screen.exitonclick()

