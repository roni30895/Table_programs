# Print batch of 100 numbers
def Batch_of_hundread(n):
    if n>0:

        for i in range(1, n+1):
            print("\t",i,end="")
    
            if i%10 == 0:
                print("\n",end="\n")
            if i%100==0:
                print("\n",end="\n")

    else:
        print("\n You enter WRONG input. Please enter valid input ")


if __name__=="__main__":
    n = int(input("Enter a number : "))
    Batch_of_hundread(n)

