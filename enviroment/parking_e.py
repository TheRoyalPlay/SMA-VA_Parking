from maspy import *
from classes import *

divider = "-------------------------------------------"
class ParkingEnviroment(Environment):
    park_space_list = []

    def __init__(self, env_name):
      super().__init__(env_name)
    
    # def create_free_space(self, id):
    #   self.park_space_list.append(SpaceClass(id))
    #   self.create(Percept("vaga",(id,"livre"),adds_event=False))
    
    # def createOcupiedSpace(self, id, name):
    #     self.park_space_list.append(SpaceClass(id, name))  

    # def create_specific_space(self, SpaceClass):
    #     self.park_space_list.append(SpaceClass)

    def create_many_spaces(self, number_spaces):
      for i in range(number_spaces):
        self.create(Percept("vaga",(i, "livre"), adds_event=False))
        self.park_space_list.append(SpaceClass(i))

    def alocate_car(self, agt, park_space_id):
        # free = 
        park_space = self.get(Percept("vaga",(park_space_id,"livre")))
        if park_space:
          # print(f"park_space = {park_space}")
          if park_space.args[1] == "livre":
            self.change(park_space,(park_space_id,agt.str_name))
            # print(f"{agt} estacionou na vaga {park_space_id}")
            self.park_space_list[park_space_id].alocate_car(agt.str_name)
            # print("")
            # print(f"park_space.args = {park_space.args}")
            # print(self.get(Percept("vaga",(park_space_id,"livre"))))
            # print("")
            return True
          else:
             print(f"Vaga {park_space_id} nao esta livre")
             return False
        else:
          print(f"Vaga {park_space_id} nao esta livre")
          return False
        
    def desalocate_car(self, agt):
        park_space = self.get(Percept("vaga",("ID",agt)))
        if park_space:
            self.change(park_space,(park_space.args[0],"livre"))
            print("")
            print(f"Carro {agt.str_name} saiu da vaga {park_space.args[0]}")
            self.park_space_list[park_space.args[0]].desalocate_car(agt.str_name)
            return True
        else:
            return False

    def verify_car_parking(self, agt, park_space_id):
        car_parking = self.get(Percept("vaga",([park_space_id],[agt])))
        if car_parking:
            print(f"Carro {agt.str_name} esta na vaga ")
            return True
        else:
            print(f"Carro {agt.str_name} nao esta na vaga")
            return False

    def verify_free_space(self, park_space):
      park_space = self.get(Percept("vaga",(park_space,"livre")))
      if park_space:
        return park_space.args
      else:
        return False

    def get_free_space(self):
        park_space = self.get(Percept("vaga",("ID","livre")))
        if park_space.args[1] == "livre":
           return park_space.args
        else:
           return False
       
    def __str__(self):
      if len(self.park_space_list) > 0:
        print(f"Ambiente :: {self._my_name}")
        print(f"Lista de Vagas:")
        for park_space in self.park_space_list:
          print(f"Vaga {park_space}")
        return f"{divider}"
      else:
        print("")
        print(f"Ambiente :: {self._my_name} :: Sem Vagas Criadas")
        return f"{divider}"



