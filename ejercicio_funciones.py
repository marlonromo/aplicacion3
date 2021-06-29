"Autor: Equipo 6"
"Matricula: A00827878"
"Matricula: A01379117"
"Matricula: A00827937"
"Matricula: A000827765"


from turtle import *

from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin.fill()
    
    circumference = 2 * (abs(start.x-end.x)+abs(start.y-end.y)) *math.pi
    step_size= circumference/360
    
    for count in range(360):
         forward(step_size)
         left(1)
         
    enf_fill()
         
    
    

def rectangle(start, end):
    "Draw rectangle from start to end."

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
    "Draw triangle from start to end."
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
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
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