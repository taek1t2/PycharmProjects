import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)





state_answer = screen.textinput(title= "Guess the State",
                                prompt="What's another state's name?".title())
print(state_answer)


map_data = pandas.read_csv("50_states.csv")
all_states = map_data.state.to_list()
user_guess_state = ""
for state_answer in all_states:
    if user_guess_state == state_answer:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()


turtle.onscreenclick(add_states_on_map)

turtle.mainloop()

