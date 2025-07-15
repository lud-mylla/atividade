from datetime import datetime, timedelta

class Treino:
    def __init__(self, id: int, data: datetime, distancia: float, tempo: timedelta):
        self.__id = id
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo


    def set_id(self, id):
        self._id = id
    
    def set_data(self, data):
        self.__data = data
    
    def set_distancia(self,distancia):
        self.__distancia = distancia

    def set_tempo(self, tempo):
        self.__tempo = tempo


    
    def get_id(self):
        return self.__id
    
    def get_data(self):
        return self.__data 
    
    def get_distancia(self):
        return self.__distancia
    
    def get_distancia(self):
        return self.__distancia
    

    def menu(self):
        while True:
          
          print("Menu de treino")
          print("1-Inserir treino")
          print("2-listar treino")
          print("3-Atualizar treino")
          print("4-Excluir treino")
          print("5-Sair")

          if 