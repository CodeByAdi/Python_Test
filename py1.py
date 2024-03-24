# ip =input("Enter target ip address? ")
# print(' your ip is '+ip)
# print("you are targeting "+input("what would you llike to target!"))
# x=2
# y='adi'
# print(str(x)+" "+y)
# a=2
# b='2'
# print(int(b)+a) #converting into int
# name=input('what is Your name? ')
# print('welcome Your Name is '+name)
# --------------
# fname=input('what is your first name?')
# lname=input('what is your last name')
# print(f"your name is {fname} {lname}")
#-------------------
# print('Hello , Thank You :)')
# petname=input("What is Name of Your Pet?")
# born_city=input("what city are you born ?")
# print(f"your new twitter handle and bio is @cyber{petname} from {born_city}")
# final_print=("your new twitter handle and bio is"+"cyber"+{petname})
#---------------------
# print(type(1))
# print(type("hello"))
# print("hello world"[4])
#-----------
# snum=input("enter second number")
# below code are neted code for student grade based on their age->
 
# if marks>=80:
# age=int(input("Enter Your age --> "))
# else age<10:
#  print("Grade B+")
# else: 
#  print("Grade B")

# elif marks>=70 and marks<=79:
#  age=int(input("Enter Your age --> "))
# if age<10:
#  print("Grade C+")
# elif age>10:
#  print("Grade C")

# elif marks>=60 and marks<=69:
#   age=int(input("Enter Your age --> "))
# if age<10:
#  print("Grade D+")
# elif age>10:
#  print("Grade D")
# elif  marks>= 50 and marks<=59:
#  print("grade C")
# elif   marks<=50:
#   age=int(input("Enter Your age --> "))
# if age<10:
#  print("Grade C")
# elif age>10:
#  print("Grade F")
# ----------------------------

# score = input("Enter your marks --> ")
# score = int(score)

# if score >= 90:
#     age = int(input("Enter Your age --> "))
#     if age < 10:
#         print("Grade A+")
#     else:
#         print("Grade A")
# elif score >= 80:
#     age = int(input("Enter Your age --> "))
#     if age < 10:
#         print("Your Grade is B+")
#     else:
#         print("Your grade is B")


#  if marks<=80 and marks >=70 :
#  age=int(input("Enter Your age --> "))
#  else:
   
# if age<10:
#  print("Grade A+")
# else: 
#  print("Grade A")
#list------->
# for fruit in fruits:
#  print(fruit)
# fav=["Akshay","Mahesh","namish"]
# for i in fav:
#     print(i +"mental")

# std=["adi","arvind","vanita"]
# for studnts in std:
#   print(studnts)4
# fruits=["apple","bannana","mango","papaya"]
# for i in fruits:
#     print(i+"pie")
  
# fav=["Aditya","mahesh","ravi"]
# for i in fav:
#     print(fav+ "mental")

#-------------------------------)
# choice = int(input("what num you like to choose  "))

# def function(choice):
#  for num in range(1,choice):
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizzbuzz")
#     elif num % 3 == 0 :
#         print("fuzz")
#     elif num % 5 ==0:
#         print("buzz")
#     else:
#         print(num)

# function(choice)
#--------------------
# till = int (input("till the time  "))
# def function(till):
#     for num in range(1,till):
#         if num % 10 == 0 :
#             print("this is divided by 10  ")
#         if num % 9 == 0 :
#             print("this is divided by 9  ")
#         elif num % 9 == 0 :
#             print("this is divided by 9  ")
#         else:
#             print(num)
# function(till)
# till = int(input("what num you like to choose  "))
# def function(till):
#  for num in range(1,till):
#     if num % 10 == 0 or num % 9 == 0:
#         print("divided by 10 or 9")
#     elif num % 8 == 0 :
#         print("divided by 8")
#     elif num % 5 ==0:
#         print("divided by 5")
#     else:
#         print(num)

# function(till)

# greeting=input("Whats Your Name  ")
# def function(greeting):
    #greeting @1

#Guess word from list-->
# function(greeting)
# wlist=[]
# guess_by_user=(input("guess the word ")).lower()
# #selecting rando word 
# secret_word=random.choice(guess_by_user)

# if guess_by_user in wlist:
#     print("You guess correct word buddy --> "+ guess_by_user)
# else:
#     print("your word not matching any word!!!")
import random

print("Welcome to Hangman!")

words = ["hacker", "bounty", "random"]
secret_word = random.choice(words)
print("You get 5 aguesses")
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

num = 0
game_over = False

while not game_over:
    guess = input("Guess a letter ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print(f"You have {guesses_left} guesses left")
        if num >= 5:
            print("You Loser")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("You Win")
        game_over = True
