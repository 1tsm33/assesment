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

