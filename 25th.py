
# age = 20
# if age>=18:
#     print("eligible to vote")
# elif age>15:
#     print("too young")
# else:
#     print("not eligible to vote")

#if else
# mark=input("Enter your mark : ")
# if mark >=70 and mark<100:
#     print("GRADE A")
# elif mark >= 60 and mark <70:
#     print("GRADE B")
# elif mark >= 50 and mark <60:
#     print("GRADE C")
# elif mark >= 40 and mark <50:
#     print("GRADE D")
# elif mark >= 0 and mark <40:
#     print("GRADE E")
# else:
#     print("You have a missing mark")

#loops
# for i in range (10):
#     if i%2==1:
#         print (i*i)


#while loop
# while True:
#     print("while loop")
#     break

#functions
# def product(a, b):
#     return(a*b)
# print(product(5,2))

# def voting(age):
#     if age>=18:
#         print("eligible to vote")
#     elif age>15:
#         print("too young")
#     else:
#         print("not eligible to vote")

# voting(int(input("Age: ")))

# def grading(mark):
#      if mark >=70 and mark<100:
#         print("GRADE A")
#      elif mark>= 60 and mark <70:
#         print("GRADE B")
#      elif mark >= 50 and mark <60:
#         print("GRADE C")
#      elif mark >= 40 and mark <50:
#         print("GRADE D")
#      elif mark >= 0 and mark <40:
#         print("GRADE E")
#      else:
#         print("You have a missing mark")
    
# grading(int(input("mark: ")))
#challenge
#take list of numbers and return sum of even numbers in the list
# i =[2, 4 ,5, 12, 45, 23, 22, 44, 23,44, 22 ,12, 223 ,222]
# sum=0
# for number in i:
#     if number%2==0:
#         sum += number
#         print(sum)

#program printing first 10 fibonnaci numbers
a, b = 0, 1

# Loop 10 times to print first 10 Fibonacci numbers
# for i in range(10):
#     print(a)
#     a, b = b, a + b

#ROCK PAPER SCISSOR GAME
import random

def play_game():
    # Define the three options
    options = ['rock', 'paper', 'scissors']

    # Get the user's choice
    user_choice = input("Enter your choice (rock/paper/scissors): ")

    # Get the computer's choice
    computer_choice = random.choice(options)

    # Print the choices
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You win!")
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You win!")
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
    else:
        print("Computer wins!")

# Play the game
play_game()







