define player = Character("You") # Main char is a deer
define driver = Character("Driver") #Bull/Ox
define fox = Character("Fox")
define cat = Character("Cat")
define StatCheck = renpy.add_python_directory('Game_Logic.py')

default Health = 10
default Attack = 3
default Defence = 5
default Strength = 3
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
#ith Fade(1, 1, 1)
play sound 'Atmos/Cart.wav' 


#NOTE: Renpy has a really odd file naming convention:
#    Files can only be located within the image folder (unless pointers are used)
#    Names cannot be camelCase nor capitalised
#
#Convetion to be used for scenes follows standard film naming:
#      int/ext (interior/exterior) [space] location [space] specific location [space] day/night
# i.e. ext palace courtyard night

scene int cart captured

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
    #Initial 1/3
    "Step outside with the others":
        "Resigned to the fact of slavery, you quietly step outside"
        #jump outside_cart
        return #end the game for now
    #Initial 2/3
    "Your hands are only loosely bound, you reckon you can take him":
        menu Cart_Combat_Scene:
            "How are you fighting him?"
            #Combat 1/2
            "Go for the legs! (Agil check)":
                $ roll = StatCheck.Stat_check(Agility)
                #show roll  will eventually show a number on screen
                if roll >= 18:
                    "As the driver turns to leave you boot him in the back of his knees"
                    "He completely looses his balance faling out of the cart"
                    "His head slams hard onto the dirt, knocking him out cold"
                    #jump outside_cart
                    return #end the game for now

                elif roll < 5:
                    "You attempt to boot the back of the drivers knees as he is about to leave but in your haste you totally miss!"
                    "You end up square on your butt, fortunately the driver didn't seem to notice or just assumed you were still feeling uneasy"
                    #jump sabel_as_slave
                    return #end the game for now


                elif 5 >= roll < 18:
                    "You hit the back of the drivers knees causing them to buckle slightly... To your horror nothing happens"
                    driver "Are you done? I was being nice but now it's my turn!"
                    "The driver whips his body round and backhands you"
                    with Fade
                    #jump sabel_as_slave
                    return #end the game for now

            #Combat 2/2     
            "Go for the face! (Str check)":
                $ roll = StatCheck.Stat_check(Strength)
                if roll >= 15:
                    "You somehow manage to strike him straight in the snout, causing the bull to stagger back in shocked pain"
                    "It doesn't take long for him to recover though and throws you a right hook"
                    #ugf tripple nested if is coming up, maybe find a better way to code this
                else:
                    driver "Are you done? I was being nice but now it's my turn!"
                    "The driver whips his body round and backhands you"
                    with Fade
                    #jump sabel_as_slave
                    return #end the game for now
    #Initial 3/3       
    "Step outside and run! (Agility and sta check)":
        "Jump to outside run logic"
        #Agility check to avoid whip
        #Sta check to keep running 

