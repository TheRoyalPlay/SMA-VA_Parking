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
        print(f"\nAgente({self.my_name[0]}) :: {src} solicitou qualquer vaga    ")
        # self.print(f":: {src} solicitou qualquer vaga")
        free_space_id = self.action("PE").get_free_space()
        if free_space_id:
          # print(free_space_id)
          print(f"Agente({self.my_name[0]}) :: Vaga {free_space_id[0]+1} livre")
          self.send(src,achieve,Goal("estacionar",free_space_id[0]))
        else: 
          self.send(src,tell,Belief("sem vagas"))
          print(f"Agente({self.my_name[0]}) :: Sem vaga livre")

    @pl(gain,Goal("InformarFavorita","Favorita"))
    def inform_occupied(self, src, fav_space):
        # print(f"{src} solicitou Vaga {fav_space}")
        print(f"\nAgente({self.my_name[0]}) :: {src} solicitou Vaga {fav_space+1}    ")
        exist_fav_space = self.action("PE").verify_free_space(fav_space)

        if exist_fav_space[1] == "livre":
          print(f"Agente({self.my_name[0]}) :: Vaga {fav_space+1} livre    ")
          self.send(src,achieve,Goal("estacionar",fav_space))
        else:
          print(f"Agente({self.my_name[0]}) :: Vaga {fav_space+1} esta ocupada    ")
          free_space_id = self.action("PE").get_free_space()
          if free_space_id:
            print(f"Agente({self.my_name[0]}) :: Vaga {free_space_id[0]+1} esta livre para {src}    ")
            self.send(src,tell,Belief("vaga livre",(free_space_id[0])))
          else:
            self.send(src,tell,Belief("sem vagas"))
            print(f"Agente({self.my_name[0]}) :: Sem vaga livre    ")
            
    def __str__(self):
        text = f"Parking Agent :: {self.str_name}\n"
        text += divider
        return f"{text}"