import pygame

# Inicializa o Pygame
pygame.init()

# Cria uma janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))

# Define o título da janela
titulo = "Meu Jogo"
pygame.display.set_caption(titulo)

# Cria uma fonte
fonte = pygame.font.SysFont("Arial", 30)

# Define o texto a ser escrito
texto = "Olá, mundo!"

# Renderiza o texto
texto_renderizado = fonte.render(texto, True, (0, 0, 0))

# Loop principal
while True:
    # Preenche a janela com uma cor branca
    janela.fill((255, 255, 255))

    # Desenha o texto na janela
    janela.blit(texto_renderizado, (100, 100))

    # Atualiza a janela
    pygame.display.update()

    # Verifica eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()