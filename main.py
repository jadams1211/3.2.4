def assignment1():
    print("Assignment 1 completed")

def assignment2():
    print("Assignment 2 completed")

def execute_assignment(assignment_number):
    if assignment_number == 1:
        assignment1()
    elif assignment_number == 2:
        result = assignment2()
        print(result)
    else:
        print("Invalid assignment number")

while True:
    user_input = input("Enter assignment number (1 or 2) or 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    if user_input.isdigit():
        assignment_number = int(user_input)
        execute_assignment(assignment_number)    
    else:
        print("Please enter a valid assignment number or 'exit' to quit.")