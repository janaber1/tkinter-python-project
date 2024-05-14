#python additionfunc
def add (num1, num2):
    return num1 + num2

#sub func
def sub (num1, num2):
    return num1 - num2
#multi func
def multiply (num1, num2):
    return num1 * num2
#division
def division (num1, num2):
    return num1 / num2
#while loop
def main ():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. exit")

        choice = input("Enter choice (1-5): ")

        #method 1
        if choice !=5 :
            match choice :
                case '1':
                    num1 = float(input("enter first number:"))
                    num2 = float(input("Enter second number: "))
                    result = add(num1, num2)
                    print("Result:", result)
                case '2':
                    num1 = float(input("enter first number:"))
                    num2 = float(input("Enter second number: "))
                    result = sub(num1, num2)
                    print("Result:", result)
                case '3':
                    num1 = float(input("enter first number:"))
                    num2 = float(input("Enter second number: "))
                    result = multiply(num1, num2)
                    print("Result:", result)
                case '4':
                    num1 = float(input("enter first number:"))
                    num2 = float(input("Enter second number: "))
                    if num2 != 0:
                            result = division(num1, num2)
                            print("Result:", result)
                    else:
                            print("Error: Division by zero!")
                case '5':
                    print("Calculator exited.")
                    break
                case default:
                     print("Invalid input. Please enter a valid choice.")
        else:
            print("Invalid input. Please enter a valid choice.")


    #method 2
    # if choice == '5':
    #     print("Calculator exited.")
    #     break
    # elif choice !=1 or choice !=2 or choice !=3 or choice !=4:
    #   print("Invalid input. Please enter a valid choice.")
    # else:
    #     num1 = float(input("enter first number:"))
    #     num2 = float(input("Enter second number: "))
    #
    #     if choice == '1':
    #         result = add(num1, num2)
    #         print("Result:", result)
    #     elif choice == '2':
    #         result = subtract(num1, num2)
    #         print("Result:", result)
    #     elif choice == '3':
    #         result = multiply(num1, num2)
    #         print("Result:", result)
    #     elif choice == '4':
    #         if num2 != 0:
    #             result = division(num1, num2)
    #             print("Result:", result)
    #         else:
    #             print("Error: Division by zero!")
