n=int(input("Enter the total no of key value pair you want inside your dictionary :"))
dic={}
for i in range(n):
    k=(input("enter the key: "))
    v=input("enter the value: ")
    dic.update({k:v})
print("my dictionary :",dic)
choice=(input("please enter the word that you want to see"))
if choice=='appreciate':
    print("Meaning : To admire greatly ")
    print("Antonym : Depreciate")
    print("Sentence : I was appreciate for my work :)")
elif choice=='Awesome':
    print("")
    print("Antonyms : ")
    print("It is Awesome weather")
elif choice=='sure':
    print("Meaning : certain ")
    print("Antonyms : ")
    print("sentence :Surely no doubt My ALLAH is always with me ")
elif choice=='exit':
    exit()
    print('program has been terminated ...')
