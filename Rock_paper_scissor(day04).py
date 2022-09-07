rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if(user_choice==0):
  print("Rock")
  print(rock)
elif(user_choice==1):
  print("Paper")
  print(paper)
elif(user_choice==2):
  print("Scissors")
  print(scissors)
else:
  print("invalid")

computer_choice= random.randint(0,2)
print(f"Computer choose {computer_choice}")

if(computer_choice==0):
  print("Rock")
  print(rock)
elif(computer_choice==1):
  print("Paper")
  print(paper)
elif(computer_choice==2):
  print("Scissors")
  print(scissors)
else:
  print("invalid")

if(user_choice==computer_choice):
  print("The game is draw")
elif(user_choice<computer_choice and user_choice<computer_choice-1):
  print("You lose")
elif(user_choice>computer_choice):
  print("You win")
else:
  print("wrong")




# random.choice(random.game)
# print(random.game)

