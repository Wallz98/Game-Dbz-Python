# ia_player.py
import random
import pygame


class SimpleAI:
    """
    IA simples que controla o Player 2 em lutas 1x1.
    Move-se em direção ao Player 1, realiza ataques normais e especiais com chance aleatória.
    Atualiza sprites e estado do personagem diretamente (sem depender do teclado).
    """

    def __init__(self, personagem, oponente):
        self.personagem = personagem
        self.oponente = oponente
        self.ultimo_ataque = 0
        self.cooldown_ataque = 600
        self.cooldown_movimento = 200
        self.ultimo_movimento = 0
        self.direcao = 0

        # flags
        self.should_attack = False
        self.attack_type = "ataque"

        # detectar troca de estado
        self.last_estado = None

    def update(self, tempo_atual):
        """Decide movimento e ataques"""
        self.should_attack = False

        # Se está atacando, aguarda o fim da animação
        if self.personagem.is_attacking:
            self._atualizar_estado_visual(tempo_atual)
            return

        # =======================
        # MOVIMENTO HORIZONTAL
        # =======================
        if tempo_atual - self.ultimo_movimento > self.cooldown_movimento:
            self.ultimo_movimento = tempo_atual
            distancia_x = self.oponente.rect.centerx - self.personagem.rect.centerx

            # Aproxima-se se estiver longe
            if abs(distancia_x) > 230:
                self.direcao = 1 if distancia_x > 0 else -1
            # Para e decide atacar se estiver próximo o suficiente
            elif abs(distancia_x) < 120:
                self.direcao = 0
                if tempo_atual - self.ultimo_ataque > self.cooldown_ataque:
                    chance = random.random()
                    if self.personagem.ki >= 20 and chance < 0.25:
                        self.atacar(tempo_atual, tipo="especial")
                    elif chance < 0.6:
                        self.atacar(tempo_atual, tipo="ataque")
                    else:
                        self.personagem.estado = "normal"
            else:
                self.direcao = 0
                self.personagem.estado = "normal"

        # Aplica movimento horizontal
        self.personagem.rect.x += self.direcao * self.personagem.velocidade
        if self.direcao > 0:
            self.personagem.is_facing_right = True
        elif self.direcao < 0:
            self.personagem.is_facing_right = False

        # =======================
        # MOVIMENTO VERTICAL (agora mais agressivo)
        # =======================
        diff_y = self.oponente.rect.centery - self.personagem.rect.centery

        # Se estiver longe verticalmente, sobe ou desce mais rápido
        if abs(diff_y) > 25:
            direcao_y = 1 if diff_y > 0 else -1
            # 🔹 Aumentei a velocidade vertical para ajustar mais rápido ao player
            self.personagem.rect.y += direcao_y * self.personagem.velocidade

            if not self.personagem.is_attacking:
                self.personagem.estado = "voando"
        else:
            # 🔹 Agora pousa somente se estiver realmente alinhado
            if self.personagem.estado == "voando" and not self.personagem.is_attacking:
                self.personagem.estado = "pousando"

        # =======================
        # ESTADO VISUAL
        # =======================
        if self.direcao != 0 and not self.personagem.is_attacking:
            self.personagem.estado = "andando"
        elif not self.personagem.is_attacking and self.personagem.estado not in ["voando", "pousando", "especial", "ataque"]:
            self.personagem.estado = "normal"

        self._atualizar_estado_visual(tempo_atual)

    def atacar(self, tempo_atual, tipo="ataque"):
        """Define flags de ataque e muda o estado visual"""
        self.should_attack = True
        self.attack_type = tipo
        self.ultimo_ataque = tempo_atual

        # Reinicia a animação
        self.personagem.animacao_index = 0
        self.personagem.animacao_timer = tempo_atual
        self.personagem.is_attacking = True

        if tipo == "especial":
            self.personagem.estado = "especial"
            self.personagem.ataque_especial_ativo = True
        else:
            self.personagem.estado = "ataque"
            self.personagem.ataque_especial_ativo = False
        # 🔹 IA causa dano 1.5x maior para compensar menos ataques
        self.personagem.dano_normal *= 1.0
        self.personagem.dano_especial *= 1.3
    

    def _atualizar_estado_visual(self, tempo_atual):
        """Atualiza a animação manualmente"""
        estado = self.personagem.estado

        # Reinicia animação ao mudar de estado
        if estado != self.last_estado:
            self.personagem.animacao_index = 0
            self.personagem.animacao_timer = tempo_atual
            self.last_estado = estado

        # Seleciona sprites conforme o estado
        if estado == "ataque" and hasattr(self.personagem, "sprites_ataque"):
            self.personagem.sprites = self.personagem.sprites_ataque
        elif estado == "especial" and hasattr(self.personagem, "sprites_especial"):
            self.personagem.sprites = self.personagem.sprites_especial
        elif estado == "andando" and hasattr(self.personagem, "sprites_andar"):
            self.personagem.sprites = self.personagem.sprites_andar
        elif estado == "voando" and hasattr(self.personagem, "sprites_voar"):
            self.personagem.sprites = self.personagem.sprites_voar
        elif estado == "pousando" and hasattr(self.personagem, "sprites_pousar"):
            self.personagem.sprites = self.personagem.sprites_pousar
        elif estado == "vitoria" and hasattr(self.personagem, "sprites_vitoria"):
            self.personagem.sprites = self.personagem.sprites_vitoria
        else:
            self.personagem.sprites = getattr(self.personagem, "normal", [])

        if not self.personagem.sprites:
            return

        # Intervalo mais lento para IA
        base_intervalo = getattr(self.personagem, "animacao_intervalo", 100)
        intervalo = base_intervalo * 1.4
        if self.personagem.is_attacking:
            intervalo *= 1.5

        # Atualiza frame
        if tempo_atual - self.personagem.animacao_timer > intervalo:
            self.personagem.animacao_timer = tempo_atual
            self.personagem.animacao_index += 1

            # Reseta ao fim da animação
            if self.personagem.animacao_index >= len(self.personagem.sprites):
                self.personagem.animacao_index = 0
                if self.personagem.is_attacking:
                    self.personagem.is_attacking = False
                    self.personagem.estado = "normal"
        # 🔹 Evita ataques instantâneos consecutivos
                    self.ultimo_ataque = tempo_atual

        # Corrige índice e desenha
        frame = self.personagem.sprites[self.personagem.animacao_index]
        if not self.personagem.is_facing_right:
            frame = pygame.transform.flip(frame, True, False)
        self.personagem.image = frame
