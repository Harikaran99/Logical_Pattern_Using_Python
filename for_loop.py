# PRINTING SQUARE STAR PATTERN
''' print("Printing square star pattern".upper())
line = int(input("\nEnter number of lines you want: "))
print("\nPrinting The Pattern... ")
for i in range(0,line):
    print("* * * * *") '''

# PRINTING HOLLOW SQUARE STAR PATTERN
'''print("printing hollow square pattenr".upper())
line = int(input("\nEnter Number Of Lines You Want: "))
print("\nPrinting The Pattern...")
for i in range(0,line):
     if i == 0:
         print("* * * * *")
     elif i < line:
         print("*       *")
     if i == line-1:   
         print("* * * * *") 
         print("line value is: "+ str(line))
        
print("\nprinted patterrn successfully🙌🙌🙌".upper())
print("line value is: "+ str(line)) '''

'''#PRINTING RHOMES STAR PATTERN
print("printing rhomes star pattenr".upper())
colum = int(input("\nEnter Number Of Colums You Want: "))
line = int(input("\nEnter Number Of Lines You Want: "))
for i in range (0,line):
    for j in range (0,colum):
        if colum % 2 == 0:
            space = " "
            sim = " *"
            spacolum = colum
            for k in range (0,colum):
                if i == 0 :
                    print(str(space)*int(spacolum)+str(sim)*int(colum))
                    spacolum -=1

        elif colum % 2 == 1:
            space = " "
            sim = " *"
            spacolum = colum - 1
            for k in range (0,colum):
                if i == 0 :
                    print(str(space)*int(spacolum)+str(sim)*int(colum))
                    spacolum -=1
'''
            
#PRINTING RHOMES STAR PATTERN
print("printing rhomes star pattenr".upper())
colum = int(input("\nEnter Number Of Colums You Want: "))
line = int(input("\nEnter Number Of Lines You Want: "))
for i in range (0,line):
        if  colum % 2 == 0:
            space = " "
            sim = " *"
            spacolum = line
            for k in range (0,spacolum):
                if i >= 0 :
                    print(str(space)*int(spacolum)+str(sim)*int(colum))
                    spacolum -=1
        elif colum % 2 == 1:
            space = " "
            sim = " *"
            spacolum1 = line 
            for l in range (0,spacolum1):
                if l >= 0 :
                    print(str(space)*int(spacolum1)+str(sim)*int(colum))
                    spacolum1 -=1
        break
        
           
