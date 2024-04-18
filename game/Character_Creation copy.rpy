image Player = Composite(
    (846, 1028),#dimensions
    (0, 0), #coords
    "Character/Player[Species].png"
) 
#The type of species gives marginal base stat advantages
$ Type = ['Fox', 'Cat', 'Deer']
$ Gender = ['Male', 'Female']

#Default choice is a male Deer
$ Species = Type[2]
$ sex = Gender[0]

$ Stats = {
    Health: 10,
    Attack: 3,
    Deffence: 5,
    Strength: 5,
    Agility: 6,
    Dexterity: 7
}


'''
Whilst each species are pretty weak any way,
the players choice will earn various marginal, 
traits, ad/disadvantages beyond just affecting
dialogue and cut scenes.
'''

Player
## Displaying the character selection menu
transform half_size:
    zoom 0.5


label Character_Creation:
    scene background at half_size
    show Player at center
    "Character setup"

    python:

        match Species:
            case 'Fox':
                Stats['Attack'] = 6
                Stats['Defence'] = 4
                Stats['Dexterity'] = 5
            case 'Cat':
                Stats['Health'] = 12
                Stats['Strength'] = 3
                Stats['Agility'] = 8
                Stats['Dexterity'] = 9




jump start

