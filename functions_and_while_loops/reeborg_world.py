# run this code in https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# excercise 1
# def square():
#     move()
#     turn_left()
#
# square()
# square()
# square()
# square()

#excercise 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# excercise 3 , hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(1, 7): #bcz 6 hurdles
# for i in range(6): 0 to 6
    jump()