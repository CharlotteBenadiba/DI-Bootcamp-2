'''___Exercises XP (1.1)_____________________________________________________________________________________________________________________________________''''

#____Exercise 1 : Pets   _____
class Pets():
    def __init__(self, animals):
        self.animals = animals


    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

cat1=Bengal('Salem',11)
cat2=Chartreux("Tom",2)
cat3=Siamese('Wiskers',5)

#2

all_cats = [cat1, cat2, cat3]
sara_pets = Pets(all_cats)

#4
sara_pets.walk()

#___________________________


#____Exercise 2 : Dogs _______________


#__________________________





#____  ____________________
#__________________________



#____  ____________________
#__________________________




#____  ____________________
#__________________________


#____  ____________________
#__________________________




#____  ____________________
#__________________________

'''_____________________________________________________________________________________________________________________________________'''

