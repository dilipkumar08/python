import random as rd

def Game():
    List=['Rock','Paper','Scissor']
    Computer=random.choice(0,3)
    Computer_choice=List[Computer]
    
    player=input("what do you want to chose:\n1)Rock.\n2)Paper.\n3)Sissor.\n")


    while player!='1' and player!='2' and player!='3':
        player=input("Enter only 1,2,3")


    player_choice=List[int(player)-1]
    print("yours choice is",player_choice)
    print("computer's choice is",Computer_choice)


    if Computer_choice==player_choice:
        print("the match is draw!")

    elif Computer_choice=='Rock':
        if player_choice=='Paper':
            print("you won the match :)")
        elif player_choice=='Scissor':
            print("you lose the match :(")
    
    elif Computer_choice=='Paper':
        if player_choice=='Scissor':
            print("you won the match :)")
        elif player_choice=='Rock':
            print("you lose the match :(")
    
    elif Computer_choice=='Scissor':
        if player_choice=='Rock':
            print("you won the match :)")
        elif player_choice=='Paper':
            print("you lose the match :(")


play_again='yes'
while play_again=='yes':    
    Game()
    play_again=input('Type "yes" if you want to play again!').lower()
