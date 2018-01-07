import random
import urllib

# download web image tutorial
def download_web_image(url):
    name = random.randrange(1, 1000)
    full_filename = str(name) + ".png"
    urllib.urlretrieve(url, full_filename)

# read & write files tutorial
def write_to_file(filename):
    fw = open(filename, 'w')
    fw.write('i ate too much durian. my breath stinks!!\n')
    fw.write('will need to drink a lot of water')
    fw.close()

def read_file(filename):
    fr = open(filename, 'r')
    text = fr.read()
    print(text)
    fr.close()



# functions tutorial
def bitcoin_to_ringgit(btc):
    amount = btc * 547 * 4
    print(amount)

# return values tutorial
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

# default values for arguments tutorial
def get_gender(sex="unknown"):
    if sex is "m":
        sex = "Male"
    elif sex is "f":
        sex = "Female"
    print(sex)


# variable scope tutorial
a = 123
def scope_a():
    a = 444
    print(a)

def scope_b():
    print(a)

# keyword arguments tutorial
def dumb_sentence(name="payat", action="ate", item="meatballs"):
    print(name, action, item)

# flexible number of arguments tutorial
def add_numbers(*args):
    total=0
    for a in args:
        total += a
    print(total)

# unpacking arguments tutorial
def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 4)
    print(answer)