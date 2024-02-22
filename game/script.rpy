####################
# ROFL:ROFL:ROFL:ROFL
#         _^___
# L    __/   [] \
#LOL===__        \
# L      \________]
#         I   I
#        --------/
#########################


#help me out of this hellhole, my god
##stuck in a prison of my own cringe

# this part here just adds a sound for each time a message comes in IF you add a call back the character arguments, see below
init python:
    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.music.play("notif.ogg",channel="sound")



# Declare characters used by this game. The color argument colorizes the
# name of the character.
#DEFAULT normal chars
define p = Character("[name]", color="#ffffff")
define m = Character("Mom", color="#ffffff")

##regular li definining
define a = Character("Austin", window_background="gui/textbox2.png")
define e = Character("Elaina", window_background="gui/textbox2.png")
define j = Character("Jaiden", window_background="gui/textbox2.png")
define l = Character("Leilani", window_background="gui/textbox2.png")
define r = Character("Robin", window_background="gui/textbox2.png")
define z = Character("Ziggy", window_background="gui/textbox2.png")



#################################
### Setting up chatsim chars
##########


##[word] indicates a variable! username = player username input, chosen color has a default in the code later, and then kind=nvl is how it displays in nvl fornat, then we add the icon with a zoom
define um = Character("[username]", who_prefix="{color=[chosen_color]}",kind=nvl, who_suffix="{/color}", icon = Transform("[player_icon]", zoom=0.7))
#setting the default player icon so u have an icon
default player_icon = "images/icons/user.png"


##LI nvl chat define
define am = Character("SolarJack",  kind=nvl, icon = Transform("auustin.png", zoom=0.7), callback=callbackcontinue)
define em = Character("princessEl", kind=nvl, icon = Transform("elaina.png", zoom=0.7), callback=callbackcontinue)
define jm = Character("jaiden.exe", color="#39FF14", kind=nvl, icon = Transform("jaiden.png", zoom=0.7), callback=callbackcontinue)
define lm = Character("SunshineDreams", color="#ff6f00", kind=nvl, icon = Transform("leilani.png", zoom=0.7), callback=callbackcontinue)
define rm = Character("babyblues", kind=nvl, icon = Transform("robin.png", zoom=0.7), callback=callbackcontinue)
define zm = Character("twozigzags", kind=nvl, icon = Transform("ziggy.png", zoom=0.7), callback=callbackcontinue)

##spam messages
define sm = Character("LyteUser", kind=nvl, icon = Transform("images/scammer.png", zoom=0.7), callback=callbackcontinue)
define sysm = Character("System", kind=nvl, callback=callbackcontinue)


#defining some images to make them easier to call, these are just chat backgrounds 
image austinc = "UC Austin.png"
image elainac = "UC Elaina.png"
image jaidenc = "UC Jaiden.png"
image leilanic = "UC Leilani.png"
image robinc = "UC Robin.png"
image ziggyc = "UC Ziggy.png"
image scamc = "UC Spam.png"

image login = "InputScreen.png"
image night = "bedroom night.png"
image day = "bedroom.png"
image login = "InputScreen.png"
image kitchen = "kitchen.png"
image passerror = "passworderror.png"

# group chats
image gc1 = "GC one.png"
image gc2 = "GC two.png"

#day cards
image day1 = "chapter/Dayone.png"
image day2 = "chapter/Daytwo.png"
image day3 = "chapter/Daythree.png"
image day4 = "chapter/Dayfour.png"
image day5 = "chapter/Dayfive.png"


##this shit below is me adding in code to manually add songs before i had the music playlist made in customscreens.rpy
#but i still needed one in the end to play the first song!

#define audio.one = "music/Funk.wav"
define audio.two = "music/Jitter.wav"
#define audio.three = "music/Byte.wav"
#define audio.four = "music/Lullaby.wav"
#define audio.five = "music/Whistle.wav"
#define audio.six = "music/Dial.wav"
#define audio.seven = "music/Enhance.wav"

image CG_red = "CGs/PC.png"

# The game starts here.

label start:
    


    
    $ mr.play()
    $ track = renpy.music.get_playing() #setting the track stuff up for the  music player
    play music two
    #starts ur queue from ur playlist in customscreens

    show screen textmiddle #shows the mp3 player, idk why i still havent changed this

    show login with dissolve
    
    #takes username input
    python:
        username = renpy.input(_("Please enter your username: "))

        username = username.strip()

    
    #plot twist, this isn't actually used anywhere else in the game. it's just there for immersion, u can tootally use it later though by putting in [password] as a text item if u really want
    python:
            password = renpy.input(_("Please enter your password: "), mask="*")

            password = password.strip()
    
    show passerror with vpunch
    "System" "ERROR"
    "System" "ERROR: Password invalid"

    show login with dissolve
    hide passerror

    "System" "Please verify your information by providing your name"
    #takes name input as well for character
    python:
            name = renpy.input(_("What is your name?"))

            name = name.strip()


    #check pronouns folder, this is not my pronoun tool

    jump test_one_pronoun_set
    
label after_pronouns:


    "Would you like to change your  name color?"
    #allows player to choose their name color
menu: 
    "Yes":
        jump color_choice
    "No":
        jump story_start
        $ chosen_color = "#D82797"
        #if they dont it updates to this pink color

label color_choice:
    menu:
        "Blue":
            $ chosen_color = "#2DA3D2"
        "Pink":
            $ chosen_color = "#D82797"
            #u can add in more colors by just following the syntax below
        #"Color":
            #$ chosen_color = "#hexcode"




label story_start:
    $ day = "30/06/23"
    #THIS IS HOW U SET WHAT DATE DISPLAYS IN THE BOTTOM OF THE SCREEN :) 
    scene black with dissolve 


    scene austinc
    show screen username #shows the  username screen with ur username and icon
    play sound "notif.ogg"

    
    
    show screen taskbar #shows taskbar
    show screen clock #shows clock with time and the date u set
    am "Hey, [name]!" #how to use players name, but u can use  [username] if you'd prefer
    am "Happy happy birthday!"
    am " {image=stickers/1.png}" #How i got emojis to display /stickers in the chat! check out the screens and gui files to see the NVL spacing and list legnth stuff i had to tweak to make this possible

    um "Thanks Austin!"
    um "You'll never guess what I got!"

    "ICON CHANGE PLACEHOLDER" #TODO MOVE THIS ONCE IT WORKS
    label icon_change:
                menu(icon=True):
                    #THIS is the  menu to select the icons, i have it in a 3x3 grid since there are 9 pfp options, see a normal choice menu below
                    #"{image=images/icons/user.png}":
                    "{image=images/icons/user.png}":
                        $ player_icon = "images/icons/user.png" 
                    "{image=images/icons/user2.png}":
                        $ player_icon = "images/icons/user2.png"
                    "{image=images/icons/user3.png}":
                        $ player_icon = "images/icons/user3.png"
                    "{image=images/icons/user4.png}":
                        $ player_icon = "images/icons/user4.png"
                    "{image=images/icons/user5.png}":
                        $ player_icon = "images/icons/user5.png"
                    "{image=images/icons/user6.png}":
                        $ player_icon = "images/icons/user6.png"
                    "{image=images/icons/user7.png}":
                        $ player_icon = "images/icons/user7.png"
                    "{image=images/icons/user8.png}":
                        $ player_icon = "images/icons/user8.png"
                    "{image=images/icons/user 9.png}":
                        $ player_icon = "images/icons/user 9.png"

menu:
    "Maybe tomorrow!":
        jump jaiden_chat
    "Sure!":
        jump austin_game

label jaiden_chat:
    um "Maybe tomorrow! I wanna get logged into all my stuff tonight first"
    jump day2

label austin_game:
    show austinc
    um "Sure!"
   
return