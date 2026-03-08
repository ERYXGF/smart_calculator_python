"""
What it must do:

My calculator should feel like a real tool. It must run in a continuous loop until the user chooses to quit, and handle every interaction gracefully.


Core requirements:

1) The main menu should display clearly every time, showing the user their options: addition, subtraction, multiplication, division, exponentiation (**), modulo (%), and quit.
2) Handle every possible bad input without crashing: letters instead of numbers, dividing by zero, empty input, special characters (Use try/except blocks for every input that expects a number)
3) After each calculation display the result clearly and then ask: "Would you like to perform another calculation?" — this keeps the user in the loop.
4) History feature — every calculation performed in the session gets stored in a list as a formatted string like "12.0 + 5.0 = 17.0".
5) The user can type history from the main menu to see all calculations from the current session, or clear to wipe the history.


Stretch goals:

Let the user chain calculations by using the previous result as the first number
Add a sqrt option using the math module
Let the user save their history to a .txt file

Project Structuration:
1) Addition Function
2) Substraction Function 
3) Multiplication Function
4) Division Function
5) Exponentiation Function
6) Modulo Function
7) Sqrt Function
8) Further Calculation Function
9) History Function
10) Run Everything Function
11) Display Menu Function
12) Get Number Input Function
13) Display History Function
14) Save History To File Function
"""
def get_number():
    while True:
        try:
            number = int(input("Please enter a number: "))
            return (number)
        except ValueError:
            print("Invalid input. Please enter a number: ")

def display():
    menu = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Exponentiation", "6. Modulo", "7. Sqrt", "8. History", "9. Clear History", "10. Save History", "11. Quit"]
    print("Pease select an option: ")
    for item in menu:
        print (item)

def addition():
    a = get_number()
    b = get_number()
    count = a+b
    print(f"The result of this addition is: {count}")
    return f"{a} + {b} = {count}"

def substraction():
    a = get_number()
    b = get_number()
    count = a-b
    print(f"The result of this substraction is: {count}")
    return f"{a} - {b} = {count}"

def multiplication():
    a = get_number()
    b = get_number()
    count = a*b
    print(f"The result of this multiplication is {count}")
    return f"{a} * {b} = {count}"

def division():
    a = get_number()
    b = get_number()
    if b == 0:
        print("Division by zero is not allowed.")
        return None
    count = a/b
    print(f"The result of this division is {count}")
    return f"{a} / {b} = {count}"

def exponentiation():
    a = get_number()
    b = get_number()
    count = a**b
    print(f"The result of this exponentiation is {count}")
    return f"{a} ** {b} = {count}"

def modulo():
    a = get_number()
    b = get_number()
    if b == 0:
        print("Modulo by zero is not allowed.")
        return None
    count = a%b
    print(f"The result of this modulo is {count}")
    return f"{a} % {b} = {count}"

def sqrt():
    import math
    a = get_number()
    if a < 0:
        print("Square root of a negative number is not supported.")
        return None
    count = math.sqrt(a)
    print(f"The result of this square root is {count}")
    return f"sqrt({a}) = {count}"

def history(history_list, entry):
    history_list.append(entry)

def display_history(history_list):
    if not history_list:
        print("No calculations yet.")
        return
    print("Calculation history:")
    for index, item in enumerate(history_list, start=1):
        print(f"{index}. {item}")

def operation():
    history_list = []
    while True:
        try:
            display()
            choice = int(input("Enter your choice (1-11):"))
            if choice == 1:
                entry = addition()
                if entry:
                    history(history_list, entry)
            elif choice == 2:
                entry = substraction()
                if entry:
                    history(history_list, entry)
            elif choice == 3:
                entry = multiplication()
                if entry:
                    history(history_list, entry)
            elif choice == 4:
                entry = division()
                if entry:
                    history(history_list, entry)
            elif choice == 5:
                entry = exponentiation()
                if entry:
                    history(history_list, entry)
            elif choice == 6:
                entry = modulo()
                if entry:
                    history(history_list, entry)
            elif choice == 7:
                entry = sqrt()
                if entry:
                    history(history_list, entry)
            elif choice == 8:
                display_history(history_list)
            elif choice == 9:
                history_list.clear()
                print("History cleared.")
            elif choice == 10:
                pass
            elif choice == 11:
                print("Thanks for using the Smart Calculator, we'll see you again soon !")
                break
            else:
                input("Please enter a valid option between 1 and 11:")
        except ValueError:
            print("Invalid choice selected. Please enter a valid choice between 1 and 11: ")

if __name__ == "__main__":
    operation()
