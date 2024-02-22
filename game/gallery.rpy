init python:
    gallery = Gallery()

    gallery.button("Red") 
    gallery.unlock_image("CG_Red") 

    gallery.button("blue") 
    gallery.image("CG_blue")
    gallery.condition("persistent.blue_unlocked") 

    gallery.button("green_and_orange")
    gallery.unlock_image("CG_green")
    gallery.unlock_image("CG_orange") 

    gallery.button("green_and_orange2") 
    gallery.condition("persistent.green_unlocked and persistent.orange_unlocked") 
    gallery.image("CG_green")
    gallery.image("CG_orange") 
    gallery.image("CG_pink") 
    gallery.condition("persistent.pink_unlocked") 

screen album:
    tag menu
    add "images/CustomUI/bg gallery.png"
    
    hbox:
        xalign 0.5
        yalign 0.6
        spacing 30
        grid 3 2:
            add gallery.make_button(name="Red",unlocked="CGs/small/Red_small.jpg",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="Red",unlocked="CGs/small/Red_small.jpg",locked="CGs/small/locked.jpg") 
            add gallery.make_button(name="Red",unlocked="CGs/small/Red_small.jpg",locked="CGs/small/locked.jpg") 
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="CGs/small/locked.jpg") 
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="CGs/small/locked.jpg") 
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/Red_small.jpg",locked="CGs/small/locked.jpg") 
            
            spacing 15
    imagebutton auto "images/CustomUI/g_return_%s.png" xpos 1729 ypos 87 focus_mask True action Return() hovered [ Play("sound", "audio/click.wav") ]