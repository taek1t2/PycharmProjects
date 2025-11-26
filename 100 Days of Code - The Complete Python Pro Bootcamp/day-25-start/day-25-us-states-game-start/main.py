import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

state_answer = screen.textinput(title= "Guess the State", prompt="What's another state's name?")
print(state_answer)

map = pandas.read_csv("50_states.csv")
user_guess_state = ""
for state in map:
    if user_guess_state == state:
        user_guess_state.title()


turtle.mainloop()

