#to read data to dictionary
dict1={}
n=int(input("enter no of elements"))
for i in range(n):
    k=eval(input("enter the key"))
    v=eval(input("enter the value"))
    dict1.update({k:v})
print(dict1)
