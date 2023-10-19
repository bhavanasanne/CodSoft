def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def product(a, b):
    return a * b

def quotient(a, b):
    return a / b

print("Select the operation you need:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    operation = input("Select operation(1/2/3/4): ")

    if operation in ('1', '2', '3', '4'):
        try:
            num_1 = float(input("Enter 1st number: "))
            num_2 = float(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if operation == '1':
            print(num_1, "+", num_2, "=", sum(num_1, num_2))

        elif operation == '2':
            print(num_1, "-", num_2, "=", difference(num_1, num_2))

        elif operation == '3':
            print(num_1, "*", num_2, "=", product(num_1, num_2))

        elif operation == '4':
            print(num_1, "/", num_2, "=", quotient(num_1, num_2))
        
        next_calculation = input("Continue calculation? (Y/N): ")
        if next_calculation == "N":
          break
    else:
        print("Invalid input!")