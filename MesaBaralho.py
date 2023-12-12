class MesaBaralho:
  def __init__(self, baralho):
    baralho.embaralhar()
    self.__pilha_principal = baralho.cartas
    self.__pilha_descarte = []

  def descartar(self):
    carta = self.__pilha_principal.pop()
    print(carta)
    self.__pilha_descarte.append(carta)

  def total_cartas(self):
    total = len(self.__pilha_principal) + len(self.__pilha_descarte)
    return total
  
  # verificar se uma determinada carta está no descarte
  def esta_descartada(self, valor, naipe):
    for carta in self.__pilha_descarte:
      if carta.valor == valor and carta.naipe == naipe:
        return True
    return False

  # exibir cartas na pilha 
  def exibir_pilha(self, nome_pilha = 'descarte'):
    pilha = self.__pilha_descarte
    if nome_pilha == 'principal':
      pilha = self.__pilha_principal

    for carta in pilha:
      valor_e_simbolo = f'{carta.valor} {carta.simbolo(carta.naipe)}'
      print(valor_e_simbolo)

  def retira_carta(self):
        return self.__pilha_principal.pop()

  def adiciona_descarte(self, carta):
        self.__pilha_descarte.append(carta)