import pygame
from personagens import Person


class ColisoesCombate:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.projeteis = pygame.sprite.Group()

    def verificar_colisao(self, sprite1, sprite2):
        rect1 = getattr(sprite1, 'hitbox', sprite1.rect)
        rect2 = getattr(sprite2, 'hitbox', sprite2.rect)
        return rect1.colliderect(rect2)

    def aplicar_dano(self, atacante, defensor, tela):
        """Aplica dano com lógica de direção e múltiplos hits."""
        if isinstance(atacante, Person) and isinstance(defensor, Person):
            for proj in list(self.projeteis):
                if getattr(proj, 'owner', None) == atacante:
                    if self.verificar_colisao(proj, defensor):

                        # Verifica se o atacante está virado para o oponente
                        if atacante.is_facing_right and atacante.rect.centerx < defensor.rect.centerx:
                            direcao_correta = True
                        elif not atacante.is_facing_right and atacante.rect.centerx > defensor.rect.centerx:
                            direcao_correta = True
                        else:
                            direcao_correta = False

                        if not direcao_correta:
                            proj.kill()
                            continue

                        # Define multiplicadores se for IA
                        dano_base = atacante.dano_normal
                        dano_especial = atacante.dano_especial
                        if hasattr(atacante, "controle") and atacante.controle == "ia":
                            dano_base *= 1.5
                            dano_especial *= 1.3

                        # Ataque especial → só aplica no fim da animação
                        if proj.tipo == 'especial':
                            if atacante.animacao_index < len(atacante.sprites_especial) - 1:
                                continue
                            defensor.vida -= dano_especial
                            atacante.ki -= 20
                            proj.kill()

                        # Ataque normal → pode causar múltiplos hits
                        elif proj.tipo == 'ataque':
                            if not hasattr(proj, "hits"):
                                proj.hits = 0
                            proj.hits += 1

                            defensor.vida -= dano_base
                            atacante.ki -= 1

                            # remove o projétil após 3 hits
                            if proj.hits >= 3:
                                proj.kill()

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
            self.criar_ataque(atacante, tipo='ataque')
            self.aplicar_dano(atacante, defensor, tela)
            atacante.is_attacking = False
            return True
        atacante.is_attacking = False
        return False

    def atacar_especial(self, atacante, defensor, tela):
        if atacante.ki >= 20:
            atacante.is_attacking = True
            self.criar_ataque(atacante, tipo='especial')
            self.aplicar_dano(atacante, defensor, tela)
            atacante.is_attacking = False
            return True
        atacante.is_attacking = False
        return False

    def atualizar_barras(self, tela, personagens):
        for i, personagem in enumerate(personagens):
            if i == 0:
                x_offset = 100
                retrato_x = 10
                alinhamento = "esquerda"
            else:
                x_offset = tela.get_width() - 300
                retrato_x = tela.get_width() - 80
                alinhamento = "direita"

            barra_vida_y = 15
            barra_ki_y = 45

            if hasattr(personagem, "retrato") and personagem.retrato:
                retrato = pygame.transform.scale(personagem.retrato, (70, 70))
                tela.blit(retrato, (retrato_x, barra_vida_y))

            largura_barra = 200
            altura_barra = 20

            vida_ratio = personagem.vida / personagem.vida_max
            pygame.draw.rect(tela, (255, 0, 0), (x_offset, barra_vida_y, largura_barra, altura_barra))
            pygame.draw.rect(tela, (0, 255, 0),
                             (x_offset, barra_vida_y, largura_barra * vida_ratio, altura_barra))

            ki_ratio = personagem.ki / personagem.ki_max
            pygame.draw.rect(tela, (0, 0, 0), (x_offset, barra_ki_y, largura_barra, altura_barra))
            pygame.draw.rect(tela, (255, 255, 0),
                             (x_offset, barra_ki_y, largura_barra * ki_ratio, altura_barra))

            font = pygame.font.SysFont("Arial", 18, bold=True)
            texto_nome = font.render(personagem.nome, True, (255, 255, 255))
            if alinhamento == "esquerda":
                nome_x = x_offset
            else:
                nome_x = x_offset + largura_barra - texto_nome.get_width()
            tela.blit(texto_nome, (nome_x, barra_ki_y + 25))

    def recuperar_ki(self, personagens):
        for personagem in personagens:
            personagem.ki = min(personagem.ki_max, personagem.ki + 25)

    def declarar_vencedor(self, tela, vencedor, perdedor):
        vencedor.estado = 'vitoria'
        perdedor.vida = 0
        perdedor.estado = 'derrotado'
        font = pygame.font.SysFont('Arial', 100)
        texto_vitoria = f"{vencedor.nome} Venceu!"
        win_text = font.render(texto_vitoria, True, "#b68f40")
        texto_rect = win_text.get_rect(center=(self.largura_tela // 2, self.altura_tela // 2))
        tela.blit(win_text, texto_rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def criar_ataque(self, atacante, tipo='ataque'):
        ataque = pygame.sprite.Sprite()
        if tipo == 'ataque':
            if hasattr(atacante, 'sprites_ataque') and atacante.sprites_ataque:
                ataque.image = atacante.sprites_ataque[0]
            else:
                ataque.image = pygame.Surface((50, 50), pygame.SRCALPHA)
                pygame.draw.circle(ataque.image, (255, 0, 0), (25, 25), 25)
        elif tipo == 'especial':
            if hasattr(atacante, 'projetil_img') and atacante.projetil_img:
                ataque.image = atacante.projetil_img
            else:
                ataque.image = pygame.Surface((50, 50), pygame.SRCALPHA)
                pygame.draw.circle(ataque.image, (0, 0, 255), (25, 25), 25)
        else:
            raise ValueError("Tipo de ataque inválido!")

        ataque.rect = ataque.image.get_rect(center=atacante.rect.center)
        if tipo == 'especial':
            ataque.hitbox = ataque.image.get_rect(center=ataque.rect.center).inflate(
                ataque.image.get_width(), ataque.image.get_height())
        else:
            ataque.hitbox = ataque.image.get_rect(center=ataque.rect.center)

        ataque.direcao = 'direita' if atacante.is_facing_right else 'esquerda'
        ataque.owner = atacante
        ataque.tipo = tipo
        self.projeteis.add(ataque)

    def atualizar_projeteis(self):
        for proj in list(self.projeteis):
            proj.rect.x += 10 if proj.direcao == 'direita' else -10
            if hasattr(proj, 'hitbox'):
                if proj.tipo == 'especial':
                    proj.hitbox = proj.image.get_rect(center=proj.rect.center).inflate(
                        proj.image.get_width(), proj.image.get_height())
                else:
                    proj.hitbox = proj.image.get_rect(center=proj.rect.center)
            if proj.rect.right < 0 or proj.rect.left > self.largura_tela:
                proj.kill()
