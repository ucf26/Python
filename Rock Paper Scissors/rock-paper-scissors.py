import random 

choices = ['rock', 'paper', 'scissors']


computer = random.choice(choices)
player = None

while True:
    
    computer = random.choice(choices)
    player = None
    
    while player not in choices:
        player = input("Rock, Paper or Scissors? :").lower()
    
    
    if player == computer:
        print("Computer: ",computer)
        print("Player: ",player)
        print("Tie !!\n")
        
    elif player == 'rock':
        if computer == 'paper':
            print("Computer: ",computer)
            print("Player: ",player)
            print("you lose !!\n")
        if computer == 'scissors':
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win ^_^ !!\n")
            
    elif player == 'scissors':
        if computer == 'paper':
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win ^_^ !!\n")
        if computer == 'rock':
            print("Computer: ",computer)
            print("Player: ",player)
            print("you lose !!\n")
            
    else : # player is paper
        if computer == 'scissors':
            print("Computer: ",computer)
            print("Player: ",player)
            print("you lose !!\n")
        if computer == 'rock':
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win ^_^ !!\n")
    
    again = None
    while again not in ['yes', 'no']:
        again = input('Again?.. (yes/no)').lower()
    
    if again != 'yes':
            break 
        
        
        
print('Bye..!')

    
        