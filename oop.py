import threading

class Parent():
    def print_parent_name(self):
        print('Vader')

class Child(Parent):
    def print_child_name(self):
        print('Luke')

    # overide
    def print_parent_name(self):
        print('Skywalker')


class Enemy():
    # team is a class variable
    team = "Empire"

    def __init__(self, life):
        # life is an instance variable
        self.life = life

    def attack(self):
        print('ouchh!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('I am dead :-(')
        else:
            print(str(self.life) + ' life left')

class Mario():
    def move(self):
        print('i am moving!')

class Shroom():
    def eat_shroom(self):
        print('Now i am big!')

class BigMario(Mario,Shroom):
    pass

class SimpleMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())


stormTrooper = Enemy(5)
darthVader = Enemy(50)

print (darthVader.team)
print (stormTrooper.team)
stormTrooper.attack()
stormTrooper.attack()
stormTrooper.checkLife()
darthVader.checkLife()
darthVader.team = "Sith"
print (darthVader.team)
print (stormTrooper.team)

# inheritance tutorial
hero = Child()
hero.print_child_name()
hero.print_parent_name()

# multiple inheritance tutorial
bm = BigMario()
bm.move()
bm.eat_shroom()

# threading tutorial
x = SimpleMessenger(name='send out messages')
y = SimpleMessenger(name='receive messages')
x.start()
y.start()