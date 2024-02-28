print("Enter the Row and Column Size of First Matrix: ", end="")
rOne = int(input())
cOne = int(input())
print("Enter " +str(rOne * cOne)+ " Elements: ", end="")
mOne = []
for i in range(rOne):
    mOne.append([])
    for j in range(cOne):
        num = int(input())
        mOne[i].append(num)

print("\nEnter Row and Column Size of Second Matrix: ", end="")
rTwo = int(input())
if cOne != rTwo:
    print("\nMultiplication Not Possible!")
    exit()
else:
    cTwo = int(input())
    print("Enter " +str(rTwo * cTwo)+ " Elements: ", end="")
    mTwo = []
    for i in range(rTwo):
        mTwo.append([])
        for j in range(cTwo):
            num = int(input())
            mTwo[i].append(num)

    # now multiplying two matrices
    mThree = []
    for i in range(rOne):
        mThree.append([])
        for j in range(cTwo):
            sum = 0
            for k in range(cOne):
                sum = sum + (mOne[i][k] * mTwo[k][j])
            mThree[i].append(sum)

    # now printing the multiplication result
    print("\nMultiplication Result of Two Given Matrix is:")
    for i in range(rOne):
        for j in range(cTwo):
            print(mThree[i][j], end=" ")
        print()