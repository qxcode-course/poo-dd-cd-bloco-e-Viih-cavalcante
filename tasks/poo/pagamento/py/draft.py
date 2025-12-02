from abc import ABC, abstractmethod
class Pagamento(ABC):
    def __init__(self, valor: float , descriçao: str):
        self.valor: float = valor
        self.descriçao = descriçao 
    def resumo(self) -> str:
        return f"pagamento de R$ {self.valor}: {self.descriçao}"
    def validar_valor(self) -> None:
        if self.valor<= 0:
            raise ValueError("falhou: valor invalido")
    @abstractmethod
    def processar(self):
        pass
class CartãoCredito(Pagamento)
    def __init__(self, num: int, nome: str, limite: float, valor: float, descriçao: str):
        super().__init__(valor,descriçao)