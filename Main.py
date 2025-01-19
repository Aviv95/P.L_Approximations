from sympy import Matrix, symbols
from Linear import linear
from Polynomial import polynomial


def main():

    table= [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]


    while True:
        print("\nChoose the method you want to use:")
        print("1. Linear Interpolation")
        print("2. Polynomial Interpolation")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice=="3":
            print("Exiting the program...")
            print("Goodbye!")
            break

        try:
            x_point = 2.5

            if choice=="1":
                print("\nLinear Interpolation:")
                print(f"The approximation result for {[x_point]} is", linear(table,x_point))

            elif choice=="2":
                print("\nPolynomial Interpolation:")
                print(f"The approximation result for {[x_point]} is", polynomial(table,x_point))

            else:
                print("Invalid choice. Please enter a valid choice (1/2/3).")

        except ValueError as e:
            print(f"Error: {ValueError}")

        except Exception as e:

            print(f"An unexpected error occurred: {e}")

if __name__=="__main__":
    main()