#calculator in python use if-else,while, do while
while True:
        
        print("Basic python calculator")#print the text on terminal
        while True:
            print("Choose an option")
            answer = int(input("1-Addition\n2-Substraction\n3-Multiplication\n4-Division\n"))#option chosen by the user
            if answer == 1:#Correct option
                  break
            elif answer == 2:#Correct option
                  break
            elif answer == 3:#Correct option
                  break
            elif answer ==4:#Correct option
                  break
            else:#Incorrect option
                  print("The option is incorrect, try again.")
                  
        
        #variables to use for operations
        print("Enter 2 numbers to do the operation")#
        a=float(input())
        b=float(input())
        #///////////////////////////////////

        #Addition
        while answer==1:
              addition=float(a+b)#Do the operation
              print("The answer is {}".format(addition))#print the result
              break
        
        #Substraction
        while answer==2:
              substraction=float(a-b)#Do the operation
              print("The answer is {}".format(substraction))#print the result
              break
        
        #Multiplication
        while answer==3:
              multiplication=float(a*b)#Do the operation
              print("The answer is {}".format(multiplication))#print the result
              break
        
        #Division
        while answer==4:
              division=float(a/b)#Do the operation
              print("The answer is {}".format(division))#print the result
              break
        
        break #finish the cycle



