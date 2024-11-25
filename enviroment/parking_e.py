from maspy import *
from classes import *

class ParkingEnviroment(Environment):
    space_list = []

    def __init__(self, env_name):
        super().__init__(env_name)
    
    def createFreeSpace(self, id):
        self.space_list.append(SpaceClass(id))
    
    # def createOcupiedSpace(self, id, name):
    #     self.space_list.append(SpaceClass(id, name))  

    def createSpecificSpace(self, SpaceClass):
        self.space_list.append(SpaceClass)

    def __str__(self):
      if len(self.space_list) > 0:
        print(f"")
        print(f"Ambiente :: {self._my_name} Vagas >>>>>>>>")
        for space in self.space_list:
          print(f"Vaga :: {space}")
        return f"-------------------------------"
      else:
        return f"{self._my_name} :: Sem Vagas Criadas"

    def createManySpaces(self, quant):
      for i in range(quant):
         self.createFreeSpace(i)
         self.create(Percept("Vaga",(i, "free"), adds_event=False))
         




