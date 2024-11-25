from maspy import *

class CarAgent(Agent):
    def __init__(self, agt_name):
        super().__init__(agt_name)
        self.add(Goal("prucurar_vaga"))
        self.add(Belief("sem_vaga"))