from animal import Animal
from flying_animal import FlyingAnimal
from non_bird_flying_animal import NonBirdFlyingAnimal

myDog = Animal("Storm")
myDog.add_type("dog")
myDog.add_breed("German Shepherd")

myDog.tricks = "Sit"
myDog.tricks = "Paw"

print(myDog)

myCat = Animal("Luna")
myCat.add_type("cat")
myCat.add_breed("tabby")

myCat.tricks = "Eat"
myCat.tricks = "Sleep"

print(myCat)

myDog2 = myDog
myDog2.name = "Bruno"
myDog2.add_breed("Husky")

myDog2.tricks = "Beg"
myDog2.tricks = "Lie Down"

print(myDog2)

myBird = FlyingAnimal("Tom", 50)
myBird.add_type("goose")
myBird2 = FlyingAnimal("Tweet", 20)
myBird2.add_type("tit")

myBird.wingspan = 40
myBird2.wingspan = myBird.wingspan

print(myBird)
print(myBird2)

print(f"So far, there are {FlyingAnimal.flying_animal_count} flying animals in my zoo.")

snake = NonBirdFlyingAnimal("Noodle", 0, 100)
frog = NonBirdFlyingAnimal("Jack", 0, 15)
squirrel = NonBirdFlyingAnimal("Charlie", 7, 150)

print(f"So far, there are {NonBirdFlyingAnimal.flying_animal_count} flying animals in my zoo.")

print(NonBirdFlyingAnimal.animal_with_longest_distance())
