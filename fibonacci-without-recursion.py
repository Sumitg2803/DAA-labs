# Class to generate Fibonacci sequence
class Fibonacci:
    # Function to generate Fibonacci sequence up to n terms
    def generate(self, n):
        if n <= 0:
            print("Please enter a positive integer.")
            return

        first = 0
        second = 1
        print("Fibonacci Sequence: ", end="")

        for _ in range(n):
            print(first, end=" ")

            # Calculate the next term
            next_term = first + second
            first = second
            second = next_term
        print()

if __name__ == "__main__":
    # Initialize a Fibonacci object
    fibonacci = Fibonacci()

    while True:
        print("\n**** MENU ****")
        print("1: Generate Fibonacci Sequence 2: EXIT")
        try:
            ch = int(input("Enter Your Choice: "))
            
            if ch == 1:
                n = int(input("Enter the number of terms: "))
                fibonacci.generate(n)
            elif ch == 2:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
