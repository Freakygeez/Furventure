define player = Character("You") # Main char is a deer
define driver = Character("Driver")
define fox = Character("Fox")
define cat = Character("Cat")


default Health = 10
default Attack = 3
default Defence = 5
default Strength = 5
default Stamina = 3
default Agility = 6
default Dexterity = 7


#### PROLOGUE ####
# Our player, a lowly deer, finds themselves stripped of all of their belongings they didn't even know they had
# and fast on their way to a life of slavery.
# This pivotal moment in the game determines the next few scenes, will they manage to escape the slaver or 
# will they accept their fate to become a slave?
###################

label start:
with Fade(1, 1, 1)
play sound 'Atmos/Cart.wav' 
scene cart 

#show driver normal
driver "Right you lot, rest break!"
driver "Oh you're alive then, good. I found's you on the side of the road passed out like..."
driver "Must of been bandits or something as you looked in a sorry state an' 
        nothin' on yer save for them clothes of yours."

#show driver serious
driver "Anyway, you're mine now see, slavers rights and all that...."
driver "I'm taking you to Sabel, to be sold. I suppose you could try to run, by the state of you I'd give you maybe a hour before I found's yer again..."
driver "Wouldn't be too pleased mind, would have to take it on on yer."

#Stats['Health'] = 3
"You have 3 HP remaining. You might be able to escape but it'll be risky..."
#show driver laugh fade normal

menu Cart_Escape:
    "What do you do?"
    "Step outside with the others":
        "Resigned to the fact of slavery, you quietly step outside"
        jump outside_cart
    "Your hands are only loosely bound, you reckon you can take him":
        menu Cart_Combat_Scene:
            "How are you fighting him?"
            "Go for the legs! (Agil check)":
                python:
                    from Game_Logic import Stat_check
                    roll = Stat_check(Agility)
                #show roll  will eventually show a number on screen
                if roll >= 18:
                    "As the driver turns to leave you boot him in the back of his knees"
                    "He completely looses his balance faling out of the cart"
                    "His head slams hard onto the dirt, knocking him out cold"
                    
                elif roll < 5:
                    "You attempt to boot the back of the drivers knees as he is about to leave but in your haste you totally miss!"
                    "You end up square on your butt, fortunately the driver didn't seem to notice or just assumed you were still feeling uneasy"
                elif 5 >= roll < 18:
                    "You hit the back of the drivers knees causing them to buckle slightly... To your horror nothing happens"
                    
                    driver "Are you done? I was being nice but now it's my turn!"

                    "The driver whips his body round and backhands you"

                    with Fade
                    jump sabel_as_slave

                python:
                    from Game_Logic import Stat_check
                    roll = Stat_check(Stamina)
                    
            "Go for the face! (Agil + str check)":
                "Face combat"
                #Agil check since the player is sitting down, for them to 
                #Get up and hit in time
                # str for damage if agil check returns true
            
    "Step outside and run! (Agility and sta check)":
        "Jump to outside run logic"
        #Agility check to avoid whip
        #Sta check to keep running 


#label outside_cart:
"""
scene cart exterior with fade
    "Stepping out you are able to better see your surroundings"
    "You appear to be on a main trail heading West toward Sabel"
    "There are only two others with you, a cat and a Fox along with the Driver"
    menu Cart_Info:
        "What do you do?"
        "Talk again to the driver":
            "Driver text"
            #block of code to run
        "Talk to the cat":
            "Cat text"
            #block of code to run
        "Talk to the Fox":
            "Fox Text"
            #Code here
        "Only one guard? I'm running!":
            "Jump back to escape logic"
            #Agility check logic with sub menu
"""