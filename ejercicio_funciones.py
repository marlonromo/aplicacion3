"-Equipo 6-"
"Integrantes:"
"Ricardo Lopez  A00827878"
"Francisco Ambriz A01379117"
"Juan Pablo Ortiz A00827937"
"Marlon Romo A000827765"


from turtle import *

from freegames import vector
import math

def line(start, end):
    "Dibuja línea de principio a fin."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Dibuja cuadro de principio a fin."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    "Dibuja círculo de principio a fin."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    circumference = 2 * (abs(start.x-end.x)+abs(start.y-end.y)) * math.pi
    step_size= circumference/360
    
    for count in range(360):
         forward(step_size)
         left(1)
         
    end_fill()
         
    
    

def rectangle(start, end):
    "Dibuja rectángulo de principio a fin."

    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        if count%2 == 0:
            forward(end.x - start.x)
            left(90)
        else:
           forward((end.y - start.y))
           left(90)

    end_fill()



def triangle(start, end):
    "Dibuja triangulo de principio a fin."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for i in range(3):
         forward(end.x - start.x)
         left(120)
         forward(end.x - start.x)
    
    end_fill()
    pass  # TODO



def tap(x, y):
    "Proporciona punto de inicio o dibuja figura."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Guardar valor en estado clave."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()