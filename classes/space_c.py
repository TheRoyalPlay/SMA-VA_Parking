# from maspy import *

class SpaceClass:
    def __init__(self, id):
        self.id = id
        self.free = "livre"
        self.car = "Sem Carro"

    def __str__(self):
      return f"{self.id+1} :: {self.free} :: {self.car}"
    
    def alocate_car(self, car):
        if(self.free):
          self.car = car
          self.free = "Ocupado"
          return True
        else:
          return False

    def desalocate_car(self, car):
        if(self.car == car):
          self.car = "Sem carro"
          self.free = "livre"
          return True
        else:
          return False
