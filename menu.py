import pygame
import sys
from button import Button
from teste3 import start_game, selecionar_personagens

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load(r"C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\background\menu_asset.jpg")
BG = pygame.transform.scale(BG, (1280, 720))

def get_font(size):
    return pygame.font.Font(r"C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\background\font.ttf", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(r"C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\background\Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(r"C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\background\Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(r'C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\background\Quit Rect.png'), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

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
                    player1, player2 = selecionar_personagens()
                    start_game(player1, player2)
                    main_menu()  # Voltar ao menu principal após o jogo
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
