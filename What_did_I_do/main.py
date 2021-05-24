import random
from graphics import *

def dentro(x, y):
    return x >= 0 and x <= 400 and y >= 0 and y <= 300

def forcaDraw(janela, plano):
    barra1 = plano[0]
    barra2 = plano[1]
    barra3 = plano[2]
    lin = plano[3]
    txt = plano[4]
    uses = plano[5]

    barra1.setFill("black")
    barra2.setFill("black")
    barra3.setFill("black")

    txt.setFace("courier")

    uses.setFace("courier")
    uses.setStyle("bold")
    uses.draw(janela)

    uses = plano[6]
    uses.setFace("courier")
    uses.setStyle("bold")
    uses.draw(janela)

    barra1.draw(janela)
    barra2.draw(janela)
    barra3.draw(janela)
    lin.draw(janela)
    txt.draw(janela)

def criaJogo(janela, plano, rec, inicia, itens, att, xp, yp, lx1, lx2, ly1, ly2):
    if att:
        if xp >= lx1 and xp <= lx2 and yp >= ly1 and yp <= ly2:
            rec.setFill("green")

            update(5)
            update(30)
            for i in itens:
                i.undraw()

            forcaDraw(janela, plano)
            inicia = True
            att = False
        else:
            rec.setFill("gray")
    
    return inicia, att

def purpleFaceMove(janela, ppFace, key, itens, plano):

    ponto = ppFace.getAnchor()
    xp = ponto.getX()
    yp = ponto.getY()

    if key == "Left" and dentro(xp, yp):
        ppFace.move(-5, 0)
    elif key == "Right" and dentro(xp, yp):
        ppFace.move(5, 0)
    elif key == "Down" and dentro(xp, yp):
        ppFace.move(0, 5)
    elif key == "Up" and dentro(xp, yp):
        ppFace.move(0, -5)

    if xp < 0:
        ppFace.move(405, 0)
    elif xp > 400:
        ppFace.move(-405, 0)
    if yp < 0:
        ppFace.move(0, 305)
    elif yp > 300:
        ppFace.move(0, -305)

def animacao(janela, ser_mov, dire, des, acabou):
    if des == True:
        for parte in list(ser_mov):
            parte.draw(janela)
        des = False

    pos = ser_mov[0].getCenter()

    if pos.getY() >= 40:
        dire = 2
    elif pos.getY() <= 26:
        dire = 1

    if dire == 1:
        for parte in list(ser_mov):
            parte.move(0, 0.4)
    elif dire == 2:
        for parte in list(ser_mov):
            parte.move(0, -0.4)

    if acabou:
        for parte in list(ser_mov):
            parte.undraw()

    return dire, des

def usarpalavra(janela, key, alfabeto, alfabeto_check, alfabeto_un, un_alfa, un_alfaP, acabou):
    if acabou == False:
        cnt = 0
        for i in range(9):
            if alfabeto_un[cnt] == False:
                aumento = 30*(i+1)
                risquinho = Line(Point(15+aumento, 185),
                                 Point(35+aumento, 185))
                risquinho.draw(janela)
                alfabeto_un[cnt] = True
                un_alfa.append(risquinho)
            cnt += 1
        for i in range(9):
            if alfabeto_un[cnt] == False:
                aumento = 30*(i+1)
                risquinho = Line(Point(15+aumento, 215),
                                 Point(35+aumento, 215))
                risquinho.draw(janela)
                alfabeto_un[cnt] = True
                un_alfa.append(risquinho)
            cnt += 1
        for i in range(8):
            if alfabeto_un[cnt] == False:
                aumento = 30*(i+1)
                risquinho = Line(Point(15+aumento, 245),
                                 Point(35+aumento, 245))
                risquinho.draw(janela)
                alfabeto_un[cnt] = True
                un_alfa.append(risquinho)
            cnt += 1

        cnt = 0
        for i in range(9):
            if alfabeto_check[cnt] == False and (key == alfabeto[cnt].upper() or key == alfabeto[cnt].lower()):
                aumento = 30*(i+1)
                txt = Text(Point(25+aumento, 175), alfabeto[cnt].upper())
                txt.draw(janela)
                alfabeto_check[cnt] = True
                un_alfaP.append(txt)
            cnt += 1
        for i in range(9):
            if alfabeto_check[cnt] == False and (key == alfabeto[cnt].upper() or key == alfabeto[cnt].lower()):
                aumento = 30*(i+1)
                txt = Text(Point(25+aumento, 205), alfabeto[cnt].upper())
                txt.draw(janela)
                alfabeto_check[cnt] = True
                un_alfaP.append(txt)
            cnt += 1
        for i in range(8):
            if alfabeto_check[cnt] == False and (key == alfabeto[cnt].upper() or key == alfabeto[cnt].lower()):
                aumento = 30*(i+1)
                txt = Text(Point(25+aumento, 235), alfabeto[cnt].upper())
                txt.draw(janela)
                alfabeto_check[cnt] = True
                un_alfaP.append(txt)
            cnt += 1
    return un_alfa, un_alfaP

def attChances(janela, chances, num_chance, ser, ser_mov, plano, un_ris, un_pal, un_alfa, un_alfaP, acabou):
    if chances == 6:
        num_chance.undraw()
        num_chance = Text(Point(375, 280), "6")
        num_chance.setFace("courier")
        num_chance.setStyle("bold")
        num_chance.draw(janela)

        ser[0].draw(janela)

    elif chances == 5:
        num_chance.undraw()
        num_chance = Text(Point(375, 280), "5")
        num_chance.setFace("courier")
        num_chance.setStyle("bold")
        num_chance.draw(janela)

        ser[1].draw(janela)

    elif chances == 4:
        num_chance.undraw()
        num_chance = Text(Point(375, 280), "4")
        num_chance.setFace("courier")
        num_chance.setStyle("bold")
        num_chance.draw(janela)

        ser[2].draw(janela)

    elif chances == 3:
        num_chance.undraw()
        num_chance = Text(Point(375, 280), "3")
        num_chance.setFace("courier")
        num_chance.setStyle("bold")
        num_chance.draw(janela)

        ser[3].draw(janela)

    elif chances == 2:
        num_chance.undraw()
        num_chance = Text(Point(375, 280), "2")
        num_chance.setFace("courier")
        num_chance.setStyle("bold")
        num_chance.draw(janela)

        ser[4].draw(janela)

    elif chances == 1:
        num_chance.undraw()
        num_chance = Text(Point(375, 280), "1")
        num_chance.setFace("courier")
        num_chance.setStyle("bold")
        num_chance.draw(janela)

        ser[5].draw(janela)

    elif chances == 0:
        num_chance.undraw()
        num_chance = Text(Point(375, 280), "0")
        num_chance.setFace("courier")
        num_chance.setStyle("bold")
        num_chance.draw(janela)

        update(1)
        update(30)
        num_chance.undraw()
        for partes in ser:
            partes.undraw()
        for partes in ser_mov:
            partes.undraw()
        for partes in plano:
            partes.undraw()
        for partes in un_ris:
            partes.undraw()
        for partes in un_pal:
            partes.undraw()
        for partes in un_alfa:
            partes.undraw()
        for partes in un_alfaP:
            partes.undraw()
        acabou = True

    elif chances == 10:
        update(1)
        update(30)
        num_chance.undraw()
        for partes in ser:
            partes.undraw()
        for partes in ser_mov:
            partes.undraw()
        for partes in plano:
            partes.undraw()
        for partes in un_ris:
            partes.undraw()
        for partes in un_pal:
            partes.undraw()
        for partes in un_alfa:
            partes.undraw()
        for partes in un_alfaP:
            partes.undraw()
        acabou = True

    return num_chance, chances, ser, ser_mov, plano, un_ris, un_pal, un_alfa, un_alfaP, acabou

def jogo_velha(janela, troca, palavra, under_p, check_un, risq_un, key, alfabeto, alfabeto_check, alfabeto_un, chances, num_chance, ser, ser_mov, plano, un_ris, un_pal, un_alfa, un_alfaP, acabou,anima):
    if troca:
        troca = False

        arq = open("palavras.txt")
        lista_palavras = arq.readlines()
        arq.close()

        indic = random.randint(0, 99)
        ax = lista_palavras[indic]

        palavra = ""

        for i in range(len(ax)):
            palavra += ax[i]+" "

        palavra = palavra.split()

        under_p = []
        check_un = []
        risq_un = []
        alfabeto = []
        alfabeto_check = []
        alfabeto_un = []
        chances = 7

        num_chance = Text(Point(375, 280), "7")
        num_chance.setFace("courier")
        num_chance.setStyle("bold")
        num_chance.draw(janela)

        for i in range(len(palavra)):
            under_p.append(False)
            check_un.append(False)
            risq_un.append(False)

        for i in range(26):
            alfabeto_check.append(False)
            alfabeto_un.append(False)
            alfabeto.append(chr(i+ord('a')))

    encontrou = False
    click = False
    for i in range(len(palavra)):
        if key == palavra[i].lower() or key == palavra[i].upper():
            under_p[i] = True
            encontrou = True
            click = True
        elif key >= 'a' and key <= 'z':
            click = True

        if under_p[i] == False and risq_un[i] == False:
            aumento = 30*(i+1)
            risquinho = Line(Point(30+aumento, 115), Point(50+aumento, 115))
            risquinho.draw(janela)
            un_ris.append(risquinho)
            risq_un[i] = True
        elif under_p[i] and not(check_un[i]):
            aumento = 30*(i+1)
            txt = Text(Point(40+aumento, 105), palavra[i])
            txt.draw(janela)
            un_pal.append(txt)
            check_un[i] = True

    testando = True
    for i in check_un:
        if i == False:
           testando = False

    if testando:
       chances = 11
       encontrou = False

    if not(encontrou) and click:
        num_chance, chances, ser, ser_mov, plano, un_ris, un_pal, un_alfa, un_alfaP, acabou = attChances(
            janela, chances - 1, num_chance, ser, ser_mov, plano, un_ris, un_pal, un_alfa, un_alfaP, acabou)

    un_alfa, un_alfaP = usarpalavra(
        janela, key, alfabeto, alfabeto_check, alfabeto_un, un_alfa, un_alfaP, acabou)



    if acabou:
        troca = True
        anima = False

    return troca, palavra, under_p, check_un, risq_un, alfabeto, alfabeto_check, alfabeto_un, chances, num_chance, ser, ser_mov, plano, un_ris, un_pal, un_alfa, un_alfaP, acabou, anima

def derrota(janela, plano, key, after_game, der, pos, loseFaces, lose_moves, inicia_game, palavra,txt_palavra):
    if not(after_game):
        for partes in der:
            partes.draw(janela)
        for partes in loseFaces:
            partes.draw(janela)
        after_game = True

        txt_palavra_fr = Text(Point(135, 55),"A palavra era:")
        txt_palavra_fr.setFace("courier")
        txt_palavra_fr.draw(janela)
        der.append(txt_palavra_fr)

        txt_palavra = []
        for i in range(len(palavra)):
            ax_palavra = Text(Point(210+(10*i), 56), palavra[i])
            ax_palavra.setFace("courier")
            ax_palavra.setFill("blue")
            ax_palavra.setStyle("bold")
            ax_palavra.draw(janela)
            txt_palavra.append(ax_palavra)
            

    if pos.getX() >= 45 and pos.getX() <= 155 and pos.getY() >= 240 and pos.getY() <= 260:
        der[1].setFill("green")

        update(5)
        update(30)
        
        for partes in der:
            partes.undraw()
        for faces in loseFaces:
            faces.undraw()
        for partes in txt_palavra:
            partes.undraw()

        inicia_game = True

        forcaDraw(janela, plano)
    else:
        der[1].setFill("gray")
    if pos.getX() >= 265 and pos.getX() <= 335 and pos.getY() >= 240 and pos.getY() <= 260:
        der[3].setFill("yellow")
        update(5)
        key = "Escape"
    else:
        der[3].setFill("gray")

    ind = 0
    for i in loseFaces:
        pos_x = i.getAnchor().getX()
        pos_y = i.getAnchor().getY()

        if lose_moves[ind] == 1 and pos_x < 90:
            lose_moves[ind] = 2
        elif lose_moves[ind] == 2 and pos_y > 165:
            lose_moves[ind] = 3
        elif lose_moves[ind] == 3 and pos_x > 310:
            lose_moves[ind] = 4
        elif lose_moves[ind] == 4 and pos_y < 115:
            lose_moves[ind] = 1

        if lose_moves[ind] == 1:
            i.move(-3,0)
        elif lose_moves[ind] == 2:
            i.move(0,3)
        elif lose_moves[ind] == 3:
            i.move(3,0)
        elif lose_moves[ind] == 4:
            i.move(0,-3)

        ind += 1

    return key, after_game, der, loseFaces, lose_moves, inicia_game, txt_palavra

def vitoria(janela, plano, key, after_game, win, pos, winFaces, win_moves, inicia_game, palavra,txt_palavra):
    if not(after_game):
        for partes in win:
            partes.draw(janela)
        for partes in winFaces:
            partes.draw(janela)
        after_game = True

        txt_palavra_fr = Text(Point(135, 55),"A palavra era:")
        txt_palavra_fr.setFace("courier")
        txt_palavra_fr.draw(janela)
        win.append(txt_palavra_fr)

        txt_palavra = []
        for i in range(len(palavra)):
            ax_palavra = Text(Point(210+(10*i), 56), palavra[i])
            ax_palavra.setFace("courier")
            ax_palavra.setFill("blue")
            ax_palavra.setStyle("bold")
            ax_palavra.draw(janela)
            txt_palavra.append(ax_palavra)

    if pos.getX() >= 45 and pos.getX() <= 155 and pos.getY() >= 240 and pos.getY() <= 260:
        win[1].setFill("green")

        update(5)
        update(30)
        
        for partes in win:
            partes.undraw()
        for faces in winFaces:
            faces.undraw()
        for partes in txt_palavra:
            partes.undraw()

        inicia_game = True

        forcaDraw(janela, plano)
    else:
        win[1].setFill("gray")
    if pos.getX() >= 265 and pos.getX() <= 335 and pos.getY() >= 240 and pos.getY() <= 260:
        win[3].setFill("yellow")
        update(5)
        key = "Escape"
    else:
        win[3].setFill("gray")

    ind = 0
    for i in winFaces:
        pos_x = i.getAnchor().getX()
        pos_y = i.getAnchor().getY()

        if win_moves[ind] == 1 and pos_x > 310:
            win_moves[ind] = 2
        elif win_moves[ind] == 2 and pos_y > 165:
            win_moves[ind] = 3
        elif win_moves[ind] == 3 and pos_x < 90:
            win_moves[ind] = 4
        elif win_moves[ind] == 4 and pos_y < 115:
            win_moves[ind] = 1

        if win_moves[ind] == 1:
            i.move(3,0)
        elif win_moves[ind] == 2:
            i.move(0,3)
        elif win_moves[ind] == 3:
            i.move(-3,0)
        elif win_moves[ind] == 4:
            i.move(0,-3)

        ind += 1

    return key, after_game, win, winFaces, win_moves, inicia_game, txt_palavra

def main():
    janela = GraphWin("Estrela's Jogo da Forca", 400, 300)

    faces = ["purpleFace.png", "kingFace.png", "loseFace.png"]

    purpleFace = Image(Point(350, 45), faces[0])
    purpleFace.draw(janela)

    l_f1 = Image(Point(235, 115), faces[2])
    l_f2 = Image(Point(170, 115), faces[2])
    l_f3 = Image(Point(115, 115), faces[2])
    l_f4 = Image(Point(235, 165), faces[2])
    l_f5 = Image(Point(170, 165), faces[2])
    l_f6 = Image(Point(285, 165), faces[2])

    loseFaces = [l_f1, l_f2, l_f3, l_f4, l_f5, l_f6]
    lose_moves = [1, 1, 1, 3, 3, 3]

    w_f1 = Image(Point(235, 115), faces[1])
    w_f2 = Image(Point(170, 115), faces[1])
    w_f3 = Image(Point(115, 115), faces[1])
    w_f4 = Image(Point(235, 165), faces[1])
    w_f5 = Image(Point(170, 165), faces[1])
    w_f6 = Image(Point(285, 165), faces[1])

    winFaces = [w_f1, w_f2, w_f3, w_f4, w_f5, w_f6]
    win_moves = [1, 1, 1, 3, 3, 3]

    frs = Text(Point(185, 25), 'Mexa o PurpleFace até "PLAY" (≧▽≦)')
    frs.setFace("courier")
    frs.draw(janela)
    frs2 = Text(Point(170, 45), 'Aperte "ESC" para sair do jogo :(')
    frs2.setFace("courier")
    frs2.draw(janela)

    rect_jog = Rectangle(Point(175, 140), Point(225, 160))
    rect_jog.setFill("gray")
    rect_jog.draw(janela)
    jogar = Text(Point(200, 150), "PLAY")
    jogar.setStyle("bold")
    jogar.draw(janela)

    itens = [frs, rect_jog, frs2, jogar]

    game_on = False
    dire = 1
    des = True
    ozinho = Circle(Point(230, 26), 3)
    linha = Line(Point(230, -50), Point(230, 23))
    mao1 = Line(Point(230, 34), Point(225, 44))
    mao2 = Line(Point(230, 34), Point(235, 44))
    perna1 = Line(Point(230, 44), Point(225, 54))
    perna2 = Line(Point(230, 44), Point(235, 54))
    corpo_m = Line(Point(230, 29), Point(230, 44))

    ser_mov = [ozinho, linha, mao1, mao2, perna1, perna2, corpo_m]

    cabeca = Circle(Point(105, 49), 6)
    corpo = Line(Point(105, 55), Point(105, 75))
    mao_esq = Line(Point(105, 62), Point(90, 47))
    mao_dir = Line(Point(105, 62), Point(120, 47))
    per_esq = Line(Point(105, 75), Point(95, 87))
    per_dir = Line(Point(105, 75), Point(115, 87))

    ser = [cabeca, corpo, mao_esq, mao_dir, per_esq, per_dir]

    barra1 = Rectangle(Point(25, 15), Point(35, 110))
    barra2 = Rectangle(Point(20, 20), Point(110, 30))
    barra3 = Rectangle(Point(20, 110), Point(40, 115))
    lin = Line(Point(105, 30), Point(105, 43))
    txt = Text(Point(200, 25), "Jogo da F rca")
    uses = Text(Point(95, 150), "PALAVRAS USADAS:")
    uses_C = Text(Point(285, 280), "CHANCES SOBRANDO:")

    plano = [barra1, barra2, barra3, lin, txt, uses, uses_C]

    txt_derrota = Text(Point(200, 140), "YOU LOSE")
    txt_derrota.setFace("arial")
    txt_derrota.setFill("red")
    txt_derrota.setStyle("bold")
    txt_derrota.setSize(30)
    txt_win = Text(Point(200, 140), "YOU WIN!")
    txt_win.setFace("arial")
    txt_win.setFill("green")
    txt_win.setStyle("bold")
    txt_win.setSize(30)
    rect_jog_again = Rectangle(Point(45, 240), Point(155, 260))
    rect_jog_again.setFill("gray")
    jogar_again = Text(Point(100, 250), "PLAY AGAIN")
    jogar_again.setStyle("bold")
    rect_sai = Rectangle(Point(265, 240), Point(335, 260))
    rect_sai.setFill("gray")
    sair = Text(Point(300, 250), "LEAVE")
    sair.setStyle("bold")
    

    der = [txt_derrota, rect_jog_again,
           jogar_again, rect_sai, sair]

    win = [txt_win, rect_jog_again,jogar_again,rect_sai,sair]

    troca_palavra = True
    palavra = ""
    under_p = []
    check_un = []
    risq_un = []
    alfabeto = []
    alfabeto_check = []
    alfabeto_un = []
    un_ris = []
    un_pal = []
    un_alfa = []
    un_alfaP = []
    txt_palavra = []
    chances = 0
    acabou = False
    num_chance = -1

    inicia_game = True
    after_game = False
    att = True
    lx_1 =175
    lx_2 =225
    ly_1 =140
    ly_2 =160

    anima = False

    key = janela.checkKey()
    while key != "Escape":
        key = janela.checkKey()

        purpleFaceMove(janela, purpleFace, key, itens, plano)

        if att:
            inicia_game, att = criaJogo(janela,plano,itens[1],itens,inicia_game,att,purpleFace.getAnchor().getX(),purpleFace.getAnchor().getY(),lx_1,lx_2,ly_1,ly_2)
        elif inicia_game and att == False:
            game_on = True
            anima = True
            des = True
            anima = True
            acabou = False
            after_game = False
            inicia_game = False

        if game_on:
            troca_palavra, palavra, under_p, check_un, risq_un, alfabeto, alfabeto_check, alfabeto_un, chances, num_chance, ser, ser_mov, plano, un_ris, un_pal, un_alfa, un_alfaP, acabou, anima = jogo_velha(
                janela, troca_palavra, palavra, under_p, check_un, risq_un, key, alfabeto, alfabeto_check, alfabeto_un, chances, num_chance, ser, ser_mov, plano, un_ris, un_pal, un_alfa, un_alfaP, acabou, anima)
        if acabou:
                game_on = False

        if anima:
            dire, des = animacao(janela, ser_mov, dire, des, acabou)

        if acabou and chances == 0:
            key, after_game, der, loseFaces, lose_moves, inicia_game, txt_palavra = derrota(
                janela,plano, key, after_game, der, purpleFace.getAnchor(), loseFaces, lose_moves, inicia_game,palavra, txt_palavra)
            itens = []
            for partes in der:
                itens.append(partes)
            lx_1 = 55
            lx_2 = 155
            ly_1 = 240
            ly_2 = 260
        elif acabou and chances > 0:
            key, after_game, win, winFaces, win_moves, inicia_game, txt_palavra = vitoria(
                janela,plano, key, after_game, win, purpleFace.getAnchor(), winFaces, win_moves, inicia_game,palavra, txt_palavra)
            itens = []
            for partes in win:
                itens.append(partes)
            lx_1 = 55
            lx_2 = 155
            ly_1 = 240
            ly_2 = 260

        update(30)

    janela.close()


if __name__ == "__main__":
    main()