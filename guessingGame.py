import random

guess = int(random.random() * 10)

chance = 0


while chance < 3:
  number = input("guess a number between 0 - 9")
  if int(number) == guess:
    print("you WIN " + number)
  elif int(number) > guess:
    print("too high " + number)
  elif int(number) < guess:
    print("too low" + number)
  chance += 1  
else:
  print("3 chances over")
 
