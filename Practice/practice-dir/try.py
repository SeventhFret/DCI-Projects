### STORY GAME ###
​
# Initial Situation
print("""It was a dark and rainy night in DCI headquarters. You are one of the non-remote students up
late because your immortal desire to learn python didnt let you rest. You are staying there alone when 
suddenly a snake entered your godamn room!""")
# Options for decision making & choice made
print("(LEAVE/LOOK/SCREAM)")
choice = input("WHAT DO YOU DO? ")
​
if "LEAVE" == choice: # leaving the situation
    print("""You just didnt care of collateral damage and successfully escaped the room, not really considering that
    tomorrow someone unaware of the snake will go to work in this room and die. Well done. You are now in the hallway.""")
    # Options for decision making & choice made
    print("(SEARCH///)")
    choice = input("WHAT DO YOU DO NOW?")
    if "SEARCH" == choice:
        print("Finding a student you dislike to tell him that that room has free wifi.")
    elif "CALL" == choice:
        print("Calling 112 to let them save that snake.")
    else:
        print("You didnt do anything.")
elif "LOOK" == choice: # looking for a weapon
    print("""Thank god DCI just issued brand new 'u better learn'-baseballbats and u found one hanging on the wall.
    You take that thing and bash that endangered species head in. It does not move anymore after you let out all the
    anger and frustration of learning programming on that probably harmless snake as in germany there are no poisonous
    snakes known. Well done. You should probably meet a therapist.""")
    print("SNAKE IS DEAD, WHAT NOW?")
    # next if statements
elif "SCREAM" == choice: # screaming for help
    print("""You scream like a little girl and after a fellow student in another room politely replied 'DUDE STFU' the snake
    just jumped up to your throat and injected its poisonous venom. You died a horrible painful death.""")
    print("YOU JUST DIED MAN GODAMN")
else:
    print("YOU JUST DIED MAN GODAMN")
