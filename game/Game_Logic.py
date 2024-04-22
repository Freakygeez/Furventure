def Stat_check(player_stat = int):
    '''
    Simulates a D20 die roll, incorperating the players stat into the mix as well.
    '''

    from random import randint

    roll = randint(1,20)

    return roll + player_stat

    