#I am a python and programming newbie. If you have any tips, advice, or just want to chat. Please contact me at jarrettlumsden@gmail.com
import random
words = open("words.txt", 'r')
wordsList = words.read().splitlines()
originalList = words.read().splitlines()
letters = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
lettersCopy = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
numOfGuesses = 10
length = int(input("Think of a word.\nHow many letters are in your word?: "))
word = "." * length
values = ""
#Creates number system for user
numberSystem = ""
numberSyst = list(range(1, length + 1))
for number in numberSyst:
    numberSystem += str(number)
#Deletes words of length different than user's word
for index in reversed(wordsList):
    if len(index) != length:
        wordsList.remove(index)
#Money maker
while numOfGuesses > 0:
    #Decides word is not in list. Adds word to text file
    if len(wordsList) == 0:
        print("I give up! You win!")
        userWord = input("Please enter your word in lower-case letters: ")
        if userWord not in originalList:
            addition = open("words.txt", 'a')
            addition.write(userWord + "\n")
            addition.close()
        print("Thank you for contributing!")
        break
    letterCheck = ""
    values = ""
    print("I have " + str(numOfGuesses) + " guesses left.")
    #Finds letters not in wordsList and deletes letters
    for index in wordsList:
        for ch in index:
            letterCheck += ch
    for key in lettersCopy:
        values = lettersCopy.get(key)
        if values not in letterCheck and key in letters:
            del letters[key]
    #Letter guesser
    while True:
        guessInt = random.randint(1, 26)
        if guessInt in letters:
            guess = letters.get(guessInt)
            #Don't want to guess the same thing twice
            del letters[guessInt]
            del lettersCopy[guessInt]
            break
    #Game time
    print("Is there a(n) " + guess + " in the word?")
    confirmation = int(input("Press \"1\" for yes, or \"0\" for no: "))
    if confirmation == 1:
        while confirmation == 1:
            print(word)
            print(numberSystem)
            position = int(input("Choose the number that represents the position of the letter: ")) - 1
            confirmWord = list(word)
            word = ""
            confirmWord[position] = guess
            for ch in confirmWord:
                word += ch
            print(word)
            print(numberSystem)
            if "." not in confirmWord:
                print("I win! Try harder next time!")
                break
            print("Is there another " + guess + " in the word?")
            confirmation = int(input("Press \"1\" for yes, or \"0\" for no: "))
            #Deletes words not containing correct guess
            for index in reversed(wordsList):
                if guess not in index:
                    wordsList.remove(index)
    elif confirmation == 0 and numOfGuesses != 1:
        #Deletes words with wrong guess
        for index in reversed(wordsList):
            if guess in index:
                wordsList.remove(index)
        numOfGuesses -= 1
    else:
        #Nobody's perfect
        print("I lose! You're just too good!")
        words.close()
        break
words.close
