import random

from Carta import Carta
class Baralho:
  __cartas = []

  def __init__(self):
    for naipe in Carta.naipes_validos():
      for valor in Carta.valores_validos():
        carta = Carta(valor, naipe)
        self.__cartas.append(carta)

  @property
  def cartas(self):
    return self.__cartas

  def embaralhar(self):
    random.shuffle(self.__cartas)
