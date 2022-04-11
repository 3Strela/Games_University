from graphics import *
from time import sleep
from random import randint

def modText(var, cor, familia, estilo, tamanho):
    var.setFill(cor)
    var.setFace(familia)
    var.setStyle(estilo)
    var.setSize(tamanho)
    return var

def resetaposicoes(tela, tab_desenho):
    troca = True

    for i in range(8):
        for j in range(8):
            if troca:
                tab_desenho[i][j].setFill(color_rgb(204, 204, 255))
            else:
                tab_desenho[i][j].setFill(color_rgb(68, 68, 34))
            troca = not(troca)
        troca = not(troca)

    return tab_desenho

def mostrarposicoesvalidas(tela, tab, i, j, tab_desenho):
    opcoes = []
    if tab[i][j] == 'tb' or tab[i][j] == 'tp':
        cont = 1
        while i-cont >= 0 and tab[i-cont][j] == 'ev':
            tab_desenho[i-cont][j].setFill('green')
            opcoes.append((i-cont, j))
            cont+=1
        if i-cont >= 0 and tab[i-cont][j][1] != tab[i][j][1]: 
            tab_desenho[i-cont][j].setFill('red')
            opcoes.append((i-cont, j))
        
        cont = 1
        while i+cont < 8 and tab[i+cont][j] == 'ev':
            tab_desenho[i+cont][j].setFill('green')
            opcoes.append((i+cont, j))
            cont+=1
        if i+cont < 8 and tab[i+cont][j][1] != tab[i][j][1]: 
            tab_desenho[i+cont][j].setFill('red')
            opcoes.append((i+cont, j))
        
        cont = 1
        while j-cont >= 0 and tab[i][j-cont] == 'ev':
            tab_desenho[i][j-cont].setFill('green')
            opcoes.append((i, j-cont))
            cont+=1
        if j-cont >= 0 and tab[i][j-cont][1] != tab[i][j][1]: 
            tab_desenho[i][j-cont].setFill('red')
            opcoes.append((i, j-cont))

        cont = 1
        while j+cont < 8 and tab[i][j+cont] == 'ev':
            tab_desenho[i][j+cont].setFill('green')
            opcoes.append((i, j+cont))
            cont+=1
        if j+cont < 8 and tab[i][j+cont][1] != tab[i][j][1]: 
            tab_desenho[i][j+cont].setFill('red')
            opcoes.append((i, j+cont))

    elif tab[i][j] == 'cb' or tab[i][j] == 'cp':
        if i-2 >= 0 and j - 1 >= 0:
            if tab[i-2][j-1] == 'ev':
                tab_desenho[i-2][j-1].setFill('green')
                opcoes.append((i-2, j-1))
            elif tab[i-2][j-1][1] != tab[i][j][1]:
                tab_desenho[i-2][j-1].setFill('red')
                opcoes.append((i-2,j-1))
        if i-2 >= 0 and j + 1 < 8:
            if tab[i-2][j+1] == 'ev':
                tab_desenho[i-2][j+1].setFill('green')
                opcoes.append((i-2,j+1))
            elif tab[i-2][j+1][1] != tab[i][j][1]:
                tab_desenho[i-2][j+1].setFill('red')
                opcoes.append((i-2,j+1))
        if i-1 >= 0 and j - 2 >= 0:
            if tab[i-1][j-2] == 'ev':
                tab_desenho[i-1][j-2].setFill('green')
                opcoes.append((i-1,j-2))
            elif tab[i-1][j-2][1] != tab[i][j][1]:
                tab_desenho[i-1][j-2].setFill('red')
                opcoes.append((i-1,j-2))
        if i-1 >= 0 and j + 2 < 8:
            if tab[i-1][j+2] == 'ev':
                tab_desenho[i-1][j+2].setFill('green')
                opcoes.append((i-1,j+2))
            elif tab[i-1][j+2][1] != tab[i][j][1]:
                tab_desenho[i-1][j+2].setFill('red')
                opcoes.append((i-1,j+2))
        if i+2 < 8 and j - 1 >= 0:
            if tab[i+2][j-1] == 'ev':
                tab_desenho[i+2][j-1].setFill('green')
                opcoes.append((i+2,j-1))
            elif tab[i+2][j-1][1] != tab[i][j][1]:
                tab_desenho[i+2][j-1].setFill('red')
                opcoes.append((i+2,j-1))
        if i+2 < 8 and j + 1 < 8:
            if tab[i+2][j+1] == 'ev':
                tab_desenho[i+2][j+1].setFill('green')
                opcoes.append((i+2,j+1))
            elif tab[i+2][j+1][1] != tab[i][j][1]:
                tab_desenho[i+2][j+1].setFill('red')
                opcoes.append((i+2,j+1))
        if i+1 < 8 and j - 2 >= 0:
            if tab[i+1][j-2] == 'ev':
                tab_desenho[i+1][j-2].setFill('green')
                opcoes.append((i+1,j-2))
            elif tab[i+1][j-2][1] != tab[i][j][1]:
                tab_desenho[i+1][j-2].setFill('red')
                opcoes.append((i+1,j-2))
        if i+1 < 8 and j + 2 < 8:
            if tab[i+1][j+2] == 'ev':
                tab_desenho[i+1][j+2].setFill('green')
                opcoes.append((i+1,j+2))
            elif tab[i+1][j+2][1] != tab[i][j][1]:
                tab_desenho[i+1][j+2].setFill('red')
                opcoes.append((i+1,j+2))

    elif tab[i][j] == 'bb' or tab[i][j] == 'bp':
        cont = 1
        while i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont] == 'ev':
            tab_desenho[i-cont][j-cont].setFill('green')
            opcoes.append((i-cont, j-cont))
            cont+=1
        if i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont][1] != tab[i][j][1]: 
            tab_desenho[i-cont][j-cont].setFill('red')
            opcoes.append((i-cont, j-cont))

        cont = 1
        while i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont] == 'ev':
            tab_desenho[i+cont][j-cont].setFill('green')
            opcoes.append((i+cont, j-cont))
            cont+=1
        if i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont][1] != tab[i][j][1]: 
            tab_desenho[i+cont][j-cont].setFill('red')
            opcoes.append((i+cont, j-cont))

        cont = 1
        while i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont] == 'ev':
            tab_desenho[i+cont][j+cont].setFill('green')
            opcoes.append((i+cont, j+cont))
            cont+=1
        if i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont][1] != tab[i][j][1]: 
            tab_desenho[i+cont][j+cont].setFill('red')
            opcoes.append((i+cont, j+cont))

        cont = 1
        while i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont] == 'ev':
            tab_desenho[i-cont][j+cont].setFill('green')
            opcoes.append((i-cont, j+cont))
            cont+=1
        if i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont][1] != tab[i][j][1]: 
            tab_desenho[i-cont][j+cont].setFill('red')
            opcoes.append((i-cont, j+cont))

    elif tab[i][j] == 'kb' or tab[i][j] == 'kp':
        if i-1 >= 0 and j - 1 >= 0:
            if tab[i-1][j-1] == 'ev':
                tab_desenho[i-1][j-1].setFill('green')
                opcoes.append((i-1, j-1))
            elif tab[i-1][j-1][1] != tab[i][j][1]:
                tab_desenho[i-1][j-1].setFill('red')
                opcoes.append((i-1, j-1))
        if i-1 >= 0:
            if tab[i-1][j] == 'ev':
                tab_desenho[i-1][j].setFill('green')
                opcoes.append((i-1, j))
            elif tab[i-1][j][1] != tab[i][j][1]:
                tab_desenho[i-1][j].setFill('red')
                opcoes.append((i-1, j))
        if i-1 >= 0 and j + 1 < 8:
            if tab[i-1][j+1] == 'ev':
                tab_desenho[i-1][j+1].setFill('green')
                opcoes.append((i-1, j+1))
            elif tab[i-1][j+1][1] != tab[i][j][1]:
                tab_desenho[i-1][j+1].setFill('red')
                opcoes.append((i-1, j+1))
        if j + 1 < 8:
            if tab[i][j+1] == 'ev':
                tab_desenho[i][j+1].setFill('green')
                opcoes.append((i, j+1))
            elif tab[i][j+1][1] != tab[i][j][1]:
                tab_desenho[i][j+1].setFill('red')
                opcoes.append((i, j+1))
        if i+1 < 8 and j + 1 < 8:
            if tab[i+1][j+1] == 'ev':
                tab_desenho[i+1][j+1].setFill('green')
                opcoes.append((i+1, j+1))
            elif tab[i+1][j+1][1] != tab[i][j][1]:
                tab_desenho[i+1][j+1].setFill('red')
                opcoes.append((i+1, j+1))
        if i+1  < 8:
            if tab[i+1][j] == 'ev':
                tab_desenho[i+1][j].setFill('green')
                opcoes.append((i+1, j))
            elif tab[i+1][j][1] != tab[i][j][1]:
                tab_desenho[i+1][j].setFill('red')
                opcoes.append((i+1, j))
        if i+1  < 8 and j - 1 >= 0:
            if tab[i+1][j-1] == 'ev':
                tab_desenho[i+1][j-1].setFill('green')
                opcoes.append((i+1, j-1))
            elif tab[i+1][j-1][1] != tab[i][j][1]:
                tab_desenho[i+1][j-1].setFill('red')
                opcoes.append((i+1, j-1))
        if j - 1 >= 0:
            if tab[i][j-1] == 'ev':
                tab_desenho[i][j-1].setFill('green')
                opcoes.append((i, j-1))
            elif tab[i][j-1][1] != tab[i][j][1]:
                tab_desenho[i][j-1].setFill('red')
                opcoes.append((i, j-1))

    elif tab[i][j] == 'rb' or tab[i][j] == 'rp':
        cont = 1
        while i-cont >= 0 and tab[i-cont][j] == 'ev':
            tab_desenho[i-cont][j].setFill('green')
            opcoes.append((i-cont, j))
            cont+=1
        if i-cont >= 0 and tab[i-cont][j][1] != tab[i][j][1]: 
            tab_desenho[i-cont][j].setFill('red')
            opcoes.append((i-cont, j))
        
        cont = 1
        while i+cont < 8 and tab[i+cont][j] == 'ev':
            tab_desenho[i+cont][j].setFill('green')
            opcoes.append((i+cont, j))
            cont+=1
        if i+cont < 8 and tab[i+cont][j][1] != tab[i][j][1]: 
            tab_desenho[i+cont][j].setFill('red')
            opcoes.append((i+cont, j))
        
        cont = 1
        while j-cont >= 0 and tab[i][j-cont] == 'ev':
            tab_desenho[i][j-cont].setFill('green')
            opcoes.append((i, j-cont))
            cont+=1
        if j-cont >= 0 and tab[i][j-cont][1] != tab[i][j][1]: 
            tab_desenho[i][j-cont].setFill('red')
            opcoes.append((i, j-cont))

        cont = 1
        while j+cont < 8 and tab[i][j+cont] == 'ev':
            tab_desenho[i][j+cont].setFill('green')
            opcoes.append((i, j+cont))
            cont+=1
        if j+cont < 8 and tab[i][j+cont][1] != tab[i][j][1]: 
            tab_desenho[i][j+cont].setFill('red')
            opcoes.append((i, j+cont))

        cont = 1
        while i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont] == 'ev':
            tab_desenho[i-cont][j-cont].setFill('green')
            opcoes.append((i-cont, j-cont))
            cont+=1
        if i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont][1] != tab[i][j][1]: 
            tab_desenho[i-cont][j-cont].setFill('red')
            opcoes.append((i-cont, j-cont))

        cont = 1
        while i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont] == 'ev':
            tab_desenho[i+cont][j-cont].setFill('green')
            opcoes.append((i+cont, j-cont))
            cont+=1
        if i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont][1] != tab[i][j][1]: 
            tab_desenho[i+cont][j-cont].setFill('red')
            opcoes.append((i+cont, j-cont))

        cont = 1
        while i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont] == 'ev':
            tab_desenho[i+cont][j+cont].setFill('green')
            opcoes.append((i+cont, j+cont))
            cont+=1
        if i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont][1] != tab[i][j][1]: 
            tab_desenho[i+cont][j+cont].setFill('red')
            opcoes.append((i+cont, j+cont))

        cont = 1
        while i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont] == 'ev':
            tab_desenho[i-cont][j+cont].setFill('green')
            opcoes.append((i-cont, j+cont))
            cont+=1
        if i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont][1] != tab[i][j][1]: 
            tab_desenho[i-cont][j+cont].setFill('red')
            opcoes.append((i-cont, j+cont))

    elif tab[i][j] == 'pb':
        if i == 1:
            if tab[i+1][j] == 'ev' and tab[i+2][j] == 'ev':
                tab_desenho[i+2][j].setFill('green')
                opcoes.append((i+2, j)) 
        if i + 1 < 8 and tab[i + 1][j] == 'ev':
            tab_desenho[i+1][j].setFill('green')
            opcoes.append((i+1, j))
        if i + 1 < 8 and j + 1 < 8 and tab[i+1][j+1][1] != tab[i][j][1] and tab[i+1][j+1] != 'ev':
            tab_desenho[i+1][j+1].setFill('red')
            opcoes.append((i+1, j+1))
        if i + 1 < 8 and j - 1 >= 0 and tab[i+1][j-1][1] != tab[i][j][1] and tab[i+1][j-1] != 'ev':
            tab_desenho[i+1][j-1].setFill('red')
            opcoes.append((i+1, j-1))

    elif tab[i][j] == 'pp':
        if i == 6:
            if tab[i-1][j] == 'ev' and tab[i-2][j] == 'ev':
                tab_desenho[i-2][j].setFill('green')
                opcoes.append((i-2, j)) 
        if i - 1 < 8 and tab[i - 1][j] == 'ev':
            tab_desenho[i-1][j].setFill('green')
            opcoes.append((i-1, j))
        if i - 1 < 8 and j + 1 < 8 and tab[i-1][j+1][1] != tab[i][j][1] and tab[i-1][j+1] != 'ev':
            tab_desenho[i-1][j+1].setFill('red')
            opcoes.append((i-1, j+1))
        if i - 1 < 8 and j - 1 >= 0 and tab[i-1][j-1][1] != tab[i][j][1] and tab[i-1][j-1] != 'ev':
            tab_desenho[i-1][j-1].setFill('red')
            opcoes.append((i-1, j-1))

    return opcoes

def movimentosCheck(tab, i, j):
    result = False

    if tab[i][j] == 'tb' or tab[i][j] == 'tp':
        cont = 1
        while i-cont >= 0 and tab[i-cont][j] == 'ev':
            cont += 1
        if i-cont >= 0 and tab[i-cont][j][1] != tab[i][j][1] and tab[i-cont][j][0] == 'k': 
            result = True
        cont = 1
        while i+cont < 8 and tab[i+cont][j] == 'ev':
            cont += 1
        if i+cont < 8 and tab[i+cont][j][1] != tab[i][j][1] and tab[i+cont][j][0] == 'k': 
            result = True
        cont = 1
        while j-cont >= 0 and tab[i][j-cont] == 'ev':
            cont += 1
        if j-cont >= 0 and tab[i][j-cont][1] != tab[i][j][1] and tab[i][j-cont][0] == 'k': 
            result = True
        cont = 1
        while j+cont < 8 and tab[i][j+cont] == 'ev':
            cont += 1
        if j+cont < 8 and tab[i][j+cont][1] != tab[i][j][1] and tab[i][j+cont][0] == 'k':
            result = True

    elif tab[i][j] == 'cb' or tab[i][j] == 'cp':
        if i-2 >= 0 and j - 1 >= 0 and tab[i-2][j-1][1] != tab[i][j][1] and tab[i-2][j-1][0] == 'k':
            result = True
        if i-2 >= 0 and j + 1 < 8 and tab[i-2][j+1][1] != tab[i][j][1] and tab[i-2][j+1][0] == 'k':
            result = True
        if i-1 >= 0 and j - 2 >= 0 and tab[i-1][j-2][1] != tab[i][j][1] and tab[i-1][j-2][0] == 'k':
            result = True
        if i-1 >= 0 and j + 2 < 8 and tab[i-1][j+2][1] != tab[i][j][1] and tab[i-1][j+2][0] == 'k':
            result = True
        if i+2 < 8 and j - 1 >= 0 and tab[i+2][j-1][1] != tab[i][j][1] and tab[i+2][j-1][0] == 'k':
            result = True
        if i+2 < 8 and j + 1 < 8 and tab[i+2][j+1][1] != tab[i][j][1] and tab[i+2][j+1][0] == 'k':
            result = True
        if i+1 < 8 and j - 2 >= 0 and tab[i+1][j-2][1] != tab[i][j][1] and tab[i+1][j-2][0] == 'k':
            result = True
        if i+1 < 8 and j + 2 < 8 and tab[i+1][j+2][1] != tab[i][j][1] and tab[i+1][j+2][0] == 'k':
            result = True

    elif tab[i][j] == 'bb' or tab[i][j] == 'bp':
        cont = 1
        while i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont] == 'ev':
            cont += 1
        if i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont][1] != tab[i][j][1] and tab[i-cont][j-cont][0] == 'k': 
            result = True
        cont = 1
        while i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont] == 'ev':
            cont += 1
        if i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont][1] != tab[i][j][1] and tab[i+cont][j-cont][0] == 'k': 
            result = True
        cont = 1
        while i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont] == 'ev':
            cont += 1
        if i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont][1] != tab[i][j][1] and tab[i+cont][j+cont][0] == 'k': 
            result = True
        cont = 1
        while i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont] == 'ev':
            cont += 1
        if i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont][1] != tab[i][j][1] and tab[i-cont][j+cont][0] == 'k': 
            result = True

    elif tab[i][j] == 'kb' or tab[i][j] == 'kp':
        if i-1 >= 0 and j - 1 >= 0 and tab[i-1][j-1][1] != tab[i][j][1] and tab[i-1][j-1][0] == 'k':
            result = True
        if i-1 >= 0 and tab[i-1][j][1] != tab[i][j][1] and tab[i-1][j][0] == 'k':
            result = True
        if i-1 >= 0 and j + 1 < 8 and tab[i-1][j+1][1] != tab[i][j][1] and tab[i-1][j+1][0] == 'k':
            result = True
        if j + 1 < 8 and tab[i][j+1][1] != tab[i][j][1] and tab[i][j+1][0] == 'k':
            result = True
        if i+1 < 8 and j + 1 < 8 and tab[i+1][j+1][1] != tab[i][j][1] and tab[i+1][j+1][0] == 'k':
            result = True
        if i+1  < 8 and tab[i+1][j][1] != tab[i][j][1] and tab[i+1][j][0] == 'k':
            result = True
        if i+1  < 8 and j - 1 >= 0 and tab[i+1][j-1][1] != tab[i][j][1] and tab[i+1][j-1][0] == 'k':
            result = True
        if j - 1 >= 0 and tab[i][j-1][1] != tab[i][j][1] and tab[i][j-1][0] == 'k': 
            result = True

    elif tab[i][j] == 'rb' or tab[i][j] == 'rp':
        cont = 1
        while i-cont >= 0 and tab[i-cont][j] == 'ev':
            cont += 1
        if i-cont >= 0 and tab[i-cont][j][1] != tab[i][j][1] and tab[i-cont][j][0] == 'k': 
            result = True
        cont = 1
        while i+cont < 8 and tab[i+cont][j] == 'ev':
            cont += 1
        if i+cont < 8 and tab[i+cont][j][1] != tab[i][j][1] and tab[i+cont][j][0] == 'k': 
            result = True
        cont = 1
        while j-cont >= 0 and tab[i][j-cont] == 'ev':
            cont += 1
        if j-cont >= 0 and tab[i][j-cont][1] != tab[i][j][1] and tab[i][j-cont][0] == 'k': 
            result = True
        cont = 1
        while j+cont < 8 and tab[i][j+cont] == 'ev':
            cont += 1
        if j+cont < 8 and tab[i][j+cont][1] != tab[i][j][1] and tab[i][j+cont][0] == 'k':
            result = True
        cont = 1
        while i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont] == 'ev':
            cont += 1
        if i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont][1] != tab[i][j][1] and tab[i-cont][j-cont][0] == 'k': 
            result = True
        cont = 1
        while i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont] == 'ev':
            cont += 1
        if i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont][1] != tab[i][j][1] and tab[i+cont][j-cont][0] == 'k': 
            result = True
        cont = 1
        while i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont] == 'ev':
            cont += 1
        if i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont][1] != tab[i][j][1] and tab[i+cont][j+cont][0] == 'k': 
            result = True
        cont = 1
        while i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont] == 'ev':
            cont += 1
        if i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont][1] != tab[i][j][1] and tab[i-cont][j+cont][0] == 'k': 
            result = True

    elif tab[i][j] == 'pb':
        if i + 1 < 8 and j + 1 < 8 and tab[i+1][j+1][1] != tab[i][j][1] and tab[i+1][j+1][0] == 'k':
            result = True
        elif i + 1 < 8 and j-1 >= 0 and tab[i+1][j-1][1] != tab[i][j][1] and tab[i+1][j-1][0] == 'k':
            result = True

    elif tab[i][j] == 'pp':
        if i - 1 >= 0 and j + 1 < 8 and tab[i-1][j+1][1] != tab[i][j][1] and tab[i-1][j+1][0] == 'k':
            result = True
        elif i - 1 >= 0 and j-1 >= 0 and tab[i-1][j-1][1] != tab[i][j][1] and tab[i-1][j-1][0] == 'k':
            result = True

    return result

def reiOpcoes(tab, vet):
    i = vet[0][0]
    j = vet[0][1]

    if i-1 >= 0 and j - 1 >= 0 and tab[i-1][j-1][1] != tab[i][j][1]:
        vet.append((i-1,j-1))
    if i-1 >= 0 and tab[i-1][j][1] != tab[i][j][1]:
        vet.append((i-1,j))
    if i-1 >= 0 and j + 1 < 8 and tab[i-1][j+1][1] != tab[i][j][1]:
        vet.append((i-1,j+1))
    if j + 1 < 8 and tab[i][j+1][1] != tab[i][j][1]:
        vet.append((i,j+1))
    if i+1 < 8 and j + 1 < 8 and tab[i+1][j+1][1] != tab[i][j][1]:
        vet.append((i+1,j+1))
    if i+1  < 8 and tab[i+1][j][1] != tab[i][j][1]:
        vet.append((i+1,j))
    if i+1  < 8 and j - 1 >= 0 and tab[i+1][j-1][1] != tab[i][j][1]:
        vet.append((i+1,j-1))
    if j - 1 >= 0 and tab[i][j-1][1] != tab[i][j][1]: 
        vet.append((i,j-1))

    return vet

def mateRei(tab, i, j, x, y):
    result = True

    if tab[i][j] == 'tb' or tab[i][j] == 'tp':
        cont = 1
        if i-cont >= 0 and i-cont == x and j == y: 
                result = False
        while i-cont >= 0 and tab[i-cont][j] == 'ev':
            cont += 1
            if i-cont >= 0 and i-cont == x and j == y: 
                result = False
        if i-cont >= 0 and i-cont == x and j == y: 
                result = False
        cont = 1
        if i+cont >= 0 and i+cont == x and j == y: 
                result = False
        while i+cont < 8 and tab[i+cont][j] == 'ev':
            cont += 1
            if i+cont >= 0 and i+cont == x and j == y: 
                result = False
        if i+cont >= 0 and i+cont == x and j == y: 
                result = False
        cont = 1
        if j-cont >= 0 and i == x and j-cont == y: 
                result = False
        while j-cont >= 0 and tab[i][j-cont] == 'ev':
            cont += 1
            if j-cont >= 0 and i == x and j-cont == y: 
                result = False
        if j-cont >= 0 and i == x and j-cont == y: 
                result = False
        cont = 1
        if j+cont >= 0 and i == x and j+cont == y: 
                result = False
        while j+cont < 8 and tab[i][j+cont] == 'ev':
            cont += 1
            if j+cont >= 0 and i == x and j+cont == y: 
                result = False
        if j+cont >= 0 and i == x and j+cont == y: 
                result = False

    elif tab[i][j] == 'cb' or tab[i][j] == 'cp':
        if i-2 >= 0 and j - 1 >= 0 and i-2 == x and j - 1 == y:
            result = False
        if i-2 >= 0 and j + 1 < 8 and i-2 == x and j + 1 == y:
            result = False
        if i-1 >= 0 and j - 2 >= 0 and i-1 == x and j - 2 == y:
            result = False
        if i-1 >= 0 and j + 2 < 8 and i-1 == x and j + 2 == y:
            result = False
        if i+2 < 8 and j - 1 >= 0 and i+2 == x and j - 1 == y:
            result = False
        if i+2 < 8 and j + 1 < 8 and +2 == x and j + 1 == y:
            result = False
        if i+1 < 8 and j - 2 >= 0 and i+1 == x and j - 2 == y:
            result = False
        if i+1 < 8 and j + 2 < 8 and i+1 == x and j + 2 == y:
            result = False

    elif tab[i][j] == 'bb' or tab[i][j] == 'bp':
        cont = 1
        if i-cont >= 0 and j-cont >= 0 and i-cont == x and j-cont == y: 
            result = False
        while i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont] == 'ev':
            cont += 1
            if i-cont >= 0 and j-cont >= 0 and i-cont == x and j-cont == y: 
                result = False
        if i-cont >= 0 and j-cont >= 0 and i-cont == x and j-cont == y: 
            result = False
        cont = 1
        if i+cont < 8 and j-cont >= 0 and i+cont == x and j-cont == y: 
            result = False
        while i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont] == 'ev':
            cont += 1
            if i+cont < 8 and j-cont >= 0 and i+cont == x and j-cont == y: 
                result = False
        if i+cont < 8 and j-cont >= 0 and i+cont == x and j-cont == y: 
            result = False
        cont = 1
        if i+cont < 8 and j+cont < 8 and i+cont == x and j+cont == y: 
            result = False
        while i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont] == 'ev':
            cont += 1
            if i+cont < 8 and j+cont < 8 and i+cont == x and j+cont == y: 
                result = False
        if i+cont < 8 and j+cont < 8 and i+cont == x and j+cont == y: 
            result = False
        cont = 1
        if i-cont >= 0 and j+cont < 8 and i-cont == x and j+cont == y: 
            result = False
        while i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont] == 'ev':
            cont += 1
            if i-cont >= 0 and j+cont < 8 and i-cont == x and j+cont == y: 
                result = False
        if i-cont >= 0 and j+cont < 8 and i-cont == x and j+cont == y: 
            result = False

    elif tab[i][j] == 'kb' or tab[i][j] == 'kp':
        if i-1 >= 0 and j - 1 >= 0 and i-1 == x and j - 1 == y:
            result = False
        if i-1 >= 0 and i-1 == x and j == y :
            result = False
        if i-1 >= 0 and j + 1 < 8 and i-1 == x and j + 1 == y:
            result = False
        if j + 1 < 8 and i == x and j + 1 == y:
            result = False
        if i+1 < 8 and j + 1 < 8 and i+1 == x and j + 1 == y:
            result = False
        if i+1  < 8 and i+1 == x and j == y:
            result = False
        if i+1  < 8 and j - 1 >= 0 and i+1 == x and j - 1 == y:
            result = False
        if j - 1 >= 0 and i == x and j - 1 == y: 
            result = False

    elif tab[i][j] == 'rb' or tab[i][j] == 'rp':
        cont = 1
        if i-cont >= 0 and i-cont == x and j == y: 
                result = False
        while i-cont >= 0 and tab[i-cont][j] == 'ev':
            cont += 1
            if i-cont >= 0 and i-cont == x and j == y: 
                result = False
        if i-cont >= 0 and i-cont == x and j == y: 
                result = False
        cont = 1
        if i+cont >= 0 and i+cont == x and j == y: 
                result = False
        while i+cont < 8 and tab[i+cont][j] == 'ev':
            cont += 1
            if i+cont >= 0 and i+cont == x and j == y: 
                result = False
        if i+cont >= 0 and i+cont == x and j == y: 
                result = False
        cont = 1
        if j-cont >= 0 and i == x and j-cont == y: 
                result = False
        while j-cont >= 0 and tab[i][j-cont] == 'ev':
            cont += 1
            if j-cont >= 0 and i == x and j-cont == y: 
                result = False
        if j-cont >= 0 and i == x and j-cont == y: 
                result = False
        cont = 1
        if j+cont >= 0 and i == x and j+cont == y: 
                result = False
        while j+cont < 8 and tab[i][j+cont] == 'ev':
            cont += 1
            if j+cont >= 0 and i == x and j+cont == y: 
                result = False
        if j+cont >= 0 and i == x and j+cont == y: 
                result = False
        cont = 1
        if i-cont >= 0 and j-cont >= 0 and i-cont == x and j-cont == y: 
            result = False
        while i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont] == 'ev':
            cont += 1
            if i-cont >= 0 and j-cont >= 0 and i-cont == x and j-cont == y: 
                result = False
        if i-cont >= 0 and j-cont >= 0 and i-cont == x and j-cont == y: 
            result = False
        cont = 1
        if i+cont < 8 and j-cont >= 0 and i+cont == x and j-cont == y: 
            result = False
        while i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont] == 'ev':
            cont += 1
            if i+cont < 8 and j-cont >= 0 and i+cont == x and j-cont == y: 
                result = False
        if i+cont < 8 and j-cont >= 0 and i+cont == x and j-cont == y: 
            result = False
        cont = 1
        if i+cont < 8 and j+cont < 8 and i+cont == x and j+cont == y: 
            result = False
        while i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont] == 'ev':
            cont += 1
            if i+cont < 8 and j+cont < 8 and i+cont == x and j+cont == y: 
                result = False
        if i+cont < 8 and j+cont < 8 and i+cont == x and j+cont == y: 
            result = False
        cont = 1
        if i-cont >= 0 and j+cont < 8 and i-cont == x and j+cont == y: 
            result = False
        while i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont] == 'ev':
            cont += 1
            if i-cont >= 0 and j+cont < 8 and i-cont == x and j+cont == y: 
                result = False
        if i-cont >= 0 and j+cont < 8 and i-cont == x and j+cont == y: 
            result = False

    elif tab[i][j] == 'pb':
        if i + 1 < 8 and j + 1 < 8 and i + 1 == x and j + 1 == y:
            result = False
        elif i + 1 < 8 and j - 1 >= 0 and i + 1 == x and j - 1 == y:
            result = False

    elif tab[i][j] == 'pp':
        if i - 1 >= 0 and j + 1 < 8 and i - 1 == x and j + 1 == y:
            result = False
        elif i - 1 >= 0 and j-1 >= 0 and i - 1 == x and j-1 == y:
            result = False

    return result

def fugirRei(tab, player_cor):
    op_rei = [] 
    pecas_adv = []
    i = -1
    j = -1
    if player_cor == 1:
        for i in range(8):
            for j in range(8):
                if tab[i][j] == 'kp':
                    op_rei.append((i, j))
                elif tab[i][j][1] != 'p' and tab[i][j] != 'ev':
                    pecas_adv.append((i,j))
    else:        
        for i in range(8):
            for j in range(8):
                if tab[i][j] == 'kb':
                    op_rei.append((i, j))
                elif tab[i][j][1] != 'b' and tab[i][j] != 'ev':
                    pecas_adv.append((i,j))

    op_rei = reiOpcoes(tab, op_rei)

    for posRei in op_rei:
        op = True
        for peca in pecas_adv:
            ax = mateRei(tab, peca[0], peca[1], posRei[0], posRei[1])
            if ax == False:
                op = False
        if op:
            i = posRei[0]
            j = posRei[1]
            break

    return (i, j)

def checaCheck(player_vez, tab, tela, player_cor):
    tipo_check = -1
    incheck = False

    vet_brancas = []
    vet_pretas = []
    for i in range(8):
        for j in range(8):
            if tab[i][j] == 'kb':
                vet_brancas.append((i,j))
            elif tab[i][j] == 'kp':
                vet_pretas.append((i,j))
    if len(vet_brancas) > 0:
        vet_brancas = reiOpcoes(tab, vet_brancas)
    if len(vet_pretas) > 0:
        vet_pretas = reiOpcoes(tab, vet_pretas)

    pecas_brancas = []
    pecas_pretas = []
    for i in range(8):
        for j in range(8):
            if tab[i][j][1] == 'b':
                pecas_brancas.append((i,j))
            elif tab[i][j][1] == 'p':
                pecas_pretas.append((i,j))

    mate_Brancas = False
    opcoes = 0
    if len(vet_brancas) > 0:
        for posRei in vet_brancas:
            op = True
            for peca in pecas_pretas:
                ax = mateRei(tab, peca[0], peca[1], posRei[0], posRei[1])
                if ax == False:
                    op = False
            if op:
                opcoes += 1
        if opcoes == 0:
            mate_Brancas = True
            tipo_check = 1

    mate_Pretas = False
    opcoes = 0
    if len(vet_pretas) > 0:
        vet_pretas = reiOpcoes(tab, vet_pretas)
        for posRei in vet_pretas:
            op = True
            for peca in pecas_brancas:
                ax = mateRei(tab, peca[0], peca[1], posRei[0], posRei[1])
                if ax == False:
                    op = False
            if op:
                opcoes += 1
        if opcoes == 0:
            mate_Pretas = True
            tipo_check = 2

    mate_Brancas = False
    mate_Pretas = False
    if tipo_check == -1 and mate_Brancas == False and mate_Pretas == False and len(vet_pretas) != 0 and len(vet_brancas) != 0:
        check_pretas = False
        for pecas in pecas_brancas:
            check_pretas = movimentosCheck(tab, pecas[0], pecas[1])
            if check_pretas:
                break

        check_brancas = False
        for pecas in pecas_pretas:
            check_brancas = movimentosCheck(tab, pecas[0], pecas[1])
            if check_brancas:
                break

        if check_pretas:
            msg = Text(Point(400, 570),'Pretas em Check')
            msg = modText(msg, 'gray', 'courier', 'bold', 20)
            msg.draw(tela)
            if player_cor == 1:
                incheck = True
            sleep(1.5)
            msg.undraw()
        
        if check_brancas:
            msg = Text(Point(400, 570),'Brancas em Check')
            msg = modText(msg, 'white', 'courier', 'bold', 20)
            msg.draw(tela)
            sleep(1.5)
            if player_cor == 0:
                incheck = True
            msg.undraw()    
    
    return tipo_check, incheck

def xadrezJogo(tela, tabuleiro, tab_desenho, tab_pecas, ppX, ppY):
    game_on = True
    player_vez = 1

    txt_player = Text(Point(400, 30),'Vez do player '+ str(player_vez))
    txt_player = modText(txt_player, 'white', 'courier', 'bold', 18)
    txt_player.draw(tela)

    winnerB = True
    check = -1

    while game_on:
        if check == -1:
            mouse = tela.getMouse()

        trocavez = False
        indI = -1
        indJ = -1

        if check == -1:
            for i in range(8):
                for j in range(8):
                    if mouse.getX() >= ppX*(j+1) and mouse.getX() <= ppX*(j+1)+ppX and mouse.getY() >= ppY*(i+1) and mouse.getY() <= ppY*(i+1)+ppY:
                        indI = i
                        indJ = j

            if (indI == -1 or indJ == -1) or (tabuleiro[indI][indJ] == 'ev'):
                msg = Text(Point(400, 570),'Selecione uma peca do tabuleiro')
                msg = modText(msg, 'red', 'courier', 'bold', 20)
                msg.draw(tela)
                sleep(1.5)
                msg.undraw()
            elif (tabuleiro[indI][indJ][1] == 'p' and player_vez == 1) or (tabuleiro[indI][indJ][1] == 'b' and player_vez == 2): 
                msg1 = Text(Point(350, 570),'Selecione uma peca sua')
                msg1 = modText(msg1, 'red', 'courier', 'bold', 20)
                msg1.draw(tela)
                if tabuleiro[indI][indJ][1] == 'p':
                    msg2 = Text(Point(580, 570),'  (Brancas)')
                    msg2 = modText(msg2, 'white', 'courier', 'bold', 20)
                else:
                    msg2 = Text(Point(580, 570),' (Pretas)')
                    msg2 = modText(msg2, 'gray', 'courier', 'bold', 20)    
                msg2.draw(tela)
                sleep(1.5)
                msg1.undraw()
                msg2.undraw()
            else:
                opcoes = mostrarposicoesvalidas(tela, tabuleiro, indI, indJ, tab_desenho)
                if len(opcoes) > 0:
                    mouse = tela.getMouse()
                    
                    indI_new = -1
                    indJ_new = -1

                    for i in range(8):
                        for j in range(8):
                            if mouse.getX() >= ppX*(j+1) and mouse.getX() <= ppX*(j+1)+ppX and mouse.getY() >= ppY*(i+1) and mouse.getY() <= ppY*(i+1)+ppY:
                                indI_new = i
                                indJ_new = j

                    pos_valida = False
                
                    for pos in opcoes:
                        if pos[0] == indI_new and pos[1] == indJ_new:
                            pos_valida = True

                    tab_desenho = resetaposicoes(tela, tab_desenho)

                    if pos_valida:
                        tab_pecas[indI][indJ].undraw() 
                        tab_pecas[indI_new][indJ_new].undraw()

                        if indI_new == 7 and tabuleiro[indI][indJ] == 'pb':
                            new_pos = Image(Point(ppX*(indJ_new+1)+ppX/2, ppY*(indI_new+1)+ppY/2), 'IMGS/rb.png')
                            tabuleiro[indI_new][indJ_new] = 'rb'
                        elif indI_new == 0 and tabuleiro[indI][indJ] == 'pp':
                            new_pos = Image(Point(ppX*(indJ_new+1)+ppX/2, ppY*(indI_new+1)+ppY/2), 'IMGS/rp.png')
                            tabuleiro[indI_new][indJ_new] = 'rp'
                        else:
                            new_pos = Image(Point(ppX*(indJ_new+1)+ppX/2, ppY*(indI_new+1)+ppY/2), 'IMGS/'+tabuleiro[indI][indJ]+'.png')
                            tabuleiro[indI_new][indJ_new] = tabuleiro[indI][indJ]
                        new_pos.draw(tela)
                        tab_pecas[indI_new][indJ_new] = new_pos
                        tabuleiro[indI][indJ] = 'ev'
                        trocavez = True
                        check = checaCheck(player_vez, tabuleiro, tela)
                    else:
                        msg = Text(Point(400, 570),'Selecione uma posição válida')
                        msg = modText(msg, 'red', 'courier', 'bold', 20)
                        msg.draw(tela)
                        sleep(1.5)
                        msg.undraw()
                else:
                    msg = Text(Point(400, 570),'Selecione uma peca que possa se movimentar')
                    msg = modText(msg, 'red', 'courier', 'bold', 20)
                    msg.draw(tela)
                    sleep(1.5)
                    msg.undraw()

            reiBrancos = False
            reiPretos = False
            for i in range(8):
                for j in range(8):
                    if tabuleiro[i][j] == 'kb':
                        reiBrancos = True
                    elif tabuleiro[i][j] == 'kp':
                        reiPretos = True

            if not(reiBrancos) or not(reiPretos):
                game_on = False
                if reiPretos:
                    winnerB = False 

            if trocavez and game_on:
                player_vez += 1
                if player_vez == 3:
                    player_vez = 1

                txt_player.undraw()
                txt_player = Text(Point(400, 30),'Vez do player '+ str(player_vez))
                if player_vez == 1:
                    txt_player = modText(txt_player, 'white', 'courier', 'bold', 18)
                else:
                    txt_player = modText(txt_player, 'gray', 'courier', 'bold', 18)
                txt_player.draw(tela)
        
        else:
            game_on = False

    for i in range(8):
        for j in range(8):
            tab_desenho[i][j].undraw()
            tab_pecas[i][j].undraw()

    txt_player.undraw()

    if check == 1:
        txt_win = Text(Point(400, 300),'Brancas em Check Mate')
        txt_win = modText(txt_win, 'white', 'courier', 'bold', 26)
        txt_win.draw(tela)
        sleep(2)
        txt_win.undraw()
        winnerB = False
 
    elif check == 2:
        txt_win = Text(Point(400, 300),'Pretas em Check Mate')
        txt_win = modText(txt_win, 'gray', 'courier', 'bold', 26)
        txt_win.draw(tela)
        sleep(2)
        txt_win.undraw()
        winnerB = True

    if winnerB:
        txt_win = Text(Point(400, 300),'Player 1 GANHOU!!')
        txt_win = modText(txt_win, 'white', 'courier', 'bold', 26)
        txt_win.draw(tela)
        sleep(2)
        txt_win.undraw()
    else:
        txt_win = Text(Point(400, 300),'Player 2 GANHOU!!')
        txt_win = modText(txt_win, 'gray', 'courier', 'bold', 26)
        txt_win.draw(tela)
        sleep(2)
        txt_win.undraw()

def comePecaBot(tab, i, j):
    result = False

    if tab[i][j] == 'tb' or tab[i][j] == 'tp':
        cont = 1
        while i-cont >= 0 and tab[i-cont][j] == 'ev':
            cont += 1
        if i-cont >= 0 and tab[i-cont][j][1] != tab[i][j][1] and tab[i-cont][j] != 'ev': 
            result = True
        cont = 1
        while i+cont < 8 and tab[i+cont][j] == 'ev':
            cont += 1
        if i+cont < 8 and tab[i+cont][j][1] != tab[i][j][1] and tab[i+cont][j] != 'ev': 
            result = True
        cont = 1
        while j-cont >= 0 and tab[i][j-cont] == 'ev':
            cont += 1
        if j-cont >= 0 and tab[i][j-cont][1] != tab[i][j][1] and tab[i][j-cont] != 'ev': 
            result = True
        cont = 1
        while j+cont < 8 and tab[i][j+cont] == 'ev':
            cont += 1
        if j+cont < 8 and tab[i][j+cont][1] != tab[i][j][1] and tab[i][j+cont] != 'ev':
            result = True

    elif tab[i][j] == 'cb' or tab[i][j] == 'cp':
        if i-2 >= 0 and j - 1 >= 0 and tab[i-2][j-1][1] != tab[i][j][1] and tab[i-2][j-1] != 'ev':
            result = True
        if i-2 >= 0 and j + 1 < 8 and tab[i-2][j+1][1] != tab[i][j][1] and tab[i-2][j+1] != 'ev':
            result = True
        if i-1 >= 0 and j - 2 >= 0 and tab[i-1][j-2][1] != tab[i][j][1] and tab[i-1][j-2] != 'ev':
            result = True
        if i-1 >= 0 and j + 2 < 8 and tab[i-1][j+2][1] != tab[i][j][1] and tab[i-1][j+2] != 'ev':
            result = True
        if i+2 < 8 and j - 1 >= 0 and tab[i+2][j-1][1] != tab[i][j][1] and tab[i+2][j-1] != 'ev':
            result = True
        if i+2 < 8 and j + 1 < 8 and tab[i+2][j+1][1] != tab[i][j][1] and tab[i+2][j+1] != 'ev':
            result = True
        if i+1 < 8 and j - 2 >= 0 and tab[i+1][j-2][1] != tab[i][j][1] and tab[i+1][j-2] != 'ev':
            result = True
        if i+1 < 8 and j + 2 < 8 and tab[i+1][j+2][1] != tab[i][j][1] and tab[i+1][j+2] != 'ev':
            result = True

    elif tab[i][j] == 'bb' or tab[i][j] == 'bp':
        cont = 1
        while i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont] == 'ev':
            cont += 1
        if i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont][1] != tab[i][j][1] and tab[i-cont][j-cont] != 'ev': 
            result = True
        cont = 1
        while i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont] == 'ev':
            cont += 1
        if i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont][1] != tab[i][j][1] and tab[i+cont][j-cont] != 'ev': 
            result = True
        cont = 1
        while i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont] == 'ev':
            cont += 1
        if i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont][1] != tab[i][j][1] and tab[i+cont][j+cont] != 'ev': 
            result = True
        cont = 1
        while i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont] == 'ev':
            cont += 1
        if i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont][1] != tab[i][j][1] and tab[i-cont][j+cont] != 'ev': 
            result = True

    elif tab[i][j] == 'kb' or tab[i][j] == 'kp':
        if i-1 >= 0 and j - 1 >= 0 and tab[i-1][j-1][1] != tab[i][j][1] and tab[i-1][j-1] != 'ev':
            result = True
        if i-1 >= 0 and tab[i-1][j][1] != tab[i][j][1] and tab[i-1][j] != 'ev':
            result = True
        if i-1 >= 0 and j + 1 < 8 and tab[i-1][j+1][1] != tab[i][j][1] and tab[i-1][j+1] != 'ev':
            result = True
        if j + 1 < 8 and tab[i][j+1][1] != tab[i][j][1] and tab[i][j+1] != 'ev':
            result = True
        if i+1 < 8 and j + 1 < 8 and tab[i+1][j+1][1] != tab[i][j][1] and tab[i+1][j+1] != 'ev':
            result = True
        if i+1  < 8 and tab[i+1][j][1] != tab[i][j][1] and tab[i+1][j] != 'ev':
            result = True
        if i+1  < 8 and j - 1 >= 0 and tab[i+1][j-1][1] != tab[i][j][1] and tab[i+1][j-1] != 'ev':
            result = True
        if j - 1 >= 0 and tab[i][j-1][1] != tab[i][j][1] and tab[i][j-1] != 'ev': 
            result = True

    elif tab[i][j] == 'rb' or tab[i][j] == 'rp':
        cont = 1
        while i-cont >= 0 and tab[i-cont][j] == 'ev':
            cont += 1
        if i-cont >= 0 and tab[i-cont][j][1] != tab[i][j][1] and tab[i-cont][j] != 'ev': 
            result = True
        cont = 1
        while i+cont < 8 and tab[i+cont][j] == 'ev':
            cont += 1
        if i+cont < 8 and tab[i+cont][j][1] != tab[i][j][1] and tab[i+cont][j] != 'ev': 
            result = True
        cont = 1
        while j-cont >= 0 and tab[i][j-cont] == 'ev':
            cont += 1
        if j-cont >= 0 and tab[i][j-cont][1] != tab[i][j][1] and tab[i][j-cont] != 'ev': 
            result = True
        cont = 1
        while j+cont < 8 and tab[i][j+cont] == 'ev':
            cont += 1
        if j+cont < 8 and tab[i][j+cont][1] != tab[i][j][1] and tab[i][j+cont] != 'ev':
            result = True
        cont = 1
        while i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont] == 'ev':
            cont += 1
        if i-cont >= 0 and j-cont >= 0 and tab[i-cont][j-cont][1] != tab[i][j][1] and tab[i-cont][j-cont] != 'ev': 
            result = True
        cont = 1
        while i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont] == 'ev':
            cont += 1
        if i+cont < 8 and j-cont >= 0 and tab[i+cont][j-cont][1] != tab[i][j][1] and tab[i+cont][j-cont] != 'ev': 
            result = True
        cont = 1
        while i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont] == 'ev':
            cont += 1
        if i+cont < 8 and j+cont < 8 and tab[i+cont][j+cont][1] != tab[i][j][1] and tab[i+cont][j+cont] != 'ev': 
            result = True
        cont = 1
        while i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont] == 'ev':
            cont += 1
        if i-cont >= 0 and j+cont < 8 and tab[i-cont][j+cont][1] != tab[i][j][1] and tab[i-cont][j+cont] != 'ev': 
            result = True

    elif tab[i][j] == 'pb':
        if i + 1 < 8 and j + 1 < 8 and tab[i+1][j+1][1] != tab[i][j][1] and tab[i+1][j+1] != 'ev':
            result = True
        elif i + 1 < 8 and j-1 >= 0 and tab[i+1][j-1][1] != tab[i][j][1] and tab[i+1][j-1] != 'ev':
            result = True

    elif tab[i][j] == 'pp':
        if i - 1 >= 0 and j + 1 < 8 and tab[i-1][j+1][1] != tab[i][j][1] and tab[i-1][j+1] != 'ev':
            result = True
        elif i - 1 >= 0 and j-1 >= 0 and tab[i-1][j-1][1] != tab[i][j][1] and tab[i-1][j-1] != 'ev':
            result = True

    return result

def botOpcoes(tab, cor, ischeck):
    opcoes = []

    if not(ischeck):
        for i in range(8):
            for j in range(8):
                if (tab[i][j][1] == 'b' and cor == 0) or (tab[i][j][1] == 'p' and cor == 1):
                    opcoes.append((i, j))
    else:
        for i in range(8):
            for j in range(8):
                if (tab[i][j] == 'kb' and cor == 0) or (tab[i][j] == 'kp' and cor == 1):
                    opcoes.append((i, j))     

    return opcoes

def xadrezJogoBot(tela, tabuleiro, tab_desenho, tab_pecas, ppX, ppY):
    game_on = True
    player_vez = randint(0, 1)
    
    if player_vez == 0:
        player_cor = 1 #Player - branco  // Bot - preto
    else:
        player_cor = 0 #Player - preto  // Bot - branco

    if player_vez == 0:
        txt_player = Text(Point(400, 30),'Vez do player')
    else:
        txt_player = Text(Point(400, 30),'Vez do bot')

    if (player_cor == 1 and player_vez == 0) or (player_cor == 0 and player_vez == 1):
        txt_player = modText(txt_player, 'white', 'courier', 'bold', 18)
        txt_player.draw(tela)

    winnerB = True
    check = -1
    incheck = False

    while game_on:

        if check == -1 and player_vez == 0:
            mouse = tela.getMouse()

        trocavez = False
        indI = -1
        indJ = -1

        if check == -1:
            if player_vez == 0:
                for i in range(8):
                    for j in range(8):
                        if mouse.getX() >= ppX*(j+1) and mouse.getX() <= ppX*(j+1)+ppX and mouse.getY() >= ppY*(i+1) and mouse.getY() <= ppY*(i+1)+ppY:
                            indI = i
                            indJ = j
     
            else:
                opcoesBot = botOpcoes(tabuleiro, player_cor, incheck)
                for peca in opcoesBot:
                    if comePecaBot(tabuleiro, peca[0], peca[1]):
                        indI = peca[0]
                        indJ = peca[1]
                        break
                if indI == -1 and indJ == -1:
                    posBot = opcoesBot[randint(0, len(opcoesBot) - 1)]
                    indI = posBot[0]
                    indJ = posBot[1]

            if ((indI == -1 or indJ == -1) or (tabuleiro[indI][indJ] == 'ev')) and player_vez == 0:
                msg = Text(Point(400, 570),'Selecione uma peca do tabuleiro')
                msg = modText(msg, 'red', 'courier', 'bold', 20)
                msg.draw(tela)
                sleep(1.5)
                msg.undraw()
        
            elif player_vez == 0 and ((tabuleiro[indI][indJ][1] == 'p' and player_cor == 1) or (tabuleiro[indI][indJ][1] == 'b' and player_cor == 0)): 
                msg1 = Text(Point(350, 570),'Selecione uma peca sua')
                msg1 = modText(msg1, 'red', 'courier', 'bold', 20)
                msg1.draw(tela)
                if tabuleiro[indI][indJ][1] == 'p':
                    msg2 = Text(Point(580, 570),'  (Brancas)')
                    msg2 = modText(msg2, 'white', 'courier', 'bold', 20)
                else:
                    msg2 = Text(Point(580, 570),' (Pretas)')
                    msg2 = modText(msg2, 'gray', 'courier', 'bold', 20)    
                msg2.draw(tela)
                sleep(1.5)
                msg1.undraw()
                msg2.undraw()
        
            else:
                opcoes = mostrarposicoesvalidas(tela, tabuleiro, indI, indJ, tab_desenho)
                if player_vez == 1:
                    sleep(1)
                if len(opcoes) > 0:
                    if player_vez == 0:
                        mouse = tela.getMouse()
                    
                    indI_new = -1
                    indJ_new = -1

                    if player_vez == 0:
                        for i in range(8):
                            for j in range(8):
                                if mouse.getX() >= ppX*(j+1) and mouse.getX() <= ppX*(j+1)+ppX and mouse.getY() >= ppY*(i+1) and mouse.getY() <= ppY*(i+1)+ppY:
                                    indI_new = i
                                    indJ_new = j
                    else:
                        for peca in opcoes:
                            if incheck:
                                ax_pos = fugirRei(tabuleiro, player_cor)
                                indI_new = ax_pos[0]
                                indJ_new = ax_pos[1]
                                break
                            if tabuleiro[peca[0]][peca[1]][1] != tabuleiro[indI][indJ][1] and tabuleiro[peca[0]][peca[1]] != 'ev':
                                indI_new = peca[0]
                                indJ_new = peca[1]
                                break
                        if indI_new == -1 and indJ_new == -1:
                            posBot = opcoes[randint(0, len(opcoes)-1)]
                            indI_new = posBot[0]
                            indJ_new = posBot[1]

                    pos_valida = False
                
                    for pos in opcoes:
                        if pos[0] == indI_new and pos[1] == indJ_new:
                            pos_valida = True

                    tab_desenho = resetaposicoes(tela, tab_desenho)

                    if pos_valida:
                        tab_pecas[indI][indJ].undraw() 
                        tab_pecas[indI_new][indJ_new].undraw()

                        if indI_new == 7 and tabuleiro[indI][indJ] == 'pb':
                            new_pos = Image(Point(ppX*(indJ_new+1)+ppX/2, ppY*(indI_new+1)+ppY/2), 'IMGS/rb.png')
                            tabuleiro[indI_new][indJ_new] = 'rb'
                        elif indI_new == 0 and tabuleiro[indI][indJ] == 'pp':
                            new_pos = Image(Point(ppX*(indJ_new+1)+ppX/2, ppY*(indI_new+1)+ppY/2), 'IMGS/rp.png')
                            tabuleiro[indI_new][indJ_new] = 'rp'
                        else:
                            new_pos = Image(Point(ppX*(indJ_new+1)+ppX/2, ppY*(indI_new+1)+ppY/2), 'IMGS/'+tabuleiro[indI][indJ]+'.png')
                            tabuleiro[indI_new][indJ_new] = tabuleiro[indI][indJ]
                        new_pos.draw(tela)
                        tab_pecas[indI_new][indJ_new] = new_pos
                        tabuleiro[indI][indJ] = 'ev'
                        trocavez = True
                        check, incheck = checaCheck(player_vez, tabuleiro, tela, player_cor)
                    elif player_vez == 0:
                        msg = Text(Point(400, 570),'Selecione uma posição válida')
                        msg = modText(msg, 'red', 'courier', 'bold', 20)
                        msg.draw(tela)
                        sleep(1.5)
                        msg.undraw()
                elif player_vez == 0:
                    msg = Text(Point(400, 570),'Selecione uma peca que possa se movimentar')
                    msg = modText(msg, 'red', 'courier', 'bold', 20)
                    msg.draw(tela)
                    sleep(1.5)
                    msg.undraw()

            reiBrancos = False
            reiPretos = False
            for i in range(8):
                for j in range(8):
                    if tabuleiro[i][j] == 'kb':
                        reiBrancos = True
                    elif tabuleiro[i][j] == 'kp':
                        reiPretos = True

            if not(reiBrancos) or not(reiPretos):
                game_on = False
                if reiPretos:
                    winnerB = False

            if trocavez and game_on:
                player_vez += 1
                if player_vez == 2:
                    player_vez = 0

                txt_player.undraw()
                
                if player_vez == 0:
                    txt_player = Text(Point(400, 30),'Vez do player')
                else:
                    txt_player = Text(Point(400, 30),'Vez do bot')
                if (player_cor == 1 and player_vez == 0) or (player_cor == 0 and player_vez == 1):
                    txt_player = modText(txt_player, 'white', 'courier', 'bold', 18)
                else:
                    txt_player = modText(txt_player, 'gray', 'courier', 'bold', 18)    
                txt_player.draw(tela)
        
        else:
            game_on = False

    for i in range(8):
        for j in range(8):
            tab_desenho[i][j].undraw()
            tab_pecas[i][j].undraw()

    txt_player.undraw()

    if check == 1:
        txt_win = Text(Point(400, 300),'Brancas em Check Mate')
        txt_win = modText(txt_win, 'white', 'courier', 'bold', 26)
        txt_win.draw(tela)
        sleep(2)
        txt_win.undraw()
        winnerB = False
 
    elif check == 2:
        txt_win = Text(Point(400, 300),'Pretas em Check Mate')
        txt_win = modText(txt_win, 'gray', 'courier', 'bold', 26)
        txt_win.draw(tela)
        sleep(2)
        txt_win.undraw()
        winnerB = True

    if (winnerB and player_cor == 1) or (not(winnerB) and player_cor == 0):
        txt_win = Text(Point(400, 300),'Player GANHOU!!')
        txt_win = modText(txt_win, 'white', 'courier', 'bold', 26)
        txt_win.draw(tela)
        sleep(2)
        txt_win.undraw()
    else:
        txt_win = Text(Point(400, 300),'Bot GANHOU!!')
        txt_win = modText(txt_win, 'gray', 'courier', 'bold', 26)
        txt_win.draw(tela)
        sleep(2)
        txt_win.undraw()

def tabNormal(tela, who):
    arq = open('tab_padrao.txt')
    arq_txt = arq.readlines()
    arq.close()

    tabuleiro = []
    tab_desenho = []
    tab_pecas = []
    ax = []
    cnt = 0
    for itens in arq_txt:
        cnt += 1
        itens.split()
        aux = ""
        for i in itens:
            if i != ' ' and i != '\n':
                aux += i
            if len(aux) == 2:
                ax.append(aux)
                aux = ""
        tabuleiro.append(ax)
        ax = []

    ppX = 80
    ppY = 60

    troca = True

    for i in range(8):
        ax_desen = []
        ax_pecas = []
        for j in range(8):
            desenho = Rectangle(Point(ppX*(j+1), ppY*(i+1)), Point(ppX*(j+1)+ppX, ppY*(i+1)+ppY))
            if troca:
                desenho.setFill(color_rgb(204, 204, 255))
            else:
                desenho.setFill(color_rgb(68, 68, 34))
            troca = not(troca)
            desenho.draw(tela)
            peca = Image(Point(0,0),'IMGS/bb.png' )
            if tabuleiro[i][j] != 'ev':
                peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/'+tabuleiro[i][j]+'.png')
                peca.draw(tela)
            ax_desen.append(desenho)
            ax_pecas.append(peca)
        tab_desenho.append(ax_desen)
        tab_pecas.append(ax_pecas)
        troca = not(troca)

    if who == 1:
        xadrezJogo(tela, tabuleiro, tab_desenho, tab_pecas, ppX, ppY)
    else:
        xadrezJogoBot(tela, tabuleiro, tab_desenho, tab_pecas, ppX, ppY)

def tabEsp(tela, who):
    tabuleiro = []
    tab_desenho = []
    tab_pecas = []

    ppX = 80
    ppY = 60

    troca = True

    sorteBrancos = ['tb', 'cb', 'bb', 'rb', 'bb', 'cb', 'tb',
                    'pb', 'pb', 'pb', 'pb', 'pb',
                    'ev', 'ev', 'ev', 'ev', 'ev', 'ev', 'ev', 'ev',
                    'ev', 'ev', 'ev', 'ev', 'ev', 'ev', 'ev', 'ev']
    sortePretos =  ['tp', 'cp', 'bp', 'rp', 'bp', 'cp', 'tp',
                    'pp', 'pp', 'pp', 'pp', 'pp',
                    'ev', 'ev', 'ev', 'ev', 'ev', 'ev', 'ev', 'ev',
                    'ev', 'ev', 'ev', 'ev', 'ev', 'ev', 'ev', 'ev']

    for i in range(8):
        ax_desen = []
        ax_pecas = []
        ax_tb = []
        for j in range(8):
            desenho = Rectangle(Point(ppX*(j+1), ppY*(i+1)), Point(ppX*(j+1)+ppX, ppY*(i+1)+ppY))
            if troca:
                desenho.setFill(color_rgb(204, 204, 255))
            else:
                desenho.setFill(color_rgb(68, 68, 34))
            troca = not(troca)
            desenho.draw(tela)
            peca = Image(Point(0,0),'IMGS/bb.png' )
            if i == 0 and j == 0:
                peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/kb.png')
                peca.draw(tela)
                ax_tb.append('kb')
            elif i == 0 and j == 1:
                peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/pb.png')
                peca.draw(tela)
                ax_tb.append('pb')
            elif i == 1 and j == 1:
                peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/pb.png')
                peca.draw(tela)
                ax_tb.append('pb') 
            elif i == 1 and j == 0:
                peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/pb.png')
                peca.draw(tela)
                ax_tb.append('pb') 
            elif i == 7 and j == 7:
                peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/kp.png')
                peca.draw(tela)
                ax_tb.append('kp')
            elif i == 7 and j == 6:
                peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/pp.png')
                peca.draw(tela)
                ax_tb.append('pp')
            elif i == 6 and j == 6:
                peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/pp.png')
                peca.draw(tela)
                ax_tb.append('pp') 
            elif i == 6 and j == 7:
                peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/pp.png')
                peca.draw(tela)
                ax_tb.append('pp') 
            else:
                if len(sorteBrancos)>0:
                    indice = randint(0, len(sorteBrancos)-1)
                    if sorteBrancos[indice] != 'ev':
                        peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/'+sorteBrancos[indice]+'.png')
                        peca.draw(tela)
                    ax_tb.append(sorteBrancos[indice])
                    sorteBrancos.pop(indice)
                else:
                    indice = randint(0, len(sortePretos)-1)
                    if sortePretos[indice] != 'ev':
                        peca = Image(Point(ppX*(j+1)+ppX/2, ppY*(i+1)+ppY/2), 'IMGS/'+sortePretos[indice]+'.png')
                        peca.draw(tela)
                    ax_tb.append(sortePretos[indice])
                    sortePretos.pop(indice)

            ax_desen.append(desenho)
            ax_pecas.append(peca)
        tab_desenho.append(ax_desen)
        tab_pecas.append(ax_pecas)
        tabuleiro.append(ax_tb)
        troca = not(troca)

    if who == 1:
        xadrezJogo(tela, tabuleiro, tab_desenho, tab_pecas, ppX, ppY)
    else:
        xadrezJogoBot(tela, tabuleiro, tab_desenho, tab_pecas, ppX, ppY)

def intrucoes(tela):
    arq = open('instru.txt')
    txt = arq.read()
    arq.close()

    ind = 0
    ppX = 30
    ppY = 50

    bord = Rectangle(Point(650,480),Point(750,520))
    bord.setFill('gray')
    bord.draw(tela)

    voltar = Text(Point(700, 500),'Voltar')
    voltar = modText(voltar, 'white', 'courier', 'bold', 18)
    voltar.draw(tela)

    bord2 = Rectangle(Point(365,380),Point(485,420))
    bord2.setFill('gray')
    bord2.draw(tela)

    prox = Text(Point(425, 400),'Proximo')
    prox = modText(prox, 'white', 'courier', 'bold', 18)
    prox.draw(tela)

    torre = Image(Point(200,400), 'IMGS/torre.png')
    txt_trr = Text(Point(180,540),'Torre')
    txt_trr = modText(txt_trr, 'white', 'courier', 'bold', 16)
    bispo = Image(Point(200,400), 'IMGS/bispo.png')
    txt_bp = Text(Point(180,540),'Bispo')
    txt_bp = modText(txt_bp, 'white', 'courier', 'bold', 16)
    cavalo = Image(Point(200,400), 'IMGS/cavalo.png')
    txt_cv = Text(Point(180,540),'Cavalo')
    txt_cv = modText(txt_cv, 'white', 'courier', 'bold', 16)
    rainha = Image(Point(200,400), 'IMGS/rainha.png')
    txt_rn = Text(Point(180,540),'Rainha')
    txt_rn = modText(txt_rn, 'white', 'courier', 'bold', 16)
    rei = Image(Point(200,400), 'IMGS/rei.png')
    txt_rr = Text(Point(180,540),'Rei')
    txt_rr = modText(txt_rr, 'white', 'courier', 'bold', 16)
    peao = Image(Point(200,400), 'IMGS/peao.png')
    txt_pe = Text(Point(180,540),'Peao')
    txt_pe = modText(txt_pe, 'white', 'courier', 'bold', 16)
    txt_pe.draw(tela)
    peao.draw(tela)
    
    ind_sel = 0
    selecao = [peao, torre, bispo, cavalo, rainha, rei]
    selecao_txt = [txt_pe, txt_trr, txt_bp, txt_cv, txt_rn, txt_rr]
    excluir = [bord, bord2, voltar, prox]

    pos_mouse = tela.checkMouse()
    while True:
        pos_mouse = tela.checkMouse()
        if ind < len(txt):
            if txt[ind] == '\n':
                ppY += 20
                ppX = 30
            elif txt[ind] == ' ':
                ppX += 10
            else:
                tt = Text(Point(ppX, ppY), txt[ind])
                tt.setFill('white')
                tt.setFace('courier')
                tt.setStyle('bold')
                tt.draw(tela)
                excluir.append(tt)
                ppX += 10
        ind += 1

        if pos_mouse != None and pos_mouse.getX() >= 650 and pos_mouse.getX() <= 750 and pos_mouse.getY() >= 480 and pos_mouse.getY() <= 520:
            break
        if pos_mouse != None and pos_mouse.getX() >= 365 and pos_mouse.getX() <= 485 and pos_mouse.getY() >= 380 and pos_mouse.getY() <= 420:
            bord2.setFill('blue')
            sleep(0.25)
            selecao[ind_sel].undraw()
            selecao_txt[ind_sel].undraw()
            ind_sel = (ind_sel + 1) % 6
            selecao[ind_sel].draw(tela)
            selecao_txt[ind_sel].draw(tela)
            bord2.setFill('gray')

    bord.setFill('blue')
    sleep(0.5)

    for itens in excluir:
        itens.undraw()
    for pecas in selecao:
        pecas.undraw()
    for txt in selecao_txt:
        txt.undraw()

def menuSelect(tela, menu):
    menu[1].setFill('gray')
    for itens in menu:
        itens.draw(tela)

    selecao_tp = True
    desenha_ops = True
    desenha_who = True
    desenha_confirma = True
    sl_tp = -1
    sl_who = -1

    menu_on = True
    menu_resto = []

    while menu_on:
        pos_mouse = tela.checkMouse()

        if selecao_tp:
            selecionou_jg = False
            if pos_mouse != None and pos_mouse.getX() >= 350 and pos_mouse.getX() <= 450 and pos_mouse.getY() >= 180 and pos_mouse.getY() <= 220:
                selecionou_jg = True
                menu[1].setFill('green')

            if selecionou_jg == True and desenha_ops:
                r1 = Rectangle(Point(265, 255), Point(370, 295))
                r1.setFill('gray')
                r1.draw(tela)
                menu_resto.append(r1)
                r2 = Rectangle(Point(430, 255), Point(565, 295))
                r2.setFill('gray')
                r2.draw(tela)
                menu_resto.append(r2)

                tt_nr = Text(Point(320, 275), 'Normal')
                tt_nr = modText(tt_nr, 'white', 'courier', 'bold', 18)
                tt_nr.draw(tela)
                menu_resto.append(tt_nr)

                tt_esp = Text(Point(500, 275), 'Especial')
                tt_esp = modText(tt_esp, 'white', 'courier', 'bold', 18)
                tt_esp.draw(tela)
                menu_resto.append(tt_esp)

                desenha_ops = False

            selecionou_tipo = -1
            if desenha_ops == False and pos_mouse != None and pos_mouse.getX() >= 265 and pos_mouse.getX() <= 370 and pos_mouse.getY() >= 255 and pos_mouse.getY() <= 295:
                    selecionou_tipo = 1
            if desenha_ops == False and pos_mouse != None and pos_mouse.getX() >= 430 and pos_mouse.getX() <= 565 and pos_mouse.getY() >= 255 and pos_mouse.getY() <= 295:
                    selecionou_tipo = 2

            if selecionou_tipo == 1:
                sl_tp = 1
                r1.setFill('green')
                r2.setFill('gray')
            elif selecionou_tipo == 2:
                sl_tp = 2
                r1.setFill('gray')
                r2.setFill('green')

            if sl_tp != -1 and desenha_who:
                r3 = Rectangle(Point(265, 330), Point(370, 370))
                r3.setFill('gray')
                r3.draw(tela)
                menu_resto.append(r3)
                r4 = Rectangle(Point(430, 330), Point(565, 370))
                r4.setFill('gray')
                r4.draw(tela)
                menu_resto.append(r4)

                tt_pl = Text(Point(320, 350), 'Player')
                tt_pl = modText(tt_pl, 'white', 'courier', 'bold', 18)
                tt_pl.draw(tela)
                menu_resto.append(tt_pl)

                tt_bot = Text(Point(500, 350), 'Bot')
                tt_bot = modText(tt_bot, 'white', 'courier', 'bold', 18)
                tt_bot.draw(tela)
                menu_resto.append(tt_bot)

                desenha_who = False

            selecionou_who = -1
            if desenha_who == False and pos_mouse != None and pos_mouse.getX() >= 265 and pos_mouse.getX() <= 370 and pos_mouse.getY() >= 330 and pos_mouse.getY() <= 370:
                    selecionou_who = 1
            if desenha_who == False and pos_mouse != None and pos_mouse.getX() >= 430 and pos_mouse.getX() <= 565 and pos_mouse.getY() >= 330 and pos_mouse.getY() <= 370:
                    selecionou_who = 2

            if selecionou_who == 1:
                sl_who = 1
                r3.setFill('green')
                r4.setFill('gray')
            elif selecionou_who == 2:
                sl_who = 2
                r3.setFill('gray')
                r4.setFill('green')

            if sl_who != -1 and desenha_confirma:
                box = Rectangle(Point(325, 405), Point(475, 445))
                box.setFill('gray')
                box.draw(tela)
                menu_resto.append(box)

                tt_con = Text(Point(400, 425), 'Confirmar')
                tt_con = modText(tt_con, 'white', 'courier', 'bold', 18)
                tt_con.draw(tela)
                menu_resto.append(tt_con)

                desenha_confirma = False

            if desenha_confirma == False and pos_mouse != None and pos_mouse.getX() >= 325 and pos_mouse.getX() <= 475 and pos_mouse.getY() >= 405 and pos_mouse.getY() <= 445:
                box.setFill('green')
                sleep(0.5)
                menu_on = False

        if pos_mouse != None and pos_mouse.getX() >= 80 and pos_mouse.getX() <= 270 and pos_mouse.getY() >= 480 and pos_mouse.getY() <= 520:
            menu[2].setFill('blue')
            sl_tp=0
            menu_on=False
            sleep(0.5)
            menu[2].setFill('gray')

        if pos_mouse != None and pos_mouse.getX() >= 610 and pos_mouse.getX() <= 690 and pos_mouse.getY() >= 480 and pos_mouse.getY() <= 520:
            menu[3].setFill('red')
            sl_tp=-1
            menu_on=False
            sleep(0.5)

    for itens in menu:
        itens.undraw()
    for itens in menu_resto:
        itens.undraw()

    return sl_tp, sl_who

def main():
    tela = GraphWin('Xadrez', 800, 600)
    tela.setBackground('black')

    titulo = Text(Point(400, 70), 'Xadrez')
    titulo = modText(titulo, 'orange', 'courier', 'bold', 26)


    r1 = Rectangle(Point(350, 180), Point(450, 220))
    r1.setFill('gray')
    r2 = Rectangle(Point(80, 480), Point(270, 520))
    r2.setFill('gray')
    r3 = Rectangle(Point(610, 480), Point(690, 520))
    r3.setFill('gray')

    tt_jg = Text(Point(400, 200), 'Jogar')
    tt_jg = modText(tt_jg, 'white', 'courier', 'bold', 18)

    instru = Text(Point(175, 500), 'Instruções')
    instru = modText(instru, 'white', 'courier', 'bold', 20)

    sair = Text(Point(650, 500), 'Sair')
    sair = modText(sair, 'white', 'courier', 'bold', 20)

    menu = [titulo, r1, r2, r3, tt_jg, instru, sair]

    lupi = True
    while lupi:
        tip, who = menuSelect(tela, menu)
        if tip == 0:
            intrucoes(tela)
        elif tip == 1:
            tabNormal(tela, who)
        elif tip == 2:
            tabEsp(tela, who)
        else:
            break

    tela.close()

if __name__ == '__main__':
    main()