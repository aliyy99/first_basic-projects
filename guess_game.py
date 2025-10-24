import json
import os
import random

file="game_guess.json"

if not os.path.exists(file):
    with open(file,"w",encoding="utf-8") as f:
        json.dump([],f,ensure_ascii=False,indent=3)

def read_score():
  with open(file,"r",encoding="utf-8") as f:
    return json.load(f)
def show_score():
  scores=read_score()
  for item in scores:
    print(f"game: {item["Game"]}, prediction computer: {item["prediction computer"]}, prediction person:{item["prediction person"]}, scores: {item["result"]}")

def save_score(scores):
  with open(file,"w",encoding="utf-8") as f:
    json.dump(scores,f,ensure_ascii=False,indent=3)  

def add_score():
  scores=read_score()
  game=f"{i}.game"
  prediction_cp=guess_cp
  prediction_p=guess_n
  result=f"computer {score_cp} - {score_p} person"
  score={
    "Game":game,
    "prediction computer":prediction_cp,
    "prediction person":prediction_p,
    "result":result
  }

  scores.append(score)
  save_score(scores)

score_p=0
score_cp=0

i=0
while True:
    print("="*30)      
    print("WELCOME TO PREDICTION GAME")  
    print("="*30)
    print("1.Start game")
    print("2.Show the scores")
    print("3.Exit")
    print("="*30)
    choice=int(input("please choose an option(1-3):"))
      
    if choice==3:
      print("GAME OVER !")
      break
    elif choice==2:
      show_score()
    elif choice!=1 and choice!=2 and choice!=3:
      print("invalid input. please enter between 1 and 3 numbers.")
      continue
    else:
      predict=list(range(1,11))
      number_cp=random.randint(1,10)
      guess_n=0
      while True:
        guess=int(input("enter your prediction(1-10):"))
    
        if number_cp==guess:
           print("that is correct")
           guess_n+=1
           print(f"prediction score: {guess_n}")
           print("="*30)
           break
        elif guess<1 or guess>10:
           print("invalid input. please enter between 1 and 10.")
           continue
        elif number_cp<guess:
           print("enter more little number !")    
           guess_n+=1
        else:
          print("enter more big number !")    
          guess_n+=1


      number=int(input("enter a number between 1 and 10:"))
      guess_cp=0
      while True:
         guess=random.choice(predict)
         predict.remove(guess)
         if guess==number:
          print("that is correct")
          guess_cp+=1
          print(f"prediction score: {guess_cp}")
          print("="*30)
          break
         elif guess<number:
          print("enter more big number !")
          guess_cp+=1
          continue
         elif guess>number:
          print("enter more little number !")    
          guess_cp+=1
          continue
      i+=1
      if guess_n==guess_cp:
         print("you are equal")  
         print("="*30)  
         score_cp+=0
         score_p+=0
         add_score()
       
      elif guess_cp<guess_n:
         print("Computer win !")  
         print("="*30)
         score_cp+=1
         add_score()
      
      else:
          print("Person win !")
          print("="*30)
          score_p+=1
          add_score()
    
       
        
       



