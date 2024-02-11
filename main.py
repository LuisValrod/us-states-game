import turtle
import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)
import pandas as pd


data = pd.read_csv('50_states.csv')

states = data['state']
l_states = states.to_list() # l_states = data.state.to_list()

print(l_states)
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
turtle.shape(image)

'''
This function has been used to get the x and y coordinates of the different states
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# 
# turtle.mainloop()
'''
n = 0
game_is_on = True
while game_is_on:
    if n == 0:
        answer_state = ''
        while answer_state.title() not in l_states:
            answer_state = screen.textinput(title='Guess the State', prompt="What's another state")
            if answer_state is None:
                break
    else:
        answer_state = ''
        while answer_state.title() not in l_states:
            answer_state = screen.textinput(title=f'{n}/{len(data)} States', prompt="What's another state")
            if answer_state is None:
                break
    if answer_state is None:
        break
    state = data[data['state'] == answer_state.title()]

    writer.goto(int(state['x'].iloc[0]), int(state['y'].iloc[0]))
    writer.write(answer_state.title())

    n += 1
    if n < 50:
        game_is_on = False

screen.exitonclick()




