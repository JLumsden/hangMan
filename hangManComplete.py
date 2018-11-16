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
numberSystem = ""
numberSyst = list(range(1, length + 1))
for number in numberSyst:
    numberSystem += str(number)
for index in reversed(wordsList):
    if len(index) != length:
        wordsList.remove(index)
while numOfGuesses > 0:
    if len(wordsList) == 0:
        print("I give up! You win!")
    letterCheck = ""
    values = ""
    print("I have " + str(numOfGuesses) + " guesses left.")
    for index in wordsList:
        for ch in index:
            letterCheck += ch
    for key in lettersCopy:
        values = lettersCopy.get(key)
        if values not in letterCheck and key in letters:
            del letters[key]
    while True:
        guessInt = random.randint(1, 26)
        if guessInt in letters:
            guess = letters.get(guessInt)
            del letters[guessInt]
            del lettersCopy[guessInt]
            break
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
    elif confirmation == 0 and numOfGuesses != 1:
        for index in reversed(wordsList):
            if guess in index:
                wordsList.remove(index)
        numOfGuesses -= 1
    else:
        print("I lose! You're just too good!")
        break
