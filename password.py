#SYEDA IRRAM HASSAN
#Random Password Gernerator using Python
#CODESOFT INTERNSHIP TASK 3

import secrets 
#generate random numbers that are secure
import string 
#provides  string constants to define alphabet

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

#concatenate the above string constants to make alphabet
alphabet = letters + digits + special_chars
#specifying the length of password
psw_length = int(input("Enter your desired password length: "))

psw = ''  #psw is an empty string
for i in range(psw_length):
    psw += ''.join(secrets.choice(alphabet))   
print(psw)
#secrets.choice(Alphabet)returns one character,randomly
#no whitespace want so we add join method
#the password should contain one special character and two digits
while True:
    psw = ''
    for i in range(psw_length):
        psw += ''.join(secrets.choice(alphabet))
    if (any(char in special_chars for char in psw) and sum(char in digits for char in psw)>=2):
        break
print(psw)
#use an infinite while loop that runs so long as the password string pwd does not meet the constraints
#when psw satisfied for loop will break

