##              Password Validator
#   This program will check if your password is valid
#   according to specific criteria:
#       a. Greater than 15 letters
#       b. Have at least one capital letter
#       c. Have at least one number
#       d. Have at least one special char (!@#$%^&*()_+ etc)

#Ask the user for password
def askUser():
    userPassword = str(input("Input a password: "))
    return userPassword

userPass = askUser()

#A. Make sure the password is greater than 15 letters
charCounter = 0
for char in userPass:
    charCounter += 1
    if charCounter<15:
        greaterFifteen = False
    else:
        greaterFifteen = True

#B. Make sure it has at least one capital letter
capCounter = 0
for char in userPass:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        capCounter += 1
        if capCounter >= 1:
            capLetter = True
        else:
            capLetter = False

if capLetter == True:
    print("Oks")
else:
    print("ayaw")