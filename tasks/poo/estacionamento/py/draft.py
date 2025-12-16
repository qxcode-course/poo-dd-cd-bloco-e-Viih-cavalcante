from abc import ABC, abstractmethod

class Veiculo:                                            
    def __init__(self, id: str, tipo: str):
        self.__id: str = id
        self._tipo: str = tipo
        self._horaEntrada: int = 0

    
    def getId(self) -> str:
        return self.__id
    
    def getTipo(self) -> str:
        return self._tipo
    
    def setEntrada(self, horaEntrada: int) -> None:
        self._horaEntrada = horaEntrada

    def getEntrada(self) -> int:
        return self._horaEntrada
    
    @abstractmethod 
    def calcularValor(self, horaSaida: int) -> None:                          
        pass 

    def __str__(self) -> str:
        x = 10 - len(self._tipo)               
        y = 10 - len(self.__id)
        unders = x * "_"                                                                  
        unders2 = y * "_"      
        return f"{unders + self._tipo} : {unders2 + self.__id} : {self._horaEntrada}"

class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")

    def calcularValor(self,horaSaida: int):
        return 3
    
class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id,"Moto")

    def calcularValor(self, horaSaida: int):
        tempo = horaSaida - self._horaEntrada
        tempo /= 20
        return tempo
    
class Carro(Veiculo):
    def __init__(self, id: int):
        super().__init__(id, "Carro")

    def calcularValor(self, horaSaida: int):
        tempo = horaSaida - self._horaEntrada
        tempo /= 10
        if tempo < 5:
            return 5
        else:
            return tempo
        
class Estacionamento:
    def __init__(self):
        self.__horaAtual: int = 0
        self.__veiculos: list[Veiculo] = []

    def procurarVeiculos(self, id: str) -> int:
        for i in range(0, len(self.__veiculos)):
            if self.__veiculos[i].getld() == id:
                return i
            return -1
        
    def passarTempo(self, tempo: int) -> None:
        self.__horaAtual += tempo

    def estacionar(self, veiculo: Veiculo) -> None:
        veiculo.setEntrada(self.__horaAtual)
        self.__veiculos.append(veiculo)

    def pagar(self, id: str)  -> None:
        pos = self.procurarVeiculo(id)
        if pos != -1:
            veiculo = self.__veiculos.pop(pos)
            print(f"{veiculo.getTipo()} chegou {veiculo.getEntrada()} saiu {self.__horaAtual}. Pagar R$ {veiculo.calcularValor(horaSaida = self.__horaAtual):_.2f}")
    def __str__(self) -> str:
        if len(self.__veiculos) != 0:
            return f"{"\n".join(str(x) for x in self.__veiculos)}\nHora atual: {self.__horaAtual}"
        else:
            return f"Hora atual: {self.__horaAtual}"
def main():

    while True:
        linha: str = input() 
        print("$" + linha)
        args: list[str] = linha.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(Estacionamento) 
        elif args[0] == "tempo":
            Estacionamento.passarTempo(tempo= int(args[1]))   
        elif args[0] == "estacionar":
            if args[1] == "bike":
                veiculo = Bike(args[2])
                Estacionamento.estacionar(veiculo)
            elif args[1] == "moto":
                veiculo = Moto(args[2])
                Estacionamento.estacionar(veiculo)
            elif args[1] == "carro":
                veiculo = Carro(args[2])
                Estacionamento.estacionar(veiculo)
        elif args[0] == "pagar":
            Estacionamento.pagar(args[1])

main()


