print("Printing The Pramid Pattern....")
print("Enter a number that is grater then 4 else the code is not work")
row_line = int(input("Enter Number of row line you want: "))
length = (row_line-1)+row_line
spac_var = ((length*2)/2)
space = " "
sub = 1
a=0
b=1
c=a+b
if row_line >= 4:
    for i in range (0,row_line):
        if i <=2:
         print(str(space)*int(spac_var),end=" ")
         print(str(" "+str(c))*sub)
         b=a
         a=c
         c=a+b
         spac_var -=1
         sub +=1
        elif i>=2:
         print(str(space)*int(spac_var),end=" ")
         print(str("  "+str(c))*sub)
         b=a
         a=c
         c=a+b
         spac_var -=1
         sub +=1
                
        
else :
    print("please enter valid number !")

        






