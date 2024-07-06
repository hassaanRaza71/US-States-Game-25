from turtle import Turtle,Screen
import pandas
FONT = ("Courier", 8, "bold")

turtle=Turtle()
screen=Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
Turtle().shape(image)
game_is_on=True
data=pandas.read_csv("50_states.csv")
state_list=data["state"].to_list()
states_guessed=[]
answer_state = screen.textinput("Guess the State", "What's another state's name?")
while len(states_guessed)<50:
    
    if answer_state.lower()=="exit":
        missing_states=[]
        for state in state_list:
            if state not in states_guessed:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    
    if answer_state.title() in state_list:
        state_data = data[data.state == answer_state.title()]
        x_coordinate = int(state_data.x)
        y_coordinate = int(state_data.y)
        state_marker = Turtle()
        state_marker.hideturtle()
        state_marker.penup()
        state_marker.goto(x_coordinate, y_coordinate)
        state_marker.write(answer_state.title(), align="center", font=FONT)
        states_guessed.append(answer_state.title())
        answer_state = screen.textinput(f"{len(states_guessed)}/50 States Correct", "What's another state's name?")
    else:
        answer_state = screen.textinput(f"{len(states_guessed)}/50 States Correct", "What's another state's name?")







screen.mainloop()