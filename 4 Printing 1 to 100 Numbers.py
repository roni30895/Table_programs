# Printing 1 to 100 Numbers
def numbers():
    for i in range(1,11):
        print("\n",i, end=" ")
        add=10
        for j in range(1,10):
            print("\t",i+add,end=" ")
            add=add+10

if __name__=="__main__":
    numbers()