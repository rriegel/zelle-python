#quadratic.py
#   A program that computes real roots of a quadratic equation
#   Illustrates the use of the math library.
#   Note: this program crashes if the equation has no real roots

import math # This makes the math libraries available

def main():
    print("This progragam computes the real soultions of a given quadratic")
    print() # To give a line of space for cleaner presentation


    a = float(input("Enter coefficient a: "))
#   the "float" specification ensures that the input is stored as
#   a floating decimal variable

    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print ()
    print("The solutions are:", root1, root2 )

main()
