# Question 1

def add(number_1, number_2):
    return number_1 + number_2

def sub(number_1, number_2):
    return number_1 - number_2

def mult(number_1, number_2):
    return number_1 * number_2

def div(number_1, number_2):
    if number_2 == 0:
        return f"Cannot divide by zero" 
    else:
        return number_1 / number_2

while True:
    try:
        # Get first number 
        number_1 = int(input("Enter the first number: "))
        # Get second number
        number_2 = int(input("Enter the second number: "))
        # Get operator
        operator = input("Choose operation (+, -, *, /) or 'exit' to quit ").strip()
    
    
        if operator == "+":
            print(f"Result:", add(number_1, number_2))
        

        elif operator == "-":
            print(f"Result:", sub(number_1, number_2))
        
        elif operator == "*":
            print(f"Result:", mult(number_1, number_2))
    
        elif operator =="/":
            print(f"Result:", div(number_1, number_2))
        elif operator.lower() == "exit":
            print("Exiting calculator... Goodbye!")
            break
        else:
            print("Invalid operator. Please choose +, -, *, / or exit.")


    except ValueError:
        print("Invalid input, Enter a valid number")            



# Question 2

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop

    num = int(user_input)   # convert to integer

    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

        
# Question 3

while True:
    age = int(input("Enter your age (or type exit to quit): "))
    
    if age == exit:
        print("Goodbye!")
        break
    
    try:
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except ValueError:
        print("Invalid input. Please enter a number")