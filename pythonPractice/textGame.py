print("Hello welcome to the text game!")
print("You are trying to get to the town of Rivendell.")

q1 = input("You stand at a crossroads. To the left is the great dark forest of Mirkwood. To the right is the Misty Mountains. Which way do you go? (left/right) ")
if (q1 == "left"):
    print("You have entered the great dark forest of Mirkwood.")
    q2 = input("You come to a river. Do you swim across or build a raft? (swim/raft) ")
    if (q2 == "swim"):
        print("You have drowned.")
    elif (q2 == "raft"):
        print("You have made it across the river.")
        q4 = input("You come to a clearing. Do you rest or keep moving? (rest/move) ")
        if (q4 == "rest"):
            print("You miss a band of orcs that come through the clearing.")
            q5 = input("You see a strange man following the orcs. Do you follow him or keep moving? (follow/move)")
            if (q5 == "follow"):
                print("You meet him and he tells you he is a ranger and he is hunting the orcs. He offers to take you to Rivendell.")
                print("You have made it to Rivendell!")
            elif (q5 == "move"):
                print("You are ambushed by a band of orcs.")
        elif (q4 == "move"):
            print("You are ambushed by a band of orcs.")
        
elif (q1 == "right"):
    print("You have entered the Misty Mountains.")
    q3 = input("You come to a cave. Do you go in or scout it out? (in/scout) ")
    if (q3 == "in"):
        print("You have been eaten by a troll.")
    elif (q3 == "scout"):
        print("You see a troll inside but you are able to sneak past it.")
        q6 = input("It is very dark in the cave. Do you light a torch or keep moving? (light/move) ")
        if (q6 == "light"):
            print("You light the torch and are able to avoid the scattered bones on the ground.")
            q7 = input("There is a dark tunnel to the left and a light tunnel to the right. Which way do you go? (left/right) ")
            if (q7 == "left"):
                print("You have entered the a dragon's lair and have been eaten.")
            elif (q7 == "right"):
                print("You have made it out of the cave and have reached Rivendell!")
        elif (q6 == "move"):
            print("You step on a bone and the troll wakes up and eats you.")

