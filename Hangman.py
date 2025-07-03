import random

#functions
def get_random_word():
  word_list = ["ant", "boy", "dog", "man", "goat", "boat", "woman" ]
  word = random.choice(word_list)
  return word


def print_start_word(word, guess_letters):
  blank_word = "_" * len(word)

  print(f"You have used these letters:{guess_letters}")

  hint1 = random.randint(0, len(word)-1)
  hint2 = random.randint(0, len(word)-1)

  letter_hint1 = word[hint1]
  letter_hint2 = word[hint2]

  new1 = blank_word[:hint1]+letter_hint1+blank_word[hint1+1:]
  blank_word = new1

  new2 = blank_word[:hint2]+letter_hint2+blank_word[hint2+1:]
  return new2


def get_correct_index(word, guess):
  count = 0
  for lett in word:
    if lett != guess:
        count += 1
    else:
      break

  return count
         
    
def replace_index(correct_index, guessing_word, word):
  replacement = word[correct_index]
  new = guessing_word[:correct_index]+replacement+guessing_word[correct_index+1:]
  return new
   

#statments
word = get_random_word()
# print(word)

guess_letters = []
max_wrong_trys = 6
wrong_trys = 0

start_word = print_start_word(word, guess_letters)
print(start_word)

while wrong_trys < max_wrong_trys and start_word != word:
  guess = input("Enter a letter:")

  if guess in guess_letters:
    print(f"you guessed {guess}")
    continue

  guess_letters.append(guess)
  print(f"Guesed letters : {guess_letters}, Remaing trys : {max_wrong_trys-wrong_trys}")
 
  if guess in word:
    correct_index= get_correct_index(word, guess)
    start_word = replace_index(correct_index, start_word, word)
    print(start_word)
  else:
    wrong_trys += 1
    print(f"{guess} is not in the word")

if start_word == word:
  print("You guessed the correct word")
else:
  print(f"You finished your trys.")

