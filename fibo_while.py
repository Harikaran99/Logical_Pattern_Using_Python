a = 0               
b = 1       
c = a + b 
i = 0          
number=int(input("Enter noumber of lenght you want:")) 

while number>i:
     print(c ,end=" ")
     b=a
     a=c
     c=a+b
     i+=1