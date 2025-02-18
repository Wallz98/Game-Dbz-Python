import pygame
import os
from colisoes_combate import ColisoesCombate
from personagens import Vegeta, Goku, Picollo
from sys import exit
import time

def mostrar_vencedor(tela, vencedor):
    fonte = pygame.font.Font(None, 100)
    texto = fonte.render(f"{vencedor.nome} Venceu!", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(tela.get_width() // 2, tela.get_height() // 2))

    tela.fill((0, 0, 0))
    tela.blit(texto, texto_rect)
    pygame.display.flip()
    time.sleep(3)  # Exibe o vencedor por 3 segundos

def selecionar_personagens():
    pygame.init()
    largura, altura = 1080, 720
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Seleção de Personagens")

    # Caminhos relativos para as imagens
    base_path = os.path.dirname(__file__)
    goku_img_path = os.path.join(base_path, "Sprites", "Goku_ssj2", "GokuMenu.png")
    vegeta_img_path = os.path.join(base_path, "Sprites", "vegeta_ssj2", "VegetaMenu.png")
    picollo_img_path = os.path.join(base_path, "Sprites", "Picollo", "PicolloMenu.png")

    goku_img = pygame.image.load(goku_img_path)
    vegeta_img = pygame.image.load(vegeta_img_path)
    picollo_img = pygame.image.load(picollo_img_path)

    largura_imagem = largura // 6
    altura_imagem = altura // 3
    goku_img = pygame.transform.scale(goku_img, (largura_imagem, altura_imagem))
    vegeta_img = pygame.transform.scale(vegeta_img, (largura_imagem, altura_imagem))
    picollo_img =pygame.transform.scale(picollo_img,(largura_imagem, altura_imagem) )
    goku_rect = goku_img.get_rect(center=(300, 360))
    vegeta_rect = vegeta_img.get_rect(center=(780, 360))
    picollo_rect = picollo_img.get_rect(center=( 540, 360))

    fonte = pygame.font.Font(None, 50)
    instrucoes_texto = fonte.render("Player 1: Clique para escolher!", True, (255, 255, 255))
    instrucoes_rect = instrucoes_texto.get_rect(center=(largura // 2, 100))

    player1_escolhido = None
    player2_escolhido = None
    player_atual = 1

    relogio = pygame.time.Clock()

    while True:
        tela.fill((0, 0, 0))
        tela.blit(instrucoes_texto, instrucoes_rect)
        tela.blit(goku_img, goku_rect)
        tela.blit(vegeta_img, vegeta_rect)
        tela.blit(picollo_img, picollo_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if goku_rect.collidepoint(event.pos):
                    if player_atual == 1:
                        player1_escolhido = Goku(350, 550, controle='wasd')
                        player_atual = 2
                        instrucoes_texto = fonte.render("Player 2: Clique para escolher!", True, (255, 255, 255))
                    elif player_atual == 2:
                        player2_escolhido = Goku(700, 550, controle='setas', is_facing_right=False)
                elif vegeta_rect.collidepoint(event.pos):
                    if player_atual == 1:
                        player1_escolhido = Vegeta(350, 550, controle='wasd')
                        player_atual = 2
                        instrucoes_texto = fonte.render("Player 2: Clique para escolher!", True, (255, 255, 255))
                    elif player_atual == 2:
                        player2_escolhido = Vegeta(700, 550, controle='setas', is_facing_right=False)

                elif picollo_rect.collidepoint(event.pos):
                    if player_atual == 1:
                        player1_escolhido = Picollo(350, 550, controle='wasd')
                        player_atual = 2
                        instrucoes_texto = fonte.render("Player 2: Clique para escolher!", True, (255, 255, 255))
                    elif player_atual == 2:
                     player2_escolhido = Picollo(700, 550, controle='setas', is_facing_right=False)

        if player1_escolhido and player2_escolhido:
            return player1_escolhido, player2_escolhido

        pygame.display.flip()
        relogio.tick(60)

def start_game(player1, player2):
    pygame.init()
    largura, altura = 1080, 720
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Dragon Ball Z")
    # Caminho relativo para a música de fundo
    base_path = os.path.dirname(__file__)
    music_path = os.path.join(base_path,  "SoundTrack", "Dragon Ball Z OST - Battle Theme.mp3")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)

    # Caminho relativo para os frames do fundo animado
    caminho_base = os.path.join(base_path, "background", "tornei gif")
    frames = [pygame.transform.scale(
        pygame.image.load(os.path.join(caminho_base, f"frame-{str(i).zfill(2)}.gif")), (largura, altura)
    ) for i in range(1, 16)]

    try:
        kamehameha_img_path = os.path.join(base_path, "Sprites", "Goku_ssj2", "kamehameha.png")
        final_flash_img_path = os.path.join(base_path, "Sprites", "vegeta_ssj2", "vegeta_ssj2", "Final-Flash.png")
        kamehameha_img = pygame.image.load(kamehameha_img_path)
        final_flash_img = pygame.image.load(final_flash_img_path)
    except Exception as e:
        print(f"Erro ao carregar as imagens: {e}")
        kamehameha_img = None
        final_flash_img = None

    sistema_colisao = ColisoesCombate(largura, altura)
    todas_sprites = pygame.sprite.Group(player1, player2)
    clock = pygame.time.Clock()
    frame_atual = 0
    ultimo_frame = pygame.time.get_ticks()
    tempo_ki = pygame.time.get_ticks()

    # Reinicia a vida dos jogadores
    player1.vida = player1.vida_max
    player2.vida = player2.vida_max

    while True:  # Loop principal do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        agora = pygame.time.get_ticks()
        if agora - ultimo_frame > 100:
            frame_atual = (frame_atual + 1) % len(frames)
            ultimo_frame = agora

        keys = pygame.key.get_pressed()
        tempo_atual = pygame.time.get_ticks()

        # Atualiza o estado dos personagens
        player1.update(keys, tempo_atual, tela)
        player2.update(keys, tempo_atual, tela)

        # Processa os ataques (normal e especial)
        if keys[pygame.K_j]:  # Ataque normal de Goku
            sistema_colisao.atacar_normal(player1, player2, tela)
        if keys[pygame.K_KP0]:  # Ataque normal de Vegeta
            sistema_colisao.atacar_normal(player2, player1, tela)
        if keys[pygame.K_k]:   # Ataque especial de Goku
            sistema_colisao.atacar_especial(player1, player2, tela)
        if keys[pygame.K_KP1]: # Ataque especial de Vegeta
            sistema_colisao.atacar_especial(player2, player1, tela)

        if agora - tempo_ki > 5000:
            sistema_colisao.recuperar_ki([player1, player2])
            tempo_ki = agora

        sistema_colisao.limitar_movimento(player1)
        sistema_colisao.limitar_movimento(player2)

        # Verifica se algum jogador perdeu
        if player1.vida <= 0 or player2.vida <= 0:
            vencedor = player1 if player1.vida > 0 else player2
            mostrar_vencedor(tela, vencedor)  # Mostra o vencedor na tela
            return True  # Indica que o jogo terminou e pode ser reiniciado

        # Ordem de desenho:
        tela.blit(frames[frame_atual], (0, 0))
        sistema_colisao.atualizar_barras(tela, [player1, player2])
        todas_sprites.draw(tela)
        player1.atualizar_projetil(tela)
        player2.atualizar_projetil(tela)

        pygame.display.flip()
        clock.tick(60)

def main():
    while True:
        p1, p2 = selecionar_personagens()
        jogo_terminado = start_game(p1, p2)  # Inicia o jogo e verifica se terminou
        if jogo_terminado:
            print("Reiniciando o jogo...")
            time.sleep(2)  # Pausa de 2 segundos antes de reiniciar

if __name__ == "__main__":
    main()
