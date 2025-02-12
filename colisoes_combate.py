import pygame
from personagens import Person  # Certifique-se de que Person (e suas subclasses) estão implementados

class ColisoesCombate:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.projeteis = pygame.sprite.Group()  # Grupo de projéteis

    def verificar_colisao(self, sprite1, sprite2):
        """
        Verifica a colisão entre dois sprites usando a hitbox se disponível,
        ou o rect padrão caso contrário.
        """
        rect1 = getattr(sprite1, 'hitbox', sprite1.rect)
        rect2 = getattr(sprite2, 'hitbox', sprite2.rect)
        return rect1.colliderect(rect2)

    def aplicar_dano(self, atacante, defensor, tela):
        """
        Itera sobre os projéteis disparados pelo atacante e, se algum colidir com o defensor,
        aplica o dano (normal ou especial) e remove o projétil.
        """
        if isinstance(atacante, Person) and isinstance(defensor, Person):
            for proj in list(self.projeteis):  # Itera sobre uma cópia para evitar problemas ao remover itens
                if getattr(proj, 'owner', None) == atacante:
                    if self.verificar_colisao(proj, defensor):
                        if proj.tipo == 'ataque':  # Ataque normal
                            defensor.vida -= atacante.dano_normal
                            atacante.ki -= 1
                        elif proj.tipo == 'especial':  # Ataque especial
                            defensor.vida -= atacante.dano_especial
                            atacante.ki -= 20
                        defensor.vida = max(0, defensor.vida)
                        print(f"{defensor.nome} agora tem {defensor.vida} de vida!")
                        if defensor.vida == 0:
                            self.declarar_vencedor(tela, atacante, defensor)
                        proj.kill()  # Remove o projétil após o acerto

    def limitar_movimento(self, sprite):
        """Impede que o sprite saia da área visível da tela."""
        if sprite.rect.left < 0:
            sprite.rect.left = 0
        if sprite.rect.right > self.largura_tela:
            sprite.rect.right = self.largura_tela
        if sprite.rect.top < 0:
            sprite.rect.top = 0
        if sprite.rect.bottom > self.altura_tela:
            sprite.rect.bottom = self.altura_tela

    def atacar_normal(self, atacante, defensor, tela):
        """
        Se houver ki suficiente, realiza o ataque normal:
         - Cria o projétil normal (usando, se disponível, o primeiro sprite de 'sprites_ataque').
         - Em seguida, verifica a colisão e aplica o dano.
        """
        if atacante.ki >= 1:
            atacante.is_attacking = True
            self.criar_ataque(atacante, tipo='ataque')
            self.aplicar_dano(atacante, defensor, tela)
            self.remover_projeteis(atacante)
            atacante.is_attacking = False
            return True
        atacante.is_attacking = False
        return False

    def atacar_especial(self, atacante, defensor, tela):
        """
        Se houver ki suficiente, realiza o ataque especial:
         - Cria o projétil especial (usando a imagem 'projetil_img' do personagem, que vem de personagens.py).
         - Em seguida, verifica a colisão (usando a hitbox do projétil, do mesmo tamanho da imagem, dobrada)
           e aplica o dano.
        """
        if atacante.ki >= 20:
            atacante.is_attacking = True
            self.criar_ataque(atacante, tipo='especial')
            self.aplicar_dano(atacante, defensor, tela)
            self.remover_projeteis(atacante)
            atacante.is_attacking = False
            return True
        atacante.is_attacking = False
        return False

    def atualizar_barras(self, tela, personagens):
        """Atualiza as barras de vida e de ki dos personagens na tela."""
        for personagem in personagens:
            # Barra de vida
            pygame.draw.rect(tela, (255, 0, 0),
                             (personagem.barra_vida_pos[0], personagem.barra_vida_pos[1], 200, 20))
            pygame.draw.rect(tela, (0, 255, 0),
                             (personagem.barra_vida_pos[0], personagem.barra_vida_pos[1],
                              200 * (personagem.vida / personagem.vida_max), 20))
            font = pygame.font.SysFont('Arial', 14)
            texto_nome = font.render(personagem.nome, True, (255, 255, 255))
            tela.blit(texto_nome,
                      (personagem.barra_vida_pos[0] + 100 - texto_nome.get_width() // 2,
                       personagem.barra_vida_pos[1] + 2))
            # Barra de ki
            pygame.draw.rect(tela, (0, 0, 0),
                             (personagem.barra_ki_pos[0], personagem.barra_ki_pos[1], 200, 20))
            pygame.draw.rect(tela, (255, 255, 0),
                             (personagem.barra_ki_pos[0], personagem.barra_ki_pos[1],
                              200 * (personagem.ki / personagem.ki_max), 20))

    def recuperar_ki(self, personagens):
        """Recupera uma quantidade fixa de ki para cada personagem."""
        for personagem in personagens:
            personagem.ki = min(personagem.ki_max, personagem.ki + 25)
            print(f"{personagem.nome} recuperou 25 de ki!")

    def declarar_vencedor(self, tela, vencedor, perdedor):
        """Exibe a mensagem de vitória e define os estados dos personagens."""
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

    def remover_projeteis(self, atacante):
        """
        Remove os projéteis que saíram da tela ou que já colidiram com o atacante.
        Apenas remove os projéteis pertencentes ao 'atacante'.
        """
        for proj in list(self.projeteis):
            if getattr(proj, 'owner', None) == atacante:
                if proj.rect.right < 0 or proj.rect.left > self.largura_tela:
                    proj.kill()
                elif proj.rect.colliderect(atacante.rect):
                    proj.kill()

    def criar_ataque(self, atacante, tipo='ataque'):
        """
        Cria o projétil do ataque, posicionando-o no centro do atacante.
        - Para 'ataque' (normal): utiliza o primeiro sprite de 'sprites_ataque' se disponível;
          caso contrário, cria um projétil dummy (círculo vermelho).
        - Para 'especial': utiliza a imagem em 'projetil_img' (definida em personagens.py);
          caso não exista, cria um projétil dummy (círculo azul).
        A hitbox é definida com as mesmas dimensões da imagem do projétil, e para ataques especiais
        a mesma é inflada (dobrada) para abranger toda a imagem.
        """
        ataque = pygame.sprite.Sprite()
        if tipo == 'ataque':
            if hasattr(atacante, 'sprites_ataque') and atacante.sprites_ataque:
                ataque.image = atacante.sprites_ataque[0]
            else:
                # Projétil dummy vermelho 50x50
                ataque.image = pygame.Surface((50, 50), pygame.SRCALPHA)
                pygame.draw.circle(ataque.image, (255, 0, 0), (25, 25), 25)
        elif tipo == 'especial':
            if hasattr(atacante, 'projetil_img') and atacante.projetil_img:
                ataque.image = atacante.projetil_img
            else:
                # Projétil dummy azul 50x50
                ataque.image = pygame.Surface((50, 50), pygame.SRCALPHA)
                pygame.draw.circle(ataque.image, (0, 0, 255), (25, 25), 25)
        else:
            raise ValueError("Tipo de ataque inválido!")
        
        # Posiciona o projétil no centro do atacante
        ataque.rect = ataque.image.get_rect()
        ataque.rect.center = atacante.rect.center
        
        # Define a hitbox. Se for ataque especial, dobra as dimensões da imagem:
        if tipo == 'especial':
            ataque.hitbox = ataque.image.get_rect(center=ataque.rect.center).inflate(
                ataque.image.get_width(), ataque.image.get_height()
            )
        else:
            ataque.hitbox = ataque.image.get_rect(center=ataque.rect.center)
        
        # Define a direção do projétil com base na orientação do atacante
        ataque.direcao = 'direita' if atacante.is_facing_right else 'esquerda'
        
        # Armazena o dono e o tipo do projétil
        ataque.owner = atacante
        ataque.tipo = tipo
        
        self.projeteis.add(ataque)

    def atualizar_projeteis(self):
        """
        Atualiza a posição dos projéteis, movimentando-os conforme sua direção,
        atualiza a hitbox para refletir possíveis mudanças na imagem e remove os que
        saem da área visível.
        """
        for proj in list(self.projeteis):
            proj.rect.x += 10 if proj.direcao == 'direita' else -10
            if hasattr(proj, 'hitbox'):
                if proj.tipo == 'especial':
                    # Dobra a dimensão da hitbox para ataques especiais
                    proj.hitbox = proj.image.get_rect(center=proj.rect.center).inflate(
                        proj.image.get_width(), proj.image.get_height()
                    )
                else:
                    proj.hitbox = proj.image.get_rect(center=proj.rect.center)
            if proj.rect.right < 0 or proj.rect.left > self.largura_tela:
                proj.kill()
