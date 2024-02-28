file=open("abcs.txt","w+");
fname=input("please enter your first name ")
ltname=input("please enter your last name ")

file.write(fname + '\n')
file.write(ltname)

file.close()


#writtting data 

file=open("abcs.txt",mode="r+")
data=file.read()
print(data)
file.close()











        