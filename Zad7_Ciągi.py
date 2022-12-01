givenInput = input("Enter string:")
listInput = list(givenInput)
print(listInput)


#Tworzenie list z liczbami, literami i innymi
ints = []
strs = []
other = []

for i in listInput:
    try:
        ints.append(int(i))
    except:
        if i.isalpha():
            strs.append(i)
        else:
            other.append(i)
       

# Zadanie 1
inputLen = len(givenInput)
print(inputLen)


# Zadanie 2
print("Ilość liter",len(strs))

# Zadanie 3
print("Ilość cyfr:",len(ints))

# Zadanie 4
print("Ilość innych znaków:",len(other))

# Zadanie 5
x = 0
for i in strs:
    if i.isupper():
        x += 1
print("Ilość wielkich liter:",x)

# Zadanie 6
x = 0
for i in strs:
    if i.islower():
        x += 1
print("Ilość małych liter:",x)

# Zadanie 7
print('Liczba z intów: ',*ints, sep='')
    

# Zadanie 8
x = 0
for i in ints:
    x += i
print("Suma liczb:",x)

# Zadanie 9
print("Ilość ltier 'a':",strs.count('a'));
