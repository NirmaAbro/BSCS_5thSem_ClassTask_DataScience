n=input("please enter your number for fact")
def fact(n):
    if n==1:
        return 1
    else:
        total=n*fact(n-1)
        print(total)