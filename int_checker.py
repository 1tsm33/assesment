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
num_rounds = int_check("How many rounds would you like to play? Push <enter> for infinite mode. ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds= 10

print("program continues")


