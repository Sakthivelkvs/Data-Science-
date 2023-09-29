def add(a,b):
    c=a+b
    print("Addition=",c)
def sub(a,b):
    c=a-b
    print("Subtraction=",c)
def mul(a,b):
    c=a*b
    print("Multiplication=",c)
def div(a,b):
    c=a/b
    print("Division=",c)
while True:
    print("1.ADDITION\n2.SUBRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT")
    ch=int(input("Enter Your Choice"))
    if (ch == 5):
        break
    x = int(input("\nEnter first Number "))
    y = int(input(" Enter Second Number"))
    if(ch==1):
        add(x,y)
    elif(ch==2):
        sub(x,y)
    elif(ch==3):
        mul(x,y)
    elif(ch==4):
        div(x,y)
    else:
        print("Invalid Choice")


