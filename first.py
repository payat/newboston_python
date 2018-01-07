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

# functions tutorial
functions.bitcoin_to_ringgit(3.85)
functions.bitcoin_to_ringgit(3)
functions.bitcoin_to_ringgit(1)

# return values tutorial
dude_limit = functions.allowed_dating_age(37)
print("Dude can date girls", dude_limit, "or older")

# default values for arguments tutorial
functions.get_gender("m")
functions.get_gender("f")
functions.get_gender("Q")
functions.get_gender()

# variable scope tutorial
functions.scope_a()
functions.scope_b()

# keyword arguments tutorial
functions.dumb_sentence()
functions.dumb_sentence(action="puke")
functions.dumb_sentence(action="loves", name="lutfi", item="nuna leaf")

# flexible number of arguments tutorial
functions.add_numbers(12)
functions.add_numbers(1,3,5,7,11,13)

# unpacking arguments tutorial
payats_data = [37, 2, 1]
functions.health_calculator(payats_data[0], payats_data[1], payats_data[2])
functions.health_calculator(*payats_data)

# download web image tutorial
#functions.download_web_image("https://www.lowyat.net/wp-content/uploads/2016/02/logo-purple.png")

# read & write file tutorial
functions.write_to_file("data.txt")
functions.read_file("data.txt")