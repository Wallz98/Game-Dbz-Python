import pygame
from colisoes_combate import ColisoesCombate
from personagens import Vegeta, Goku
from sys import exit
# import menu  # Importa o arquivo menu.py

def selecionar_personagens():
    pygame.init()
    largura, altura = 1080, 720
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Seleção de Personagens")

    # Carregar imagens dos personagens
    goku_img = pygame.image.load(
        r"C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\Sprites\Goku_ssj2\GokuMenu.png")
    vegeta_img = pygame.image.load(
        r"C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\Sprites\vegeta_ssj2\VegetaMenu.png")

    # Escalar imagens proporcionalmente
    largura_imagem = largura // 6  # 1/6 da largura da tela
    altura_imagem = altura // 3    # 1/3 da altura da tela
    goku_img = pygame.transform.scale(
        goku_img, (largura_imagem, altura_imagem))
    vegeta_img = pygame.transform.scale(
        vegeta_img, (largura_imagem, altura_imagem))

    # Posições das imagens
    goku_rect = goku_img.get_rect(center=(300, 360))
    vegeta_rect = vegeta_img.get_rect(center=(780, 360))

    fonte = pygame.font.Font(None, 50)
    instrucoes_texto = fonte.render(
        "Player 1: Clique para escolher!", True, (255, 255, 255))
    instrucoes_rect = instrucoes_texto.get_rect(center=(largura // 2, 100))

    player1_escolhido = None
    player2_escolhido = None
    player_atual = 1

    relogio = pygame.time.Clock()

    while True:
        tela.fill((0, 0, 0))

        # Exibir textos e imagens
        tela.blit(instrucoes_texto, instrucoes_rect)
        tela.blit(goku_img, goku_rect)
        tela.blit(vegeta_img, vegeta_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if goku_rect.collidepoint(event.pos):
                    if player_atual == 1:
                        player1_escolhido = Goku(350, 550, controle='wasd')
                        player_atual = 2
                        instrucoes_texto = fonte.render(
                            "Player 2: Clique para escolher!", True, (255, 255, 255))
                    elif player_atual == 2:
                        player2_escolhido = Goku(
                            700, 550, controle='setas', is_facing_right=False)
                elif vegeta_rect.collidepoint(event.pos):
                    if player_atual == 1:
                        player1_escolhido = Vegeta(350, 550, controle='wasd')
                        player_atual = 2
                        instrucoes_texto = fonte.render(
                            "Player 2: Clique para escolher!", True, (255, 255, 255))
                    elif player_atual == 2:
                        player2_escolhido = Vegeta(
                            700, 550, controle='setas', is_facing_right=False)

        if player1_escolhido and player2_escolhido:
            return player1_escolhido, player2_escolhido

        pygame.display.flip()
        relogio.tick(60)


def start_game(player1, player2):
    pygame.init()

    largura, altura = 1080, 720
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Sprites")

    caminho_base = r"C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\background\tornei gif\\"

    def carregar_frames(caminho_base):
        frames = []
        for i in range(1, 16):
            caminho_imagem = f"{caminho_base}frame-{str(i).zfill(2)}.gif"
            try:
                imagem = pygame.image.load(caminho_imagem)
                frames.append(imagem)
            except pygame.error as e:
                print(f"Erro ao carregar a imagem: {caminho_imagem}. Detalhes: {e}")
        return frames

    frames = carregar_frames(caminho_base)

    frame_atual = 0
    tempo_por_frame = 100
    ultimo_tempo = pygame.time.get_ticks()

    todas_as_sprites = pygame.sprite.Group(player1, player2)
    sistema_colisao = ColisoesCombate(largura, altura)

    relogio = pygame.time.Clock()
    tempo_recuperacao_ki = pygame.time.get_ticks()

    while True:
        relogio.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        agora = pygame.time.get_ticks()
        if agora - ultimo_tempo >= tempo_por_frame:
            ultimo_tempo = agora
            frame_atual = (frame_atual + 1) % len(frames)

        if agora - tempo_recuperacao_ki >= 5000:
            sistema_colisao.recuperar_ki([player1, player2])
            tempo_recuperacao_ki = agora

        tela.fill((0, 0, 0))
        tela.blit(pygame.transform.scale(frames[frame_atual], (largura, altura)), (0, 0))

        keys = pygame.key.get_pressed()
        tempo_decorrido = pygame.time.get_ticks()
        player1.update(keys, tempo_decorrido)
        player2.update(keys, tempo_decorrido)

        if keys[pygame.K_j]:
            sistema_colisao.atacar_normal(player1, player2, tela)
        if keys[pygame.K_k]:
            sistema_colisao.atacar_especial(player1, player2, tela)
        if keys[pygame.K_KP0]:
            sistema_colisao.atacar_normal(player2, player1, tela)
        if keys[pygame.K_KP1]:
            sistema_colisao.atacar_especial(player2, player1, tela)

        sistema_colisao.limitar_movimento(player1)
        sistema_colisao.limitar_movimento(player2)
        sistema_colisao.atualizar_barras(tela, [player1, player2])

        todas_as_sprites.draw(tela)
        pygame.display.flip()


if __name__ == "__main__":
    player1, player2 = selecionar_personagens()
    start_game(player1, player2)
