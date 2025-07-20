import random 
def get_choices():
    player_choice=input("what's player choice ")
    options=["rock","papers","scissors"]

    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print("you chose"+player+ ",computer chose"+computer)
    if player==computer:
     print("score: you = 0 and computer = 0")
     
     return "it's a tie"
    elif player=="paper" and computer=="rock":
     print('score: you = 1 and computer = 0')
     return " paper engulfed the rock, You won!"
    elif player=="rock" and computer=="scissors":
       print('score: you = 1 and computer = 0')
       return "you smashed the scissors, You won!"
    elif player=="scissors" and computer=="paper":
       print('score: you = 1 and computer = 0')
       return "you won"
    else:
       print('score: you = 0 and computer = 1')
       return "computer won"
    
    
    
def play_again(yes,No):
   again=input('do you want to play again yes or No ')
   if again==yes:
      get_choices()
   else:
      print('exit the game')
      
   
   

choices =get_choices()
result=check_win(choices['player'],choices['computer'])
print(result)

again=play_again('yes','No')
