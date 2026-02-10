print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 ''')

print("Ahoy, brave adventurer! Welcome to Treasure Quest.")
print("Your quest: uncover the legendary hidden fortune!")

left_right = input('You stand at a forked path. Which way? Type "left" or "right" \n').lower()

if left_right == "left":
    swim_wait = input('Ahead lies a misty river with a distant isle. Type "wait" for a raft. Type "swim" to cross.\n').lower()
    if swim_wait == "wait":
        door = input('You reach the isle safely. A cave has 3 portals: red, yellow, blue. Which do you enter?\n').lower()
        if door == "red":
            print("Flames erupt from the portal! You are scorched. Quest Over.")
        elif door == "yellow":
            print("Golden light floods in! You seize the treasure! Victory!")
        elif door == "blue":
            print("Fierce guardians lunge from the shadows! Quest Over.")
        else:
            print("Doesn't exit. Quest Over.")
    elif swim_wait == "swim":
        print("Voracious piranhas swarm! Quest Over.")
    else:
        print("Ancient traps spring to life! Crushed by stone. Game Over.")
elif left_right == "right":
    print("A swirling vortex of shadows engulfs you! Game Over.")
else:
    print("You tumble into a spike pit! Quest Over.")
