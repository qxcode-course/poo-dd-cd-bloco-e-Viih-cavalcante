from abc import ABC, abstractmethod

class Veiculo:
    def __init(self, id: str, tipo: str):
        self.__id: str = id
        self._tipo: str = tipo
        self._horaEntrada: int = 0

    def getld(self) -> str:
        return self.__id
    def getTipo(self) -> str:
        return self.__tipo
    def setEntrada(self) -> int:
        return self._horaEntrada
    @abstractmethod
    def calcularValor(self, horaSaida: int) -> None:
        pass
    def __strt__(self) -> str:
        x = 10 - len(self.__tipo)
        y = 10 - len(self.__id)
        unders =x * "_"
        unders2 = y * "_"
        return f"{unders + self._tipo} : {unders2 + self.__id} : {self._horaEntrada}"

class Bike(veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")
    def calcularValor(self,horaSaida: int):
        return 3
class Moto(veiculo):
    def __init__(self, id: str):
        super().__init__(id,"Moto")
    def calcularValor(self, horaSaida: int):
        tempo = horaSaida - self._horaEntrada
        tempo /= 20
        return tempo




def main():
    while True:
        linha: str = input()
        print("$" + linha)
        args: list [str] = linha.split(" ")
main()

