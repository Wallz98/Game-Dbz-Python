<<<<<<< HEAD
import pygame
import sys
import time
import os
from button import Button
from main import start_game, selecionar_personagens, selecionar_fase

pygame.init()

# ===============================
# CONFIGURAÇÕES INICIAIS
# ===============================
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Fundo do menu
BG_PATH = os.path.join(BASE_DIR, 'background', 'menu_asset.jpg')
BG = pygame.image.load(BG_PATH)
BG = pygame.transform.scale(BG, (1280, 720))

# Música de fundo
MUSIC_PATH = os.path.join(
    BASE_DIR,
    'SoundTrack',
    'Dragon Ball Z - CHA-LA HEAD-CHA-LA [8-Bit] - ころん-COLON 8BIT MUSIC-.mp3'
)
pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.play(-1)


def get_font(size):
    """Retorna a fonte personalizada."""
    FONT_PATH = os.path.join(BASE_DIR, 'background', 'font.ttf')
    return pygame.font.Font(FONT_PATH, size)


def show_winner(vencedor):
    """Mostra o vencedor por alguns segundos antes de retornar ao menu."""
    time.sleep(3)
    main_menu()


# ===============================
# SUBMENU DE MODO DE JOGO
# ===============================
def play_menu():
    """Tela que permite escolher 1 Player (IA) ou 2 Players."""
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        TITLE_TEXT = get_font(90).render("SELECT MODE", True, "#b68f40")
        TITLE_RECT = TITLE_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        # Botões
        ONE_PLAYER_BUTTON = Button(
            image=pygame.image.load(os.path.join(BASE_DIR, 'background', 'Play Rect.png')),
            pos=(640, 250),
            text_input="1 PLAYER", font=get_font(65),
            base_color="#d7fcd4", hovering_color="White"
        )
        TWO_PLAYER_BUTTON = Button(
            image=pygame.image.load(os.path.join(BASE_DIR, 'background', 'Play Rect.png')),
            pos=(640, 380),
            text_input="2 PLAYERS", font=get_font(65),
            base_color="#d7fcd4", hovering_color="White"
        )
        BACK_BUTTON = Button(
            image=pygame.image.load(os.path.join(BASE_DIR, 'background', 'Quit Rect.png')),
            pos=(640, 530),
            text_input="BACK", font=get_font(65),
            base_color="#d7fcd4", hovering_color="White"
        )

        for button in [ONE_PLAYER_BUTTON, TWO_PLAYER_BUTTON, BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # ====== 1 PLAYER (VS IA) ======
                if ONE_PLAYER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    player1, player2 = selecionar_personagens()
                    fase = selecionar_fase()  # ✅ Seleção de fase
                    vencedor = start_game(player1, player2, fase, use_ai=True)
                    show_winner(vencedor)

                # ====== 2 PLAYERS ======
                if TWO_PLAYER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    player1, player2 = selecionar_personagens()
                    fase = selecionar_fase()  # ✅ Seleção de fase
                    vencedor = start_game(player1, player2, fase, use_ai=False)
                    show_winner(vencedor)

                # ====== VOLTAR ======
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


# ===============================
# MENU PRINCIPAL
# ===============================
def main_menu():
    """Tela principal do menu."""

    # === Garante que a música de fundo do menu toque ===
    MUSIC_PATH = os.path.join(BASE_DIR, 'SoundTrack',
                              'Dragon Ball Z - CHA-LA HEAD-CHA-LA [8-Bit] - ころん-COLON 8BIT MUSIC-.mp3')
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(MUSIC_PATH)
        pygame.mixer.music.play(-1)

    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)


        PLAY_BUTTON = Button(
            image=pygame.image.load(os.path.join(BASE_DIR, 'background', 'Play Rect.png')),
            pos=(640, 250),
            text_input="PLAY", font=get_font(75),
            base_color="#d7fcd4", hovering_color="White"
        )
        OPTIONS_BUTTON = Button(
            image=pygame.image.load(os.path.join(BASE_DIR, 'background', 'Options Rect.png')),
            pos=(640, 400),
            text_input="OPTIONS", font=get_font(75),
            base_color="#d7fcd4", hovering_color="White"
        )
        QUIT_BUTTON = Button(
            image=pygame.image.load(os.path.join(BASE_DIR, 'background', 'Quit Rect.png')),
            pos=(640, 550),
            text_input="QUIT", font=get_font(75),
            base_color="#d7fcd4", hovering_color="White"
        )

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_menu()  # ✅ Vai para o submenu
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("⚙️ Opções ainda não implementadas.")
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


# ===============================
# EXECUÇÃO DIRETA
# ===============================
if __name__ == "__main__":
    main_menu()
=======
import pygame
import sys
import time
import os
from button import Button
from main import start_game, selecionar_personagens

pygame.init()

# Configuração da tela
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# Define o diretório base do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Carrega o fundo do menu
BG_PATH = os.path.join(BASE_DIR, 'background', 'menu_asset.jpg')
BG = pygame.image.load(BG_PATH)
BG = pygame.transform.scale(BG, (1280, 720))

# Carrega e toca a música de fundo em loop
MUSIC_PATH = os.path.join(BASE_DIR,  'SoundTrack',
                          'Dragon Ball Z - CHA-LA HEAD-CHA-LA [8-Bit] - ころん-COLON 8BIT MUSIC-.mp3')
pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.play(-1)


def get_font(size):
    """Retorna a fonte desejada."""
    FONT_PATH = os.path.join(BASE_DIR, 'background', 'font.ttf')
    return pygame.font.Font(FONT_PATH, size)


def show_winner(vencedor):
    """Exibe o vencedor na tela por 3 segundos e volta ao menu."""
    SCREEN.fill((0, 0, 0))  # Preenche a tela com preto
    font = pygame.font.Font(None, 100)
    winner_text = font.render(f"{vencedor} WINS!", True, (255, 255, 255))
    SCREEN.blit(winner_text, (640 - winner_text.get_width() //
                2, 360 - winner_text.get_height() // 2))
    pygame.display.update()

    time.sleep(3)  # Aguarda 3 segundos
    main_menu()  # Retorna ao menu principal


def main_menu():
    """Tela principal do menu."""
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        # Botões
        PLAY_BUTTON = Button(
            image=pygame.image.load(os.path.join(BASE_DIR, 'background', 'Play Rect.png')), pos=(640, 250),
            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White"
        )
        OPTIONS_BUTTON = Button(
            image=pygame.image.load(os.path.join(BASE_DIR, 'background', 'Options Rect.png')), pos=(640, 400),
            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White"
        )
        QUIT_BUTTON = Button(
            image=pygame.image.load(os.path.join(BASE_DIR, 'background', 'Quit Rect.png')), pos=(640, 550),
            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White"
        )

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    while True:
                        player1, player2 = selecionar_personagens()
                        vencedor = start_game(
                            player1, player2)  # Inicia o jogo
                        show_winner(vencedor)  # Exibe o vencedor

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
