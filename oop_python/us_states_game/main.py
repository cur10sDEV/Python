import turtle
import pandas

screen = turtle.Screen()
screen.title("Name the U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("./50_states.csv")
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

answered_states = []
names_list = data.state.to_list()
x_cor_list = data.x.to_list()
y_cor_list = data.y.to_list()

while len(answered_states) < 50:
    user_input = screen.textinput(f"{len(answered_states)}/50 States Correct", "What's another state's name?").lower()

    if user_input == "exit":
        diff_list = [name for name in names_list if name not in answered_states]

        diff_data = pandas.DataFrame(diff_list)
        diff_data.to_csv("./missed_states.csv")
        break

    for i in range(len(names_list)):
        name = names_list[i]
        if name.lower() == user_input:
            name_count = answered_states.count(name)
            if name_count == 0:
                answered_states.append(name)
                x_cor = x_cor_list[i]
                y_cor = y_cor_list[i]
                pen.goto(x=x_cor, y=y_cor)
                pen.write(name, align="center", font=("Arial", 10, "normal"))


turtle.mainloop()
#########################################################
# Get mouse click location
# def get_mouse_click_location(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_location)
