import random 

class Carta:
  __valores_validos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

  __naipes_validos = ['ouros', 'copas', 'paus', 'espadas']

  def __init__(self, valor, naipe):
    #inicializa a carta pássando
    self.valor = valor
    self.naipe = naipe

  #getter vem  primeiro (n modifica, só chama o valor)
  @property 
  def valor(self):
    return self.__valor

  #setter (pode usar p modificar o valor)
  @valor.setter
  def valor(self, valor):
    valor = str(valor).upper()
    if valor not in self.__valores_validos:
      raise ValueError('Valor inválido!')

    self.__valor = valor

  @property
  def naipe(self):
    return self.__naipe

  @naipe.setter
  def naipe(self, naipe):
    if naipe.lower() not in self.__naipes_validos:
      raise ValueError('Naipe inválido')
    
    self.__naipe = naipe

  def __str__(self):
    return f'{self.__valor} de {self.__naipe}'
  
  @staticmethod
  def simbolo(naipe):
    naipe = naipe.lower()
    if naipe == 'copas':
      return '♥'
    if naipe =='ouros':
      return '♦'
    if naipe == 'paus':
      return '♣'
    if naipe =='espadas':
      return '♠'

  @classmethod
  def valor_numerico(cls, valor):
    valor = str(valor).upper()
    if valor not in cls.__valores_validos:
      raise ValueError('Valor inválido')

    if valor not in ['A', 'J', 'Q', 'K']:
      return int(valor)

    if valor == 'A':
      return 1
    if valor == 'J':
      return 11
    if valor == 'Q':
      return 12
    if valor == 'K':
      return 13

  @classmethod
  def valores_validos(cls):
    return cls.__valores_validos

  @classmethod
  def naipes_validos(cls):
    return cls.__naipes_validos