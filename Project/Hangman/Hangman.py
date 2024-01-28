from word import words
import random
import string

def get_valid_word(words):
    word=random.choice(words) #Randomly choose somthing from list
    while "_" in word or " "in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters=set(word) #letters in world
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #what the user has gussed

    lives=6

    #getting user  input
    while len(word_letters)>0 and lives>0:
        
        #tell user letters used and live remaning
        print("You have",lives,"lives left and You have used these letters : ", " ".join(used_letters))

        #what current world is 
        world_list =[letter if letter in used_letters else "_" for letter in word]
        word_list_dis=" ".join(world_list)
        print("Current World is ",word_list_dis)
        user_letter=input("Guess a letter:  ").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1

        elif user_letter in used_letters:
            print("You have already used that character please try again ")

        else:
            print("Invlid character. please try again...")

    if lives == 0:
        print("You dies , sorry word was" ,word)
    else:
        print("You guessed  the world  ", word, " !!!")


    print(word_list_dis)

hangman()