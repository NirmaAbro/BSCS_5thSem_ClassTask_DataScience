import random
def lucky(names,number):
    #function first creates an empty list called "selected" to store the randomly selected participants
    selected=[]
    participants=names.copy()
    for i in range(0,number-1):
        guess=random.randrange(0,number-i)
        selected.append(participants[guess])
        participants.remove(participants[guess])
    return selected

def main():
    participants=["nirma","kiran","sana","dua","zoya","mehro"]
    print(lucky(participants,3))
    
if __name__=="__main__":
    main()


