import pygame
import time
import random

# Inicializa o pygame
pygame.init()

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Definindo as dimensões da janela
largura_janela = 600
altura_janela = 400

# Inicializa a janela do jogo
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Jogo da Cobrinha')

# Definindo o relógio do jogo
relogio = pygame.time.Clock()

# Definindo o tamanho do bloco da cobrinha e a velocidade do jogo
tamanho_bloco = 10
velocidade_jogo = 15

# Definindo a fonte do jogo
fonte = pygame.font.SysFont("bahnschrift", 25)

def mensagem(msg, cor):
    mesg = fonte.render(msg, True, cor)
    janela.blit(mesg, [largura_janela / 6, altura_janela / 3])

def mostrar_pontuacao(pontos):
    valor = fonte.render("Pontos: " + str(pontos), True, branco)
    janela.blit(valor, [0, 0])

def jogo():
    fim_jogo = False
    fim_de_jogo = False

    x1 = largura_janela / 2
    y1 = altura_janela / 2

    x1_mudanca = 0
    y1_mudanca = 0

    corpo_cobrinha = []
    comprimento_cobrinha = 1

    # Inicializa a pontuação
    pontuacao = 0

    comida_x = round(random.randrange(0, largura_janela - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_janela - tamanho_bloco) / 10.0) * 10.0

    while not fim_jogo:

        while fim_de_jogo:
            janela.fill(azul)
            mensagem("Você perdeu! Pressione Q-Quit ou C-Continue", vermelho)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        fim_de_jogo = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        if x1 >= largura_janela or x1 < 0 or y1 >= altura_janela or y1 < 0:
            fim_de_jogo = True
        x1 += x1_mudanca
        y1 += y1_mudanca
        janela.fill(preto)
        pygame.draw.rect(janela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca_cobrinha = []
        cabeca_cobrinha.append(x1)
        cabeca_cobrinha.append(y1)
        corpo_cobrinha.append(cabeca_cobrinha)
        if len(corpo_cobrinha) > comprimento_cobrinha:
            del corpo_cobrinha[0]

        for bloco in corpo_cobrinha[:-1]:
            if bloco == cabeca_cobrinha:
                fim_de_jogo = True

        for bloco in corpo_cobrinha:
            pygame.draw.rect(janela, branco, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        # Exibe a pontuação
        mostrar_pontuacao(pontuacao)
        
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_janela - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_janela - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobrinha += 1
            # Atualiza a pontuação quando a comida é comida
            pontuacao += 10

        relogio.tick(velocidade_jogo)

    pygame.quit()
    quit()

jogo()
