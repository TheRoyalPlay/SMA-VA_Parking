from classes import *
from agents import *
from enviroment import *

if __name__== "__main__":
    parking = ParkingEnviroment("PE1")
    ag1 = CarAgent("CAR1")
    ag2 = ParkingAgent("PA1")
    # Passa um objeto para criar um espaço
    # s1 = SpaceClass("-1")
    # print(s1)
    # parking.createSpecificSpace(s1)    
    print(parking)
    print(ag1)
    print(ag2)
    # Cria um número "num" de espaços
    num = 4
    parking.createManySpaces(num)


    print(parking)

    Admin().connect_to([ag1,ag2],parking)
    Admin().start_system()
