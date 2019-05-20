#importa biblioteca de funcoes graficas com turtle
import turtle_FuncoesGeometria as func
import turtle as t
"""
---------------------------------------------------------
Funcao: desenharQuadConcentricosReducao
 Desenha quadrados concentricos com reducao do espaco
	entre os quadrados
 Param largIni - largura inicial
 Param tamMin - tamanho minimo do quadrado
"""
def desenharQuadConcentricosReducao(largIni, tamMin):
    #print(largIni)
    if largIni < tamMin: # condicao de parada
        func.mover(0,0)
        return
    func.desenharQuadrado(largIni)
    pos = largIni//(tamMin/2)
    func.posicionarQuina(pos, pos)
    desenharQuadConcentricosReducao((largIni-2*pos), tamMin)

"""
Funcao: desenharQuadConcentricos
 Desenha quadrados concentricos 
 Param largIni - largura inicial
 Param tamMin - tamanho minimo do quadrado
"""
def desenharQuadConcentricos(largIni, tamMin):
    #print(largIni)
    if largIni < tamMin:
        func.mover(0,0)
        return
    func.desenharQuadrado(largIni)
    pos = tamMin
    func.posicionarQuina(pos, pos)
    desenharQuadConcentricos((largIni-2*pos), pos)
    retardo ()

def retardo ():
    t.left (90)
    desenharQuadConcentricos (300, 20)
    
    
"""
---------------------------------------------------------
"""

#principal

larguraInicial = 300
largLimite = 20

desenharQuadConcentricos(larguraInicial, largLimite)
#desenharQuadConcentricosReducao(larguraInicial, largLimite)
