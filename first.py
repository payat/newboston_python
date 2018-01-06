# import tutorial
import functions
import random
random_num = random.randrange(1, 1000)
print('random number', random_num)
functions.add_numbers(21, 14, random_num)

# if tutorial
myNumber = 10

for n in range(10, 40, 5):
    if n is myNumber:
        print(n, "is the magic number")
        # break
    elif n is 0:
        print(n, "is zero")
        # break
    else:
        print(n)

# for tutorial
foods = ["nasi lemak", "roti canai", "durian", "cincaluk", "budu"]
for f in foods:
    print(f)
    panjang = len(f)
    #print(panjang)
    print(len(f))

# range, while & comments tutorial
'''
buttcrack = 5
while buttcrack < 10:
    print("butts ", buttcrack)
    buttcrack += 1
print("the end")
'''

# break tutorial
magicnumber  = 7
for n in range(21):
    if n is magicnumber:
        print(n, " is the magic number!")
        break
    else:
        print (n)

# continue tutorial
numbersTaken = [2, 7, 9, 13]
for n in range(19):
    if n in numbersTaken:
        continue
    print (n)

# Sets tutorial
groceries = {"minyak", "telur", "roti", "kaya", "telur"}
print(groceries)

if "minyak" in groceries:
    print("Dah ada minyak lahhh")
else:
    print("Kena beli minyak")

# dictionary tutorial
workmates = {'joe' : ' calm and cool', 'vicky' : ' loud and annoying', 'tony' : ' quiet and shy'}
for k, v in workmates.items():
    print(k + v)
