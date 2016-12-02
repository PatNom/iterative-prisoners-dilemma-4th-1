####
# Each team's file must define four tokens:
#     team_name: BA
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'BA' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    


def move(their_history):
    '''will only take their history into acocunt when moving'''
    thc= their_history.count('b') + their_history.count('c')
    bhalf= their_history.count('b') > their_history.count('c')
    chalf= their_history.count('c') > their_history.count('b')
   
    
    
    
    
    '''will figure out whether or not the b's or c's are larger, and it will decide what to do based on that'''
    
    
    
    if bhalf== True:
        for x in range(0,thc):
            print 'b',
        
    if chalf==True:
        for x in range(0,thc):
            print 'c',
         
    if bhalf==False and chalf == False:
        for x in range(0,thc):
            print'b',
    
    '''if their_history is empty then it will return b'''
    if thc==0:
        print 'b',

    
'''def test_move(my_history, their_history, my_score, their_score, result):
    calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(their_history=' ',my_history=' ', my_score=0, their_score=0, result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             
              
    
''' 


