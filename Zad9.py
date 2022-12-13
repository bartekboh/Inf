import random


# Zadanie 1
def inputLength(givenInput):
    inputLen = len(givenInput)
    print('Długość ciągu', inputLen)


# Zadanie 2
def strsLen():
    print("Ilość liter", len(strs))


# Zadanie 3
def intsLen():
    print("Ilość cyfr:", len(ints))


# Zadanie 5
def uppersLen():
    x = 0
    for i in strs:
        if i.isupper():
            x += 1
    print("Ilość wielkich liter:", x)


# Zadanie 6
def lowerLen():
    x = 0
    for i in strs:
        if i.islower():
            x += 1
    print("Ilość małych liter:", x)


# Zadanie 7
def intOfInts():
    print('Liczba z intów: ', *ints, sep='')


# Zadanie 8
def sumInts():
    x = 0
    for i in ints:
        x += i
    print("Suma liczb:", x)


# Zadanie 9
def countA():
    print("Ilość ltier 'a':", strs.count('a'));


myList = []

# Creating list [a-z,0-9]
for i in string.ascii_lowercase:
    myList.append(i)
for i in range(9):
    myList.append(i)

lines = random.randrange(50,301)

text_file = open("file.txt", "w")
for i in range(lines):
    chars = random.randrange(3,21)
    for x in range(chars):
        char = myList[random.randrange(0, len(myList))]
        text_file.write(format(str(char)))
    text_file.write('\n')


print("Lines: {}".format(lines))

text_file.close()


# ----------------7------------------
# givenInput to listLine
text_file = open('file.txt', 'r')

givenInput = text_file.readlines() #Wszystkie linie z file.txt

q = 0
for i in givenInput:
    listLine = list(givenInput[q])  #Zamienia jedna linie na liste
    if listLine[-1] == '\n':
        listLine.pop()
    else:
        pass

    q += 1

    ints = []
    strs = []
    other = []

    #Tworzenie list ints strs i other
    for x in listLine:
        if x != '\n':
            try:
                ints.append(int(x))
            except ValueError:
                if x.isalpha():
                    strs.append(x)
                else:
                    other.append(x)
        else:
            pass
    print('\n Numer wiersza:',q)
    print('Ciąg:',i[0:-2])
    inputLength(listLine)
    strsLen()
    intsLen()
    uppersLen()
    lowerLen()
    intOfInts()
    sumInts()
    countA()


text_file.close()
