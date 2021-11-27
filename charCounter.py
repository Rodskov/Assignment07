#       Character Counter
#   This program will count the number of words,
#   vowels, and consonants in the sentence that
#   will be input by the user.

#Step 1: Ask the user to input a sentence.
def askUser():
    userSentence = str(input("What would be your sentence?: "))
    return userSentence

userSentence = askUser()

#Step 2: Add references for vowels and consonants.
vowelsList = ["a", "e", "i", "o", "u"]
consonantsList = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "y", "z"]

#Step 3: Do the counting program.
##Word Counter
def wordCounter():
    splitSentence = userSentence.split()
    count = len(splitSentence)
    return count
wordCount = wordCounter()
##Vowel Counter
vowelCount = 0
for l in userSentence:
    if l.lower() in vowelsList:
        vowelCount += 1
#Consonant Counter
consonantCount = 0
for l in userSentence:
    if l.lower() in consonantsList:
        consonantCount += 1

#Step 4: Show the output
def userKnow():
    print(f"Number of words: {wordCount}\nNumber of vowels: {vowelCount}\nNumber of consonants: {consonantCount}")
userKnow()