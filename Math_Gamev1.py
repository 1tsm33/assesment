import math
import random

# Main routine
#Quiz variables
difficulty_list = ["easy", "medium", "hard"]
mode = "regular"
rounds_played = 0
feedback = ""

quiz_history = []

print()
print("🐉Welcome to the math game🐉")
print()

def instructions():
    print("""💜💜Welcome to Math Game.💜💜  
              💿💿I will be giving you simple math questions and 
              you are going to answer them. 
              It is as simple as that! 
              The questions will be multiplication and addition. 
              Good luck babe!!💿💿""")
# Main routine

# ask the user if they want intructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructins if the user wants them...
if want_instructions == "yes":
    instructions()

#Ask and get what level of difficulty they would like
print()
user_choice = string_checker(
    """Please choose your diffuculty level from E= easy, M= medium, H= hard."""
    difficulty_list).strip().lower()
print("You choose: ", user_choice)
print()

# checks users enter yes (y) or no (n)

def yes_no(question):

    """Check user response to to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("pleas enter yes / no")

def int_check(question):
    while True:
        error = "Please enter an integer more than / equal to 5."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that number is more than / equal to 5
            if response < 5:
                print(error)
            else:
                return response

        # if user does not enter an integer
        # output the error message

        except ValueError:
            print(error)

# lower limits and an optional exit code for infinite mode
# / quitting the game

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play, 5 or more? Push <enter> for infinite mode. ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds= 10

print("program continues")

# Check that user have entered a valid
# option base on a list
# Check that user have entered a valid
# option base on a list
def instructions():
    print("""if you choose (x) that is multiplication.
             If you choose (+) that is addition.
             And if you choose (-) that is subtraction.""")

def string_checker (question, valid_ans = ("yes", "no")):
    error = f"please enter a valid option from the folowing list: {valid_ans}"
    while True:
        # Get user response and make sure it is lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # Print error if user does not enter something valid
        print(error)
        print()

# Main routine
math_list= ["x", "+", "-", "xxx"]
want_instructions = string_checker("would you like to see the instructions? ")
print("You chose:  ", want_instructions)

# Display the instructins if the user wants them...
if want_instructions == "yes":
    instructions()

user_choice = string_checker("Chose equation type: ", math_list)
if user_choice == "x":
    print("You chose multiplacation")
elif user_choice == "+":
    print("You chose edition")
elif user_choice == "-":
    print("You chose subtraction")
elif user_choice == "xxx":
    print("You chose to exit 🎲")

else:
    print(error)
    print("You choose: ",feedback)
    # Check user has enterd a valid
    # option based on a list.
def string_checker(question, valid_ans =("yes", "no")):

    while True:
         # Get user response and make sure its lowercase
         user_choice= input(quesyion), Lower()

         for item in valid_ans:
            # Checks if user response in word list

            if item == user_response:
                return item

         # Print error if user does not enter something that is valid
         print(error)
         print()

#Question generator
def generate_question():
   number1 = random.randint(low,high)
   number2 = random.randint(low,high)
   operation = random.choice(ops)

   #Operations
   if operation=="x":
     ans = number1*number2
   elif operation=="+":
     ans = number1+number2
   elif operation=="-":
     ans = number1-number2
   else:
     ans = number1
     number1 = number1*number2
  
  #Question
   question = f"What is {number1} {operation} {number2}?"
   return question, answer 
quiz_history = []
ops = ["+", "-", "x"]
difuculty_list = ["easy", "medium", "hard"]
correct_answer = 0
incorrect_answer = 0

low = 1
high = None

if user_choice == difficulty_list[0]:
    high = 20
    ops = ["+", "x"]
    exit_code = "xxx"

else:
    high = 30
    ops = ["+", "-", "x"]
    exit_code = "xxx"

#Game loop starts here 

while rounds_played < num_rounds:

    rounds_played += 1

#Question Heading
if mode == "infinite":
    rounds_heading = f"\n Queastion {rounds_played} (Infinite Mode)
    else:
        rounds_heading = f"\n Question {rounds_played} of {num_rounds} "

    print(rounds_heading)
    print()

    question = generate_question()
    user_answer = int_check(question[0])

    #If users enter the exit code, break the loop
    if user_answer == "xxx":
        break

    #If users are in the infinite mode, incrase number of rounds
    if mode == "infinite":
        num_rounds += 1

#To check if you enterd a number or not and shows you the answer
if user_answer == question[1]:
    print(f"Correct! The nswer is {question[1]}!")
    correct_answer +=1

elif user_answer != question[1]:
    print(f"Inncorrect! The answer is {question[1]}!")
    incorrect_answer +=1

else:
    print(Please enter a number.)


