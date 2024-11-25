# from maspy import *

class SpaceClass:
    def __init__(self, id):
        self.id = id
        self.free = "livre"
        self.car = "Sem Carro"

    def __str__(self):
      return f"{self.id} :: {self.free} :: {self.car}"
    
    def alocateCar(self, car):
        if(self.free):
          self.car = car
          self.free = False
          return True
        else:
          return False

    def desalocateCar(self, car):
        if(self.car == car):
          self.car = "Sem carro"
          self.free = True
          return True
        else:
          return False
