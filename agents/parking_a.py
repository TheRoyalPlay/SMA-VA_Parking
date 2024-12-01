from maspy import *

divider = "-------------------------------------------"
class ParkingAgent(Agent):
    def __init__(self, agt_name):
        super().__init__(agt_name)

    # @pl(gain,Goal("InformarQualquer","Agent"), Belief("vaga",("Id","Livre")),"Estacionamento")        
    # def inform_free(self,src,agent,parkin_space):
    #     if parkin_space[1] == "livre":
    #       space_id = parkin_space[0]
    #       self.print(f"Informando vaga livre :: {space_id} :: {agent}")
    #       self.send(agent,achieve,Goal("estacionar",(space_id,"Livre")))
    #     else:
    #       space_id = parkin_space[0]
    #       self.print(f"Informando vaga ocupada :: {space_id} :: {agent}")
    #       self.send(agent,achieve,Goal("estacionar",(space_id,"Livre")))

    @pl(gain,Goal("InformarQualquer"))        
    def inform_free(self,src):
        print(f"{src} solicitou qualquer vaga")
        free_space_id = self.action("PE").get_free_space()
        if free_space_id:
          # print(free_space_id)
          # self.action("PE").alocate_car(src, free_space_id)
          self.send(src,achieve,Goal("estacionar",free_space_id[0]))
        else: 
          self.send(src,tell,Belief("sem vagas"))
          self.print("Sem vaga livre")

    @pl(gain,Goal("InformarFavorita","Favorita"))
    def inform_occupied(self, src, fav_space):
        print(f"{src} solicitou Vaga {fav_space}")
        exist_fav_space = self.action("PE").verify_free_space(fav_space)

        if exist_fav_space[1] == "livre":
          self.send(src,achieve,Goal("estacionar",fav_space))

        else:
          # print(f"Vaga {fav_space} esta ocupada")
          self.print(f"Vaga {fav_space} esta ocupada")
          print("")
          free_space_id = self.action("PE").get_free_space()
          if free_space_id:
            print(f"Vaga {free_space_id[0]} esta livre para {src} ")
            self.send(src,tell,Belief("vaga livre",(free_space_id[0])))
          else:
            self.send(src,tell,Belief("sem vagas"))
            self.print("Sem vaga livre")
            
    def __str__(self):
        print(f"Parking Agent :: {self.str_name}")
        return f"{divider}"