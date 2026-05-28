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
print("You chose:", want_instructions)

# Display the instructins if the user wants them...
if want_instructions == "yes":
    instructions()

user_choice = string_checker("Chose equation type : ", math_list)
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



