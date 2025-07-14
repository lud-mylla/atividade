from datetime import datetime

class Paciente:
    def __init__(self, nome: str, cpf: str, telefone: str, nascimento: datetime):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = datetime
   

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf 

    def get_telefone(self):
        return self.__telefone
    
    def set