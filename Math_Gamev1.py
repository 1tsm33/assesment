
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
    print("""if you choose (*) that is multiplication.
             If you choose (+) that is addition.
             And if you choose (-) that is subtraction.""")

def string_checker (question, valid_ans = ("yes", "no")):
    error = f"please enter a valid option from the folowing list: {valid_ans}"
    while True:
        # Get user response and make sure it is lowercase
        user_response = input (question).lower()

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
    feedback = "You chose multiplacation"
elif user_choice == "+":
    feedback = "You chose edition"
elif user_choice == "-":
    feedback = "You chose subtraction"
elif user_choice == "xxx":
    feedback = "You chose to excit 🎲"

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

