from maspy import *
from classes import *
from agents import *
from enviroment import *
import random as rand

divider = "-------------------------------------------"

def list_cars(car_list):
    print(f"Lista de Carros: ")
    print(f"Carro :: Vaga Favorita")
    for car in car_list:
      print(car)
    print(f"{divider}")

def create_agents(agent_quantity, spaces_num):
    for i in range(agent_quantity):
      fav_space = rand.randrange(-1, spaces_num) # (-1) sigfica falta de favoritismo
      car_list.append(CarAgent("CAR",fav_space))

if __name__== "__main__":
    # Inicia o ambiente
    park_env = ParkingEnviroment("PE")
    # Cria as vagas inicias com id sequenciais, até o valor "num"
    spaces_num = 4
    park_env.create_many_spaces(spaces_num)
    print(park_env)
    # Cria um agente de controle de vagas
    parking_controller = ParkingAgent("PA")
    print(parking_controller)
    # Cria os agentes com base na quantidade e quantidade de vagas
    car_list: list[CarAgent] = []
    agent_quantity = 15
    create_agents(agent_quantity, spaces_num)
    # Conecta os agentes com o ambiente
    # parking_channel = Channel("Estacionamento")
    # connect_agents(car_list, parking_controller, park_env, parking_channel)
    Admin().connect_to(parking_controller, park_env)
    for i in range(len(car_list)):
      Admin().connect_to(car_list[i], park_env)
    # Mostra a lista de carros
    list_cars(car_list)
    #Inicia o sistema
    Admin().start_system()

