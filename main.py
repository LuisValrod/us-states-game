import turtle
import warnings



warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)
import pandas as pd


data = pd.read_csv('50_states.csv')

all_states = data.state.to_list()
guessed_states = []

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

'''
This function has been used to get the x and y coordinates of the different states
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# 
# turtle.mainloop()
'''

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                              "name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)





# n = 0
# game_is_on = True
# guessed_states = []
# while game_is_on:
#     if n == 0:
#         answer_state = ''
#         while answer_state.title() not in l_states:
#             answer_state = screen.textinput(title='Guess the State', prompt="What's another state")
#             if answer_state is None:
#                 break
#     else:
#         answer_state = ''
#         while answer_state.title() not in l_states:
#             answer_state = screen.textinput(title=f'{n}/{len(data)} States', prompt="What's another state")
#             if answer_state is None:
#                 break
#     if answer_state is None:
#         break
#     state = data[data['state'] == answer_state.title()]
#
#     writer.goto(int(state['x'].iloc[0]), int(state['y'].iloc[0]))
#     writer.write(answer_state.title())
#
#     guessed_states.append(answer_state.title())
#     n += 1
#     if n < 50:
#         game_is_on = False
#
# screen.exitonclick()
# print(guessed_states)




