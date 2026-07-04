# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    window hide
    scene bg sb1 with dissolve
    pause

    scene bg sb2 with dissolve
    pause

    scene bg sb3 with dissolve
    pause

    scene bg sb4 with dissolve
    pause

    scene bg sb5 with dissolve
    pause

    scene bg sb6 with dissolve
    pause

    scene bg sb7 with dissolve
    pause

    scene bg sb8 with dissolve
    pause

    scene bg sb9 with dissolve
    pause
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # This ends the game.

    return
