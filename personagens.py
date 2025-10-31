import os
import pygame
from pygame.locals import *
from personagem import Person
# Função para carregar imagens de uma pasta

def carregar_sprites(pasta, tamanho):
    sprites = []
    # Ordena para garantir a sequência correta
    for arquivo in sorted(os.listdir(pasta)):
        if arquivo.endswith('.png'):
            caminho_completo = os.path.join(pasta, arquivo)
            imagem = pygame.image.load(caminho_completo).convert_alpha()
            imagem_redimensionada = pygame.transform.scale(imagem, tamanho)
            sprites.append(imagem_redimensionada)
    return sprites


# Obtém o caminho base do jogo
game_base_path = os.path.dirname(os.path.abspath(__file__))

class Vegeta(Person):
    def __init__(self, x, y, controle='setas', is_facing_right=True):
        super().__init__(x, y, "Vegeta", 1, 12, 150, 100, controle, is_facing_right)
        tamanho_desejado = (100, 100)
        base_path = os.path.join(
            game_base_path, 'Sprites', 'vegeta_ssj2', 'vegeta_ssj2')
        self.sprites_andar = carregar_sprites(os.path.join(
            base_path, 'Movimentacao'), tamanho_desejado)
        self.sprites_voar = carregar_sprites(
            os.path.join(base_path, 'Voando'), tamanho_desejado)
        self.sprites_pousar = carregar_sprites(
            os.path.join(base_path, 'pousando'), tamanho_desejado)
        self.sprites_ataque = carregar_sprites(
            os.path.join(base_path, 'atacando'), tamanho_desejado)
        self.sprites_especial = carregar_sprites(
            os.path.join(base_path, 'especial'), tamanho_desejado)
        self.sprites_vitoria = carregar_sprites(
            os.path.join(base_path, 'vitoria'), tamanho_desejado)
        self.normal = carregar_sprites(os.path.join(
            base_path, 'normal'), tamanho_desejado)

        self.projetil_img = pygame.image.load(os.path.join(
            base_path, 'Final-Flash.png')).convert_alpha()
        self.projetil_img = pygame.transform.scale(self.projetil_img, (int(self.projetil_img.get_width() * 0.5),
                                                                       int(self.projetil_img.get_height() * 0.5)))

# Classe Goku


class Goku(Person):
    def __init__(self, x, y, controle='wasd', is_facing_right=True):
        super().__init__(x, y, "Goku", 1, 12, 150, 100, controle, is_facing_right)
        tamanho_desejado = (100, 100)
        base_path = os.path.join(game_base_path, 'Sprites', 'Goku_ssj2')
        self.sprites_andar = carregar_sprites(
            os.path.join(base_path, 'andando'), tamanho_desejado)
        self.sprites_voar = carregar_sprites(
            os.path.join(base_path, 'voando'), tamanho_desejado)
        self.sprites_pousar = carregar_sprites(
            os.path.join(base_path, 'pousando'), tamanho_desejado)
        self.sprites_ataque = carregar_sprites(
            os.path.join(base_path, 'atacando'), tamanho_desejado)
        self.sprites_especial = carregar_sprites(
            os.path.join(base_path, 'especial'), tamanho_desejado)
        self.sprites_vitoria = carregar_sprites(
            os.path.join(base_path, 'vitoria'), tamanho_desejado)
        self.normal = carregar_sprites(os.path.join(
            base_path, 'normal'), tamanho_desejado)
        self.projetil_img = pygame.image.load(os.path.join(
            base_path, 'kamehameha.png')).convert_alpha()
        self.projetil_img = pygame.transform.scale(self.projetil_img, (int(self.projetil_img.get_width() * 0.5),
                                                                       int(self.projetil_img.get_height() * 0.5)))
        self.tempo_ataque_duracao = 800


class Picollo(Person):
    def __init__(self, x, y, controle='setas', is_facing_right=True):
        super().__init__(x, y, "Picollo", 1, 12, 150, 100, controle, is_facing_right)
        tamanho_desejado = (90, 90)
        base_path = os.path.join(game_base_path, 'Sprites', 'Picollo')
        self.sprites_andar = carregar_sprites(os.path.join(
            base_path, 'movimentacao'), tamanho_desejado)
        self.sprites_voar = carregar_sprites(
            os.path.join(base_path, 'voando'), tamanho_desejado)
        self.sprites_pousar = carregar_sprites(
            os.path.join(base_path, 'pousando'), tamanho_desejado)
        self.sprites_ataque = carregar_sprites(
            os.path.join(base_path, 'atacando'), tamanho_desejado)
        self.sprites_especial = carregar_sprites(
            os.path.join(base_path, 'especial'), tamanho_desejado)
        self.sprites_vitoria = carregar_sprites(
            os.path.join(base_path, 'vitoria'), tamanho_desejado)
        self.normal = carregar_sprites(os.path.join(
            base_path, 'normal'), tamanho_desejado)

        # Carregar o projétil e reduzir seu tamanho pela metade
        self.projetil_img = pygame.image.load(os.path.join(
            base_path, 'makankosapo.png')).convert_alpha()
        self.projetil_img = pygame.transform.scale(self.projetil_img, (int(self.projetil_img.get_width() * 0.25),
                                                                       int(self.projetil_img.get_height() * 0.25)))

    def atualizar_projetil(self, tela):
        """
        Exibe o projétil do ataque especial do Piccolo em uma posição ajustada.
        """
        if self.ataque_especial_ativo and self.projetil_img:
            if self.estado == 'especial' and self.animacao_index >= len(self.sprites_especial) - 1:
                if self.is_facing_right:
                    pos_x = self.rect.right - 6
                else:
                    pos_x = self.rect.left - self.projetil_img.get_width() + 10

                # Ajustar a posição Y para ficar mais alto
                # Ajuste para ficar mais alto
                pos_y = self.rect.y + \
                    (self.rect.height - self.projetil_img.get_height()) // 2 - 20

                # Exibir o projétil
                if not self.is_facing_right:
                    proj_img = pygame.transform.flip(
                        self.projetil_img, True, False)
                    tela.blit(proj_img, (pos_x, pos_y))
                else:
                    tela.blit(self.projetil_img, (pos_x, pos_y))


class Bardock(Person):
    def __init__(self, x, y, controle='setas', is_facing_right=True):
        super().__init__(x, y, "Bardock", 1, 12, 150, 100, controle, is_facing_right)
        tamanho_desejado = (100, 100)
        base_path = os.path.join(
            game_base_path, 'Sprites', 'Bardock')
        self.sprites_andar = carregar_sprites(os.path.join(
            base_path, 'Movimentacao'), tamanho_desejado)
        self.sprites_voar = carregar_sprites(
            os.path.join(base_path, 'Voando'), tamanho_desejado)
        self.sprites_pousar = carregar_sprites(
            os.path.join(base_path, 'pousando'), tamanho_desejado)
        self.sprites_ataque = carregar_sprites(
            os.path.join(base_path, 'atacando'), tamanho_desejado)
        self.sprites_especial = carregar_sprites(
            os.path.join(base_path, 'especial'), tamanho_desejado)
        self.sprites_vitoria = carregar_sprites(
            os.path.join(base_path, 'vitoria'), tamanho_desejado)
        self.normal = carregar_sprites(os.path.join(
            base_path, 'normal'), tamanho_desejado)

        self.projetil_img = pygame.image.load(os.path.join(
            base_path, 'especial.png')).convert_alpha()
        self.projetil_img = pygame.transform.scale(self.projetil_img, (int(self.projetil_img.get_width() * 0.25),
                                                                       int(self.projetil_img.get_height() * 0.25)))
        self.tempo_ataque_duracao = 800


class TeenGohan(Person):
    def __init__(self, x, y, controle='setas', is_facing_right=True):
        super().__init__(x, y, "Teen Gohan", 1, 12, 150, 100, controle, is_facing_right)
        tamanho_desejado = (90, 90)
        base_path = os.path.join(
            game_base_path, 'Sprites', 'Teen Gohan')
        self.sprites_andar = carregar_sprites(os.path.join(
            base_path, 'Movimentacao'), tamanho_desejado)
        self.sprites_voar = carregar_sprites(
            os.path.join(base_path, 'Voando'), tamanho_desejado)
        self.sprites_pousar = carregar_sprites(
            os.path.join(base_path, 'pousando'), tamanho_desejado)
        self.sprites_ataque = carregar_sprites(
            os.path.join(base_path, 'atacando'), tamanho_desejado)
        self.sprites_especial = carregar_sprites(
            os.path.join(base_path, 'especial'), tamanho_desejado)
        self.sprites_vitoria = carregar_sprites(
            os.path.join(base_path, 'vitoria'), tamanho_desejado)
        self.normal = carregar_sprites(os.path.join(
            base_path, 'normal'), tamanho_desejado)

        self.projetil_img = pygame.image.load(os.path.join(
            base_path, 'Kamehameha.png')).convert_alpha()
        self.projetil_img = pygame.transform.scale(self.projetil_img, (int(self.projetil_img.get_width() * 0.35),
                                                                       int(self.projetil_img.get_height() * 0.35)))
        self.tempo_ataque_duracao = 800
