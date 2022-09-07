print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
your_choice1= input("Where do you want to go, left or right?\n")
lower_case_choice1= your_choice1.lower()

if(lower_case_choice1=="right"):
  print("Game over! You fell into a hole")

elif(lower_case_choice1=="left"):
  your_choice2= input("Do you want to swim or wait for the boat?\n")
  lower_case_choice2= your_choice2.lower()

  if(lower_case_choice2=="swim"):
    print("Haha! you are attacked by trouts! GAME OVER!!")
  elif(lower_case_choice2=="wait"):
    print("The boat will take to the last step")
    your_choice3= input("Which door will you choose, blue yellow or red\n")
    lower_case_choice3= your_choice3.lower()
    if(lower_case_choice3=="red"):
      print("Game over you loser")
    elif(lower_case_choice3=="blue"):
      print("Such a loser!!!!")
    elif(lower_case_choice3=="yellow"):
      print("Congratulations you won the game!")
    else:
      print("Wrong input")
  else:
    print("Wrong input")
else:
  print("You lose")
      
    
    
