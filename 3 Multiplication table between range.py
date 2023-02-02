# Multiplication table between range which is taken from user

def multiplication_table(start, end):
    
    for i in range(1,11):
        print("\n ",i,"|", end=" ")
        for j in range(start,end+1):
            print("\t",i*j, end=" ")

if __name__=="__main__":
    start=int(input("\n Enter the number from where you want to print table : "))
    end=int(input("\n Enter the number upto which you want to print table : "))
    multiplication_table(start,end)