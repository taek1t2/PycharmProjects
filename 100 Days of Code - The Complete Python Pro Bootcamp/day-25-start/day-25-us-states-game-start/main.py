import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


state_answer = screen.textinput(title= "Guess the State",
                                prompt="What's another state's name?".title())

map_data = pandas.read_csv("50_states.csv")
all_states = map_data.state.to_list()

t = turtle.Turtle()
t.hideturtle()
t.penup()
data = map_data[map_data.state == state_answer]
t.goto(data.x.item(), data.y.item())
t.write(state_answer)


turtle.mainloop()

