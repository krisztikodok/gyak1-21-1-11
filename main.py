"""
class votersElligibility(Exception):
  def __init__(self): #constructor method
    super()
"""

class Animal(object):
  def __init__(self,animal_type):
    print("Animal type:", animal_type)

class Mammal(Animal):
  def __init__(self):
    super().__init__("Mammal")
    print("Mammals give birth directly")

class Reptile(Animal):
  def __init__(self):
    super().__init__("Reptile")
    print("Reptiles reproduce in 3 ways: oviparity (laying eggs),viviparity(live birt) and ovo-viviparity(in between)")