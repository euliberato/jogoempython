#Informações do aluno:
#Nome: Carlos Ruan Jovino Liberato da Silva
#Número da Matrícula: 514651
#Engenharia de software 2021.2

import turtle
import math
import random

'''Configs da tela'''
tela = turtle.Screen()
tela.setup(450,450)
tela.title('Tartaruga Carnivora Adventures')

'''Borda'''
borda = turtle.Turtle()
borda.penup()
borda.setposition(-210,-210)
borda.pendown()
borda.pensize(3)

'''Essa estrutura de repetição irá fazer as linhas (desenhos) que irão demarcar a borda. '''
borda.color('Black', 'Lightblue')
borda.begin_fill()
for side in range(4):
    borda.forward(415)
    borda.left(90)
    borda.hideturtle()
borda.end_fill()

#Essa estrutura irá repetir 4 vezes até completar os 4 lados do quadrado

'''Informações sobre a pontuação'''
pontos = 0
toxico = 3

#Essas variaveis acima servem para guardar os valores iniciais dos pontos e vida.

status = turtle.Turtle() 
status.goto(0,0)
status.penup()
status.pendown
status.pensize(3)
status.hideturtle()
status.setposition(-206,205)
text1 = 'Pontos: %s' %pontos
status.write(text1, False, align='left', font='Arial')

#O "status" acima define a string que foi inserida dentro do jogo para controlar os pontos. É relacionado aos pontos.

#text1 irá guardar os textos

status2 = turtle.Turtle()
status2.goto(0,0)
status2.penup()
status2.pendown
status2.pensize(3)
status2.hideturtle()
status2.setposition(-110,205)
text2 = 'Vida: %s' %toxico
status2.write(text2, False, align='left', font='Arial')

#O "status2" acima define a string que foi inserida dentro do jogo para controlar os pontos. É relacionado as vidas.

#text2 irá guardar os textos 

'''Configs do player (tartaruga).'''
player = turtle.Turtle()
player.color('Black', 'Lightyellow')
player.shape('turtle')
player.speed(0)
player.penup()
velocidade_inicial = 1

'''Sistema de pontuação'''
comida = turtle.Turtle()
comida.color('black', 'lightgreen')
comida.shape('circle')
comida.penup()
comida.speed(0)
comida.setposition(random.randint(-200,200), random.randint(-200,200))

veneno = turtle.Turtle()
veneno.color('black', 'red')
veneno.shape('circle')
veneno.penup()
veneno.speed(0)
veneno.setposition(random.randint(-200,200), random.randint(-200,200))

#Veneno e Veneno representam as variaveis utilizadas para a criação dos objetos que serão usados para os pontos e vida.

''' Abaixo são funções que irão definir valores para a captura das teclas. '''
def cima():
    player.forward(45)
def baixo():
    player.left(45)
def esquerda():
    player.right(45)
def direita():
    player.back(45)

#As funções acima servem para ser utilizadas posteriormente atraves de uma chamada pelo comando listen e serão acionadas quando as teclas configuradas forem pressionadas.

''' Abaixo são as teclas configuradas com suas respectivas funções. '''
turtle.listen()
turtle.onkey(cima, 'Up')
turtle.onkey(baixo, 'Left')
turtle.onkey(esquerda, 'Right')
turtle.onkey(direita, 'Down')
 
    
while True:
    player.forward(velocidade_inicial)

    '''Configs de limitação da borda'''
    if player.xcor() > 200 or player.xcor() < -200:
        player.goto(0,0)

    if player.ycor() > 200 or player.ycor() < -200:
        player.goto(0,0)

    #Se as coordenadas do personagem tentarem ultrapassar as coordenadas (dos quadrantes) o personagem retornará ao centro do jogo.

    '''Configs da colisão com o sistema de pontuação'''
    item1 = math.sqrt(math.pow(player.xcor()-comida.xcor(),2) + math.pow(player.ycor()-comida.ycor(),2))
    item2 = math.sqrt(math.pow(player.xcor()-veneno.xcor(),2) + math.pow(player.ycor()-veneno.ycor(),2))
    if (item1 < 20): 
        comida.setposition(random.randint(-200,200), random.randint(-200,200))
        veneno.setposition(random.randint(-200,200), random.randint(-200,200))
        pontos += 1
        print(pontos)
        status.penup()
        status.hideturtle()
        status.setposition(-206,205)
        text1 = 'Pontos: %s' %pontos
        status.clear()
        status.write(text1, align='left', font='Arial')

    #Conjunto de ações que será realizado caso o player interfira nas coordenadas da comida: atualização das coordenadas, soma de pontos, atualização da pontuação e configuração do posicionamento da tela. Detalhe: o "status" está na parte mais acima do código para aparecer logo no inicio do jogo, se ele estivesse presente só na estrutura if, as informações de pontos e vida só iriam aparecer caso o jogador fizesse alguma interação e isso poderia deixar o usuário confuso.
        
    if (item2 < 20):
        veneno.setposition(random.randint(-200,200), random.randint(-200,200))
        comida.setposition(random.randint(-200,200), random.randint(-200,200))
        toxico -= 1
        print(toxico)
        status2.penup()
        status2.hideturtle()
        status2.setposition(-110,205)
        text2 = 'Vida: %s' %toxico
        status2.clear()
        status2.write(text2, align='left', font='Arial')

    #Conjunto de ações que será realizado caso o player interfira nas coordenadas do veneno: mesmas ações do if anterior, porém, nesse caso, irá ser subtraido uma vida das 3 vidas iniciais.
        
    if toxico == 0 :
        tela.bye()    
tela.mainloop()