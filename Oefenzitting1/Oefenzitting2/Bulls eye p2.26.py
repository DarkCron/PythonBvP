from graphics import GraphicsWindow

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

window = GraphicsWindow(WINDOW_WIDTH, WINDOW_HEIGHT)

canvas = window.canvas()
canvas.setBackground("white")

canvas.setColor("black")
canvas.drawLine(50, 50, 350, 50)
canvas.drawLine(50, 50, 50, 350)
canvas.drawLine(50, 350, 350, 350)
canvas.drawLine(350, 50, 350, 350)

modifier = 10
offset = 50
canvas.drawOval(offset, offset, 400 - 2 * offset, 400 - 2 * offset)

while 2*offset < 300:
    offset += modifier
    canvas.setColor("white")
    canvas.drawOval(offset, offset, 400 - 2 *offset, 400 - 2 * offset)
    offset += modifier
    canvas.setColor("black")
    canvas.drawOval(offset, offset, 400 - 2 * offset, 400 - 2 * offset)



window.wait()
