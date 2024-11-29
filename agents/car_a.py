from maspy import *
from time import *
import random as rand
class CarAgent(Agent):
  fav_space = 0

  def __init__(self, agt_name, fav_space):
    super().__init__(agt_name)
    self.add_favorite_space(fav_space)

  def add_favorite_space(self, fav_space):
    self.fav_space = fav_space
    if fav_space == -1:
      self.add(Goal("prucurarVaga"))
    else:
      self.add(Goal("prucurarVagaFavorita"))
      self.add(Belief("favorita",(fav_space)))

  def get_fav(self):
    if self.fav_space == -1:
      return "Sem Favorita"
    else:
      space = self.get(Belief("favorita",("FAV")))
      return space.args
  
  @pl(gain,Goal("prucurarVaga"))
  def search_espicifc_space(self,src):
    sleep_time = rand.randrange(2, 15)
    sleep(sleep_time)
    self.send("PA",achieve,Goal("InformarQualquer"))

  @pl(gain,Goal("prucurarVagaFavorita"),Belief("favorita",("LocalFavorito")))
  def search_fav_space(self,src,local_favorito):
    sleep_time = rand.randrange(2, 15)
    sleep(sleep_time)
    self.send("PA",achieve,Goal("InformarFavorita", local_favorito))
  
  @pl(gain,Goal("estacionar","Vaga"))
  def park(self,src,park_space):
    succes = self.action("PE").alocate_car(self, park_space)
    if succes:
      print(f"{self.str_name} estacionou na Vaga {park_space}")
      print("")
      # self.action("PE").__str__()
    else:
      print(f"Vaga {park_space} estava ocupada")
      print("")
    sleep(rand.randrange(3, 20))
    self.add(Goal("sair"))

  @pl(gain,Belief("sem vagas"))
  def no_spaces(self,src):
    self.add(Goal("sair"))

  @pl(gain,Goal("sair"))
  def quit_park(self, src):
    self.action("PE").desalocate_car(self)
    print(f"{self.str_name} Saiu do estacionamento")
    self.stop_cycle()
    # print(self.action("PE").__str__())

  def __str__(self):
    fav = self.get_fav()
    # if fav:
    #   return f"Carro :: {self.str_name} :: {self.fav_space}"
    # else:
    #     return f"Carro :: {self.str_name} :: Sem Favorita"
    return f"{self.str_name} :: {fav}"
