import random

class jogador:

    # Coloco o construtor para criar o jogador e suas ações
    def __init__(self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, inimigo): # Crio um ataque simples sem defesa
        inimigo.vida -= self.ataque

    def atacar_defendido(self, inimigo): # Caso alguém defenda o ataque vira esse
        dano = self.ataque - inimigo.defesa
        if dano > 0:
            inimigo.vida -= dano

# Cria o bot com o range de valores igual do player mas de forma aleatória
def criar_bot(vida_bot=0, ataque_bot=0, defesa_bot=0):
    vida_bot = random.randint(1,10)
    ataque_bot = random.randint(1,5)
    defesa_bot = random.randint(1,4)
    return vida_bot, ataque_bot, defesa_bot

# Crio o jogador perguntando todos os stats
def criar_jogador():

    pontos = 15 # O jogador vai ter uma quantidade específica de pontos para gastar em todos os seus atributos

    while True: # Crio um loop que só acaba quando o jogador digita uma quantidade dentro da estipulada
        vida = int(input(f"Você tem {pontos} pontos para usar\nQual será sua vida ? (1-10)  "))
        if 1 <= vida <= 10:
            pontos -= vida
            break
        else:
            print("Valor inválido - digite novamente\n")
    while True:    
        ataque = int(input(f"Você tem {pontos} pontos para usar\nQual será seu ataque ? (1-5)  "))
        if 1 <= ataque <= 5 and pontos >= ataque: # Aqui rola um segundo teste para saber se o jogador tem pontos suficientes para gastar
            pontos -= ataque
            break
        else:
            print("Valor inválido - digite novamente\n")
    while True:
        defesa = int(input(f"Você tem {pontos} pontos para usar\nQual será sua defesa ? (0-5)  "))
        if 0 <= defesa <= 5 and pontos >= defesa:
            break
        else:
            print("Valor inválido - digite novamente\n")

    return vida, ataque, defesa

# Crio o modelo do jogo, o loop infinito até um dos dois morrerem
def jogo(player: object, bot:object):
    
    # Coloco um menu inicial para os dois saberem os stats de cada um e planejar suas ações
    print("Bem vindo ao combate !")
    print(f"Seus atributos: \n Dano: {player.ataque} \n Defesa: {player.defesa}")
    print(f"Atributos do seu adversário: \n Dano: {bot.ataque} \n Defesa: {bot.defesa}")
    print(f"Você - {'♡'*player.vida} x Bot - {'♡'*bot.vida}")

    while True:
        escolha_player = input("Qual será sua ação ? \n Atacar - Defender  ").lower().strip()
        escolha_bot = random.choice(['atacar', 'defender'])

        if player.vida > 0 and bot.vida > 0: # Verifica se os dois estão vivos
            # Verifico as três opções possíveis de ataque e defesa entre os dois, defesa e defesa não gera nada na vida
            if escolha_player == 'atacar' and escolha_bot == 'atacar':
                player.atacar(bot)
                bot.atacar(player)
            
            elif escolha_player == 'atacar' and escolha_bot == 'defender':
                player.atacar_defendido(bot)

            elif escolha_player == 'defender' and escolha_bot == 'atacar':
                bot.atacar_defendido(player)
        
        # Após a ação eu verifico novamente se estão vivos para acabar o jogo sem ter uma ação avulsa no final
        if player.vida <= 0 or bot.vida <= 0:
            if player.vida > bot.vida:
                print(f"Você venceu !!!\nFicou com {player.vida} de vida.")
            
            elif bot.vida > player.vida:
                print("Você perdeu :(")
            
            else:
                print("Empatou :O")
            
            break

        # Caso ninguém tenha morrido, eu mostro as ações e a vida novamente para saberem o que aconteceu com a vida e como o adversário está jogando    
        print(f"Você escolheu {escolha_player} e o seu adversário escolheu {escolha_bot}")
        print()
        print(f"Você - {'♡'*player.vida} x Bot - {'♡'*bot.vida}")


def main():

    vida_bot, ataque_bot, defesa_bot = criar_bot() 
    bot = jogador(vida_bot, ataque_bot, defesa_bot) # Crio o objeto bot com os stats do bot criado aleatóriamente
    
    vida, ataque, defesa = criar_jogador()
    player = jogador(vida, ataque, defesa) # Crio o objeto do meu player

    jogo(player, bot) # Que os jogos comecem...

main()
