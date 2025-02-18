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
