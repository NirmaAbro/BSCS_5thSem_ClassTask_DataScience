file = open("pythonnn.txt", "w+")
print("congrats ! your file is created now")
file = open("pythonn.txt", mode='w')
n = file.write("hellow this is a new project on python on file handling ;-)")
# print(n);
file.close()
choice = 0
while choice < 9:
    print("welcome to Nirma Abro file handling project ")
    print("1. to check file is readable or not.")
    print("2. to show all the data in a file")
    print("3. to add new student record in a file")
    print("4. to delete student record in a file")
    print("5. to search student in a file")
    print("6 . to show all studen data in a file ")
    print("7. to exit the program;-)")

    Choice = int(input("please enter your choice "))
    # if (choice<=0 or choice>=7):
    #    print("Wrong Choice");
    #    continue
    if choice == 1:
        file = open("pythonnn.txt", "w+")
        if file.readable():
            print("file is readable:-)")
        else:
            print("file is not readable :-(")
            file.close()
            continue
    if choice == 2:

        file = open("pythonnn.txt", "w+")

        fname = input("please enter your first name ")
        ltname = input("please enter your last name ")

        file.write(fname + '\n')
        file.write(ltname)

        file.close()
    if choice==3:
        file=open("pythonnn.txt",mode="r")
        data=file.read()
        file.close()
