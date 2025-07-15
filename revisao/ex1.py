from datetime import datetime, timedelta

class Treino:
    def __init__(self, id: int, data: datetime, distancia: float, tempo: timedelta):
        self._id = id
        self._data = data
        self._distancia = distancia
        self._tempo = tempo

    # Getters
    def get_id(self) -> int:
        return self._id

    def get_data(self) -> datetime:
        return self._data

    def get_distancia(self) -> float:
        return self._distancia

    def get_tempo(self) -> timedelta:
        return self._tempo

    # Setters
    def set_id(self, id: int):
        self._id = id

    def set_data(self, data: datetime):
        self._data = data

    def set_distancia(self, distancia: float):
        self._distancia = distancia

    def set_tempo(self, tempo: timedelta):
        self._tempo = tempo

    # ToString
    def __str__(self) -> str:
        return (f"Treino ID: {self._id}, Data: {self._data.strftime('%Y-%m-%d %H:%M:%S')}, "
                f"Distância: {self._distancia:.2f} km, Tempo: {str(self._tempo)}")


class TreinoUI:
    def __init__(self):
        self.treinos = []

    def inserir_treino(self):
        try:
            id = int(input("Digite o ID do treino: "))
            data_str = input("Digite a data do treino (formato YYYY-MM-DD HH:MM:SS): ")
            data = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
            distancia = float(input("Digite a distância percorrida (km): "))
            tempo_str = input("Digite o tempo da corrida (formato HH:MM:SS): ")
            h, m, s = map(int, tempo_str.split(':'))
            tempo = timedelta(hours=h, minutes=m, seconds=s)

            treino = Treino(id, data, distancia, tempo)
            self.treinos.append(treino)
            print("Treino inserido com sucesso!\n")
        except Exception as e:
            print(f"Erro ao inserir treino: {e}\n")

    def listar_treinos(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.\n")
            return

        print("Lista de Treinos:")
        for treino in self.treinos:
            print(treino)
        print()

    def atualizar_treino(self):
        try:
            id = int(input("Digite o ID do treino que deseja atualizar: "))
            treino = next((t for t in self.treinos if t.get_id() == id), None)

            if treino is None:
                print("Treino não encontrado.\n")
                return

            print("Digite os novos dados (deixe vazio para manter o valor atual):")

            data_str = input(f"Data atual {treino.get_data().strftime('%Y-%m-%d %H:%M:%S')}: ")
            if data_str:
                treino.set_data(datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S"))

            distancia_str = input(f"Distância atual {treino.get_distancia()} km: ")
            if distancia_str:
                treino.set_distancia(float(distancia_str))

            tempo_str = input(f"Tempo atual {str(treino.get_tempo())} (HH:MM:SS): ")
            if tempo_str:
                h, m, s = map(int, tempo_str.split(':'))
                treino.set_tempo(timedelta(hours=h, minutes=m, seconds=s))

            print("Treino atualizado com sucesso!\n")
        except Exception as e:
            print(f"Erro ao atualizar treino: {e}\n")

    def excluir_treino(self):
        try:
            id = int(input("Digite o ID do treino que deseja excluir: "))
            treino = next((t for t in self.treinos if t.get_id() == id), None)

            if treino is None:
                print("Treino não encontrado.\n")
                return

            self.treinos.remove(treino)
            print("Treino excluído com sucesso!\n")
        except Exception as e:
            print(f"Erro ao excluir treino: {e}\n")

    def menu(self):
        while True:
            print("Menu Treino")
            print("1. Inserir treino")
            print("2. Listar treinos")
            print("3. Atualizar treino")
            print("4. Excluir treino")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.inserir_treino()
            elif opcao == '2':
                self.listar_treinos()
            elif opcao == '3':
                self.atualizar_treino()
            elif opcao == '4':
                self.excluir_treino()
            elif opcao == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    ui = TreinoUI()
    ui.menu()
