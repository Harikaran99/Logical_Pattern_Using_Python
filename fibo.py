a = 0               
b = 1       
c = a + b           
number=int(input("Enter number of lenght you want:")) 

for i in range (0,number):
    print(c ,end=" ")
    b=a
    a=c
    c=a+b

