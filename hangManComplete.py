#I am a python and programming newbie. If you have any tips, advice, or just want to chat. Please contact me at jarrettlumsden@gmail.com
import random
words = open("words.txt", 'r')
wordsList = words.read().splitlines()
originalList = words.read().splitlines()
letters = {1:"a", 2:"e", 3:"i", 4:"o", 5:"u", 6:"y", 7:"b", 8:"c", 9:"d", 10:"f", 11:"g", 12:"h", 13:"j", 14:"k", 15:"l", 16:"m", 17:"n", 18:"p", 19:"q", 20:"r", 21:"s", 22:"t", 23:"v", 24:"w", 25:"x", 26:"z"}
lettersCopy = {1:"a", 2:"e", 3:"i", 4:"o", 5:"u", 6:"y", 7:"b", 8:"c", 9:"d", 10:"f", 11:"g", 12:"h", 13:"j", 14:"k", 15:"l", 16:"m", 17:"n", 18:"p", 19:"q", 20:"r", 21:"s", 22:"t", 23:"v", 24:"w", 25:"x", 26:"z"}
numOfGuesses = 10
length = int(input("Think of a word.\nHow many letters are in your word?: "))
word = "." * length
values = ""
vowelConfirmation = 0
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
        if vowelConfirmation == 0:
            guessInt = random.randint(1, 6)
        else:
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
        vowelConfirmation = 1
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
            #Hopefully more efficient word deleter
            for index in reversed(wordsList):
                count = 0
                while count < length:
                    wordCheck = list(index)
                    if confirmWord[count] != ".":
                        if confirmWord[count] != wordCheck[count]:
                            wordsList.remove(index)
                    count += 1
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
