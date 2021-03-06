####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'LaurCar' # Only 10 chars displayed.
strategy_name = 'Weary Collusion'
strategy_description = 'Colludes until betrayed but will collude again if trust regained'

def betrayed(their_history):
    '''Checks if we were betrayed'''
    
    thHis = their_history
    
    if thHis[-3:] == 'bbb':
        return True
    else: 
        return False
        
def colPerc(their_history):
    '''Determines the percentage of their history that is collusion'''
    
    thHis = their_history
    if len(thHis) > 0:
        tot = float(len(thHis))
        colN = 0.0
        colP = 0.0
        for move in thHis:
            if move == 'c': 
                colN += 1
        colP = colN/tot
        return colP
    else: 
        return 'No History'
    
def betPerc(their_history):
    '''Determines the percentage of their history that is betrayal'''
    
    thHis = their_history
    if len(thHis) > 0:
        tot = float(len(thHis))
        betN = 0.0
        betP = 0.0
        for move in thHis:
            if move == 'b': 
                betN += 1
        betP = betN/tot
        return betP
    else:
        return 'No History'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    #Changes Variables Names because underscore conventions suck, and so does my spelling, so do you see the issue? Right.
    mHis = my_history
    thHis = their_history
    mScore = my_score
    thScore = their_score
    
    #Calls the percentage algorithms so that we have a percentage of betrayal and one of collusion
    colP = colPerc(thHis)
    betP = betPerc(thHis)
    
    #The first move will always be to collude
    if mHis == '':
        return 'c'
    
    #runs this if mine and their total history is over two 
    if len(mHis) > 2 and len(thHis) > 2:
        if thHis[-3:] == 'bbb':   #returns b if their last three moves are 'bbb'
            return 'b'
        
        if thHis[-2:] == 'cc' and thHis[-3] == 'b':   #returns c if they betrayed three times ago and colluded for the last two times
            return 'c'
        
        if colP >= 0.65 and thHis[-2:] == 'cc':   #returns b if they're collusion percentage is overor equal to 65% and they have colluded the last two times
            return 'b'
        
        if betP >= 0.8 and thHis[-1] == 'b':   #returns b if they're betrayal percentage is over or equal to 80% and they betrayed in the last time
            return 'b'
    
    return 'c' #returns c if none of the other ifs are filled 
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +", ".join(["'"+my_history+"'", "'"+their_history+"'",
            str(my_score), 
            str(their_score)])+") returned " + "'" + 
            real_result + "'" + " and should have returned '" + 
            result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Collude on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
            print 'Test Passed'
    
     # Test 2: If betrayed 3 times, betray back
    if test_move(my_history='cbb', 
                their_history='bbb', 
                my_score=0, 
                their_score=0, 
                result='b'):
          print 'Test Passed'  
 
   # Test 3: If offered collusion twice after betrayal, collude
    if test_move(my_history='bbb', 
                their_history='bbbcbcc',
                my_score=0,
                their_score=0,
                result='c'):
        print 'Test Passed'
   
    # Test 4: If they collude 90% of the time, betray them
    if test_move(my_history= 'ccc', 
                their_history= 'cccccccccc', 
                my_score=0,
                their_score=0,
                result='b'):
        print 'Test Passed'
        
    # Test 5: When all else fails, collude
    if test_move(my_history='bbbbbbbbbb',
                their_history='ccbcbcbcbcbcbc',
                my_score=0,
                their_score=0,
                result='c'):
        print 'Test Passed'
    
    #Second Move
    if test_move(my_history='c',
                their_history='c',
                my_score=0,
                their_score=0,
                result='c'):
        print 'Test Passed'