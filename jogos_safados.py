import pygame
import pgzrun
import random

def redimencionar(ator, altura):
    escala = altura / ator.height
    novo = pygame.transform.smoothscale(
        ator._orig_surf, (int(ator.width * escala), altura)
        )
    ator_orig_surf = ator._surf = novo 
    ator._update_pos()


vidas = 3
estado_jogo = "JOGANDO"
WIDTH = 800
HEIGHT = 600
TITLE = "Jogos safados e gulosos do pygames zero"
heroi = Actor("diabão", (100,100))
redimencionar(heroi, 70)
moeda = Actor("moedas",(400,300))
inimigo = Actor("jesus",(700,500))
redimencionar(inimigo, 80)
pontos = 0
PONTOS_VITORIA = 100
estado_inimigo = "PATRULHA"
RAIO_DE_VISAO_QD = 180**2
VELOCIDADE_inimigo_PATRULHA = 1.5
VELOCIDADE_inimigo_PERSEGUICAO = 1.5
rota_patrulha = [(100,100), (600,100)]
indice_rota = 0


def draw():
    global pontos, vidas
    screen.fill((6,6,6))
    if estado_jogo == "JOGANDO":
        heroi.draw()
        inimigo.draw()
        moeda.draw()
        screen.draw.text(f"Pontos: {pontos}/{PONTOS_VITORIA}",topleft=(20,20), fontsize=32, color="gold",shadow=(1,1),scolor="blue")
        screen.draw.text(f"VIDAS: {vidas}/3",topleft=(20,40), fontsize=32, color="gold",shadow=(1,1),scolor="blue")
        if estado_inimigo == "PERSEGUICAO":
            cor_visao = (255 ,50,50)
        else:
            cor_visao = (100,100,255)
        screen.draw.circle(inimigo.pos,100,cor_visao)
        if estado_inimigo == "PERSEGUICAO":
            status_alerta = "ALERTA: OPPS,O inimigo TE VIU!"
        else:
            status_alerta = "Status: Oculto"
        screen.draw.text(status_alerta, midbottom=(WIDTH// 2,HEIGHT - 15),fontsize=22, color="crimson"if estado_inimigo == "PERSEGUICAO" else "lime")
    elif estado_jogo == "VITORIA":
        screen.draw.text("E ISSO AI! ESCAPOU COM SUCESSO", center=(WIDTH // 2,250), fontsize=50,color="lightgreen",shadow=(2,2),scolor= "black")
        screen.draw.text("presione [R] para jogar novamente",center=(WIDTH // 2,350),fontsize= 26, color= "yellow")
  
        
    elif estado_jogo == "GAMEOVER":
        screen.draw.text("SE FUDEU", center=(WIDTH // 2,220),fontsize=64,color="crimson",shadow=(2,2),scolor="black")

def update():
    global pontos, vidas, estado_jogo
    if keyboard.right:
        heroi.x = heroi.x + 2
    if keyboard.left:
        heroi.x = heroi.x - 2
    if keyboard.up:
        heroi.y = heroi.y - 2
    if keyboard.down:
        heroi.y = heroi.y + 2
    atualizar_ia_inimigo()
    if heroi.colliderect(moeda):
        pontos= pontos + 1
        moeda.x = random.randint(50,WIDTH - 50)
        moeda.y = random.randint(50,HEIGHT - 50)
    if heroi.colliderect(inimigo):
        vidas = vidas - 1
        if vidas<= 0:
            estado_jogo = "GAMEOVER"
        else:
            inimigo.x = random.choice([60,WIDTH - 60])
            inimigo.y = random.choice([60,WIDTH - 60])
    if keyboard.r:
        reiniciar_jogo()

def atualizar_ia_inimigo():
    global estado_inimigo,indice_rota,estado_jogo
    dx = heroi.x - inimigo.x
    dy = heroi.y - inimigo.y
    distancia_qd = dx**2 + dy**2
    if distancia_qd <= RAIO_DE_VISAO_QD:
        estado_inimigo = "PERSEGUICAO"
    else:
        estado_inimigo = "PATRULHA"
    if estado_inimigo == "PERSEGUICAO":
        if inimigo.x < heroi.x: inimigo.x += VELOCIDADE_inimigo_PERSEGUICAO
        elif inimigo.x > heroi.x: inimigo.x -= VELOCIDADE_inimigo_PERSEGUICAO
        if inimigo.y < heroi.y: inimigo.y += VELOCIDADE_inimigo_PERSEGUICAO
        elif inimigo.y > heroi.y: inimigo.y -= VELOCIDADE_inimigo_PERSEGUICAO

    elif estado_inimigo == "PATRULHA":
        alvo_x, alvo_y = rota_patrulha[indice_rota]
        if inimigo.x < alvo_x: inimigo.x += VELOCIDADE_inimigo_PATRULHA
        elif inimigo.x > alvo_x: inimigo.x -= VELOCIDADE_inimigo_PATRULHA
        if inimigo.y < alvo_y: inimigo.y += VELOCIDADE_inimigo_PERSEGUICAO
        elif inimigo.y > alvo_y: inimigo.y -= VELOCIDADE_inimigo_PERSEGUICAO
        
        if abs(inimigo.x - alvo_x) < 5 and abs(inimigo.y - alvo_y) < 5:
            indice_rota = (indice_rota + 1) % len(rota_patrulha)
            
def reiniciar_jogo():
 global estado_jogo, estado_inimigo, indice_rota, vidas
 estado_jogo = "JOGANDO"
 estado_inimigo = "PATRULHA"
 indice_rota = 0 
 heroi.pos = (100, 500)
 inimigo.pos = (700, 100)
 vidas = 3   
pgzrun.go()