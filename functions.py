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

bitcoin_to_ringgit(3.85)
bitcoin_to_ringgit(3)
bitcoin_to_ringgit(1)

dude_limit = allowed_dating_age(37)
print("Dude can date girls", dude_limit, "or older")

get_gender("m")
get_gender("f")
get_gender("Q")
get_gender()

a = 123
scope_a()
scope_b()

dumb_sentence()
dumb_sentence(action="puke")
dumb_sentence(action="loves", name="lutfi", item="nuna leaf")

add_numbers(12)
add_numbers(1,3,5,7,11,13)

payats_data = [37, 2, 1]
health_calculator(payats_data[0], payats_data[1], payats_data[2])

health_calculator(*payats_data)