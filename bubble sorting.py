def bubble_sort(a):  
    
    for i in range(0,len(a)-1):  
        for j in range(len(a)-1):  
            if(a[j]>a[j+1]):  
                temp = a[j]  
                a[j] = a[j+1]  
                a[j+1] = temp  
    return a 
  
a = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", a)  
 
print("The sorted list is: ", bubble_sort(a))  
