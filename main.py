class votersElligibility(Exception):

  def __init__(self):  #constructor method
    super()


try:
  age = 21
  print("Age is " + str(age))
  if age < 18:
    raise votersElligibility
except votersElligibility:
  print("Less than 18")
else:
  print("Age ok")
finally:
  print("EOF")
print("\n\n")


class Animal(object):

  def __init__(self, animal_type):
    print("Animal type:", animal_type)


class Mammal(Animal):

  def __init__(self):
    super().__init__(
        "Mammal")  #super calls a method from the parent class (Animal)
    print("Mammals give birth directly")


class Reptile(Animal):

  def __init__(self):
    super().__init__("Reptile")
    print(
        "Reptiles reproduce in 3 ways: oviparity (laying eggs),viviparity(live birt) and ovo-viviparity(in between)"
    )


dog = Mammal()
print("\n\n")
bearded_dragon = Reptile()
