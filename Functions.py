def Display(txt, speed='normal' ):
    '''
    Emulates a typed feel, default is about very fast touch type speed
    '''

    from time import sleep
    match speed:
        case 'normal':
            for char in txt:
                print (char,end='')
                sleep(0.02)
        case 'fast':
            for char in txt:
                print (char,end='')
                sleep(0.01)
        case 'slow':
            for char in txt:
                print (char,end='')
                sleep(0.1)
    sleep(0.5)

def Choice (choices=['Option A','Option B','Option C'], question='What do you do?'):
    '''
    Uses fancy menus
    '''
    from rich.panel import Panel as option
    from rich import print
    answer = False
    while answer == False:
        for choice in range(len(choices)):
            print(option.fit(choices[choice]),end=' ')
        Display('\n'+question,'fast')
        
        user_input = input(': ').title()
        if user_input in choices:
            answer = True
            return user_input
        else:
            Display('\n'+"Sorry, that wasn't a valid choice...\n",'fast')



def __Choice__ (choices=['A','B','C'], question='What do you do?'):
    '''
    Legacy code

    Accepts a list of choices <- you probably don't want more than three to not confuse the player nor ruin the look.
    The menu box will scale automatically according to the amount of choices available.
    Checks the input is a valid choice and then returns it
    '''
    from rich.panel import Panel
    choice_in_list = False
    while not choice_in_list:
        a = len(str(choices)) 
        b = 10 # length of '    --    '
        c = len(choices) * 20 #length of gaps between choices
        x = a+b+c
        print("\n")
        for i in range(x):
            print("_",end='')
        print('\n')

        for i in range(len(choices)):
            if choices[i] != choices[-1]:
                print ("        ",choices[i],"        ",end='    --    ')
            else:
                print ("        ",choices[i],"        ",end='')
        print ('\n')
    
        for i in range(x):
            print("_",end='')
        print('\n')
        choice = input(question +' ')
        if choice in choices:
            choice_in_list
            return choice
        else:
            Display('Sorry, that choice is not available, try again...')
        
#TODO get decryption working

def Create_Character(NAME='Player',HP=10,MANA=10,STRENGTH=3,DEFENCE=6,INTELIGENCE=3,AGILITY=4, a_monster=False, mode='easy'):
   #TODO Finish this function
   
    '''
    Responsible for the character sheet creation, stores as an encrypted json.
    '''

    character = {'Name': NAME,
                    'HP': HP,
                    'Mana': MANA,
                    'Strength': STRENGTH,
                    'Defence': DEFENCE,
                    'Intelligence': INTELIGENCE,
                    'Agility': AGILITY
                }
    monster = {'Name': NAME,
                    'HP': HP,
                    'Mana': MANA,
                    'Strength': STRENGTH,
                    'Defence': DEFENCE,
                    'Intelligence': INTELIGENCE,
                    'Agility': AGILITY
                }
    if not a_monster:
        with open('CharacterData/'+NAME+'.TerminalQuest','wb') as f:
            f.write(character)
        return character
#TODO confirm percentages
    elif mode == 'easy':
       with open('CharacterData/Player.TerminalQuest','rb') as f:
           PLAYER = f.read()
           monster['HP'] = PLAYER['HP']*1.25
           monster['Defence'] = PLAYER['Defence']//2
           monster['Mana'] = 2

       with open('CharacterData/'+NAME+'.TerminalQuest','wb') as f:
           f.write(monster)
       return monster
    
    elif mode == 'medium':
       with open('CharacterData/Player.TerminalQuest','rb') as f:
           PLAYER = f.read()
           monster['HP'] = PLAYER['HP']*2
           monster['Defence'] = (PLAYER['Defence']*3)//4
           monster['Mana'] = 4

       with open('CharacterData/'+NAME+'.TerminalQuest','wb') as f:
            f.write(monster)
       return monster
    

    elif mode == 'hard':
       with open('CharacterData/Player.TerminalQuest','rb') as f:
           PLAYER = f.read()
           monster['HP'] = PLAYER['HP']*4
           monster['Defence'] = PLAYER['Defence']*2
           monster['Mana'] = 20

       with open('CharacterData/'+NAME+'.TerminalQuest','wb') as f:
           f.write(monster)
       return monster



def Random_Event(possible_events = []):
    '''
    Randomly selects from a list of possible events and returns the choice.
    '''
    from random import choice

    return(choice(possible_events))



def img_to_bin(img, name):
    '''
    Converts image to raw binary format
    '''
    from PIL.Image import open
    from numpy import asarray
    
    pic = open(img)
    d = asarray(pic)
    d = (d*2)/4
    d.tofile(name)


def bin_to_img(img):
    from PIL.Image import fromarray, open
    from PIL import ImageShow
    from numpy import asarray

    d = asarray(img)
    d = (d*4)/2
    pic = fromarray(d)
    return ImageShow(pic)


bin_to_img('/media/unkown/GREENUSB/TerminalQuest/test_bin')