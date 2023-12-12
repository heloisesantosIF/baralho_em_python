from Baralho import Baralho
from MesaBaralho import MesaBaralho

class JogoDaBatalha:
    def __init__(self, mesa):

        self.__mesa = mesa
        self.__cartas_jogador_1 = []
        self.__cartas_jogador_2 = []
        self.__pontos_jogador_1 = 0
        self.__pontos_jogador_2 = 0     

        for i in range(0, 3):
            carta = mesa.retira_carta()
            self.__cartas_jogador_1.append(carta)

            carta = mesa.retira_carta()
            self.__cartas_jogador_2.append(carta)  
    
    def maior_carta(self,cartas_jogador):
        carta_maior = cartas_jogador[0]
        maior_valor = carta_maior.valor_numerico(carta_maior.valor)
        for carta in cartas_jogador:
            valor = carta.valor_numerico(carta.valor)
            if valor > maior_valor:
                carta_maior = carta
                maior_valor = valor

        return carta_maior

    def jogar(self):
        carta_1 = self.maior_carta(self.__cartas_jogador_1)
        valor_1 = carta_1.valor_numerico(carta_1.valor)
        self.__cartas_jogador_1.remove(carta_1)
        self.__mesa.adiciona_descarte(carta_1)

        carta_2 = self.maior_carta(self.__cartas_jogador_2)
        valor_2 = carta_2.valor_numerico(carta_2.valor)
        self.__cartas_jogador_2.remove(carta_2)
        self.__mesa.adiciona_descarte(carta_2)

        if valor_1 == valor_2:
            self.__pontos_jogador_1 += 1
            self.__pontos_jogador_2 += 1  
        elif valor_1 > valor_2:
            self.__pontos_jogador_1 += 2
        else:
            self.__pontos_jogador_2 += 2

        resultado = f'\nJogador 1: {carta_1.valor} de {carta_1.naipe}\n'
        resultado += f'Jogador 2: {carta_2.valor} de {carta_2.naipe}'

        if len(self.__cartas_jogador_1) == 0:
            resultado += f'\n\n{self.finaliza()}\n\n'

        return resultado 

    def finaliza(self):
        if self.__pontos_jogador_1 == self.__pontos_jogador_2:
            return f'Ocorreu empate cada jogador com {self.__pontos_jogador_1} pontos.'
        elif self.__pontos_jogador_1 > self.__pontos_jogador_2:
            return f'Jogador 1 venceu com {self.__pontos_jogador_1} pontos.'         
        else:
            return f'Jogador 2 venceu com {self.__pontos_jogador_2} pontos.'

baralho1 = Baralho()
mesa1 = MesaBaralho(baralho1)

batalha = JogoDaBatalha(mesa1)

for i in range(0,3):
    retorno = batalha.jogar()
    print(retorno)
    input('ENTER para continuar...')