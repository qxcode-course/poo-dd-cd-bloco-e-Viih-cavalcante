from abc import ABC, abstractmethod

class Animal (ABC):
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

class Elefante(Animal):
  def __init__(self, nome: str):
    super().__init__(nome)

  def fazerSom(self):
    print(f"uuuuuuuurrrmm uuuuuh")
  def mover(self):
    print(f"jogar agua")
class Cobra(Animal):
  def _init_(self, nome: str):
    super()._init_(nome)
 
