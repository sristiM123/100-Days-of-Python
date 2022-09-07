#Step 1 



#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_game= False
from hangman_words import word_list



random_choice= random.choice(word_list)
word_lenght= len(random_choice)
# print(random_choice)

a=6

# for a in c:
#   if (guess ==a):
#     print("right")
#   else:
#     print("wrong")


display=[]
word_lenght= len(random_choice)
for _ in range(word_lenght):
  display += "_"

  
while not end_game:
  
  guess= input("Enter a letter: ").lower()
  for position in range(word_lenght):
    letter = random_choice[position]
    # print(f"Current position: {position}\n Current 
    # letter: {letter}\n Guessed letter: {guess}")
    
    if letter == guess:
        display[position] = letter
      
  if guess not in random_choice:
    a-=1
    if a == 0:
      end_game=True
      print("You lost")
        
  print(f"{' '.join(display)}")

       
  if "_" not in display:
    end_game=True
    print("you win")

  print(stages[a])      





  
  
  
  

  
  
  
  
