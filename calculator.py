print("________CALCULATOR________")
a=int(input("Enter no. 1 : "))
b=int(input("Enter no. 2 : "))
print('''ARITHMETIC OPERATIONS
1. Addition
2. Subtraction
3. Multiplication 
4. Division      ''')
Choice = int(input("Enter the choice of operation which you want to perform : "))
if Choice==1 :
    print("result :" , a+b) 
elif Choice==2 :
    print("result :" , a-b) 
elif Choice==3 :
    print("result :" , a*b) 
elif Choice==4 :
    print("result :" , a/b) 
else :
    print ("Please enter a valid Choice of operation ")
