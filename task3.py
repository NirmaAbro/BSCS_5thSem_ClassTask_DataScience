year = int(input("enter any year "));
if (year%4 == 0 and year%100 != 0) and ( year%400 ==0):
    print (year,"is a leap year ");
else:
    print(year ,"is not a leap year ");