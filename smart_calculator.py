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

def operation():
    while True:
        try:
            display()
            choice = int(input("Enter your choice (1-11):"))
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                pass
            elif choice == 8:
                pass
            elif choice == 9:
                pass
            elif choice == 10:
                pass
            elif choice == 11:
                print("Thanks for using the Smart Calculator, we'll see you again soon !")
                break
            else:
                input("Please enter a valid option between 1 and 11:")
        except ValueError:
            print("Invalid choice selected. Please enter a valid choice between 1 and 11: ")

if __name__ == "main__":
    operation()
