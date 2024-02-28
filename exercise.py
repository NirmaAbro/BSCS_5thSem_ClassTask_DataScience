print("This program computes your average homework grade");
n=int(input("How many assignments are there "));
for i in range(n):
    print();
    print("ASSIGNMENT 1");
    a=int(input("Point earned ?"));
    b=int(input("points possible"));
    if a>=b:
        print("enter a value which is less than b ")
    print();
    print("Assignment 2");
    
    c=int(input("point earned ?"));
    d=int(input("point possible ?"));
    print();
    print("Assignments 3");
    
    e=int(input("point earned ?"));
    f=int(input("point possible ?"));
    print();
    total=a+c+e;
    percentage=total/n;
    if percentage!=n:
    print("your total score :",percentage);


