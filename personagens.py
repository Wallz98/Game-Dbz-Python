import os
import pygame
from pygame.locals import *

# Função para carregar imagens de uma pasta
def carregar_sprites(pasta, tamanho):
    sprites = []
    for arquivo in sorted(os.listdir(pasta)):  # Ordenar para garantir a sequência correta
        if arquivo.endswith('.png'):  # Verificar se é um arquivo de imagem
            caminho_completo = os.path.join(pasta, arquivo)
            imagem = pygame.image.load(caminho_completo)
            imagem_redimensionada = pygame.transform.scale(imagem, tamanho)
            sprites.append(imagem_redimensionada)
    return sprites

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
        self.controle = controle  # Agora o controle é um atributo da classe base
        self.is_facing_right = is_facing_right
        self.vida = self.vida_max
        self.ki = self.ki_max
        self.imagem = None
        self.atacar = False
        self.animacao_timer = 0
        self.animacao_intervalo = 100
        self.animacao_index = 0
        self.estado = 'normal'

        # Inicializando a velocidade do personagem
        self.velocidade = 5

        # Inicializar o rect para que o sprite seja manipulado pelo Pygame
        self.rect = pygame.Rect(x, y, 100, 100)

        # Posições fixas das barras de vida e ki
        self.barra_vida_pos = (self.rect.x, 10)  # Barra de vida fixada no topo
        self.barra_ki_pos = (self.rect.x, 40)    # Barra de ki fixada abaixo da barra de vida

        # Novo atributo que indica se o personagem está atacando
        self.is_attacking = False

    def aplicar_dano(self, atacante, defensor):
        """
        Aplica dano ao defensor com base no estado do atacante.
        """
        if atacante.is_attacking:  # Verifique se o atacante está no estado de ataque
            if atacante.estado == 'ataque':  # Ataque normal
                defensor.vida -= atacante.dano_normal  # Aplique o dano normal
            elif atacante.estado == 'especial':  # Ataque especial
                defensor.vida -= atacante.dano_especial  # Aplique o dano especial
            print(f"{defensor.nome} agora tem {defensor.vida} de vida!")

    def atualizar_barras(self, tela):
        # Barra de vida com o nome do personagem
        pygame.draw.rect(tela, (255, 0, 0), (self.barra_vida_pos[0], self.barra_vida_pos[1], 200, 20))  # Barra de vida maior
        pygame.draw.rect(tela, (0, 255, 0), (self.barra_vida_pos[0], self.barra_vida_pos[1], 200 * (self.vida / self.vida_max), 20))
        
        # Desenha o nome do personagem no meio da barra de vida
        font = pygame.font.SysFont('Arial', 14)  # Fonte para o nome
        texto_nome = font.render(self.nome, True, (255, 255, 255))  # Cor branca para o texto
        tela.blit(texto_nome, (self.barra_vida_pos[0] + 100 - texto_nome.get_width() // 2, self.barra_vida_pos[1] + 2))  # Posiciona o nome no centro da barra

        # Barra de ki (cor amarela)
        pygame.draw.rect(tela, (0, 0, 0), (self.barra_ki_pos[0], self.barra_ki_pos[1], 200, 20))  # Barra de ki maior (preto para borda)
        pygame.draw.rect(tela, (255, 255, 0), (self.barra_ki_pos[0], self.barra_ki_pos[1], 200 * (self.ki / self.ki_max), 20))  # Barra de ki amarela

    def update(self, keys, tempo_decorrido):
        # Movimento do player 1 (AWSD)
        if self.controle == 'wasd':
            if keys[pygame.K_a]:
                self.rect.x -= self.velocidade
                self.is_facing_right = False
                self.estado = 'andando'
            elif keys[pygame.K_d]:
                self.rect.x += self.velocidade
                self.is_facing_right = True
                self.estado = 'andando'
            else:
                self.estado = 'normal'

            if keys[pygame.K_w]:
                self.rect.y -= self.velocidade
                self.estado = 'voando'
            elif keys[pygame.K_s]:
                self.rect.y += self.velocidade
                self.estado = 'pousando'

            if keys[pygame.K_j]:
                self.estado = 'ataque'
                self.is_attacking = True  # Marca que o personagem está atacando
            if keys[pygame.K_k]:
                self.estado = 'especial'
                self.is_attacking = True  # Marca que o personagem está atacando

        # Movimento do player 2 (setas)
        elif self.controle == 'setas':
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.velocidade
                self.is_facing_right = False
                self.estado = 'andando'
            elif keys[pygame.K_RIGHT]:
                self.rect.x += self.velocidade
                self.is_facing_right = True
                self.estado = 'andando'
            else:
                self.estado = 'normal'

            if keys[pygame.K_UP]:
                self.rect.y -= self.velocidade
                self.estado = 'voando'
            elif keys[pygame.K_DOWN]:
                self.rect.y += self.velocidade
                self.estado = 'pousando'

            if keys[pygame.K_KP0]:
                self.estado = 'ataque'
                self.is_attacking = True  # Marca que o personagem está atacando
            if keys[pygame.K_KP1]:
                self.estado = 'especial'
                self.is_attacking = True  # Marca que o personagem está atacando

        # Limites da tela
        self.rect.x = max(0, min(self.rect.x, 1080 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 720 - self.rect.height))

        # Troca de sprites com base no estado
        if self.estado == 'andando' and self.sprites_andar:
            self.sprites = self.sprites_andar
        elif self.estado == 'voando' and self.sprites_voar:
            self.sprites = self.sprites_voar
        elif self.estado == 'pousando' and self.sprites_pousar:
            self.sprites = self.sprites_pousar
        elif self.estado == 'ataque' and self.sprites_ataque:
            self.sprites = self.sprites_ataque
        elif self.estado == 'especial' and self.sprites_especial:
            self.sprites = self.sprites_especial
        else:
            self.sprites = self.normal

        if tempo_decorrido - self.animacao_timer > self.animacao_intervalo:
            self.animacao_timer = tempo_decorrido
            self.animacao_index += 1
            if self.animacao_index >= len(self.sprites):
                self.animacao_index = 0

        self.image = self.sprites[min(self.animacao_index, len(self.sprites) - 1)]
        if not self.is_facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

    def parar_ataque(self):
        self.is_attacking = False  # Parar o ataque quando a tecla de ataque for solta

# Classe Vegeta
class Vegeta(Person):
    def __init__(self, x, y, controle='setas', is_facing_right=True):
        super().__init__(x, y, nome="Vegeta", dano_normal=1, dano_especial=12, vida_max=150, ki_max=100, controle=controle, is_facing_right=is_facing_right)
        
        tamanho_desejado = (100, 100)
        base_path = r'C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\Sprites\vegeta_ssj2\vegeta_ssj2'
        
        self.sprites_andar = carregar_sprites(os.path.join(base_path, 'Movimentacao'), tamanho_desejado)
        self.sprites_voar = carregar_sprites(os.path.join(base_path, 'Voando'), tamanho_desejado)
        self.sprites_pousar = carregar_sprites(os.path.join(base_path, 'pousando'), tamanho_desejado)
        self.sprites_ataque = carregar_sprites(os.path.join(base_path, 'atacando'), tamanho_desejado)
        self.sprites_especial = carregar_sprites(os.path.join(base_path, 'especial'), tamanho_desejado)
        self.normal = carregar_sprites(os.path.join(base_path, 'normal'), tamanho_desejado)

        self.sprites = self.normal
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Classe Goku
class Goku(Person):
    def __init__(self, x, y, controle='wasd', is_facing_right=True):
        super().__init__(x, y, nome="Goku", dano_normal=1, dano_especial=12, vida_max=150, ki_max=100, controle=controle, is_facing_right=is_facing_right)
        
        tamanho_desejado = (100, 100)
        base_path = r'C:\Users\walla\Desktop\Faculdade\2024_2\Programação modular\TP1\Sprites\Goku_ssj2'
        
        self.sprites_andar = carregar_sprites(os.path.join(base_path, 'andando'), tamanho_desejado)
        self.sprites_voar = carregar_sprites(os.path.join(base_path, 'voando'), tamanho_desejado)
        self.sprites_pousar = carregar_sprites(os.path.join(base_path, 'pousando'), tamanho_desejado)
        self.sprites_ataque = carregar_sprites(os.path.join(base_path, 'atacando'), tamanho_desejado)
        self.sprites_especial = carregar_sprites(os.path.join(base_path, 'especial'), tamanho_desejado)
        self.normal = carregar_sprites(os.path.join(base_path, 'normal'), tamanho_desejado)
        

        self.sprites = self.normal
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
