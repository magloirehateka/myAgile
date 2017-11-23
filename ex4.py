
def ex4():
    a = []
    while len(a) <3:
        num=int(input("Enter the number: "))
        a.append(num)
        maxNum = a[0]
        for i in range(1, len(a)):
            if a [i] > maxNum:
                maxNum=a[i]
    print(maxNum)

ex4()
