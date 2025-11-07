import turtle
import random

# função 1: configura a tela
def configurar_tela():
    janela = turtle.Screen()
    janela.bgcolor("black") # fundo preto para destaque
    janela.title("arte generativa com turtle")
    t = turtle.Turtle()
    t.speed(0) # velocidade máxima para a animação
    t.pensize(2)
    return t

# funçaõ 2: desenha o padrão principal
def desenhar_espiral(t, tamanho_maximo):
    cores = ["red", "purple", "blue", "green", "orange", "yellow"]
    tamanho = 0

    while tamanho < tamanho_maximo:
        # muda a cor a cada interação
        t.pencolor(random.choice(cores))

        #desenha a linha e avança
        t.forward(tamanho)

        # gira em um ângulo fixo (cria a espiral)
        t.right(91)

        # aumenta o tamanho do passo
        tamanho += 1

# --- programa principal ---
tartaruga = configurar_tela()
desenhar_espiral(tartaruga, 300)

turtle.done() # mantém a janela aberta até ser fechada manualmente

