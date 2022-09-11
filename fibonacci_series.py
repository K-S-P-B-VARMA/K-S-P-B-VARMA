nterms=int(input("how many terms?"))

n1,n2=0,1
count=0

if nterms<=0:
    print("enter the positive numbers")
elif nterms==1:
    print("fibanocci upto",nterms,":")
    print(n1)
else:
    print("fobanocci sequence is")
    while count<nterms:
      print(n1)  
      nth = n1+n2
      n1 = n2
      n2 = nth
      count += 1

           
