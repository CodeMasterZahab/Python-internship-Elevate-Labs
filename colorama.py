from colorama import Fore, Style

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b!=0 else "Error! Division by zero."

while True:
    print(Fore.CYAN + "\n--- Fancy CLI Calculator ---" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit" + Style.RESET_ALL)

    choice = input(Fore.GREEN + "Enter choice (1-5): " + Style.RESET_ALL)
    if choice == '5': break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1': print(Fore.MAGENTA + f"Result: {add(a,b)}" + Style.RESET_ALL)
    elif choice == '2': print(Fore.MAGENTA + f"Result: {sub(a,b)}" + Style.RESET_ALL)
    elif choice == '3': print(Fore.MAGENTA + f"Result: {mul(a,b)}" + Style.RESET_ALL)
    elif choice == '4': print(Fore.MAGENTA + f"Result: {div(a,b)}" + Style.RESET_ALL)
    else: print("Invalid choice!")
