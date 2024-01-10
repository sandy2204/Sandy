import random

print("Welcome to Random Password Generator")
randome_chars ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+=/-|"

numb_of_pass = int(input("Please Enter the Number of passwords to be generated: "))
pass_len=int(input("Enter the Length of the password: "))

print("Results: ")
for x in range(numb_of_pass):
    pwd = ""
    for chars in range(pass_len):
        pwd= pwd+ random.choice(randome_chars)
    print(pwd)