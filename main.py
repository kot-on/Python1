import re
import random
def start():
    a = random.randint(0,9)
    with open('Key.txt', 'r',encoding='utf-8') as f:
        keyword = f.readlines()
    word = keyword[a].strip().lower()
    return word
start()
def display_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        =========
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        =========
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        =========
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        =========
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        =========
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |     
        =========
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        =========
        """
    ]
    return stages[min(attempts, len(stages) - 1)]   
attempts = 0
guessed_letters = []
correct_letters = []
secret_word = start()
while attempts < 6:
    display_word = ""
    for letter in secret_word:
       if letter in correct_letters:
          display_word += letter + " "
       else:
          display_word += "_ "
    print("\nСлово:", display_word.strip())
    print(display_hangman(attempts))
    if all(letter in correct_letters for letter in secret_word):
       print("\nПоздравляем! Вы угадали слово:", secret_word)
       break
    guess = input("Введите букву: ").strip().lower()
    if len(guess) != 1 or not guess.isalpha():
       print("Пожалуйста, введите одну букву!")
       continue
    if guess in guessed_letters:
       print("Вы уже пробовали эту букву!")
       continue
    guessed_letters.append(guess)
    if guess in secret_word:
       correct_letters.append(guess)
       print("Верно!")
    else: 
       attempts += 1
       print("Неверно!")
if attempts == 6:
   print(display_hangman(attempts))
   print("\nВы проиграли! Загаданное слово было:", secret_word)