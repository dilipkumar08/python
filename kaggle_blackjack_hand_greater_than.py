def handscore(hand):
    kgj={'K':10,'Q':10,'J':10}
    ace=0
    h=0
    for i in hand:
        if i in {'K','J','Q'}:
            h+=10
        elif i=='A':
            h+=1
            
            ace+=1
        else:
            h+=int(i)
     
    while(ace>0):
        if h+10>21:
            ace=0
        else:
            h+=10
            ace-=1
    return h
            

def blackjack_hand_greater_than(hand_1, hand_2):
    
    h1=handscore(hand_1)
    h2=handscore(hand_2)
    if h1>h2 and h1<=21:
        return True
    elif h2>21 and h1<=21:
        return True
    elif h1>21 and h2<21:
        return False
    else:
        return False
        

    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    pass

# Check your answer
q3.check()   
