def guess_answer(guess, answer):
  global score
  still_guessing = True
  attempt = 0
  while still_guessing and attempt<3:
    if guess.lower() == answer.lower():
      print("Hurry!!! your answer is correct")
      score = score + 1
      still_guessing = False
    else:
      if attempt < 2:
        guess = input("Sorry,wrong answer -----Try again")
        attempt = attempt + 1

  if attempt == 3:
    print("The correct answer is ",answer)

score = 0
print("-----Questions-----")
guess_1 = input("What is the color of apple? : ")
guess_answer(guess_1, "red")          
guess_2 = input("The actual colour of sun light? : ")
guess_answer(guess_2, "white")  
guess_3 = input("What is 6*7? : ")
guess_answer(guess_3, "42")
print("Your score is " + str(score))

