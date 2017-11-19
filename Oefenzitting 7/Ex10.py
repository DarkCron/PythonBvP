from graphics import GraphicsWindow

g = GraphicsWindow(600,600)
c = g.canvas()



def sierpinski(canvas, x, y, size, depth, iterations, currentIteration=0):
    if currentIteration == 0:
        c.setFill("black")
        c.drawPolygon((size)//2 + x,y , x,depth+y, size+x,depth+y)
        c.setFill("white")

    if currentIteration == iterations:
        return
    top_x = x + size // 2
    top_y = y + depth
    left_x = x + size // 4
    left_y = top_y - depth // 2
    right_x = x + size//2 + size//4
    right_y = left_y
    triangle_height = depth // 2
    canvas.drawPolygon(top_x, top_y, left_x, left_y, right_x, right_y)
    sierpinski(canvas, x, y + depth // 2, size // 2, depth // 2, iterations, currentIteration + 1)
    sierpinski(canvas, left_x, y, size // 2, depth // 2, iterations, currentIteration + 1)
    sierpinski(canvas, top_x, y+depth//2, size//2, depth // 2, iterations, currentIteration + 1)

    return


sierpinski(c, 100, 100, 400, 400, 5)
g.wait()
