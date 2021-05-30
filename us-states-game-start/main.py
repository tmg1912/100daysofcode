import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv('50_states.csv')
all_states = states_data.state.to_list()

print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(f"{len(guessed_states)}/50 states guessed", "Guess another state").title()

    if guess == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if guess in all_states and guess not in guessed_states:
        guessed_states.append(guess)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        xpos = int(states_data[states_data.state == guess].x)
        ypos = int(states_data[states_data.state == guess].y)
        new_turtle.goto(xpos, ypos)
        new_turtle.write(guess, align='center', font=('Arial',8,'normal'))

# screen.onscreenclick()
# turtle.mainloop()
# screen.exitonclick()