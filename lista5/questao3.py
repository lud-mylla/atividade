from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = telefone
        self.__nascimento = datetime 

    def get_id(self): 
        return self.__id
    def get_nome(self): 
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def get_nascimento(self):
        return self.__nascimento

    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def set_nascimento(self, nascimento): self.__nascimento = nascimento

    def __str__(self):
        nasc_str = self.__nascimento.strftime("%d/%m/%Y")
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - Nascimento: {nasc_str}"

class ContatoUI:
    __contatos = []

    @classmethod
    def menu(cls):
        print("\n1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Pesquisar 6-Aniversariantes 7-Sair")
        return input("Escolha: ")

    @classmethod
    def inserir(cls):
        try:
            id = int(input("id "))
            nome = input("Nome: ")
            email = input("Email: ")
            fone = input("Fone: ")
            nascimento_str = input("Data de nascimento (dd/mm/aaaa): ")
            nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")
            cls.__contatos.append(Contato(id, nome, email, fone, nascimento))
            print("Contato adicionado!")
        except Exception as e:
            print(f"Erro ao inserir contato: {e}")

    @classmethod
    def listar(cls):
        if not cls.__contatos:
            print("Nenhum contato.")
        else:
            for c in cls.__contatos:
                print(c)

    @classmethod
    def atualizar(cls):
        id = int(input("ID do contato: "))
        for c in cls.__contatos:
            if c.get_id() == id:
                nome = input("Novo nome (Enter para manter): ")
                email = input("Novo email (Enter para manter): ")
                fone = input("Novo fone (Enter para manter): ")
                nasc_str = input("Nova data de nascimento (dd/mm/aaaa) (Enter para manter): ")

                if nome: c.set_nome(nome)
                if email: c.set_email(email)
                if fone: c.set_fone(fone)
                if nasc_str:
                    try:
                        nascimento = datetime.strptime(nasc_str, "%d/%m/%Y")
                        c.set_nascimento(nascimento)
                    except:
                        print("Data inválida. Nascimento não alterado.")

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
        nome = input("Nome para buscar (iniciais): ").lower()
        encontrados = [c for c in cls.__contatos if c.get_nome().lower().startswith(nome)]
        if encontrados:
            for c in encontrados:
                print(c)
        else:
            print("Nenhum contato encontrado.")

    @classmethod
    def aniversariantes(cls):
        try:
            mes = int(input("Digite o mês o número do mês: "))
            encontrados = [c for c in cls.__contatos if c.get_nascimento().month == mes]
            if encontrados:
                print(f"\nContatos que fazem aniversário no mês {mes}:")
                for c in encontrados:
                    print(c)
            else:
                print("Nenhum aniversariante neste mês.")
        except:
            print("Mês inválido.")

    @classmethod
    def executar(cls):
        while True:
            op = cls.menu()
            if op == '1': cls.inserir()
            elif op == '2': cls.listar()
            elif op == '3': cls.atualizar()
            elif op == '4': cls.excluir()
            elif op == '5': cls.pesquisar()
            elif op == '6': cls.aniversariantes()
            elif op == '7':
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida.")

ContatoUI.executar()


