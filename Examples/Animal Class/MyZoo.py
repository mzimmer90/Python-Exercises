from animal import Animal, FlyingAnimal

myDog = Animal("Storm")
myDog.add_type("dog")
myDog.add_breed("German Shepherd")

myDog.add_trick("Sit")
myDog.add_trick("Paw")

print(myDog)

myCat = Animal("Luna")
myCat.add_type("cat")
myCat.add_breed("tabby")

myCat.add_trick("Eat")
myCat.add_trick("Sleep")

print(myCat)

myDog2 = myDog
myDog2.add_breed("Husky")
myDog2.set_name("Bruno")

myDog2.add_trick("Beg")
myDog2.add_trick("Lie Down")

print(myDog2)

myBird = FlyingAnimal("Tom", 5)
