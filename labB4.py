num=int(input("Enter a number "))
factorial=1
if num<0:
    print("please enter a number greater than zero")
elif num==0:
    print ("the factorial of 0 is one ")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of ",num,"is",factorial)