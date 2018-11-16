import random
import copy
words = open("words.txt", 'r')
wordsList = words.read().splitlines()
letters = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
lettersCopy = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
inverseLetters = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
numOfGuesses = 10
length = int(input("Think of a word.\nHow many letters are in your word?: "))
word = "." * length
letterCheck = ""
values = ""
numberSystem = ""
numberSyst = list(range(1, length + 1))
for number in numberSyst:
    numberSystem += str(number)
for index in reversed(wordsList):
    if len(index) != length:
        wordsList.remove(index)
print(wordsList)
while numOfGuesses > 0:
    values = ""
    print("I have " + str(numOfGuesses) + " guesses left.")
    guessInt = random.randint(1, 26)
    for key in letters:
        if guessInt == key:
            guess = letters.get(guessInt)
            del letters[key]
            del lettersCopy[key]
            break
    print(letters)
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
            for index in reversed(wordsList):
                if guess not in index:
                    wordsList.remove(index)
        print(wordsList)
    elif confirmation == 0 and numOfGuesses != 1:
        for index in reversed(wordsList):
            if guess in index:
                wordsList.remove(index)
        print(wordsList)
        for index in wordsList:
            for ch in index:
                letterCheck += ch
        for key in lettersCopy:
            values = lettersCopy.get(key)
            if values not in letterCheck and key in letters:
                print(values)
                del letters[key]
        numOfGuesses -= 1
    else:
        print("I lose! You're just too good!")
        break
