class Contato:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class ContatoUI:
    __contatos = []

    @classmethod
    def menu(cls):
        print("\n1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Pesquisar 6-Sair")
        return input("Escolha: ")

    @classmethod
    def inserir(cls):
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Fone: ")
        cls.__contatos.append(Contato(id, nome, email, fone))
        print("Contato adicionado!")

    @classmethod
    def listar(cls):
        if not cls.__contatos:
            print("Nenhum contato.")
        for c in cls.__contatos:
            print(c)

    @classmethod
    def atualizar(cls):
        id = int(input("ID do contato: "))
        for c in cls.__contatos:
            if c.get_id() == id:
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                fone = input("Novo fone: ")
                if nome: c.set_nome(nome)
                if email: c.set_email(email)
                if fone: c.set_fone(fone)
                print("Contato atualizado!")
                return
        print("Contato não encontrado.")

    @classmethod
    def excluir(cls):
        id = int(input("ID do contato: "))
        for c in cls.__contatos:
            if c.get_id() == id:
                cls.__contatos.remove(c)
                print("Contato removido!")
                return
        print("Contato não encontrado.")

    @classmethod
    def pesquisar(cls):
        nome = input("Nome para buscar: ").lower()
        encontrados = [c for c in cls.__contatos if c.get_nome().lower().startswith(nome)]
        if encontrados:
            for c in encontrados:
                print(c)
        else:
            print("Nenhum contato encontrado.")

    @classmethod
    def executar(cls):
        while True:
            op = cls.menu()
            if op == '1': cls.inserir()
            elif op == '2': cls.listar()
            elif op == '3': cls.atualizar()
            elif op == '4': cls.excluir()
            elif op == '5': cls.pesquisar()
            elif op == '6': 
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida.")

# Iniciar programa
ContatoUI.executar()
