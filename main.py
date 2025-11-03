import pygame
import os
<<<<<<< HEAD
import time
from sys import exit
from colisoes_combate import ColisoesCombate
from personagens import Vegeta, Goku, Picollo, Bardock, TeenGohan
from ia_player import SimpleAI


def mostrar_vencedor(tela, vencedor, duracao_ms=3000):
    """Mostra o vencedor na tela por `duracao_ms` milissegundos sem travar a janela."""
    fonte = pygame.font.Font(None, 100)
    texto = fonte.render(f"{vencedor.nome} Venceu!", True, (255, 215, 0))
    texto_rect = texto.get_rect(center=(tela.get_width() // 2, tela.get_height() // 2))

    inicio = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    while pygame.time.get_ticks() - inicio < duracao_ms:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # opcional: escurecer fundo e desenhar texto
        overlay = pygame.Surface(tela.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        tela.blit(overlay, (0, 0))
        tela.blit(texto, texto_rect)
        pygame.display.flip()
        clock.tick(60)


# ================= SELEÇÃO DE FASE =================
def selecionar_fase():
    pygame.init()
    largura, altura = 1080, 720
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Seleção de Fase")

    base_path = os.path.dirname(__file__)
    fases = {
        "Torneio": os.path.join(base_path, "background", "tornei gif", "frame-01.gif"),
        "Planeta Namek": os.path.join(base_path, "background", "background-2", "frame-001.gif"),
    }

    imagens = {
        nome: pygame.transform.scale(pygame.image.load(caminho), (400, 225))
        for nome, caminho in fases.items()
    }

    rects = {
        "Torneio": imagens["Torneio"].get_rect(center=(largura // 3, altura // 2)),
        "Planeta Namek": imagens["Planeta Namek"].get_rect(center=(2 * largura // 3, altura // 2)),
    }

    fonte = pygame.font.Font(None, 60)
    texto = fonte.render("Selecione a Fase", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(largura // 2, 100))

    relogio = pygame.time.Clock()

    while True:
        tela.fill((0, 0, 0))
        tela.blit(texto, texto_rect)

        for nome, img in imagens.items():
            tela.blit(img, rects[nome])
            nome_texto = fonte.render(nome, True, (255, 255, 0))
            tela.blit(
                nome_texto,
                (rects[nome].centerx - nome_texto.get_width() // 2, rects[nome].bottom + 20),
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for nome, rect in rects.items():
                    if rect.collidepoint(event.pos):
                        return nome  # Retorna o nome da fase escolhida

        pygame.display.flip()
        relogio.tick(60)


# ================= SELEÇÃO DE PERSONAGENS =================
=======
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

>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
def selecionar_personagens():
    pygame.init()
    largura, altura = 1080, 720
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Seleção de Personagens")

<<<<<<< HEAD
    base_path = os.path.dirname(__file__)
    imagens = {
        "Goku": os.path.join(base_path, "Sprites", "Goku_ssj2", "GokuMenu.png"),
        "Vegeta": os.path.join(base_path, "Sprites", "vegeta_ssj2", "VegetaMenu.png"),
        "Picollo": os.path.join(base_path, "Sprites", "Picollo", "PicolloMenu.png"),
        "Bardock": os.path.join(base_path, "Sprites", "Bardock", "BardockMenu.png"),
        "Teen Gohan": os.path.join(base_path, "Sprites", "Teen Gohan", "TeenGohanMenu.png"),
    }

    imgs = {nome: pygame.image.load(caminho) for nome, caminho in imagens.items()}
    largura_imagem, altura_imagem = largura // 6, altura // 3
    imgs = {n: pygame.transform.scale(i, (largura_imagem, altura_imagem)) for n, i in imgs.items()}

    rects = {n: imgs[n].get_rect(center=(i * largura // 6, altura // 2)) for i, n in enumerate(imgs, 1)}
=======
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
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391

    fonte = pygame.font.Font(None, 50)
    instrucoes_texto = fonte.render("Player 1: Clique para escolher!", True, (255, 255, 255))
    instrucoes_rect = instrucoes_texto.get_rect(center=(largura // 2, 100))

<<<<<<< HEAD
    player1 = player2 = None
    player_atual = 1
=======
    player1_escolhido = None
    player2_escolhido = None
    player_atual = 1

>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
    relogio = pygame.time.Clock()

    while True:
        tela.fill((0, 0, 0))
        tela.blit(instrucoes_texto, instrucoes_rect)
<<<<<<< HEAD
        for nome, img in imgs.items():
            tela.blit(img, rects[nome])
=======
        tela.blit(goku_img, goku_rect)
        tela.blit(vegeta_img, vegeta_rect)
        tela.blit(picollo_img, picollo_rect)

>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
<<<<<<< HEAD
                for nome, rect in rects.items():
                    if rect.collidepoint(event.pos):
                        if player_atual == 1:
                            player1 = criar_personagem(nome, 350, 550, controle="wasd")
                            player_atual = 2
                            instrucoes_texto = fonte.render("Player 2: Clique para escolher!", True, (255, 255, 255))
                        elif player_atual == 2:
                            player2 = criar_personagem(nome, 700, 550, controle="setas", is_facing_right=False)

        if player1 and player2:
            return player1, player2
=======
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
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391

        pygame.display.flip()
        relogio.tick(60)

<<<<<<< HEAD

# ================= CRIAÇÃO DOS PERSONAGENS =================
def criar_personagem(nome, x, y, controle="wasd", is_facing_right=True):
    """Cria o personagem e adiciona o retrato correspondente."""
    if nome == "Goku":
        personagem = Goku(x, y, controle, is_facing_right)
        retrato_path = os.path.join("Sprites", "Goku_ssj2", "GokuMenu.png")
    elif nome == "Vegeta":
        personagem = Vegeta(x, y, controle, is_facing_right)
        retrato_path = os.path.join("Sprites", "vegeta_ssj2", "VegetaMenu.png")
    elif nome == "Picollo":
        personagem = Picollo(x, y, controle, is_facing_right)
        retrato_path = os.path.join("Sprites", "Picollo", "PicolloMenu.png")
    elif nome == "Bardock":
        personagem = Bardock(x, y, controle, is_facing_right)
        retrato_path = os.path.join("Sprites", "Bardock", "BardockMenu.png")
    elif nome == "Teen Gohan":
        personagem = TeenGohan(x, y, controle, is_facing_right)
        retrato_path = os.path.join("Sprites", "Teen Gohan", "TeenGohanMenu.png")
    else:
        raise ValueError(f"Personagem desconhecido: {nome}")

    # === Carrega o retrato para a barra de vida ===
    base_path = os.path.dirname(__file__)
    retrato_absoluto = os.path.join(base_path, retrato_path)
    if os.path.exists(retrato_absoluto):
        personagem.retrato = pygame.image.load(retrato_absoluto)
    else:
        print(f"[AVISO] Retrato não encontrado: {retrato_absoluto}")
        personagem.retrato = None

    return personagem


# ================= INÍCIO DO JOGO =================
def start_game(player1, player2, fase_escolhida, use_ai=False):
=======
def start_game(player1, player2):
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
    pygame.init()
    largura, altura = 1080, 720
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Dragon Ball Z")
<<<<<<< HEAD

    base_path = os.path.dirname(__file__)

    # === Música da fase ===
    trilhas = {
        "Torneio": os.path.join(base_path, "SoundTrack", "Tournament_Theme.mp3"),
        "Planeta Namek": os.path.join(base_path, "SoundTrack", "Namek_Battle.mp3"),
    }
    if fase_escolhida in trilhas and os.path.exists(trilhas[fase_escolhida]):
        pygame.mixer.music.load(trilhas[fase_escolhida])
        pygame.mixer.music.play(-1)

    # === Fundo ===
    if fase_escolhida == "Torneio":
        caminho_base = os.path.join(base_path, "background", "tornei gif")
        frames = [pygame.transform.scale(pygame.image.load(os.path.join(caminho_base, f"frame-{str(i).zfill(2)}.gif")),
                                         (largura, altura)) for i in range(1, 16)]
    else:
        caminho_base = os.path.join(base_path, "background", "background-2")
        frames = []
        for i in range(1, 101):
            frame_path = os.path.join(caminho_base, f"frame-{str(i).zfill(3)}.gif")
            if os.path.exists(frame_path):
                frames.append(pygame.transform.scale(pygame.image.load(frame_path), (largura, altura)))
        if not frames:
            frames = [pygame.Surface((largura, altura))]
=======
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
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391

    sistema_colisao = ColisoesCombate(largura, altura)
    todas_sprites = pygame.sprite.Group(player1, player2)
    clock = pygame.time.Clock()
    frame_atual = 0
    ultimo_frame = pygame.time.get_ticks()
    tempo_ki = pygame.time.get_ticks()

<<<<<<< HEAD
    player1.vida = player1.vida_max
    player2.vida = player2.vida_max

    ia = None
    if use_ai:
        ia = SimpleAI(player2, player1)
        # marca controle 'ia' para o multiplicador de dano (se você usou isso em colisões)
        player2.controle = "ia"

    jogo_ativo = True
    vencedor = None
    tempo_vitoria = None

    while jogo_ativo:
        agora = pygame.time.get_ticks()

        # --- Eventos (usamos KEYDOWN para ataques para que pressionar dispare 1 golpe) ---
=======
    # Reinicia a vida dos jogadores
    player1.vida = player1.vida_max
    player2.vida = player2.vida_max

    while True:  # Loop principal do jogo
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

<<<<<<< HEAD
            if event.type == pygame.KEYDOWN:
                # Player1 ataques por KEYDOWN (aperta uma vez = golpe)
                if event.key == pygame.K_j:
                    sistema_colisao.atacar_normal(player1, player2, tela)
                if event.key == pygame.K_k:
                    sistema_colisao.atacar_especial(player1, player2, tela)

                # Player2 (modo 2P) ataques por KEYDOWN
                if not ia:
                    if event.key == pygame.K_KP0:
                        sistema_colisao.atacar_normal(player2, player1, tela)
                    if event.key == pygame.K_KP1:
                        sistema_colisoes = None
                        sistema_colisao.atacar_especial(player2, player1, tela)

        # --- Atualiza frame do background animado ---
=======
        agora = pygame.time.get_ticks()
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
        if agora - ultimo_frame > 100:
            frame_atual = (frame_atual + 1) % len(frames)
            ultimo_frame = agora

        keys = pygame.key.get_pressed()
<<<<<<< HEAD
        tempo_atual = agora

        # --- Atualizações dos personagens ---
        player1.update(keys, tempo_atual, tela)

        if ia:
            ia.update(tempo_atual)
            # ia.personagem é o próprio player2 — não reatribua player2 a outra instância
            # se sua IA usa player2 como personagem, não precisa sobrescrever image/rect aqui
            player2.image = ia.personagem.image
            player2.rect = ia.personagem.rect
            # quando ia.should_attack for True, ela já sinaliza o ataque (pode acontecer só um frame)
            if ia.should_attack:
                if ia.attack_type == "ataque":
                    sistema_colisoes = None
                    sistema_colisao.atacar_normal(player2, player1, tela)
                elif ia.attack_type == "especial":
                    sistema_colisao.atacar_especial(player2, player1, tela)
        else:
            player2.update(keys, tempo_atual, tela)

        # --- Atualiza projéteis e checa colisões todo frame (garante que especial/dano apareçam na HUD) ---
        sistema_colisao.atualizar_projeteis()
        # verificar colisões para ambos jogadores (proj.owner filtra internamente)
        sistema_colisao.aplicar_dano(player1, player2, tela)
        sistema_colisao.aplicar_dano(player2, player1, tela)

        # --- Ki regen ---
=======
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

>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
        if agora - tempo_ki > 5000:
            sistema_colisao.recuperar_ki([player1, player2])
            tempo_ki = agora

        sistema_colisao.limitar_movimento(player1)
        sistema_colisao.limitar_movimento(player2)

<<<<<<< HEAD
        # --- Renderização ---
=======
        # Verifica se algum jogador perdeu
        if player1.vida <= 0 or player2.vida <= 0:
            vencedor = player1 if player1.vida > 0 else player2
            mostrar_vencedor(tela, vencedor)  # Mostra o vencedor na tela
            return True  # Indica que o jogo terminou e pode ser reiniciado

        # Ordem de desenho:
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
        tela.blit(frames[frame_atual], (0, 0))
        sistema_colisao.atualizar_barras(tela, [player1, player2])
        todas_sprites.draw(tela)
        player1.atualizar_projetil(tela)
        player2.atualizar_projetil(tela)
<<<<<<< HEAD
        pygame.display.flip()
        clock.tick(60)

        # --- Verifica vitória (após desenhar pra garantir HUD atualizada) ---
        if player1.vida <= 0 or player2.vida <= 0:
            if vencedor is None:
                vencedor = player1 if player1.vida > 0 else player2
                tempo_vitoria = agora
                # pare música e prepare tela de vitória
                pygame.mixer.music.stop()
            else:
                # aguarda 3s de exibição e volta
                if agora - tempo_vitoria >= 300:
                    jogo_ativo = False

    # mostra vencedor com loop responsivo (evita travamento)
    mostrar_vencedor(tela, vencedor)
    return True


# ================= EXECUÇÃO =================
def main():
    while True:
        p1, p2 = selecionar_personagens()
        fase = selecionar_fase()
        jogo_terminado = start_game(p1, p2, fase)
        if jogo_terminado:
            print("Reiniciando o jogo...")
            time.sleep(1)


if __name__ == "__main__":
    p1, p2 = selecionar_personagens()
    fase = selecionar_fase()
    start_game(p1, p2, fase, use_ai=True)
=======

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
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
