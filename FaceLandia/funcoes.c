#include <stdio.h>

int abreBau(int playerI, int playerJ, int bauI, int bauJ, int variaI, int variaJ, int desenhado)
{
    if (playerI >= bauI - variaI && playerI <= bauI + variaI && playerJ >= bauJ - variaJ && playerJ <= bauJ + variaJ && !desenhado)
        return 1;

    return -1;
}

int winGame(int playerI, int playerJ, int finalI, int finalJ, int variaI, int variaJ)
{
    if (playerI >= finalI - variaI && playerI <= finalI + variaI && playerJ >= finalJ - variaJ && playerJ <= finalJ + variaJ)
        return 1;

    return -1;
}

int pValida(int playerI, int playerJ, int paredeIini, int paredeIfim, int paredeJini, int paredeJfim)
{
    if (playerI >= paredeIini - 8 && playerI <= paredeIfim + 8 && playerJ >= paredeJini - 8 && playerJ <= paredeJfim + 8)
        return 1;

    return -1;
}

int difTempos(int player_min, int player_seg, int bot_min, int bot_seg)
{
    return (player_min * 60 + player_seg) - (bot_min * 60 + bot_seg);
}

int verificaTabuleiro(char x)
{
    if (x == '#')
        return 1;

    if (x == 'i')
        return 2;
    
    if (x == 'f')
        return 3;
    
    if (x == 't')
        return 4;
    
    return -1;
}
