def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result



def main():
    go = True     
    while go:
        try:
            number = int(input("Enter a number to calculate its factorial: "))
            

            result = factorial(number)
            print(f"The factorial of {number} is: {result}")
        except ValueError:
            print("Please enter a valid integer.")


        while True:

            try:
                choice = input("Do you want to calculate another factorial? (y/n): ")
                if choice.lower() == "y":
                        go = True
                        break
                elif choice.lower() == "n":
                    print("Goodbye!")
                    go = False
                    break
            except ValueError:
                print("Please enter a valid choice.")

if __name__ == "__main__":
    main()
