#import biblioteca turtle
import turtle

"""
---------------------------------------------------------
Funcao: direcaoEsq
 define direcao para esquerda
 Param ang - anulo de giro para esquerda
"""
def direcaoEsq(ang):
    turtle.left(ang)
    turtle.speed (0)

"""
Funcao: desenharQuadrado
 desenha um quadrado na direcao do ang (esquerda)
 Param larg - largura do quadrado
 Param ang - anulo de giro para esquerda (default = 0)
"""
def desenharQuadrado(larg, ang = 0):
    direcaoEsq(ang)
    for i in range(4):
        turtle.forward(larg)
        turtle.left(90)
    direcaoEsq(-ang)
    turtle.speed (0)

"""
Funcao: posicionarQuina
 posicionar turtle para a quina do proximo quadrado
 Param x, y - posicao x, y
"""
def posicionarQuina(x, y):
    turtle.up() # levanta a caneta
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.down() # abaixa a caneta
    turtle.speed (0)
"""
Funcao: mover
 mover turtle para posicao x, y
 Param x, y - posicao x, y
"""

def mover (x, y):
    turtle.up() # levanta a caneta
    turtle.goto(x,y)
    turtle.down() # abaixa a caneta
    turtle.speed (0)

"""
---------------------------------------------------------
"""

    
