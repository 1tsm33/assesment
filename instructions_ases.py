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
              The questions will be multiplication. 
              Good luck babe!!💿💿""")

# Main routine

# ask the user if they want intructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructins if the user wants them...
if want_instructions == "yes":
    instructions()

print("program continues")
