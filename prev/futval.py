#futval.py
# A program to compute the value of an investmet
# carried 10 years into the future
def main():

#this first section is the introduction
    print("This is a future value function")
    print("that will predict a 10 year investment")

#this section is for the input portion
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

#this section is for the processing portion
    for i in range(10) :
        principal = principal * (1 + apr)

#this section is for the putput portion
    print("The value in 10 years is: ", principal)

main()

