def factorial(n):
    # Check if n is non-positive
    if n <= 0:
        return "Factorial is not defined for non-positive integers."

    # Initialize variables
    result = 1
    current_number = n


    while current_number > 1:
        result *= current_number
        current_number -= 1

    return result

user_input = int(input("Enter a number to calculate its factorial: "))

# Call the factorial function 
print(factorial(user_input))
