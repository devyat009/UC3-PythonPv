# Atividade:  Vamos melhorar o jogo que fizemos no exercício 32. A partir de  
# agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4  
# tentativas para tentar acertar
# Data: 27/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Importa random para sortear os números:
import random;

for i in range(4):
    numero_sorteado = random.randint(0,10)
    user_escolha = input(f'Você tem {-i+4} tentativas: ')
    # Caso a escolha esteja correta:
    if numero_sorteado == user_escolha:
        print('Você acertou! Parabéns!')
        break
    # Caso esteja errada:
    else:
        print('\nInfelizmente você errou, tente novamente.')
        print(f'O número escolhido foi: {numero_sorteado}')
