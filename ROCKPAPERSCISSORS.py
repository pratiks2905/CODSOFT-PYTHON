import random

print("----------------ROCK PAPER SCISSOR GAME --------------------")
print ('''Hii
Welcome to rock paper scissors game . let's play a game  ''')
user_score=0
computer_score=0
tie=0
while (True):
    
    strings = ("rock", "scissors", "paper")
    print('''Choose one from 
          rock
          paper
          scissors :''')
    user_input = str(input())
    computer_choice= random.choice(strings)
    if (
       (user_input == "rock" and computer_choice == "scissors") or
       (user_input == "paper" and computer_choice == "rock") or
       (user_input == "scissors" and computer_choice == "paper")
    ):
      print("user_choice =",user_input)
      print("computer_choice =",computer_choice)
      print ("User wins")
      user_score+=1
      print ('''Choose one from below :
             1 to play game again .
             2 to exit game .  ''')
      num_input=int(input())
      if num_input==1:
       continue  
      elif num_input==2:
       break
   
    elif (
       (computer_choice == "rock" and user_input == "scissors") or
       (computer_choice == "paper" and user_input == "rock") or
       (computer_choice == "scissors" and user_input== "paper")
    ):
      print("user_choice =",user_input)
      print("computer_choice =",computer_choice)
      print ("Computer wins")
      computer_score+=1 
      print ('''Choose one from below :
             1 to play game again .
             2 to exit game .  ''')
      num_input=int(input())
      if num_input==1:
       continue  
      elif num_input==2:
       break

    elif computer_choice==user_input :
     tie+=1
     print("computer_choice =",computer_choice)
     print("user_choice =",user_input)
     print("TIE")
     print ('''Choose one from below :
             1 to play game again .
             2 to exit game .  ''')
     num_input=int(input())
     if num_input==1:
       continue  
     elif num_input==2:
       break
     else :
      print ("wrong input , enter a valid input ")
      print ('''Choose one from below :
             1 to play game again .
             2 to exit game .  ''')
      num_input=int(input())
      if num_input==1:
       continue  
      elif num_input==2:
       break
print("final score !!","user score = ",user_score , "computer score = ",computer_score,"Ties=",tie)
