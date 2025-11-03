<<<<<<< HEAD
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
=======
import os
import pygame
from pygame.locals import *

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

# Classe base Person (herda de pygame.sprite.Sprite)


class Person(pygame.sprite.Sprite):
    def __init__(self, x, y, nome, dano_normal, dano_especial, vida_max, ki_max, controle, is_facing_right=True):
        super().__init__()
        self.x = x
        self.y = y
        self.nome = nome
        self.dano_normal = dano_normal
        self.dano_especial = dano_especial
        self.vida_max = vida_max
        self.ki_max = ki_max
        self.controle = controle
        self.is_facing_right = is_facing_right
        self.vida = self.vida_max
        self.ki = self.ki_max
        self.imagem = None
        self.atacar = False
        self.animacao_timer = 0
        self.animacao_intervalo = 100  # Intervalo (em ms) entre frames
        self.animacao_index = 0
        self.estado = 'normal'
        self.velocidade = 5
        self.rect = pygame.Rect(x, y, 100, 100)
        self.barra_vida_pos = (self.rect.x, 10)
        self.barra_ki_pos = (self.rect.x, 40)
        self.is_attacking = False
        self.ataque_especial_ativo = False
        self.projetil_img = None
        self.tempo_ataque = 0
        # Duração do ataque especial (deve ser compatível com o tempo necessário para a animação especial)
        self.tempo_ataque_duracao = 500

    def aplicar_dano(self, atacante, defensor):
        if atacante.is_attacking:
            if atacante.estado == 'ataque':
                defensor.vida -= atacante.dano_normal
            elif atacante.estado == 'especial':
                defensor.vida -= atacante.dano_especial
            print(f"{defensor.nome} agora tem {defensor.vida} de vida!")

    def atualizar_barras(self, tela):
        # Barra de vida
        pygame.draw.rect(
            tela, (255, 0, 0), (self.barra_vida_pos[0], self.barra_vida_pos[1], 200, 20))
        pygame.draw.rect(tela, (0, 255, 0),
                         (self.barra_vida_pos[0], self.barra_vida_pos[1], 200 * (self.vida / self.vida_max), 20))
        font = pygame.font.SysFont('Arial', 14)
        texto_nome = font.render(self.nome, True, (255, 255, 255))
        tela.blit(texto_nome, (self.barra_vida_pos[0] + 100 -
                  texto_nome.get_width() // 2, self.barra_vida_pos[1] + 2))
        # Barra de ki
        pygame.draw.rect(
            tela, (0, 0, 0), (self.barra_ki_pos[0], self.barra_ki_pos[1], 200, 20))
        pygame.draw.rect(tela, (255, 255, 0),
                         (self.barra_ki_pos[0], self.barra_ki_pos[1], 200 * (self.ki / self.ki_max), 20))

    def update(self, keys, tempo_decorrido, tela):
        # CONTROLE (WASD ou SETAS)
        if self.controle == 'wasd':
            if keys[pygame.K_a]:
                self.rect.x -= self.velocidade
                self.is_facing_right = False
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'andando'
            elif keys[pygame.K_d]:
                self.rect.x += self.velocidade
                self.is_facing_right = True
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'andando'
            else:
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'normal'

            if keys[pygame.K_w]:
                self.rect.y -= self.velocidade
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'voando'
            elif keys[pygame.K_s]:
                self.rect.y += self.velocidade
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'pousando'

            # Ataque normal
            if keys[pygame.K_j]:
                if not self.is_attacking:
                    self.estado = 'ataque'
                    self.is_attacking = True
                    self.tempo_ataque = tempo_decorrido

            # Ataque especial: inicia somente se ainda não estiver ativo
            if keys[pygame.K_k] and not self.ataque_especial_ativo:
                self.estado = 'especial'
                self.is_attacking = True
                self.ataque_especial_ativo = True
                self.tempo_ataque = tempo_decorrido

        elif self.controle == 'setas':
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.velocidade
                self.is_facing_right = False
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'andando'
            elif keys[pygame.K_RIGHT]:
                self.rect.x += self.velocidade
                self.is_facing_right = True
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'andando'
            else:
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'normal'

            if keys[pygame.K_UP]:
                self.rect.y -= self.velocidade
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'voando'
            elif keys[pygame.K_DOWN]:
                self.rect.y += self.velocidade
                if not self.ataque_especial_ativo and not self.is_attacking:
                    self.estado = 'pousando'

            if keys[pygame.K_KP0]:
                if not self.is_attacking:
                    self.estado = 'ataque'
                    self.is_attacking = True
                    self.tempo_ataque = tempo_decorrido
            if keys[pygame.K_KP1]:
                if not self.ataque_especial_ativo:
                    self.estado = 'especial'
                    self.is_attacking = True
                    self.ataque_especial_ativo = True
                    self.tempo_ataque = tempo_decorrido

        # Limitar movimento dentro da tela (exemplo: 1080x720)
        self.rect.x = max(0, min(self.rect.x, 1080 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 720 - self.rect.height))

        # Se o ataque normal ultrapassar a duração, encerra-o
        if self.is_attacking and self.estado not in ['especial'] and tempo_decorrido - self.tempo_ataque > self.tempo_ataque_duracao:
            self.parar_ataque()

        # Atualização dos sprites de acordo com o estado
        if self.estado == 'especial' and hasattr(self, 'sprites_especial') and self.sprites_especial:
            self.sprites = self.sprites_especial
            # Atualiza a animação especial sem reiniciar (não faz loop)
            if tempo_decorrido - self.animacao_timer > self.animacao_intervalo:
                self.animacao_timer = tempo_decorrido
                if self.animacao_index < len(self.sprites) - 1:
                    self.animacao_index += 1
                # Se já estiver no último frame, mantém o índice para exibir o projétil
        elif self.estado == 'andando' and hasattr(self, 'sprites_andar') and self.sprites_andar:
            self.sprites = self.sprites_andar
        elif self.estado == 'voando' and hasattr(self, 'sprites_voar') and self.sprites_voar:
            self.sprites = self.sprites_voar
        elif self.estado == 'pousando' and hasattr(self, 'sprites_pousar') and self.sprites_pousar:
            self.sprites = self.sprites_pousar
        elif self.estado == 'ataque' and hasattr(self, 'sprites_ataque') and self.sprites_ataque:
            self.sprites = self.sprites_ataque
        else:
            self.sprites = self.normal

        # Para estados que não sejam o especial, a animação roda em loop
        if self.estado != 'especial':
            if tempo_decorrido - self.animacao_timer > self.animacao_intervalo:
                self.animacao_timer = tempo_decorrido
                self.animacao_index += 1
                if self.animacao_index >= len(self.sprites):
                    self.animacao_index = 0

        # Define a imagem atual com base no frame da animação
        self.image = self.sprites[min(
            self.animacao_index, len(self.sprites) - 1)]
        if not self.is_facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

        # Exibe o projétil do ataque especial somente se a animação chegou (ou ultrapassou) o último frame
        self.atualizar_projetil(tela)

        # Se o ataque especial ultrapassar sua duração, encerra-o
        if self.estado == 'especial' and tempo_decorrido - self.tempo_ataque > self.tempo_ataque_duracao:
            self.parar_ataque()

    def atualizar_projetil(self, tela):
        """
        Exibe o projétil do ataque especial somente se:
          - o ataque especial estiver ativo,
          - a animação especial quando tiver atingido o último frame.
        """
        if self.ataque_especial_ativo and self.projetil_img:
            if self.estado == 'especial' and self.animacao_index >= len(self.sprites_especial) - 1:
                if self.is_facing_right:
                    pos_x = self.rect.right - 6
                else:
                    pos_x = self.rect.left - self.projetil_img.get_width() + 10
                pos_y = self.rect.y + \
                    (self.rect.height - self.projetil_img.get_height()) // 2 - 5
                if not self.is_facing_right:
                    proj_img = pygame.transform.flip(
                        self.projetil_img, True, False)
                    tela.blit(proj_img, (pos_x, pos_y))
                else:
                    tela.blit(self.projetil_img, (pos_x, pos_y))

    def parar_ataque(self):
        self.is_attacking = False
        if self.estado in ['ataque', 'especial']:
            self.estado = 'normal'
        self.ataque_especial_ativo = False
        # Reinicia o índice da animação para a próxima ação
        self.animacao_index = 0

# Classe Vegeta


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
                pos_y = self.rect.y + (self.rect.height - self.projetil_img.get_height()) // 2 - 20  # Ajuste para ficar mais alto

                # Exibir o projétil
                if not self.is_facing_right:
                    proj_img = pygame.transform.flip(self.projetil_img, True, False)
                    tela.blit(proj_img, (pos_x, pos_y))
                else:
                    tela.blit(self.projetil_img, (pos_x, pos_y))
>>>>>>> 338408dc92ee702e0ac4435c706ea81861d00391
