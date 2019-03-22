# imports dedent 
from textwrap import dedent

def death():
    """ Lets the player know they died and gives them an option 
    to play again if desired."""
    print("Awww shucks! You died. Nice try.")

    # play again logic
    play_again = input("Do you want to play again? (type y or n) ")
    if play_again == "y":
        done = False
    if play_again == "n":
        done = True

def survive():
    """ Lets the player know they survived and gives them
    an option to play again if desired"""
    print("Congratulations! You made it out!")

    # play again logic
    play_again = input("Do you want to play again? (type y or n) ")
    if play_again == "y":
        done = False
    if play_again == "n":
        done = True

def main():
    """ Main function. Contains the creation of all the
    rooms that are added to the room list. Also contains
    all the main logic for the player to choose where 
    they go."""

    # Welcome print statement
    print(dedent(
        """
        Welcome to the Random Adventure Game!
        To quit at any time, type "quit" or "q"
        For directions, you can type the full direction
        or just the first letter of the direction.
        Good luck!
        """))

    # Empty Room List
    room_list = []

    # --- Creation and Additions of rooms to room list---
    museum = [
        dedent("""
        You are in a museum full of paintings.
        From legend you have heard that the painting on 
        the east leads to adventures. 
        """),
        None, 1, None, None]
    room_list.append(museum)

    hall_behind_painting = [
        dedent("""
        This hall is creeepppyyyy.
        You see an upwards hallway to the south.
        You see a downwards hallway to the east.
        """),
        None, 2, 5, 0]
    room_list.append(hall_behind_painting)

    mineshaft = [
        dedent("""
        You are in a mineshaft! Every wall around
        you glistens with diamonds. You could 
        continue to follow the mineshaft to the east
        with no definite end. Or, you could choose
        to go towards the light in the north. 
        """),
        3, 4, None, 1]
    room_list.append(mineshaft)

    mineshaft_death = [
        dedent("""
        The light turned out to be an active volcano!
        Do you continue to explore the volcano? All you
        need to do is continue north.   
        """),
        9, None, None, None]
    room_list.append(mineshaft_death)

    mineshaft_exit = [
        dedent("""
        The diamond walls start to turn into solid
        diamond. Everywhere around you is diamonds,
        even as you come up to ground level for air.
        You're going to be rich! All you need to do
        is continue east. 
        """),
        None, 10, None, 2]
    room_list.append(mineshaft_exit)

    riddles = [
        dedent("""
        Magnificent doors have this on a holder:

        When you are hot, I am cooler. 
        When you are cold, I am warmer. 
        I wear a crown on land.
        My opposite wears a crown on water.
        
        Choose your direction wisely.  
        """),
        None, None, 6, None]
    room_list.append(riddles)

    stairwell_with_choice = [
        dedent("""
        The magnicent doors open and a grandiose staircase 
        appears before your eyes. Up at the top, you
        notice that the staircase splits east and west.
        """),
        1, 7, None, 9]
    room_list.append(stairwell_with_choice)

    dragon_boss = [
        dedent("""
        A blackened dragon in a wagon is maddened by your 
        surname Fagen. 

        He knows you're bright, and it is night, although
        you're slight, he wants to fight. 
        All you need is to go south. 

        """),
        None, None, 8, 6]
    room_list.append(dragon_boss)

    dragon_world = [
        dedent("""
        The dragon guard was no match for your lard.
        In his backyard dragons play cards while
        another lifeguards. 
        You send a postcard and eat swiss chard and
        you disregard your credit card. 

        Oh wait, you see an exit, do you continue south?
        """),
        7, None, 10, None]
    room_list.append(dragon_world)

    # Sets the current room to the Museum and done as False
    current_room = 0
    done = False

    # Main while loop; runs until done is True
    while not done:

        # prints the description of first room and inital question
        print(room_list[current_room][0])
        direction = input("What direction do you go? ").lower()

        # if the player chooses 'north'
        if direction == "north" or direction == "n":
            next_room = room_list[current_room][1]

            if next_room == None:
                print("You can't go that way")
            elif next_room == 9:
                death()
            elif next_room == 10:
                survive()
            else:
                current_room = next_room

        # if the player chooses 'east'
        elif direction == "east" or direction == "e":
            next_room = room_list[current_room][2]
            
            if next_room == None:
                print("You can't go that way")
            elif next_room == 9:
                death()
            elif next_room == 10:
                survive()
            else:
                current_room = next_room

        # if the player chooses 'south'
        elif direction == "south" or direction == "s":
            next_room = room_list[current_room][3]
            
            if next_room == None:
                print("You can't go that way")
            elif next_room == 9:
                death()
            elif next_room == 10:
                survive()
            else:
                current_room = next_room

        # if the player chooses 'west'
        elif direction == "west" or direction == "w":
            next_room = room_list[current_room][4]
            
            if next_room == None:
                print("You can't go that way")
            elif next_room == 9:
                death()
            elif next_room == 10:
                survive()
            else:
                current_room = next_room

        # if the player types in 'quit'
        elif direction == "quit" or direction == "q":
            answer = input("Are you sure you want to quit? (type y or n) ")
            if answer == "y":
                break
            if answer == "n":
                continue

        # in case the player types in gibberish
        else:
            print("Sorry, I don't understand what direction that is.")

# calls main function
if __name__ == "__main__":
    main()
