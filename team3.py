####
# Each team's file must define four tokens:
#     team_name: Internalized Oppressors
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random
team_name = 'Internalized Oppressors' # Only 10 chars displayed.
strategy_name = 'Oppression Powers Activated'
strategy_description = 'For the first 3 rounds, use the opponents history to decide how to move, and then after that, use percentages'

    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.


    if len(my_history) == 0:
        return 'c'
    if len(my_history) == 1:
        return 'c'
        
    if len(my_history) ==2:
        if their_history[-1] == 'b' and their_history[-2]=='c':
            return 'c'
        if their_history[-1] == 'c' and their_history[-2]=='b':
            return 'b'
        if their_history[-1] == 'b' and their_history[-2]=='b':
            return 'b'
        if their_history[-1] == 'c' and their_history[-2]=='c':
            return 'c'
    if len(my_history) ==3:
        if their_history[-1] == 'c' and their_history[-2]=='c' and their_history[-3]=='c':
            return 'c'
        if their_history[-1] == 'b' and their_history[-2]=='c' and their_history[-3]=='c':
            return 'b'
        if their_history[-1] == 'b' and their_history[-2]=='b' and their_history[-3]=='c':
            return 'b'
        if their_history[-1] == 'b' and their_history[-2]=='b' and their_history[-3]=='b':
            return 'b'
        if their_history[-1] == 'c' and their_history[-2]=='b' and their_history[-3]=='b':
            return 'c'
        if their_history[-1] == 'c' and their_history[-2]=='c' and their_history[-3]=='b':
            return 'b'
    if len(my_history) >= 3:
        be = float(their_history.count('b'))
        co = their_history.count('c')
        tot = len(their_history)
        bper = float((be/tot))
        last = their_history[-1]
        if bper <=(.1):
            return 'c'
        if bper <=(.2):
            return 'c'
        if bper <=(.3):
            return 'c'
        if bper <=(.4):
            res = random.randint(1,2)
            if res == 1:
                return 'b'
            else:
                return 'c'
        if bper <=(.5):
            return 'b'
        if bper <=(.6):
            return '6'
        if bper <=(.7):
            return 'b'
        if bper <=(.8):
            return 'b'
        if bper <=(.9):
            return 'b'
        return 'wtf happened'    