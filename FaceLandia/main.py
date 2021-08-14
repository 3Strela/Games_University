from graphics import *
from time import sleep
from ctypes import *
import random

# gcc -shared funcoes.c -o funcoesC.dll
funC = CDLL("./funcoesC.dll")

def modTxt(var, col, faml, stl):
    var.setFill(col)
    var.setFace(faml)
    var.setStyle(stl)
    
    return var

def animacao_draw(faces):
    bf = Image(Point(780, 20), faces[0])
    gf = Image(Point(20, 20), faces[1])
    pf = Image(Point(20, 400), faces[2])
    rf = Image(Point(780, 400), faces[3])

    tudo = [bf, gf, pf, rf]
    return tudo

def criaMenu():
    tit = Image(Point(400, 250), 'IMAGENS/titulo.png')
    pl = Image(Point(200, 450), 'IMAGENS/jogar.png')
    sr = Image(Point(600, 450), 'IMAGENS/Sair.png')

    itens = [tit, pl, sr]
    return itens

def animacao(itens, muda, muda2, acabou1, acabou2):
    if not(acabou1):
        if itens[0].getAnchor().getY() <= 170:
            itens[1].move(0.1, 0.11)
            itens[0].move(-0.1, 0.11)

        else:
            if itens[0].getAnchor().getX() >= 88:
                itens[0].move(-0.11, 0)
            
            else:
                muda = True
            
            if itens[1].getAnchor().getX() <= 692:
                itens[1].move(0.1, 0)
            
            if muda:
                if itens[0].getAnchor().getY() <= 285:
                    itens[1].move(0, 0.1)
                    itens[0].move(0, 0.1)
            
                elif itens[0].getAnchor().getY() <= 330:
                    itens[1].move(-0.2, 0.1)
                    itens[0].move(0.2, 0.1)
            
                elif itens[1].getAnchor().getX() >= -70:
                    itens[1].move(-0.5, 0)
                    itens[0].move(0.5, 0)
            
                else:
                    acabou1 = True
 
    if not(acabou2):
        if itens[2].getAnchor().getY() >= 330:
            itens[3].move(-0.3, -0.05)
            itens[2].move(0.3, -0.05)
        else:
            if itens[2].getAnchor().getX() <= 624:
                itens[2].move(0.3, 0)
            else:
                muda2 = True
            if itens[3].getAnchor().getX() >= 175:
                itens[3].move(-0.3, 0)
            if muda2:
                if itens[3].getAnchor().getX() >= 88:
                    itens[3].move(-0.3, -0.3)
                    itens[2].move(0.28, -0.3)
                elif itens[3].getAnchor().getY() >= 170:
                    itens[3].move(0, -0.3)
                    itens[2].move(0, -0.3)
                elif itens[3].getAnchor().getX() <= 850:
                    itens[3].move(-0.3, 0)
                    itens[2].move(0.3, 0)
                else:
                    acabou2 = True

    return itens, muda, muda2, acabou1, acabou2

def abrirBau(x, y, baus, bausDraw, resto, tela, ptX, ptY):
    aux = []
    cnt = 0
    for pos in baus:
        # if funC.abreBau(int(x), int(y), int(pos[0][0]), int(pos[0][1]), int(ptX), int(ptY), int(pos[1])) == 1
        if x >= pos[0][0] - ptX and x <= pos[0][0] + ptX and y >= pos[0][1] - ptY and y <= pos[0][1] + ptY and not(pos[1]):
            img = Image(Point(pos[0][0],pos[0][1]),'IMAGENS/bauAberto.png')
            pos = ((pos[0][0],pos[0][1]), True)
            img.draw(tela)
            bausDraw[cnt].undraw()
            bausDraw.append(img)
            resto -=1
       
        aux.append(pos)
        cnt += 1
    
    baus = aux
    return baus, bausDraw, resto

def posicaoValida(x, y, paredes):
    for itens in paredes:
        #if funC.pValida(int(x), int(y), int(itens[0][0]), int(itens[1][0]), int(itens[0][1]), int(itens[1][1])) == 1:
        if x >= itens[0][0] - 8 and x <= itens[1][0] + 8 and y >= itens[0][1] - 8 and y <= itens[1][1] + 8:
            return False

    return True

def botMoves(tela, matriz, face, i, j, posX, posY, tp, mt, tempo_player_min, tempo_player_seg):
    for itens in mt:
        itens.undraw()

    vez_adv = Text(Point(405, 300),'Vez do adversário!!')
    vez_adv = modTxt(vez_adv, color_rgb(128, 128, 0), 'courier', 'bold')
    vez_adv.setSize(36)
    vez_adv.draw(tela)

    sleep(2.5)
    
    vez_adv.undraw()
    
    for itens in mt:
        itens.draw(tela)

    img_bot = Image(Point(posX * (j + 1) + posX / 2, posY * (i + 1) + posY / 2), face)
    img_bot.draw(tela)
    
    segundos_bot = 0
    minutos_bot = 0
    txt_timer = Text(Point(660, 20),'Timer --> 0min 0seg')
    txt_timer = modTxt(txt_timer, 'white', 'courier', 'bold')
    txt_timer.draw(tela)

    tudo = [img_bot,txt_timer]

    sleep(0.5)

    ll = [0, -1, 0, 1]
    cc = [1, 0, -1, 0]

    visitados = []
    paiNode = []
    for ln in matriz:
        ax = []
        pp = []
        for cl in ln:
            ax.append(False)
            pp.append( (-1,-1) )
        paiNode.append(pp)
        visitados.append(ax)

    visitados[i][j] = True

    if tp == 0: #BFS
        fila = [(i,j)]
        while len(fila) > 0:
            pos = fila[0]
            fila.pop(0)

            sleep(0.5)
            img_bot.undraw()
            img_bot = Image(Point(posX * (pos[1] + 1) + posX / 2, posY * (pos[0] + 1) + posY / 2), face)
            img_bot.draw(tela)
            tudo.append(img_bot)

            segundos_bot += 1
            if segundos_bot == 60:
                segundos_bot = 0
                minutos_bot += 1

            txt_timer.undraw()
            txt_timer = Text(Point(660, 20), 'Timer --> ' + str(minutos_bot) + 'min ' + str(segundos_bot) + 'seg')
            txt_timer = modTxt(txt_timer, 'white', 'courier', 'bold')
            txt_timer.draw(tela)
            tudo.append(txt_timer)

            if matriz[pos[0]][pos[1]] == 'f':
                sleep(0.5)
                break

            for cordenadas in range(4):
                linha = pos[0] + ll[cordenadas]
                coluna = pos[1] + cc[cordenadas]

                if (matriz[linha][coluna] == '.' or matriz[linha][coluna] == 't' or matriz[linha][coluna] == 'f') and not(visitados[linha][coluna]):
                    visitados[linha][coluna] = True
                    fila.append((linha,coluna))
    
    elif tp == 1: #DFS
        pilha = [(i,j)]
        while len(pilha) > 0:
            pos = pilha[-1]
            pilha.pop(-1)

            sleep(0.5)
            img_bot.undraw()
            img_bot = Image(Point(posX * (pos[1] + 1) + posX / 2, posY * (pos[0] + 1) + posY / 2), face)
            img_bot.draw(tela)
            tudo.append(img_bot)
            
            segundos_bot += 1
            if segundos_bot == 60:
                segundos_bot = 0
                minutos_bot += 1

            txt_timer.undraw()
            txt_timer = Text(Point(660, 20), 'Timer --> ' + str(minutos_bot) + 'min ' + str(segundos_bot) + 'seg')
            txt_timer = modTxt(txt_timer, 'white', 'courier', 'bold')
            txt_timer.draw(tela)
            tudo.append(txt_timer)

            if matriz[pos[0]][pos[1]] == 'f':
                sleep(0.5)
                break

            for cordenadas in range(4):
                linha = pos[0] + ll[cordenadas]
                coluna = pos[1] + cc[cordenadas]

                if (matriz[linha][coluna] == '.' or matriz[linha][coluna] == 't' or matriz[linha][coluna] == 'f') and not(visitados[linha][coluna]):
                    visitados[linha][coluna] = True
                    pilha.append((linha,coluna))

    else: #Vai direto // calcula BFS dps percorre
        fila = [(i,j)]
        while len(fila) > 0:
            pos = fila[0]
            fila.pop(0)

            if matriz[pos[0]][pos[1]] == 'f':
                queroIr = (pos[0], pos[1])
                break

            for cordenadas in range(4):
                linha = pos[0] + ll[cordenadas]
                coluna = pos[1] + cc[cordenadas]

                if (matriz[linha][coluna] == '.' or matriz[linha][coluna] == 't' or matriz[linha][coluna] == 'f') and not(visitados[linha][coluna]):
                    visitados[linha][coluna] = True
                    paiNode[linha][coluna] = (pos[0], pos[1])
                    fila.append((linha,coluna))

        caminho = []
        while queroIr != (-1, -1):
            caminho.append(queroIr)
            queroIr = paiNode[queroIr[0]][queroIr[1]]
        
        caminho.reverse()
        
        for quadrado in caminho:
            sleep(0.5)
            img_bot.undraw()
            img_bot = Image(Point(posX * (quadrado[1] + 1) + posX / 2, posY * (quadrado[0] + 1) + posY / 2), face)
            img_bot.draw(tela)
            tudo.append(img_bot)

            segundos_bot += 1
            if segundos_bot == 60:
                segundos_bot = 0
                minutos_bot += 1

            txt_timer.undraw()
            txt_timer = Text(Point(660, 20), 'Timer --> ' + str(minutos_bot) + 'min ' + str(segundos_bot) + 'seg')
            txt_timer = modTxt(txt_timer, 'white', 'courier', 'bold')
            txt_timer.draw(tela)
            tudo.append(txt_timer)

        sleep(0.5)

    for al in tudo:
        al.undraw()

    for itens in mt:
        itens.undraw()

    #dd_tmp = funC.difTempos(int(tempo_player_min), int(tempo_player_seg), int(minutos_bot), int(segundos_bot))
    dd_tmp = (tempo_player_min * 60 + tempo_player_seg) - (minutos_bot * 60 + segundos_bot)

    sleep(1)
    tempos = Text(Point(400,170), 'Tempo do jogador: ' + str(tempo_player_min) + 'min ' + str(tempo_player_seg) + 'seg // Tempo do bot: ' + str(minutos_bot) + 'min ' + str(segundos_bot) + 'seg')
    tempos = modTxt(tempos, color_rgb(204, 204, 204), 'courier', 'bold')
    tempos.draw(tela)

    sleep(1.5)
    dif_tempo = Text(Point(400,200),'A diferença de tempo foi: ' + str(abs(dd_tmp) // 60) + 'min ' + str(abs(dd_tmp) % 60) + 'seg')
    dif_tempo = modTxt(dif_tempo, color_rgb(204, 204, 204), 'courier', 'bold')
    dif_tempo.draw(tela)

    sleep(2)

    venceu = True
    if dd_tmp <= 0:
        result = Text(Point(405,300),'Você ganhou :)')
        result = modTxt(result, color_rgb(0, 204, 0), 'courier', 'bold')
        result.setSize(36)        

    else:
        result = Text(Point(405,300),'Você perdeu :(')
        result = modTxt(result, color_rgb(204, 0, 0), 'courier', 'bold')
        result.setSize(36)
        venceu = False

    result.draw(tela)

    sleep(1.5)

    txt_pular = Image(Point(625, 580), 'IMAGENS/passar.png')
    txt_pular.draw(tela)

    tela.getMouse()

    tempos.undraw()
    dif_tempo.undraw()
    result.undraw()
    txt_pular.undraw()

    return venceu
        
def jogar_labirinto(tela, face, fase, dificuldade):
    ax = '2'
    if face == "IMAGENS/PinkFace.png" or face == "IMAGENS/kingFace.png":
        ax = '1'

    nome_arq = "MAPAS/lb" + str(fase + 1) + "_" + ax + ".txt"

    arq = open(nome_arq)
    pre_matriz = arq.readlines()
    arq.close()

    vez_plr = Text(Point(405,300),'Vez do jogador!!')
    vez_plr = modTxt(vez_plr, color_rgb(179, 179, 0), 'courier', 'bold')
    vez_plr.setSize(36)
    vez_plr.draw(tela)

    sleep(2.5)
    
    vez_plr.undraw()
    
    matriz = []
    col = 0
    lin = 0
    for linha in pre_matriz:
        mtr_aux = []
        col = 0
        for caracter in linha:
            if caracter != '\n' and caracter != ' ':
                mtr_aux.append(caracter)
                col += 1

        lin += 1
        matriz.append(mtr_aux)

    matriz_desenho = []
    mm_player = []
    posX = 700 // col
    posY = 500 // lin

    if fase == 1:
        posY += 4

    acresX = posX
    acresY = posY
    
    baus_list = []
    bausDraw = []
    paredes = []

    for i in range(lin):
        for j in range(col):
            #vv = funC.verificaTabuleiro(matriz[i][j])
            vv = matriz[i][j]
            if vv == '#':
                desenho = Rectangle(Point(posX * (j + 1), posY * (i + 1)), Point((posX * (j + 1)) + acresX, (posY * (i + 1)) + acresY))
                desenho.setFill('white')
                paredes.append(((posX * (j + 1), posY * (i + 1)), ((posX * (j + 1)) + acresX, (posY * (i + 1)) + acresY)))
                matriz_desenho.append(desenho)
            
            elif vv == 'i':
                player_Face = Image(Point(posX * (j + 1) + posX / 2, posY * (i + 1) + posY / 2), face)
                mm_player.append(player_Face)
            
            elif vv == 'f':
                final = Image(Point(posX * (j + 1) + posX / 2, posY * (i + 1) + posY / 2), 'IMAGENS/bandeira.png')
                endgame = (posX * (j + 1) + posX / 2, posY * (i + 1) + posY / 2)
                matriz_desenho.append(final)
            
            elif vv == 't':
                baus = Image(Point(posX * (j + 1) + posX / 2, posY * (i + 1) + posY / 2), 'IMAGENS/bau.png')
                baus_list.append(((posX * (j + 1) + posX / 2, posY * (i + 1) + posY / 2), False))
                bausDraw.append(baus)
    
    att_bau = len(baus_list)
    qt_rest = len(baus_list)
    
    bust = 0
    txt_speed = Text(Point(110,20),'Velocidade --> 5px')
    txt_speed = modTxt(txt_speed, 'white', 'courier', 'bold')
    mm_player.append(txt_speed)

    timer = 0
    segundos = 0
    minutos = 0
    txt_timer = Text(Point(660,20),'Timer --> 0min 0seg')
    txt_timer = modTxt(txt_timer, 'white', 'courier', 'bold')
    mm_player.append(txt_timer)
    
    for itens in mm_player:
        itens.draw(tela)

    for itens in bausDraw:
        itens.draw(tela)
    
    for itens in matriz_desenho:
        itens.draw(tela)

    game_on = True
    while game_on:
        key = tela.checkKey()
        plX = player_Face.getAnchor().getX()
        plY = player_Face.getAnchor().getY()
        if (key == 'a' or key == 'A' or key == 'Left') and posicaoValida(plX - 5 - bust, plY, paredes):
            player_Face.move(-5 - bust, 0)
        
        elif (key == 'd' or key == 'D' or key == 'Right') and posicaoValida(plX + 5 + bust, plY, paredes):
            player_Face.move(5 + bust, 0)
        
        elif (key == 's' or key == 'S' or key == 'Down') and posicaoValida(plX, plY + 5 + bust, paredes):
            player_Face.move(0, 5 + bust)
        
        elif (key == 'w' or key == 'W' or key == 'Up') and posicaoValida(plX, plY - 5 - bust, paredes):
            player_Face.move(0, -5 - bust)

        baus_list, bausDraw, qt_rest = abrirBau(plX, plY, baus_list, bausDraw, qt_rest, tela, posX / 2, posY / 2)
        if qt_rest != att_bau:
            att_bau -= 1
            bust = 0
            while bust == 0:
                bust = random.randint(-4, 5)

            txt_speed.undraw()
            txt_speed = Text(Point(110,20),'Velocidade --> ' + str(bust + 5) + 'px')
            txt_speed = modTxt(txt_speed, 'white', 'courier', 'bold')
            txt_speed.draw(tela)
            mm_player.append(txt_speed)

        #elif funC.winGame(int(plX), int(plY), int(endgame[0]), int(endgame[1]), int(posX / 2), int(posY / 2 - 5)) == 1:
        elif plX >= endgame[0] - (posX / 2) and plX <= endgame[0] + (posX / 2) and plY >= endgame[1] - posY / 2 - 5 and plY <= endgame[1] + posY / 2 - 5:
            game_on = False
        
        if timer == 20000:
            if segundos == 60:
                segundos = 0
                minutos += 1
      
            segundos += 1
            txt_timer.undraw()
            txt_timer = Text(Point(660, 20),'Timer --> ' + str(minutos)+ 'min ' + str(segundos) + 'seg')
            txt_timer = modTxt(txt_timer, 'white', 'courier', 'bold')
            txt_timer.draw(tela)
            mm_player.append(txt_timer)
            timer = 0
      
        timer += 1

    for tudo in mm_player:
        tudo.undraw()
    
    for tudo in bausDraw:
        tudo.undraw()

    win = True
    if fase == 0 and ax == '1':
        win = botMoves(tela, matriz,'IMAGENS/BlueFace.png', 1, 10, posX, posY, dificuldade, matriz_desenho, minutos, segundos)
    
    elif fase == 1 and ax == '1':
        win = botMoves(tela, matriz,'IMAGENS/RedFaceMini.png', 1, 4, posX, posY, dificuldade, matriz_desenho, minutos, segundos)
    
    elif fase == 0 and ax == '2':
        win = botMoves(tela, matriz,'IMAGENS/PinkFace.png', 1, 5, posX, posY, dificuldade, matriz_desenho, minutos, segundos)
    
    else:
        win = botMoves(tela, matriz,'IMAGENS/kingFaceMini.png', 19, 1, posX, posY, dificuldade, matriz_desenho, minutos, segundos)

    if not(win):
        fase = -1

    else:
        fase += 1

    return fase

def digitaTexto(tela, txt, x, y):
    pular = tela.checkMouse()

    ind = 0
    ppX = x
    ppY = y
    excluir = []
    risco = Text(Point(ppX,ppY),'|')
    risco.setFill('white')
    risco.setStyle('bold')
    risco.draw(tela)

    while pular == None:
        pular = tela.checkMouse()
        if ind < len(txt):
            if txt[ind] == '\n':
                ppY += 20
                ppX = 105
                risco.undraw()
                risco = Text(Point(ppX,ppY),'|')
                risco.setFill('white')
                risco.setStyle('bold')
                risco.draw(tela)

            elif txt[ind] == ' ':
                ppX += 10
                risco.undraw()
                risco = Text(Point(ppX,ppY),'|')
                risco.setFill('white')
                risco.setStyle('bold')
                risco.draw(tela)

            else:
                risco.undraw()
                tt = Text(Point(ppX, ppY), txt[ind])
                tt.setFill('white')
                tt.setFace('courier')
                tt.setStyle('bold')
                tt.draw(tela)
                excluir.append(tt)
                ppX += 10
                risco = Text(Point(ppX,ppY),'|')
                risco.setFill('white')
                risco.setStyle('bold')
                risco.draw(tela)

            sleep(0.075)

        ind += 1
                            
    risco.undraw()
    for letras in excluir:
        letras.undraw()

def main():
    tela = GraphWin('LabiFaces: o labirinto de Facelândia', 800, 600)
    tela.setBackground("black")

    menu_itens = criaMenu()
    for itens in menu_itens:
        itens.draw(tela)

    lt_faces = ["IMAGENS/RedFace.png", "IMAGENS/kingFace.png", "IMAGENS/PinkFace.png", "IMAGENS/BlueFace.png"]
    lt_faces_mostras = ["IMAGENS/RedFaceB.png", "IMAGENS/kingFaceB.png", "IMAGENS/PinkFaceB.png", "IMAGENS/BlueFaceB.png"]

    anima = animacao_draw(lt_faces)
    vt_ax = [False, False, False, False]
    for itens in anima:
        itens.draw(tela)

    gameloop = True
    while gameloop:
        click = tela.checkMouse()

        menu = False

        if click != None:
            if click.getX() >= 122 and click.getX() <= 277 and click.getY() >= 419 and click.getY() <= 474:
                for i in menu_itens:
                    i.undraw()
                
                for i in anima:
                    i.undraw()

                txt_op = Image(Point(200, 50), 'IMAGENS/txt_op.png')
                txt_op.draw(tela)
                opcoes = [txt_op]

                for i in range(4):
                    cx = Rectangle(Point(175 + (i * 138), 100), Point(275 + (i * 138), 200))
                    cx.setFill(color_rgb(166, 166, 166))
                    cx.draw(tela)
                    opcoes.append(cx)

                for i in range(4):
                    chars = Image(Point(225+(i*140), 150), lt_faces_mostras[i])
                    if i == 2:
                        chars = Image(Point(225+(i*137), 150), lt_faces_mostras[i])
                    
                    elif i == 3:
                        chars = Image(Point(225+(i*138), 150), lt_faces_mostras[i])
                    
                    chars.draw(tela)
                    opcoes.append(chars)

                ind_char = -1
                desen_char = False
                dificuldade = -1
                desen_dif = False
                confirma = False
                while not(confirma):
                    click = tela.checkMouse()

                    if click != None:
                        if click.getX() >= 175 and click.getX() <= 275 and click.getY() >= 100 and click.getY() <= 200:
                            ind_char = 0
                            for i in range(1, 5):
                                opcoes[i].setFill(color_rgb(166, 166, 166))
                            opcoes[1].setFill(color_rgb(77, 255, 136))
                            
                        elif click.getX() >= 313 and click.getX() <= 413 and click.getY() >= 100 and click.getY() <= 200:
                            ind_char = 1
                            for i in range(1, 5):
                                opcoes[i].setFill(color_rgb(166, 166, 166))
                            opcoes[2].setFill(color_rgb(77, 255, 136))

                        elif click.getX() >= 451 and click.getX() <= 551 and click.getY() >= 100 and click.getY() <= 200:
                            ind_char = 2
                            for i in range(1, 5):
                                opcoes[i].setFill(color_rgb(166, 166, 166))
                            opcoes[3].setFill(color_rgb(77, 255, 136))

                        elif click.getX() >= 589 and click.getX() <= 689 and click.getY() >= 100 and click.getY() <= 200:
                            ind_char = 3
                            for i in range(1, 5):
                                opcoes[i].setFill(color_rgb(166, 166, 166))
                            opcoes[4].setFill(color_rgb(77, 255, 136))

                        if ind_char != -1 and not(desen_char):
                            r1 = Rectangle(Point(55,270),Point(315,295))
                            r2 = Rectangle(Point(55,310),Point(245,335))
                            r3 = Rectangle(Point(55,350),Point(205,375))
                            recs = [r1,r2,r3]

                            desen_char = True

                            for r in recs:
                                r.setFill(color_rgb(166, 166, 166))
                                r.draw(tela)
                                opcoes.append(r)

                            txt_dif = Image(Point(190,250),'IMAGENS/txt_dif.png')
                            txt_dif.draw(tela)
                            izi = Text(Point(185,285),'Só quero passar meu tempo')
                            izi = modTxt(izi, color_rgb(0, 128, 43), 'courier', 'bold')
                            izi.draw(tela)
                            medi = Text(Point(150,325),'Simbora nessa joça')
                            medi = modTxt(medi, color_rgb(230, 46, 0), 'courier', 'bold')
                            medi.draw(tela)
                            nda = Text(Point(130,365),'Bixin ispierto')
                            nda = modTxt(nda, color_rgb(179, 0, 0), 'courier', 'bold')
                            nda.draw(tela)

                            opcoes.append(txt_dif)
                            opcoes.append(izi)
                            opcoes.append(medi)
                            opcoes.append(nda)

                        if desen_char:
                            if click.getX() >= 55 and click.getX() <= 315 and click.getY() >= 270 and click.getY() <= 295:
                                dificuldade = 0
                                for r in recs:
                                    r.setFill(color_rgb(166, 166, 166))
                                r1.setFill(color_rgb(77, 255, 136))

                            elif click.getX() >= 55 and click.getX() <= 245 and click.getY() >= 310 and click.getY() <= 335:
                                dificuldade = 1
                                for r in recs:
                                    r.setFill(color_rgb(166, 166, 166))
                                r2.setFill(color_rgb(77, 255, 136))

                            elif click.getX() >= 55 and click.getX() <= 205 and click.getY() >= 350 and click.getY() <= 375:
                                dificuldade = 2
                                for r in recs:
                                    r.setFill(color_rgb(166, 166, 166))
                                r3.setFill(color_rgb(77, 255, 136))
                        
                        if dificuldade != -1 and not(desen_dif):
                            desen_dif = True
                            boxConf = Rectangle(Point(55, 400),Point(155, 425))
                            boxConf.setFill(color_rgb(166, 166, 166))
                            conf_txt = Text(Point(105,415),'Confirmar')
                            conf_txt = modTxt(conf_txt, color_rgb(0, 0, 204), 'courier', 'bold')
                            boxConf.draw(tela)
                            conf_txt.draw(tela)
                            opcoes.append(boxConf)
                            opcoes.append(conf_txt)

                        if desen_dif:
                            if click.getX() >= 55 and click.getX() <= 155 and click.getY() >= 400 and click.getY() <= 425:
                                confirma = True
                                boxConf.setFill(color_rgb(77, 255, 136))
                        
                        if confirma:
                            sleep(0.5)
                            for itens in opcoes:
                                itens.undraw()

                txt_pular = Image(Point(625, 580), 'IMAGENS/passar.png')
                txt_pular.draw(tela)

                if ind_char == 0 or ind_char == 3:   
                    castle = Image(Point(400, 220), 'IMAGENS/castelo_dark.png')
                    castle.draw(tela)
                    arq = open('TEXTOS/histRB1.txt')
                    txt = arq.read()
                    arq.close()
                    digitaTexto(tela, txt, 105, 440)
                    castle.undraw()

                    hist = Image(Point(400, 200), 'IMAGENS/histRB.png')
                    hist.draw(tela)
                    arq = open('TEXTOS/histRB2.txt')
                    txt = arq.read()
                    arq.close()
                    digitaTexto(tela, txt, 105, 400)
                    castle.undraw()
                    hist.undraw()

                    if ind_char == 0:
                        hist2 = Image(Point(400, 220), 'IMAGENS/histRB_R.png')
                        hist2.draw(tela)
                        arq = open('TEXTOS/histRB_R.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        castle.undraw()
                        hist2.undraw()

                    else:
                        hist2 = Image(Point(400, 220), 'IMAGENS/histRB_B.png')
                        hist2.draw(tela)
                        arq = open('TEXTOS/histRB_B.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        castle.undraw()
                        hist2.undraw()

                elif ind_char == 1 or ind_char == 2:         
                    castle = Image(Point(400, 200), 'IMAGENS/castelo_light.png')
                    castle.draw(tela)
                    arq = open('TEXTOS/histKP1.txt')
                    txt = arq.read()
                    arq.close()
                    digitaTexto(tela, txt, 105, 400)
                    castle.undraw()

                    hist = Image(Point(400, 220), 'IMAGENS/histKP.png')
                    hist.draw(tela)
                    arq = open('TEXTOS/histKP2.txt')
                    txt = arq.read()
                    arq.close()
                    digitaTexto(tela, txt, 105, 440)
                    hist.undraw()

                    if ind_char == 1:
                        hist2 = Image(Point(400, 220), 'IMAGENS/histKP_K.png')
                        hist2.draw(tela)
                        arq = open('TEXTOS/histKP_K.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist2.undraw()

                    else:
                        hist2 = Image(Point(400, 220), 'IMAGENS/histKP_P.png')
                        hist2.draw(tela)
                        arq = open('TEXTOS/histKP_P.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist2.undraw()

                txt_pular.undraw()

                ind_lab = 0
                while ind_lab < 2 and ind_lab != -1:
                    ind_lab = jogar_labirinto(tela, lt_faces[ind_char], ind_lab, dificuldade)

                txt_pular = Image(Point(630, 580), 'IMAGENS/passar.png')
                txt_pular.draw(tela)

                if ind_lab != -1:
                    if ind_char == 0:
                        hist3 = Image(Point(400, 220), 'IMAGENS/FimFeliz_R.png')
                        hist3.draw(tela)
                        arq = open('TEXTOS/fimFeliz_R.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist3.undraw()

                    elif ind_char == 1:
                        hist3 = Image(Point(400, 220), 'IMAGENS/FimFeliz_K.png')
                        hist3.draw(tela)
                        arq = open('TEXTOS/fimFeliz_K.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist3.undraw()

                    elif ind_char == 2:
                        hist3 = Image(Point(400, 220), 'IMAGENS/FimFeliz_P.png')
                        hist3.draw(tela)
                        arq = open('TEXTOS/fimFeliz_P.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist3.undraw()

                    elif ind_char == 3:
                        hist3 = Image(Point(400, 220), 'IMAGENS/FimFeliz_B.png')
                        hist3.draw(tela)
                        arq = open('TEXTOS/fimFeliz_B.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist3.undraw()
                
                else:
                    if ind_char == 0:
                        hist3 = Image(Point(400, 220), 'IMAGENS/FimSad_R.png')
                        hist3.draw(tela)
                        arq = open('TEXTOS/fimSad_R.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist3.undraw()

                    elif ind_char == 1:
                        hist3 = Image(Point(400, 220), 'IMAGENS/FimSad_K.png')
                        hist3.draw(tela)
                        arq = open('TEXTOS/fimSad_K.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist3.undraw()

                    elif ind_char == 2:
                        hist3 = Image(Point(400, 220), 'IMAGENS/FimSad_P.png')
                        hist3.draw(tela)
                        arq = open('TEXTOS/fimSad_P.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist3.undraw()

                    elif ind_char == 3:
                        hist3 = Image(Point(400, 220), 'IMAGENS/FimSad_B.png')
                        hist3.draw(tela)
                        arq = open('TEXTOS/fimSad_B.txt')
                        txt = arq.read()
                        arq.close()
                        digitaTexto(tela, txt, 105, 440)
                        hist3.undraw()

                txt_pular.undraw()

                menu = True

            elif click.getX() >= 546 and click.getX() <= 651 and click.getY() >= 418 and click.getY() <= 478:
                gameloop = False
        
        if menu: 
            for i in menu_itens:
                i.draw(tela)
                
            anima = animacao_draw(lt_faces)
            vt_ax = [False, False, False, False]
            for i in anima:
                i.draw(tela)
        
        anima, vt_ax[0], vt_ax[1], vt_ax[2], vt_ax[3] = animacao(anima, vt_ax[0], vt_ax[1], vt_ax[2], vt_ax[3])

    tela.close()

if __name__ == "__main__":
    main()