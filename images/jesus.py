def update():
    if keyboard.rigth:
        heroi.x = heroi.x + 2
    if keyboard.left:
        heroi.x = heroi.x - 2 
    if keyboard.up:
        heroi.y = heroi.y - 2 
    if keyboard.down:
        heroi.y = heroi.y + 2
    if heroi.colliderect (moedas):
        moedas.x = random.randint(50, WIDTH - 50)
        moedas.y = random.randint(50, HEIGHT - 50)
    if heroi.x > inimigo.x:
        inimigo.x = inimigo.x + 2
    if heroi.x < inimigo.x:
        inimigo.x = inimigo.x - 2
    if heroi.y > inimigo.y:
        inimigo.y = inimigo.y + 2
    if heroi.y < inimigo.y:
        inimigo.y = inimigo.y - 2

    if heroi.colliderect (inimigo):
        inimigo.x = random.randint(0, WIDTH - 0)
        inimigo.y = random.randint(0, HEIGHT - 0)
        
pgzrun.go()