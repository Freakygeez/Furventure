define player = Character("You")
define driver = Character("Driver")

# Is it a brand new game?
$new = True 

#### PROLOGUE ####

label start:
    if new:
        jump Character_Creation 
    new = False

    with Fade(2, 3, 3)
    play sound 'Atmos/Cart.wav' 
    scene cart 

show driver normal
driver "Right you lot, rest break!"
driver "Oh you're alive then, good. I found's you on the side of the road passed out,
        must of been bandits or something as you looked in a sorry state an' 
        nothin' on yer save for them clothes of yours."

show driver serious
driver "Anyway, you're mine now see, slavers rights and all that.... 
        I'm taking you to Sabel, to be sold. I suppose you could try to run, by the state of you I'd give you maybe a hour before I found's yer again..."
        "Wouldn't be too pleased mind, would have to take it on on yer."
Stats['Health'] = 3
"You have 3 HP remaining. You might be able to escape but it'll be risky..."
show driver laugh fade normal

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
                    roll = Stat_check(Stats['Agility'], 18)
                    return roll
                show roll
                if roll[1] = True:
                "As the driver turns to leave you boot him in the back of his knees"
                "He falls out of the cart, you jump over him and make a dash for the nearest trees..."
                "D12 to suceed..."
                elif roll[0] > 18:
                    "As the driver turns to leave you boot him in the back of his knees"
                    "He completely looses his balance faling out of the cart"
                    "His head slams hard onto the dirt, knocking him out cold"
                    
                elif roll[0] < 5:
                    "You attempt to boot the back of the drivers knees as he is about to leave but in your haste you totally miss!"
                    "You end up square on your butt, fortunately the driver didn't seem to notice or just assumed you were still feeling uneasy"
                elif roll[1] = False:
                    "You hit the back of the drivers knees causing them to buckle slightly... To your horror nothing happens"
                    driver = "Are you done? I was being nice but now it's my turn!"
                    "The driver whips his body round and backhands you"
                    fade
                    jump sabel_as_slave

                python:
                    from Game_Logic import Stat_check
                    roll = Stat_check(Stats['Sta'], 12)
                    return roll
                show roll
                if roll[1] = True:






            "Go for the face! (Agil + str check)":
                #Agil check since the player is sitting down, for them to 
                #Get up and hit in time
                # str for damage if agil check returns true
            
    "Step outside and run! (Agility and sta check)"
        #Agility check to avoid whip
        #Sta check to keep running 

label outside_cart:
    scene cart exterior with fade
    "Stepping out you are able to better see your surroundings"
    "You appear to be on a main trail heading West toward Deapbury"
    "There are only two others with you, a cat and a kobold along with the Driver"
    menu Cart_Info:
        "What do you do?"
        "Talk again to the driver":
            #block of code to run
        "Talk to the cat":
            #block of code to run
        "Talk to the Kobold":
            #Code here
        "Only one guard? I'm running!"
            #Agility check logic with sub menu
        