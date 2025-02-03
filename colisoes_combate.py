import pygame
from personagens import Person  # Importando a classe Person

class ColisoesCombate:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela

    def verificar_colisao(self, sprite1, sprite2):
        return sprite1.rect.colliderect(sprite2.rect)

    def verificar_distancia(self, sprite1, sprite2, distancia):
        return abs(sprite1.rect.centerx - sprite2.rect.centerx) <= distancia

    def aplicar_dano(self, atacante, defensor, tela):
        if atacante.is_attacking:
            if isinstance(atacante, Person) and isinstance(defensor, Person):
                if self.verificar_colisao(atacante, defensor) and self.verificar_distancia(atacante, defensor, 50):
                    if atacante.estado == 'ataque':
                        defensor.vida -= 1
                        atacante.ki -= 1
                    elif atacante.estado == 'especial':
                        defensor.vida -= atacante.dano_especial
                        atacante.ki -= 20

                    defensor.vida = max(0, defensor.vida)
                    print(f"{defensor.nome} agora tem {defensor.vida} de vida!")

                    if defensor.vida == 0:
                        self.declarar_vencedor(tela, atacante, defensor)

    def limitar_movimento(self, sprite):
        if sprite.rect.left < 0:
            sprite.rect.left = 0
        if sprite.rect.right > self.largura_tela:
            sprite.rect.right = self.largura_tela
        if sprite.rect.top < 0:
            sprite.rect.top = 0
        if sprite.rect.bottom > self.altura_tela:
            sprite.rect.bottom = self.altura_tela

    def atacar_normal(self, atacante, defensor, tela):
        if atacante.ki >= 1:
            atacante.is_attacking = True
            if self.verificar_colisao(atacante, defensor):
                self.aplicar_dano(atacante, defensor, tela)
            atacante.is_attacking = False
            return True
        atacante.is_attacking = False
        return False

    def atacar_especial(self, atacante, defensor, tela):
        if atacante.ki >= 20:
            atacante.is_attacking = True
            if self.verificar_colisao(atacante, defensor):
                self.aplicar_dano(atacante, defensor, tela)
            atacante.is_attacking = False
            return True
        atacante.is_attacking = False
        return False

    def atualizar_barras(self, tela, personagens):
        for personagem in personagens:
            pygame.draw.rect(tela, (255, 0, 0), (personagem.barra_vida_pos[0], personagem.barra_vida_pos[1], 200, 20))
            pygame.draw.rect(tela, (0, 255, 0), (personagem.barra_vida_pos[0], personagem.barra_vida_pos[1], 200 * (personagem.vida / personagem.vida_max), 20))

            font = pygame.font.SysFont('Arial', 14)
            texto_nome = font.render(personagem.nome, True, (255, 255, 255))
            tela.blit(texto_nome, (personagem.barra_vida_pos[0] + 100 - texto_nome.get_width() // 2, personagem.barra_vida_pos[1] + 2))

            pygame.draw.rect(tela, (0, 0, 0), (personagem.barra_ki_pos[0], personagem.barra_ki_pos[1], 200, 20))
            pygame.draw.rect(tela, (255, 255, 0), (personagem.barra_ki_pos[0], personagem.barra_ki_pos[1], 200 * (personagem.ki / personagem.ki_max), 20))

    def recuperar_ki(self, personagens):
        for personagem in personagens:
            personagem.ki = min(personagem.ki_max, personagem.ki + 25)
            print(f"{personagem.nome} recuperou 25 de ki!")

    def declarar_vencedor(self, tela, vencedor, perdedor):
        # Definindo o estado de vitória do vencedor
        vencedor.estado = 'vitoria'

        # Exibindo a animação de vitória do vencedor (na posição de P

        # Removendo o P2 da tela (sumindo)
        perdedor.vida = 0  # Pode ser configurado de forma mais elegante, mas garante que o P2 "some"
        perdedor.estado = 'derrotado'  # Ou qualquer estado que indique que o P2 foi derrotado

        # Exibindo a mensagem de vitória
        font = pygame.font.SysFont('Arial', 100)
        texto_vitoria = f"{vencedor.nome} Venceu!"
        win_text = font.render(texto_vitoria, True, "#b68f40")
        texto_rect = win_text.get_rect(center=(self.largura_tela // 2, self.altura_tela // 2))

        tela.blit(win_text, texto_rect)
        pygame.display.flip()

        pygame.time.wait(3000)  # Exibe a mensagem por 3 segundos
        # Aqui, se necessário, você pode resetar o jogo ou ir para uma tela de menu ou reinício.
