import math

def sqrt(x): return math.sqrt(x)
def factorial(x): return math.factorial(int(x))
def ln(x): return math.log(x)
def power(x, b): return math.pow(x, b)

if __name__ == "__main__":
    while True:
        print("\nScientific Calculator")
        print("1. Square Root (√x)")
        print("2. Factorial (!x)")
        print("3. Natural Logarithm (ln x)")
        print("4. Power (x^b)")
        print("5. Exit")
        ch = input("Select: ")
        if ch == "1":
            x = float(input("x: ")); print("√x =", sqrt(x))
        elif ch == "2":
            x = int(input("x: ")); print("!x =", factorial(x))
        elif ch == "3":
            x = float(input("x: ")); print("ln(x) =", ln(x))
        elif ch == "4":
            x = float(input("x: ")); b = float(input("b: ")); print("x^b =", power(x, b))
        elif ch == "5":
            break
        else:
            print("Invalid choice.")
