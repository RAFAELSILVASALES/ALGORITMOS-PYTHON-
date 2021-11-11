import turtle


def desenhaQuadrado(t, tam):

    for c in range(4):
        t.forward(tam)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
desenhaQuadrado(alex, 50)
wn.exitonclick
