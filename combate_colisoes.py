import pygame


class ColisoesCombate:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela

    def verificar_colisao(self, sprite1, sprite2):
        """
        Verifica se dois sprites colidiram.c
        """
        return sprite1.rect.colliderect(sprite2.rect)

    def aplicar_dano(self, atacante, defensor):
        """
        Aplica dano ao defensor se ele colidir com o atacante enquanto este está atacando.
        """
        if atacante.is_attacking and self.verificar_colisao(atacante, defensor):
            defensor.vida -= atacante.dano
            return True  # Indica que o dano foi aplicado
        return False

    def limitar_movimento(self, sprite):
        """
        Limita o movimento do sprite dentro dos limites da tela.
        """
        if sprite.rect.left < 0:
            sprite.rect.left = 0
        if sprite.rect.right > self.largura_tela:
            sprite.rect.right = self.largura_tela
        if sprite.rect.top < 0:
            sprite.rect.top = 0
        if sprite.rect.bottom > self.altura_tela:
            sprite.rect.bottom = self.altura_tela

