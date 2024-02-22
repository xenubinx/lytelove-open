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

# The script of the game goes in this file.
init python:
    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.music.play("notif.ogg",channel="sound")
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[name]", color="#ffffff")
define m = Character("Mom", color="#ffffff")

#default chosen_color = "#000000"
#define um = Character("[username]", color=chosen_color, kind=nvl, icon = im.FactorScale("user.png", 0.7), callback=callbackcontinue)
define um = Character("[username]", who_prefix="{color=[chosen_color]}",kind=nvl, who_suffix="{/color}", icon = Transform("[player_icon]", zoom=0.7))

default player_icon = "images/icons/user.png"

##regular li definining
define a = Character("Austin", window_background="gui/textbox2.png")
define e = Character("Elaina", window_background="gui/textbox2.png")
define j = Character("Jaiden", window_background="gui/textbox2.png")
define l = Character("Leilani", window_background="gui/textbox2.png")
define r = Character("Robin", window_background="gui/textbox2.png")
define z = Character("Ziggy", window_background="gui/textbox2.png")

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


##this shit below isme adding in code to manually add songs before i had the music playlist made in screens.rpy

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
    $ track = renpy.music.get_playing()
    play music two
    #queue music one
    # queue music four
    #queue music three
    #queue music five
    #queue music seven
    #queue music six
    #queue music two 
    #queue music one
    #queue music four
    #queue music three
    #queue music five
    #queue music seven
    #queue music six


    show screen textmiddle
  
    scene wallpaper

    show login with dissolve
    
    python:
        username = renpy.input(_("Please enter your username: "))

        username = username.strip()

    

    python:
            password = renpy.input(_("Please enter your password: "), mask="*")

            password = password.strip()
    
    show passerror with vpunch
    "System" "ERROR"
    "System" "ERROR: Password invalid"

    show login with dissolve
    hide passerror

    "System" "Please verify your information by providing your name"

    python:
            name = renpy.input(_("What is your name?"))

            name = name.strip()


    #show pronouns
    #"Please select your pronouns:"
    #call pronounselection from _call_pronounselection
    jump test_one_pronoun_set
    "Would you like to change your  name color?"
label after_pronouns:

menu: 
    "Yes":
        jump color_choice
    "No":
        jump story_start

label color_choice:
    menu:
        "Blue":
            $ chosen_color = "#2DA3D2"
        "Pink":
            $ chosen_color = "#D82797"




label story_start:
    $ day = "30/06/23"

    "I still remember the day that I first met my group. Mom had given me her old work laptop because she had upgraded."
    
    "A few of my friends from school had been mentioning talking to each other on this app."
    show lytelogin with dissolve

    "Lyte."


    "It wasn’t super fancy or anything, but it was so exciting to finally be able to talk to my friends even when we weren’t in school. "

    "I made my account… probably a year ago now if I had to guess."

    "I still remember joining, and god do I regret choosing that username"

    "The app had a feature where you could join groups based on common interests." 

    "There was one for a smaller anime I liked, that none of the kids at school liked." 

    "From there, it’s like my life changed for the better."

    scene black with dissolve 

    ##fade to black 
    scene day1 with dissolve
    pause 3.0
    scene bedroom
    "I had spent all morning scrolling through some forums on my laptop"

    "I had admittedly been avoiding opening up Lyte though."

    "I wasn’t really ready for the birthday wishes, they stressed me out."

    m "[name]! It’s almost time for dinner, come on down soon."

    "Oh shit, had I really been on here that long?"

    p "Coming!"

    "I shut the lid on my laptop and attempted to hoist myself out of bed."

    "God, my joints shouldn’t be popping this much. "

    "I definitely should’ve stretched at some point."

    scene kitchen 
    "I bounded down the stairs, the smell of Mom's homemade Mac n Cheese hitting my nose the second I hit the landing."


    "{i}I giggle, sliding around the counter to grab a plate out of the cabinet.{/i}"

    p "Thank you, Ma. This smells like heaven."

    m "You’re welcome honey, now eat up. You’ve got a gift waiting for you."

    p "A gift?"

    "I knew mom tried her best, but we hadn’t done birthday gifts in a while."

    "Especially after Dad died, money had been tight. "

    "I wanted to be excited, but I couldn’t help but feel a little worried about the money aspect. "

    "Apparently Mom noticed my concern-"

    m "Don’t worry hun, this cost me way less than you think."

    m "We’ll be okay, besides.."

    m "I think you’re gonna like this one."

    "A small smile spread across my face, as I dug into the macaroni. "

    "It honestly tasted better than usual, the cheese was so gooey."

    "I couldn’t help but drool a little as I shoveled forkfuls into my mouth."

    m "Hahahahaha."

    "Startled, I look up."

    "Mom is laughing at me pretty hard."

    "And I’m sure I look like a deer caught in the headlights right now. "
    "*Gulp*"

    p "{i}Whaatt{/i}, its good!"

    p "What did you do different?"

    "She winked"
    m "It’s a secret"

    p "Oh come oon, thats not fair. What if I want to make my own?"

    "She fake pouted a moment before giving in."

    "I just added some sour cream to it to make it more creamy"

    p "Oh!! That’s genius."

    m "I know right?"


    "Once I had finished my dinner, Mom excused herself to the other room to grab my gift. "

    "I couldn’t help but still feel a little bit bad, but she seemed excited about it at least. "

    "As I rinse off my plate, I hear a gentle thud behind me as she sets a box on the table. "

    "It wasn’t wrapped or anything, but the box was bigger than I expected. "

    m "Go ahead, [name], open it."

    "I had to kneel on the chair just to reach the top of the box."

    "To my surprise, it was moms work computer."

    "It was only a few years old at most, so I was a little confused."

    p "What, why-"

    m "I got a promotion, so they sent me something a little better."
    m "No point in this one going to waste."

    "Oh my god"

    "Wait- Holy shit, she got a promotion!"

    p "MOM OH MY GOD THATS SO EXCITING!!"

    "I leapt out of my chair and hugged her."

    p "What do you do now? Are you still working with that one weird man?"

    "I couldn’t help but be excited, question after question was just spewing out of my mouth."

    "She giggled."

    m "Mostly the same stuff, but with some nice bonuses."

    m "Now let's go get this set up in your room."

    scene black with dissolve 


    "After an hour of messing with cords and moving my desk around, we finally had a space for it... "
    "Kinda."

    scene computersetup

    "It was far better than  my laptop, that’s for sure."

    m "Maybe now you won’t be so cranky and stiff."

    p "Oh a thousand percent, sitting in my bed with the laptop was killing my back."

    "After some scooting around of my desk, and some painful head bumps, we got the computer all set up and turned on."

    "It still had moms name and background, so as soon as she left I changed it up to fit my style.."

    p "Much better"

    scene black with dissolve 


  
 

    "I logged into that familiar pastel interface and was greeted with a message notification from Austin."
    scene austinc
    show screen username
    play sound "notif.ogg"

    
    
    show screen taskbar
    show screen clock
    am "Hey, [name]!"
    am "Happy happy birthday!"
    am " {image=stickers/1.png}"

    um "Thanks Austin!"
    um "You'll never guess what I got!"

    "ICON CHANGE PLACEHOLDER" #TODO MOVE THIS ONCE IT WORKS
    label icon_change:
                menu(icon=True):
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
    am "OOH WHAT DID YOUG ET?"

    um "Mom gave me her old computer!"

    am "Oh my god! That's so cool"
    am "Now you have no choice but to play some of my games with me now >:D"


    um "Hahahah, yes! I genuinely can not wait."

    am "We totally don't have to play anything today, afterall its your birthday"
    am "But you should totally download Gleam and let me add you!"
    am "We can play 2gether easier that way!"

    um "oooh okay! Sec."

    "Before I had a chance to go download the app, I had a new message notification"

    scene leilanic
    nvl clear
    play sound "notif.ogg"
    lm "AAAH HAPPY HAPPY BIRTHDAY [name]!!!"

    um "AAH THANK YOU SO MUCH uvu"

    lm "ARE YOU STOKED?"

    um "YES, I got a new computer!!"

    lm  "OOH YES, ur poor spine is free now ;p"


    um "Why is everyone just now suddenly concerned with m y spine, huh?"

    um "Smh"

    um "But yes, I moved my desk n junk around and now I can freely peruse the forums alllll day"

    lm "LOL"

    lm "As if you don't already do that"

    um "Shhh,, its fiinnee"

    um "Anyways, I gtg for a sec! Austin wants me to download gleam so we can play some games together soon."

    lm "oooh have fun! Bye!"

    p "It took me a minute to get it downloaded and all set up, mostly because passwords are not my strong suite."
    p "but."
    p "I got it up at least."
    p "I really should message Austin though and let him know."

    show austinc
    nvl clear
    um "Hey Austin! I got it downloaded."

    am "Schweet. Whats your username?"

    um "Same as here! Its [username]"

    am "sent you a fr!"

    p "A tiny blip noise came from the app and i quickly accepted his friend request."

    p "I took a minute to look over his profile."

    p "My god, he's played a LOT of games."

    p "I clicked on the most recently played game and was brought to the store page for it."

    p "Holy cow, $20?? Are all the games like this?"

    um "Jesus, i didn't realize all the games were this expensive dude"

    am "it looks scary at first, but there's a lot of sales!"


    am "There's actually a spring sale that started two days ago i think?"

    am "Ya, 2 days ago."

    um "oooh, I'll have to see if I can get a game next time i get allowance!" 

    am "brb"

    p "What-"

  

    show austingift
    " "
    p "Before I can ask him where he went, Gleam blips again. A small window appears on the screen letting me know that I've been sent a gift"
    hide austingift
    show austinc
    um "AUSTIN YOU DIDNT HAVE TO DO THAT U LIL SHIT"

    am " >:D "
    am " {image=stickers/4.png}"

    am "I told you, now you've got no choice but to play games with me now"

    um "I guess not LMAO"
    um "It's almost done downloading now!"

    am "Awesome!"

    am "Would you want to play tonight?"


menu:
    "Maybe tomorrow!":
        jump jaiden_chat
    "Sure!":
        jump austin_game

label jaiden_chat:
    um "Maybe tomorrow! I wanna get logged into all my stuff tonight first"
    am "Aw, no worries!"
    am "I'm gonna hold you to that though."
    am "have fun! I'm gonna go play some myself, I'll ttyl!"
    um "ttyl austin!"

    p "I felt a bit bad for turning Austin down, but we have all the time in the world to play now."
    p "And he wasn't the type to ever get upset."

    show jaidenc
    nvl clear
    jm "Hey hey hey!"
    jm "Happy birthday dork"
    um "you're the dork, you spend more time online than I do"
    jm " {image=stickers/9.png}"
    jm "Yeah but at least I'm learning something ;p"
    um "I am tooooo"
    jm "ah yes, my bad. Fanfiction is part of your literature requirements, yes?"
    um "..."
    um "It should be, I need to mention that to mom." 
    jm "LOL"
    jm "I'm surprised you weren't doing that already. Especially with how much you read on there."

    um "I didn't think of it, okay?"
    jm "smh, you're slacking [name]"
    um "yeah yeah, I know."

    jm "So how'd the birthday shebang go?"
    um "Pretty well! It was just me and mom."
    um "She made some pretty banging macaroni too, so I'd call it a success"

    jm "Cheese is always a success. Did you get any fun gifts?"

    um "Actually yeah!! Mom gave me her old PC, so now I'm not using my old clunky laptop anymore."
    um "Oh and Austin sent me a game on gleam!"

    jm "oooh, you're turning into a regular gamer on me now, huh?"
    jm "Can't believe you let him give you a gift but not me."

    um "PLZ, I didn't have a choice, it just popped up in a little window T^T"

    jm "I tease, i tease. Are ya gonna play it soon?"
    um "I think so! He asked about tonight, but I wanted to finish getting everything set up first"

    jm "Fair enough, you'll end up playing plenty enough anyways if he has any say ;p"

    um "I'm excited for it honestly! It'll be nice to get to hang out with you guys more often like this."

    jm "Oh for sure!"
    jm "Now I can show u some of my favorite cool youtube channels and make you watch them with  me."
    jm " {image=stickers/7.png}"

    um "OOH YES, my laptop was wayyyy too slow for the screensharing to even be possible."

    jm "On that note, it's a little late, so I'll let our resident senior citizen go to bed."
    jm "Night, [name]!"

    um ":O rude!"
    um "Goodnight! <3"
    nvl clear
    scene black with dissolve 
    jump day2

label austin_game:
    show austinc
    um "Sure!"
    am "Hells yea, I'll log in and go to the spawn so I can show you the ropes"
    um "ooh okay!"

    p "It took me a minute to figure out what I was doing, but I was soon after greeted with the view of Austins avatar"
    p "He had a really large lizard walking behind him wherever he went."
    p "The time went by faster than I expected."
    p "before I knew it, it was already 3am."

    um "Thanks Austin! That was super fun!"
    am "It was!"
    am "U better play again soon! You'll get the hang of the combat before you know it."
    um "I hope so! Those mushroom guys were tough at first"
    um "I'm gonna head off to bed now though <3"
    um "ttyl!"

    am "Gnite [name]!"
    nvl clear
    scene black with dissolve 

hide screen username
label day2: 
scene day2 with dissolve
pause 3.0
show screen username
scene jaidenc 
jm "jjjjjjjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkjkjjjj"
jm "awsssssssssssssssssssssssssssssssssssss"
jm "eEEEE"
um "Uh huh?"
jm "EEEQQQQL;"
um "Everything alright bud?"
nvl clear 


"It's actually super early, it was like 7am for me, and he's a few hours behind me. wtf."
"I waited around, but no more jumbled mess came from Jaiden."

show gc1 
lm "wake up dorks"
lm "yall have GOT to see this post" 
lm "The writing is IMMACULATE"
lm "{a=jump:fan_fic}https://www.lytechat.com/forums/post/367509{/a}"

label fan_fic:
    "Luke could hear his heartbeat almost louder than the people talking behind him. The rough brick felt rough against his skin, even the parts covered by his coat."
    "He wasn’t sure how long he’d have to stay there, Chase and Jackson had no clue he was close. There’s no way they could."

"Soft noises began to come from around the corner and Luke’s heart leapt into his throat. Are they? No- theres no way."

"Feeling around in his pocket, he felt the hard plastic of his phone and pulled it out. Luke opened the camera app and tilted it around the corner." 
"Much to his surprise and betrayal, the screen showed him that his two best friends were in a quite compromising position."

"He felt a sense of betrayal, for he had feelings for one of them. Unfortunately, he was also upset that his friends didn’t trust him enough to tell him about their relationship."

"The kissing sounds grew louder, so did his beating heart. He wanted to be anywhere but there"

em "{image=stickers/16.png}"
em "OOH A LOVE TRIANGLE? I am sold bestie"
em "do you know if they have plans to write more?"
em "or is it just like"
em "A lil snippet"
lm "I think it’s just a snippet, but it may be out of a bigger project they're working on?"
lm "At least I hope so"

rm "Chase and jackson fics omg"
rm "it’s so hard to find {i}any{/i} fics with jackson in them, let alone with him as part of the main ship."

rm "@SolarJack, how was ur new game last night loser?"
am "It was delightful, tyvm"
am "I stayed on way later than I should have though"
rm "As you usually do, of course"

jm "robin dont act like you dont have the worst sleep schedule out of all of us"
jm "staying up all night to catch the new episodes the second they air overseas"

rm "okay but at least I’m learning something"
am "hey!"
am "I am too, I’ve got the hand eye coordination of a boss bro"
rm "ok ‘bro’"

zm "Ah, I knew i smelled something"
zm "The joys of sibling bonding in here"
zm "it’s almost like u guys might actually be related or something"
zm "so crazy"

lm "Ziggy!"
zm "Hey Lei! How’s them plants doin?"
lm "{image=stickers/27.png}"
lm "A-Ma-Zing as per usual"
lm "How are your herbs doing?"
zm "uhhh.. I think some are finally beginning to sprout?"
zm "i’m not super sure what to expect with them if I’m being honest"
zm "{image=stickers/23.png}"
zm "my hair may be green, but my thumb is not"
lm "Oh don’t sweat it babes, some of the herbs you’ve got could survive even the blackest of thumbs and hearts"
lm "Besides, youre doing the work and the research, they’ll thrive"

em "shes right, even I’m keeping some succulents alive"
zm "Ok but to be fair,,,"
em "{image=stickers/17.png}"
em "SHH I know they don’t need a lot of watering"
zm "hey u said it, not me"
zm "anyways, im gonna zip out again"
zm "i wanna cook some more"

lm "oooh have fun zig! Send pics when youre done"

"..."
lm "He’s not gonna send pics is he?"
jm "nope"
rm "nnegative"
um "Not  a chance"

lm "oh well, at least i asked"
nvl clear
scene black with dissolve



scene elainac
em "So wait, what potting soil do you use for your pearls?"
em "I've just been using some cheap stuff from the store, but yours look so much better"
em "Oop-"
em "Sorry [name], that was meant for Leilani"
um "it's okay!"
um "Were you talking about succulents??"
em "yeah!"
em "I got one of the cute lil string of pearls one like she has, but mine aren't doing too hot. They're a lil bit droopy"
um "oh no! Do you know what's wrong with it?"

em "I'm not sure yet, I was talking to Leilani about it and she thinks it might be the potting soil or overwatering."
em "I dont {i}think{/i} its overwatering, so I was trying to figure out what type of soil she uses for it"

um "I know nothing about succulents but I think she has a lot of plants, so I'm sure she can help out some!"
em "That's what I'm hoping for!" 

scene black with dissolve

scene elainac

em "She actually just messaged me back"
em "Apparently, she uses one meant for succulents, but mixes it with a kind meant for cactuses???"


menu:
    "Wut-":
        jump wut_one
    "That actually kinda makes sense.":
        jump makes_sense


label wut_one: 
    um "Wut"
    em "Apparently, they're really similar to cactuses. They store water so they don't need as much because they're used to the heat."
    jump quest2

label makes_sense:
    um "That actually kinda makes sense."
    um "Because cactuses don't really need a ton of water either since they store it?"
    um  "unless i'm completely dumb"

    em "no no ur right! I'm not sure why i never thought of that?"
    jump quest2


label quest2:
    menu:
        "Do you have any other plants?":
            jump plants_what
        "Thinking is overrated":
            jump no_think

label plants_what:
    um "Do you have any other plants?"
    em "mostly just succulents!"
    em "I think my first one/oldest one is actually just an aloe vera plant-"
    um "LOL"
    um "How many do you have?"
    em "A few! I think 4-5 plants total, including the two ijust told you about"
    em "The others are just small ones, like I think they're all Echeveria elegans"
    um "what"
    em "Yeah, im not sure what it means, but they're pretty common I think"
    em "At least they look common to me bestie"



label no_think:
    um "Thinking is overrated"
    em "ugh, honestly"
    em "its like your brain NEVER works how its supposed to"
    um "YEAH"
    um "LMAO"

em "Anyways!"
em "im gonna hop off now and see if mom will take me to the garden store so i can get some more soil"
em "bye!!"
um "Ttyl!"
um "goodluck with ur pearls!"
nvl clear


scene scamc

sm "Congratulations!"
sm "You win USER"
sm "Must be 18+ to claim your prize"
sm "Please provide us with your email address and password for your Gleam account so that we can giv prize"



menu: 
    "Give them your info":
        jump get_hacked
    "Block them":
        jump get_blocked

label get_hacked:
    p "Oh, huh."
    p "I guess I signed up for something and forgot about it?"
    p "I sent them a quick message with my information and closed the app."

    "..." 
    nvl clear
    scene jaidenc
    jm "[name]..."
    jm "WHAT DID YOU DO"

    um "Uhh, what?"
    jm "WHAT DID YOU DO??"

    um "WHAT DO YOU MEAN, I'VE BEEN HOME ALL DAY"

    jm "bro"
    jm "We’ve been getting a million notifications from you on gleam."
    jm "And your profile  is completely changed"
    jm "did you manage to get hacked or something?"
    "..."

    jm "[name]..."
    jm "you did, didn’t you"
    um "I DIDNT THINK ANYTHING OF IT"
    jm "LMAO PLS"
    jm "okay okay, how did it happen? We can prolly fix it"


    um "ADD IN SCREENSHOT HERE MAX"

    jm "oh honey.."
    um "that bad?"
    jm "it’s not bad at all, or it shouldn’t be."
    jm "Do you use the same password for all your accounts tho?"
    um "nop, u told me not to"
    jm "good! As long as they haven’t changed your email yet, you should be able to get back into your account"
    jm "We can also set up two factor authentication on there to prevent it in the future"

    um "two factor wha??"
    jm "Two factor authentication"
    jm "It basically makes it so that to log in to your account you need a code outside of using your password"
    jm "So you’d put in your email/username and then your password, but then you'd have to put in a code that goes to your email or phone number to fully log in."

    jm "It keeps stinky people out, even if they do get your password"

    um "Do you have to do it every time you log in??"

    jm "yes, but if you don’t log out of Gleam, you don’t really have to worry about it too often."

    um "Oooh okay, got it"
    um "So how do we fix this?"

    jm "First things first, see if youre still logged into your account"

    um "ok, one second"

    "..."
    um "okay, im still logged in."
    jm "this is good, it means they either haven’t changed the password or haven’t kicked out your log in location"

    um "okay, so what now?"
    jm "Go to your account settings, then look at the log in locations"
    jm "Is there anything out of place there?"

    um "uhhh"
    um "there’s one that says somewhere in Russia"

    jm "russia is interesting"
    jm "ok"
    jm "so"
    jm "Click that little X to the right of the location, and that should log him out."
    jm "if it asks you if you want to log the user out, click yes"

    jm "but be quick because you’ll have to change your password fast"

    um "ok, done"
    jm "Do you know where to go to change your password?"

    um "yes, im doing it right now"

    jm "okay, when you’re done check the log in locations again."
    jm "thats my bad, i should've made you change the pass first"

    um "it’s just me it looks like"

    jm "good good"

    um "So how do we set up the fancy code thing?"

    jm "oh!"
    jm "It’s p easy"
    jm "just go to your security settings where you changed your password at and look for smthn that says multifactor or two factor authentication, or anything like that"

    jm "you can set it up with ur phone number or your email either one, but I’d recommend your email since you literally never know where ur phone is"

    um "Rude-"
    jm ";p"
    um "Okay, I think i got it set up now though"
    jm "good shit, just don’t give anyone ur password, u should know better"

    um "I had a moment of weakness, okay?"
    jm "Ah right, free games and gift cards from strangers with a flagged profile pic"
    um "yeah in hindsight it was stupid but come onnnn"
    jm "I get it ;p but I am absolutely bullying you for it in the group chat."

    nvl clear
    scene gc2
    jm "[name] rlly fell for the laziest scam in the book this morning"
    am "oh is that what happened? I couldn't tell"
    um "Woooww, austin. My feelings are hurt"
    um "this is so mean"
    um "How will I ever carry on living like this?"

    em "and I thought I was dramatic"
    lm "you are"
    lm "more than your succulents actually"
    em "Ow, I’m wounded"
    em "[name], lets leave these bullies"
    jump post_scam1

label get_blocked:
    
    um "uhh, yikes."
    um "No thanks"
    p "Without another word, I grabbed a screenshot and blocked them"

    nvl clear
    scene gc1
    um "Lol guys, look at this"
    um "{image=scamone.png}"
    um "He barely tried XD"

    jm "LMAO 'giv prize'"
    jm "hey"
    jm "hey [name]"
    jm "[name]"
    jm "giv prize"
    jm "pls"
    jm "giv prize pls"

    um "LOL, you're so obnoxious"
    jm "{image=stickers/7.png}"
    jm "maybe, but you love me"
    rm "I don't"
    rm "But also that is incredibly funny, they didn't even do it in like one big glamorous messages like they normally do either"

    jm "You guys are just jealous because I'm better than u"
   


label post_scam1:
    scene gc2
    sysm "jaiden.exe changed the chat photo."
   

    lm "LOL JAIDEN"
    em "PLS"
    em "Why do you have that image"
    rm "Didn't we just change the image away from this?"
    jm "Because it's perfect, thats why"
    jm "and yes we did, but it needed to return"
    jm "As if u dont have ur share of weird ones anyways"

    em "YEAH BUT T MAKES SENSE FOR ME TO HAVE THEM"

    jm "And it doesn't for me"

    em "NO??"

    lm "LMAO"
    zm "Jesus, what's happened in here"
    rm "Ziggy!"
    zm "Hey robin!"
    rm "how’s it hangin?"
    zm "its goin!"
    zm "I was actually about to go cook tho, oops-"
    rm "aw, have fun! Cook us something yummy"
    zm "Aye aye captain"
    nvl clear
    scene black with dissolve

scene jaidenc
jm "I'm so sorry about earlier LMAO"
jm "Mooshi decided she had to tell you all of her thoughts"
um "thank u mooshi, my life has been changed"
um "she has quite the way with words"
jm "Oh absolutely, she'd be a great lawyer"
jm "{image=stickers/6.png}"
jm "She's especially great at convincing people to give her a second dinner"
jm "you'd think shes starving with the performance she puts on"
um "A lady deserves dessert, smh"
um "you should know better"
jm "my mistake, my mistake"
nvl clear
scene black with dissolve 
hide screen username

scene day3 with dissolve
pause 3.0
show screen username
scene gc1
zm "I have returned"
zm "{image=stickers/21.png}"
zm "With food ofc"
zm " {image=pasta.png}"

lm "ziggy"
lm "What the hell is that"
zm "Spgethi!"
rm "that most definitely is not spaghetti"
rm "that is an abomination"

zm "uh no, it's called pasta"
zm "professional cuisine"
zm "u guys just don't know culture"
jm "yeah, come on"
jm "it really doesn't look that bad"
jm "I imagine the sweet gummy really compliments and pairs well with the tomato sauce and makes it less tangy."
zm "EXACTLY DUDE U GET ME"

rm "EW NO"
rm "WHAT"

am "nah, I kinda get it"
am "the apple is a bit much for me tho"
am "like the texture of the peel?"
am "{image=stickers/3.png}"

menu: 
    "That's the best part":
        jump apple_yum
    "BLEGH":
        jump apple_yuck

label apple_yum:
    um "That's like,, the best part"
    rm "WHAT"
    um "yeah! "
    um "its like a nice dried out fruit leather feel, u know from the heat"
    um "I bet it makes the apple inside reaaaaalllllly melt in your mouth, huh?"
    rm "brb, vomiting. Wtaf"
    rm "{image=stickers/15.png}"
    jump post_apple

label apple_yuck:
    um "BLEGH"
    lm "Crying rn omg"
    um "imagine the TEXTURE"
    um "Its gotta be like dried fruit leather"
    um "ugh oh god"
    um "And i bet the apple is all mushy n junk"
    rm "vomiting oh my god"


label post_apple:
    zm "Ur just jealous because you didnt think of it"
    um "On that note, I'm off"
    um "I've got to do some math work and alas, browsing amazon does not count for this one"
    sysm "[username] has logged off"
    scene black with dissolve

" "

scene gc1
nvl clear

lm "https: //www.lytechat.com/forums/post/367513/video.mp4"
lm "ugh, these videos make me tear up every time" 
lm "{image=stickers/26.png}"

"I clicked the link Leilani sent and was immediately met with a video someone had made out of clips from their story, or something like that."

"They were counting down the days they had left until they met their online friend"
"A lot of the clips were just numbers they found out on the street or in buildings somewhere."
"They even showed clips of them on the flight"
"At the last bit of the video, there was a clip of them standing out in a park, watching a car pull in."

"A girl steps out of the car, and pauses for a minute before sprinting at full force to the girl that was making the video"
"They fell to the ground hugging, after a scream of excitement of course"

"It was oddly pure and I felt a pang of loneliness hit me."

"{i} Will I ever get to meet my friends?{/i}"
"Growing up homeschooled was really isolating."
"We don't really have any groups here that also homeschool, so really my only friends were these guys."

um "Brb sobbing omg"
um "I wanna meet you all one day"
rm "omg"
rm "We absolutely need to"
em "Agree omg"
em "idc what the boys say, its a must"
lm "yesssss"

lm "I don't even know how far you guys are either"
lm "what if we all lived super close and didn't even know it omg"

um "I know jaiden is 3 hours behind me, so i don't think so sadly"
rm "sob" 

jm "dont u know its dangerous to tell strangers on the internet your location?"
jm "{image=stickers/9.png}"
jm "but yeah, i live in oregon, p close to the state border with washington tho"

um "oh that's a bummer, I'm over in Maine ;-;"
rm "WAIT U ARE"
um "uhh, ye?"
rm "@solarjack !!"
rm "omg"
um "what is wrong with maine?"
am "We're also in Maine, we're lower in the state like right near the NH line"
um "Oo, we arent too far then. The state isnt that big compared to some others"
um "im on the line too, but up towards the top super close to quebec."
um "like,, my dad used to take trips for work across into Quebec"

am "I didn't realize we were so close! Thats so fucking cool"
lm "And then there's me over here in Texas"
em "NOO NOT TEXAS BESTIE"
lm "I KNOOWW"
lm "ITS TOO HOT"
lm "But my succulents are thriving at least"
em "the only plus side"
em "I'm actually over in Virginia, but not the good part"
em "like,, the part right next to west virginia, tn, ky, that type of area"
jm "Ah, hillbilly hell i believe you referred to it?"
em "you got it"
em "At least there's plenty of farm stores"
em "I wouldn't have been able to find Leilani's special potting soil otherwise."

rm "wait zig where are you"
zm "Oh im closer to jaiden, i'm in socal"
zm "{image=stickers/22.png}"
em "what"
jm "Southern California"
jm "Which is a lot further from me than he thinks considering California takes up like over half of the west coast"
zm "duh, but like i'm closest to you out of everyone else"
jm "Fair enough i suppose"

um "So there's like,, no reasonable way for us all to meet then?"
rm "not that I can think of, no"
em "ugghh, dammit lei, u had me feeling all hyped up about this"
em "now my heart is broken"

lm "Don't get heartbroken yet, im sure we can think of something, come on"
lm "theres like so many things we can look at before we lose hope"

rm "ur right, ur right."
rm "Except the biggest problem-"
rm "literally none of us can drive, nor are we old enough to"
rm "{image=stickers/15.png}"
rm "And i cant imagine our parents being too excited to let us travel halfway across the states to meet strangers from the internet."

em "no, but like, what about siblings?"
em "I dont have any, but my mom will take me anywhere if i mention its an opportunity for something stupid, like modeling or that it would look good for colleges"
am "Its just me and robin"
rm "Alas, but we can get our license at 16 here so even if we have to wait two years, that works on our end."

em "Ziggy, jaiden, [name]?"
zm "I don't even have parents bestie, its just me and gramma"
zm "And honestly, she doesnt even like me LOL"
zm "I think she tries to pretend im not here most of the time"
lm "that is upsetting zig, are you ok?"
zm "oh yea, i can cook p much whatever i want so I dont mind it this way"
lm "Alright, fair enough"

jm "i've got an older brother, but he's like.. In New York or somewhere."
jm "He graduated college like 5 years ago so he's long gone"

lm "[name]? What about you?"

menu:
    "I'm an only child.":
        jump only_child
    "Uhh, not anymore":
        jump had_siblings

label only_child: 
    um "Oh, I'm an only child" 
    jm "at least your mom is pretty cool"
    um "The coolest tbh"

    p "I can't explain why I felt the need to lie to them about it"
    p "I guess its not technically a lie"
    p "I am an only child now"
    p "just didn't used to be"
    p "I think maybe I just didn't want them to feel bad for me?"
    jump post_sib

label had_siblings:
    um "Oh, uhhh"
    um "I don't have siblings, not anymore at least"
    lm "Ohmygod"
    lm "Im so sorry, i hope we didnt make you uncomfortable"
    um "oh no, not at all!"
    em "is it ok to ask what happened?"
    um "I don't mind."
    um "though i dont really know a lot"
    um "Mom never went into details,  but they died when i lost dad."
    um "it was like super close to christmas, so i guess it was a car wreck?"
    um "sorry, not to sound cavalier about it or anything. It's been a few years now and i was still a bit young,s o i dont have the strongest memories of them anyways"
    rm "PLS u are totally fine, im glad we know a bit more about you at least"
    jm "is that why ur homeschooled? ;p"
    um "LOL"


    um "not directly, but kinda"
    jump post_sib
label post_sib:
    um "were a bit on the poor side, and mom works from home, so its just easier to not have to take me to and from school"
    um "especially where we live so far from the closest schooL"
    jm "that makes sense"
    jm "Actually, you haven't told robin about your school situation have you?"
    rm "OwO"
    um "Haha, no not yet. I think ive only really talked about it with you when i was getting resources"
    um "What jaidens talking abt is the fact that my mom lets me read/write fics for my english and language arts grades"
    rm "ARE U SERIOUS"
    rm "@solarjack"
    rm "WHY IS MOM NOT HOMESCHOOLING US RIGHT NOW"
    am "probably because we barely leave the house as it is"
    rm ";-;"
    lm "LOL" 


em "ok back to the topic at hand tho"
em "Would we like,, go to someones house? Like all of us? Or would we go to like an anime expo"

rm "I mean, we could always do an anime expo, especially close to someones house"
rm "bonus points if it has any of the debt collectors VAs"
lm "Oooh ur right, I think theres one somewhere on the east coast isnt there?"
um "Im not 100 percent sure where at, but I know theres one near by"
um "honestly its probably New York or Boston or somewhere like that, Florida, etc"
um "the 'big' cities"
am "I think there's actually one in Augusta that they do yearly, but i fear the price"
jm "god those prices are gonna be killer for anything we do, especially considering none of us have jobs"
em "Speak for urself, my etsy business is a thing"
em "its slow, but like..  Its money "
em "{image=stickers/20.png}"
jm "true true, something is better than nothing"
lm "OOH THAT'S RIGHT, HOW IS THAT GOING"
em "I only have a few sticker designs right now, but im thinking about doing like prints soon"
em "its hard tho bc of the policies abt fan art"
em "stickers get a pass most of the time, and the Debt Collectors team encourages fan art"
em "but etsy is kinda hit and miss with prints of fan art"
lm "that sucks, but it makes sense"
um "what if you do more stationary stuff?"
um "I think you could do like bookmarks pretty cheap"
rm "Oh yeah and like sticky notes too!"
rm "not even fandom relate either, ive seen ur cute chibi art of the fruits"
rm "slap one of those guys on the corner of a sticky note and i bet they'd sell"
em "Idk why i didnt think of other stationary honestly!"

em "but back to the matter at hand"
em "On my end, I have no issues getting anywhere, especially if there are panels at the convention"
em "moms been super supportive lately of my etsy stuff as well, so i can tell her its for business research too if we go to an artists alley"
lm "you could even maybe try to set up at one one year!"
em "Oh god, i dont think my stuff is good enough for that"
em "or enough products really"
um "please, your stuff is amazing"
um "id buy all your stickers if i could"
um "my laptop might be covered, but my new computer is cleaann"
um "it looks nakey"
em "omg [name]"
em "ur too kind"
em "id send u some for free if u wanted"
um "oh absolutely not"
um "we support small businesses in this household"

rm "honestly, if austin and I could find an education event somewhere, mom and dad might be open to taking us."
am "at least on the east coast, yea"
am "dad doesn't like flying too much"
um "I do not blame him, its scary"

jm "my parents aren't too strict on where I go, especially because of the grade skipping and stuff"
jm "but we come back to the issue where none of us can drive yet"
zm "yeaaahh, gramma could care less if im even in her house, let alone alive"
zm "so thats not an issue, but the driving thing"

rm "so we really either have to wait or convince people to take us places"
rm "or public transit"

um "don't forget the money aspect either"
rm "ugghhh"
rm "give me a few days, i wanna do some math and see if we can do this"
em "i believe in you robin"
nvl clear
scene ziggyc 
zm "hey [name]"
um "hey zig! Hows it goin?"
zm "its goin, its goin"
zm "{image=stickers/23.png}"
um "is everything okay?"
zm "oh yea, just thought itd be a good time to catch up and relax!"
zm "gramma is kinda grating on me right now, so im taking a break from the real world right now"
um "Understandable!"
um "Do u wanna talk about it? Or do u just wanna bullshit around?"
zm "there's not too much to talk about, i dont think"
zm "other than her casual racism"
zm "{image=stickers/22.png}"
zm "she's been going out of her way to show me videos n stuff or news articles abt darker skinned men like shes trying to prove a point"
um "ew what the hell??"
um "is it because of your dad or? Is she just always like this?"
zm "a bit of both honestly, but i think mostly because of dad"
um "thats not right dude"
um "I wish she wasnt like that, like you cant control your dad"
zm "Exactly dude, its ridiculous"
zm "but if i tell  myself its just bc shes senile it makes me feel a bit better"
um "LMFAO"
zm "anyways, how have things been for you?"
um "pretty okay! Moms been a bit busy with work after the promotion, but i dont mind"
zm "Oh yeah! I forgot about that!"
zm "does she like it?" 
um "A lot more than she did before, she seems really content"
um "we're going on a late birthday shopping spree soon"
um "I thinks he just wants to make it up to me for all; the gifts missed"
um "but honestly, the computer was more than enough for me"
zm "I get that! It's gotta be so nice being able to have the bigger screen and see everything better"
um "Oh a thousand percent"
um "It's been nice to catch up on the episodes of debt collectors too, i dont have to hold my neck at weird angles bc of the screen"
zm "A huge win IMO"
zm "What are you gonna get on your birthday spree?"
um "I'm not too sure honestly, im thinking of just getting some stuff to upgrade my room now"
um "I might see if she'll let me buy some of elaina's stickers too ;p"
zm "Elaina would FLIP"
um "RIGHT"
um "plus, i have like,,,"
um "ZERO  merch for them yet, and stickers are a nice place to start"
um "well, i {i}had{/i} some stickers, but"
um "theyve seen better days"
zm "LOL"
zm "What did you do to them [name]?? T^T"
um "LOL, nothing I swear"
zm "Riiigghhhttt…"
um "I didnt! They've just been on my laptop for like,, the past 4 years"
zm "Suuureee, thats totally the case"
zm ";p"
zm "anyways, im gonna jet for a bit!"
zm "it's almost time for dindin"
um "Okay!! Enjoy ur food!"
zm "bye!"
um "<3"
scene black with dissolve

nvl clear
scene gc2
zm "gamers"
jm "sup"
zm "ooh perfect, just who i wanted to talk about this"
zm "ur into mythology and stuff like that right?"
jm "I'm a queer teen thats chronically online, of course i am"
zm "perfect"
zm "are you into any pagan-esque things?"
jm "to some extent i guess, why whats up?"
zm "ive been learning more abt paganism, polytheism, etc lately"
zm "tldr is that i wanna set up an altar maybe"
zm "but im not sure where to put it, especially with how grams is"
jm "ooh i see ur problem"
jm "I mean, ur altar doesn't have to be a big fancy table with crystals and jars and all that "
jm "theres like a million ways people keep theirs"
zm "wdym"
jm "uhh, well take mine for example"
jm "well my first one anyways"
jm "I made a 'digital' one so to speak"
jm "its not totally uncommon either"
zm "how do u make a 'digital' one, and why is it in quotes"
jm "quotes just because digital sounds weird, but"
jm "For example, some people make one in minecraft, like you can write in the books, put flowers near it, store diamonds n stuff in chests, etc"
jm "my first one was just a pinterest account"
jm "I had different boards, like one for spells i found, one for pretty photos of other peoples altars, one for different mythology stories, etc."
zm "oooh this sounds smart, im not sure where id start but thats not bad"
um "owo"
zm "oh hey [name]!"
um "popping in because I've actually seen people make really mini ones, like in an altoid can, an old lunch box, and even just inside of a dresser drawer."
jm "Oh yeah! Mine's technically in a dresser drawer right now, but its mostly just to keep Mooshi out of it"
zm "Mooshi is a baby and she deserves to worship the rocks"
jm "maybe if by worship you mean absolutely annihilate them and hide them"
zm "Potato, tomato"
jm "what pantheon are you vibing with my zig zagging friend?"
zm "it might be a bit basic, but I've really been enjoying the greek mythology stories"
zm "IDK what it is, but to me the thought of multiple deities fighting over control of things and causing chaos, makes a lot more sense to me than one all knowing being purposely ruining their own work."
jm "I get that completely, and theres nothing wrong with greek"
jm "the chronically online gate keepers might be snooty about it because its the most popular, but it's a classic"
jm "and it is the most well known bc of a lot of media"
jm "you should check out some of the roman mythology stories, a lot of them have overlap with greek myths and its really fascinating"
zm "I will for sure check them out! Do either of u have a favorite myth?"

menu: 
    "Hades and Persephone":
        jump hades_p
    "Achilles":
        jump achilles_p


label hades_p: 
    um "I'm personally fond of the story of Persephone and Hades, especially as the story changes over time"
    um "ppl can shit on the modern adaptations all they want, but it holds a special place in my heart"
    zm "thats fair! I think i've heard a little bit about that one"
    um "it's a fun one, I love the contrast between them as gods as well"
    jm "oh a hundred percent"
    jm "with persephone being a spring type goddess, helping bring life to the earth after winter, and hades quite literally being a god of death"
    jm "the contrast just makes my brain all happy"
    jump post_myth

label achilles_p:
    um "The story of Achilles!"
    um "most people already know it, but it's a classic"
    zm "oh yeah! He's the ankle guy right?"
    jm "LOL"
    jm "yes! His mother dipped him in a river and the only place that didnt get dipped was his ankle"
    jm "Aka the achilles heel"
    zm "what was the point of that story anyways?"
    jm "uhhh"
    jm "honestly?"
    jm "not a hundred percent sure, but I think something something, 'everyone has a weakness'"
    um "ooh yeah! That makes sense"
    jump post_myth


label post_myth:
    um "admittedly its been a while since ive read it"
    jm "honestly same, It's been a while since I've read much of anything though"
    zm "fair enough my man"
    zm "on that note, im gonna head out"
    zm "see if maybe i can convince gramma to take me to the library"
    zm "Assuming she doesnt think im a criminal in this minute"
    um "good luck ziggy!"
    nvl clear
    scene black with dissolve

hide screen username
scene day4 with dissolve
pause 3.0
show screen username
scene gc2
am "Y'all"
am "I am not kidding when I say I dont think Robin went to sleep last night"
am "i've heard the most aggressive typing and writing all night"
am "{image=stickers/3.png}"
am "and im two rooms down from her"

jm "Damn, she really do be budgeting huh?"
am "Apparently, i swear i dont think ive even heard her leave for food since the last message she sent about the meet up"

rm "{image=stickers/14.png}"
rm "FYI, i did leave once to use the bathroom and grab a hoard of snacks and drinks" 
am "Oh so thats why theres no gogurt left"
rm "Slurp slurp, u butthole"
am "pls do not slurp me"
jm "Lil weird bro"
jm ";p"
em "did you manage to figure anything out robin?"

rm "not a ton yet, i started by narrowing down states and trying to figure out which state/area to look for events"
rm "I think east coast may be the best but, like closer to elaina"
rm "that way its the middle of the coast"
rm "itd be longer travel for ziggy and jaiden, but they also have a bit more freedom than the rest of us"
rm "leilani didn't really say a ton about her situation, so i can look at alternatives later if she comes online again"
rm "but right now I think Virginia or maybe Tennessee might be our best bet"
rm "there's a lot of smaller conventions there, so the entry and hotel room would be cheaper"

jm "That's actually pretty smart"
jm "If you want to message me later, I can run a few algorithms i have to look for cheapest price estimates for a few different hotels and airlines?"
rm "I may take you up on that, but I'm still narrowing down conventions right now to see what best fits our.. Interests?"
jm "{image=stickers/10.png}"
jm "Fair enough"
um "Damn robin, you're really putting in the work on this, huh?"
rm "Might as well lol, I've got nothing better to do this week"
rm "I dont think i ever asked you either about your situation?"
rm "Like would your parents let you go?"
um "oh uh, im not sure"
um "I can ask mom tomorrow though, she doesn't work so I'd have more time to talk to her about and more time to tell her what we have in mind"
rm "hmm, okay!"
rm "just let me know! That way we can change plans now so i can keep budgeting"
um "for sure!"

p "Truth is, I'm not sure that we'd even get to do this."
p "just thinking about the price made my stomach turn"
p "Like, we're all 14, none of us have jobs or even permits or anything yet"
p "I know Robin is invested in figuring this out for us, but it feels so out of bounds"

nvl clear
scene scamc
sm "Lol, Look at this group chat"
sm "https://www.lytechat.com/group/999999999"
sm "I think they used your pictures in here"
p "At least this time, i knew this was just a scam attempt"

nvl clear
scene gc2
um "{image=scamtwo.png}"
um "So I know this one is a scam"
um "But what's the scam here"

jm "could be a few things honestly"
jm "they could just trying to get you to join the chat so they can sell it and rebrand it later"
jm "they could be using a fake link, and the link will try to steal your account"
jm "Which shouldn't be a huge issue for you, now that we have 2fa on ur account"
jm "or its a really heavily flagged group and ur acc gets banned when joining"
jm "its hard to tell" 
um "weird, lyte isnt even a popular app, why would ppl want to steal accounts?"
jm "no life middle aged men in their moms basement wanting to make ppl miserable i guess"
um "mmm i guess so, but my account has like nothing on it? And its still kinda new"
jm "whoknows honestly, maybe they think its half abandoned because you have no profile photo"
um "LOL maybe"
um "I need to get one soon but im so lazy"
jm "Fair enough, i just scribbled mine out one day on my phone bc i didnt want to have a blank profile"

rm "I just took a screencap from an anime i liked"
am "We all know who mine is :D"
rm "oh yes, the lil scaly  baby"
am "youre just jealous bc she likes me more than you"
rm "mmm, shes your gecko, so I'd hope she likes you more"

lm "Mines just a random sunflower photo we took on vacation years ago"
em "also"
em "Hi guys!"
em "{image=stickers/19.png}"

um "Hi elaina!"
um "what are you up to today?"
em "eugh, currently avoiding my mom"
em "{image=stickers/18.png}"
jm "wait why, i thought you loved ur mom?"
em "Normally yea, but shes been super weird today"
em "Like distant and kinda explosive angry over random stuff?"
em "so im just chilling out in here to avoid setting her off"
lm "oh man el, im sorry"
lm "how long has it been since she got like this last time?"
lm "{image=stickers/29.png}"
em "hmm"
em "probably a few months? But its always kinda random"
em "In a few days,or even a few hours, she'll be fine again and back to being hyper and happy"
em "so im just waiting it out up in my room"
em "{image=stickers/20.png}"
em "I told her i was doing some extra credit work, so she should leave me alone"
um "Wait, she does this often or?"
em "Oh yeah, every so often she'll randomly get a stick up her butt and start going off on everyone over every small thing"
em "I guess its just work stress or something? I dunno"
em "But if thats what being an adult is like, ill pass"

um "im gonna go out on a limb and say maybe its not?"
um "because when mom gets stressed, she does not act like that"
rm "I hate to agree, but yeah i dont think thats normal"
rm "Does she have like mental health issues or something?"
rm "like anger issues?"
em "not that I know of?"
em "And yeah i guess it is a bit odd, but maybe her work stuff is just different? I dont really know"
rm "who knows, but i think I'm fully ready to be an adult"
jm "Oh i am definitely not, our internet bill is expensive and I dont know how i'd handle paying bills on my own"
jm "{image=stickers/11.png}"
rm "jaiden ur like the most well equipped out of all of us with ur tech skills"
rm "By the time youre an adult, you'll have so many certificates n stuff that you could get hired like anywhere"
rm "Even google"
jm "eh, maybe"
jm "but like, i dont know if even wanna work for a big company"
jm "What if I want to make games myself and not work for anyone else"
rm "I mean, you could but like"
rm "Not to sound rude or anything"
rm "But what if you dont succeed?"
rm "like what if it doesnt work out?"
jm "I mean I wont know unless I try"
jm "And if it does I try again"
am "Personally, i hope u do make ur own games"
am "I need more games to play, and what game dev doesn't need playtesters"
am "{image=stickers/1.png}"
jm "my man :D" 
rm "I guess that makes sense, I'd just be worried about trying to start my own business of any sort"
em  "it is a little scary, but i think where I'm starting younger, i have time to see what works and what doesnt"
em "but also, I plan to go to college when i graduate and get a degree in something small but helpful, like business financing or something"
em "theres a lot of office work i can do with that, even without it tbh"
rm "hmm, thats smart too"
rm "I guess i just dont want to fail"
am "Its part of life sis, you wont know unless you try"
am "and theres nothing wrong with failing"
am "You gotta worry less and enjoy life sometimes"

lm "..."
lm "guys we aren't even close to being adults yet what is happening"
um "nothing wrong with talking things out though, is there?"
lm "I guess not, but yall are stressing me out"
lm "Getting all emotional on me"

nvl clear

scene scamc
sm "We've detected that your account has slowed down."
sm "Click HERE for a free limited time offer for Free RAM"
p "What the hell is RAM"
"I quickly took a screenshot and went to message Jaiden"

nvl clear
scene jaidenc
um "Jaiiideeeenn"
jm "yeeesss?"
um "What is ram"
jm "What do you mean"
um "{image=scamthree.png}"
um "I think its another scammer, but I have no idea what RAM is"
jm "LOL WHAT"
um ":("
jm "Sorry, not laughing at you, but this guys scam attempt"
jm "man your account has been popular for scams since u got hacked"
um "I know, thats what, two today already?"
jm "yeaah"
jm "Anyways, RAM isn't even something you can download"
jm "{image=stickers/9.png}"
jm "Those scams prey on people that don't know any better"
um "ooh i see"
um "so what is it"
jm "Oh! So Ram is basically something that goes inside of your computer already"
jm "It stands for Random Access Memory"
jm "it's basically just how many things your computer can remember at once"
jm "so if you don't have a lot of ram, you can probably only have one or two things open at a time"
jm "But if you have more ram, you can have like a game, a tv show going, and more"
jm "For example, laptops in general dont have a lot of RAM in them because of how small they are"
jm "So your computer can do more things on it, not just because its bigger, but because in general desktops have more RAM in them"
jm "and even if you dont have a lot of things open at once, having more RAM lets ur computer think faster basically"
jm "Does that make any sense?"
um "kinda actually!"

nvl clear
scene gc1
am "Guuysss, there's a new game coming out on gleam soon!"
jm "Oh?"
am "Hold on, i wasnt done"
am "its like a cool multiplayer game that you can play on browser"
am "you get roles and have to try to figure out what roles the other people have"
am "And you work together secretly to vote people out n stuff"
jm "Oh i think ive seen this!"
jm "Is that the one where like if youre a 'good guy' you have to vote out all the bad guy roles to win, but if youre a bad guy, you gotta kill off the good guys to win?"
am "yeah that one!"
am "its coming out on gleam soon for free, but you can cross play with people playing on browser!"
jm "Oh thats cool, i dont see a lot of cross play like that these days"
um "Ooh, id be down to play it!"
um "I can actually play something for more than 15 minutes at a time now, and i have NO idea what to play so this works out great for me"
am "heck yes"
am "What about the others"
am "@SunshineDreams @twozigzags @babyblues @princessElaina"

zm "{image=stickers/24.png}"
zm "wut"
jm "read up zig"
zm "sec"
p "..."
zm "oh hells yeah, im down!"
zm "I will kick yalls ass at this"
rm "oh in your dreams, logic based investigation type games are my only good area with games"
em "Im not great but id love to try at least!"
lm "Seconding elaina, im always down to do anything to hang with you guys"
am ">:D"
rm "i will take this as seriously as possible and take you down"
zm "In ur dreams nerd"

am "I wont lie, i really expected more convincing to get you guys to try it out"
am "Now i have no idea what to do with myself"
am "{image=stickers/3.png}"
jm "Lmao, just take it as a win bud"
am "Oh i am, because i know i will in fact be losing almost every game when we do play"
um "so when does it come out?"
am "uhh, let me check"
"..."
am "It looks like it comes out in like 3 days!"
um "oh thats not too bad at all!"
am "right? I love when games are announced shortly before they actually come out"
jm "A god send"

em "that lines up perfectly for me honestly, because i have a few small exams coming up tomorrow, but after that i will be free"
lm "a perfect way to destress then"

rm "I think i have one like the day it releases?"
rm "but after i get out of class, we are set and ready besties"

jm "may the best gamer win"
scene black with dissolve
nvl clear
# new day

scene day5 with dissolve
pause 3.0
scene scamc
sm "YOU WIN"
sm "Click HERE to claim your free vacation to Florida!"
sm "All expenses paid vacation"

scene black with dissolve

nvl clear
scene gc2
um "Good morning gamers, we have another one"
um "{image=scamfour.png}"
jm "Damn, its too bad its a scam"
jm "Free travel is exactly what we need right now"
jm "Isn't that right robin?"
rm "GJRFA"
am "I still do not know that she has slept properly between that and studying for exams"
am "I thinks she's gone feral"
rm "I did sleep, but like 4 hours i think"
rm "Im too distracted to sleep to be fair though"
rm "{image=stickers/15.png}"
em "{image=stickers/17.png}"
em "Girl, i've got exams too, but you need sleep"
em "even if you memorize everything, if youre too tired youre gonna have a rough time during testing"
rm "I know i know"
rm "but my brain just will not let me sleep"
rm "Besides, I found out about some more small conventions in TN"
lm "Ooh what did you find?"

rm "There's one, like just outside of a bigger city next to Elaina that has $30 entry per person"
jm "Oh shit actually? That's not terrible"
jm "thats per day?"
rm ":)"
rm "For the whole weekend"
am "Oh shit, thats really cheap"
zm "almost cheap enough to be sketchy"

rm "Yeah i thought that too, but it's just because it's in a smaller town"
rm "And the parking situation is non existent"
rm "And a lot of the voice actors and people at the panels aren't big huge celebs, but still look like mostly people some of us have heard of"
em "What's their artist alley situation look like? Do they have vendors?"

rm "Oh yeah, oddly enough the convention space is like mostly the artist alley, with a small stage for some of the panels during the day"

lm "I guess that makes the cheaper entry price make sense tbh, they probably get a decent amount of money out of the vendors as well"

rm "that was my thought as well"
jm "did you get to look at the travel situation any yet? Or hotels?"
rm "not yet, I'm looking loosely here later tonight after i study some more"
rm "it's hard to get accurate prices for the travel, because i dont know where everyone is or where they can travel from, but i can at least provide some options"
rm "the room situation should be easier, i've just gotta look what's nearby and see rates during the convention season"
rm "also wanna see if they offer a discount rate for convention attendees too, because some places do that"

em "Ooh okay you're thinking way smarter than I would"
em "I know its a lot of work, but I'm glad you're handling it because you're thinking of a lot of stuff i would have never thought of"

rm "Actually, Jaiden was the one that told me to look at the discount one. One of his sites mentioned a hotel somewhere that actually hosts conventions had discount rates, so i wanna see if this one does"

jm ":)"
am "Not 2 distract, but u two ladies better be studying hard, because we have two more days until the game is out and we can play"

zm "I have arrived"
zm "and in two days time, i will reign supreme"
rm "In your dreams"
zm "Oh come on robin, you know you looovee meee ;)"
rm "ew"
rm "no thank u"

lm "LMAO GIRL"
em "Aww, Ziggy have a crush?"
zm "{image=stickers/24.png}"
zm "no but robin might"
rm "again, no thank you"
rm "competitive =/=  flirting"

scene black with dissolve
nvl clear

scene gc2
em "hey guys"
em "I really am thinking more lately about expanding my etsy shop again"
um "I think you should go for it!"
um "it's already getting views and shops, even with only having a few stickers, so why not"
em "yeah exactly!"
em "I'm still just at a loss on what I want to add in"
em "I'm kinda considering taking the suggestion of doing non fan-art stuff too though, i think some of them might do well" 

um "I think you should do it!"
lm "oh yeah absolutely!"
lm "the lil chibi cherries you did were super cute"
lm "{image=stickers/27.png}"
lm "theyd make the perfect sticker for like water bottles and laptops"
rm "I've gotta agree, I'd love some chibi fruits to accent my Debt Collectors stickers i got from you"
em "OMG U GOTS OME FROM ME"
rm ">:D"
rm "yes! Kinda?"
rm "Austin sent the link to mom and explained, and she got them for me as a gift"
am "Yes i did"
am "{image=stickers/4.png}"
em "OMG"
em "Sobbing, youre too sweet, both of you"
em "I love u both sm"


um "Alright guys, I'm off for the night!"
um "@babyblues, I'm gonna talk to mom tonight about the whole convention plan and see what she says!"
sysm "[username] has logged off"

scene black with dissolve
scene kitchen 

"I shut my computer down and headed downstairs to talk to mom"

m "Hey kiddo, whats up?"
p "Nothing much, just wanted to hang out a bit and chat now that you're off work."
"She slides into a kitchen chair, with her face propped up in her hands."
m "All ears hun, what's been going on lately?"
m "Have you done all your classwork for the week"
p "Oh yeah! Well most of it, I've been struggling with some of the math stuff. I think I want to try out a different program"
m "Math is tough, but your writing looks great! I took a peek at your account earlier, and it's really improving!"
"I cringed a little inside at the thought of my mom reading my fanfiction, but it made me really happy to hear that she was seeing improvement"
"It wasn't like I wanted to be a writer or anything, but I do still enjoy it as a hobby"
p "I'm glad actually, I've been really proud of how the story is developing"
m "It had me invested! I haven't read your most recent chapter, but I love what's going on. The tension is better than what I've read in normal fiction books."
m "As for math, we have a little extra  money right now. Do you want a new book or do you wanna sign up for a new program or something?"
p "There's actually a free site Jaiden told me about! It's donation based to keep it up, but it's totally free to use."
p "It basically looks at how you're doing in certain areas and if you're doing well, you do less of that type of problem, or do more advanced ones of it."
p "And if you're not, you get more practice on easier problems for that type."
m "Oh that sounds really nice actually!"
m "Does it keep track of like a score or anything?"
p "I'm not sure, I think it gives you points for each problem you do, but I don't think it gives a graded score."
m "I like that, if you want to try it out go ahead."
m "Just do the same that you did before and send me screenshots of your 'score' at the end of the week"
p "I can do that!"
p "How has work been?"
m "I'm really liking it actually, it's a lot more relaxed than I thought it would be."
p "What are you doing with it?"
m "A lot of looking at statistics and schedules for the new hires."
m "It's now my job to set their schedules and see what areas they're doing good in or not so good in so I can let their supervisor know and they can get training in it."
p "Oh that sounds really relaxed, so you don't have to make calls anymore?"
m "Not too often. I still have to call their supervisors occasionally, because some of them don't always check the chat or their email."
m "Overall it's not too bad."
p "That's not bad honestly! Especially with the pay raise you got with it"
m "Mhm"
m "So what's going on these days with your little online friend group?"
p "Hmm"
p "A lot?"
m "I'm all ears kiddo"
p "Let's see.."
p "Uhh, well Elaina is adding more stickers and stuff to her Etsy store soon. I kinda wanna get some for my computer, since I'm not using my laptop anymore"
p "Ziggy moved in with his grandma, I'm not sure why but I don't feel like it's my place to ask."
m "Is he doing okay? I know how older people get sometimes"
p "Overall, I think so. His grandma has been saying some weird, casually racist stuff lately though because of his dad."
m "I will never for the life of me understand why people are like that"
p "Honestly though"
m "What about the twins?"
p "Oh!"
p "Uhh, Austin gifted me a game on Gleam that we're gonna try to play soon! It's like a fantasy style game where you go on quests in dungeons and kill like goblins and stuff."
m "Mmm, sounds like DND to me"
p "I guess so, i've never gotten to play it so I wouldn't know."
m "Ugh, we're gonna have to get you to play soon. Your father and I used to play all the time."
m "That's how we met you know?"
p "Oh really?"
m "Mhm, our high school had a DND club that played every Thursday night."
p "Huh, that's super neat."
p "... I think"
p "Anyways, Robin has been a lil absent and frazzled lately."
p "She's studying for exams and has been busy with it. According to Austin, she hasn't really been sleeping much either."
p "It doesn't help that she's trying to plan a big group meet up for all of us"
p "It's not like a real plan or anything, like it's all kinda just.. Hypothetical?"
p "But she's really going in deep."
"Mom was just smiling and nodding along with me as I spoke. I felt a lot less nervous about bringing it up"
p "Like she narrowed down the states that would be possible, started looking at which convention, now she's looking at what hotel room prices would be like and all that."
m "She sounds like she's very busy right now."
m "How do you guys plan on paying for all that and getting there?"
p "That's the thing, we aren't a hundred percent sure yet."
p "I guess she's trying to get numbers together first for everyone to see if it's even possible?"
m "She's got a lot of ambition, I'll give her that."
m "Aren't there more of you in that group chat though?"
p "Oh yeah! I still haven't caught you up on Leilani and Jaiden yet!"
p "Leilani hasn't had a whole lot going on lately, not that she's said anyways."
p "I think her school year may already be over though."
p "And Jaiden is just grooving along, he helped me when my account almost got hacked."
"I made sure to include that almost in there because I didn't want mom to not trust me on the internet. It took enough convincing to let her let me have free access"
m "He sounds like such a gentleman"
p "I guess. He is super smart though! He knows how to code and he taught me some stuff about computers and online safety, which was really nice of him"
m "I'll bet. Maybe one day he can teach me how to properly use a spreadsheet"
"I let out a laugh and playfully rolled my eyes at her"

scene black with dissolve
"We carried on the rest of the evening, laughing and chatting. Mom about work and her coworkers, and me about the goings on in the friend group and the shows I had been watching."
"Mom never ended up saying anything about our meetup plans we had been talking about, but she never seemed like she was opposed to the idea."
"I don't know that we'll ever go through with our plans to meet up, but I do know that we kept having this conversation for a while."







return
