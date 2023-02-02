# Printing a table by getting input from user

def table(n):
    for i in range(1,11):
        print("\n",n, "X", i,"=", n*i)

if __name__=="__main__":
    n=int(input("\n Enter the number whose table you want to print : "))
    table(n)
