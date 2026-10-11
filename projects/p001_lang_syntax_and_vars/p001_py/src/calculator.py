
capabilities = "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulo\n6. Factorial\n"

def compute_factorial(num):
    # TODO_1
    print("Syke")

def computation(op, num_01, num_02):
    # TODO_2
    print("Syke 2")

def main_loop():
    print("Currently, I can do for you:\n" + capabilities)
    operation = input("What do you want? (you can write the number of the operation or the name): ")
    if operation.lower() == "factorial" or operation == "6":
        num_01 = input("Factorial for number: ")
        compute_factorial(num_01)
    else:
        num_01 = input("term 1 is: ")
        num_02 = input("term_2 is: ")
        computation(operation, num_01, num_02)

if __name__ == "__main__":
    print("Hi. I am a simple calculator")
    while True:
        main_loop()
        break
    print("the end.")

