# Multiplication table

def multiplication_table():
    for i in range(1,11):
        print("\n ",i,"|", end=" ")
        for j in range(1,11):
            print("\t",i*j,end=" ")
    
    print()
    
    for i in range(1,11):
        print("\n ",i,"|", end=" ")
        for j in range(11,21):
            print("\t",i*j,end=" ")
    
    print()

    for i in range(1,11):
        print("\n ",i,"|", end=" ")
        for j in range(21,31):
            print("\t",i*j,end=" ")
 
 
if __name__=="__main__":
    multiplication_table()