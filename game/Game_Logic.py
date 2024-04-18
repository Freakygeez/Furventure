def Stat_check(player_stat, required_roll = int):
    '''
    A simple logic test, the 'required_roll' is an arbitrary int
    from at least 5 -> 20 with higher numbers representing greater
    difficulty.
    The player 'rolls' a die which generates a random integer, this 
    int then has the 'player_stat' added onto it.
    If the 'resulting_number' >= 'required_roll' the function returns
    true.

    i.e. 

    A player wishes to jump across a closing drawbridge:
     . This requires a dex check of 18 to suceed
     . The player's dex is currently 6

     They roll a 12
     12 + 6 = 18
     The function returns True

     Note, this function is not concerned about edge cases yet,
     the code of crit' success/fail is too difficult to realistically 
     implement

    '''

    from random import randint

    roll = randint(1,20)

    result = roll + player_stat

    if result >= required_roll:
        return roll, True
    else:
        return roll, False
    