#       Character Counter
#   This program will count the number of words,
#   vowels, and consonants in the sentence that
#   will be input by the user.

#Step 1: Ask the user to input a sentence.
def askUser():
    userSentence = input("What would be your sentence?: ")
    return userSentence

userSentence = askUser()

#Step 2: Add references for vowels and consonants.
vowels = ['aeiouAEIOU']
consonants = ['bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ']

#Step 3: Do the counting program.

##Word Counter
def wordCounter():
    splitSentence = userSentence.split()
    count = len(splitSentence)
    return count
wordCount = wordCounter()
print(wordCount)