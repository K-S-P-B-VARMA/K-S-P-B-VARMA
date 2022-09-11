num=int(input("enter a number"))
if num>1:
    
    for i in range(2,num):
        
        if num%i ==0:
            
            print("not a prime number")
        
        else:
            
            print("it is a prime number")
            break
else:
    print("not a prime number")
