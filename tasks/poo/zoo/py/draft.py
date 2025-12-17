from abc import ABC, abstractmethod

class animal (ABC):
 def __init__(self, nome: str):
   self.__nome: str = nome

 def apresentarNome(self) -> str:
    print(f"Eu sou um(a) {self.__nome}!")

 @abstractmethod
 def fazerSom(self):
   pass
 
 @abstractmethod
 def mover(self):
   pass
 
class Leão(Animal):
   def __init__(self, nome: str):
    super().__init__(nome)

   def fazerSom(self):
     print(f"roawwwwww")

   def mover(self):
     print(f"azunhão")

   class Elefante(animal):
     def__init__(self, nome: str):
     super().__init__(nome)
     def fazerSom(self):
       print(f"")
 
