import random
import string
print("Welcome to Random Password Generator")
def randompassword(length):
    alphabetc = list(string.ascii_uppercase)
    alphabets = list(string.ascii_lowercase)
    special_characters = ["!", "@", "#", "$", "&", "-",
                            "_", "=", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    randomletter = alphabetc+alphabets+special_characters
    strongpassword = ""
    for i in range(length):
        password = random.choice(randomletter)
        strongpassword = strongpassword+password
    return strongpassword

user = int(input("Enter number of password you want: "))
length = int(input("Enter the length of password: "))
for _ in range(user):
    print(randompassword(length))
