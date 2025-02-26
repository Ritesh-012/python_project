def main():
    # Ask the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform basic arithmetic operations
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2 if num2 != 0 else "undefined (division by zero)"

    # Use F-strings for output
    print(f"The sum of {num1} and {num2} is {sum_result:.2f}")
    print(f"The difference between {num1} and {num2} is {difference_result:.2f}")
    print(f"The product of {num1} and {num2} is {product_result:.2f}")
    print(f"The quotient of {num1} and {num2} is {quotient_result}")

if __name__ == "__main__":
    main()
    