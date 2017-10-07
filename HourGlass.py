from  graphics import GraphicsWindow
import math

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_CENTER_X = WINDOW_WIDTH // 2
WINDOW_CENTER_Y = WINDOW_HEIGHT // 2

window = GraphicsWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
canvas = window.canvas()
canvas.setBackground("white")

OFFSET_MODIFIER_WIDTH = 4  # example 4 = WINDOW_WITH /4 as offset from border => higher is less offset
OFFSET_MODIFIER_HEIGHT = 10

OFFSET_X = WINDOW_WIDTH / OFFSET_MODIFIER_WIDTH
OFFSET_Y = WINDOW_HEIGHT / OFFSET_MODIFIER_HEIGHT

#
# NOTE: I handle the triangles from upper triangle to lower.
# First I handle the 'base' line x and y coordinates, and lastly
# the middle vertex.
#
# Upper Triangle:
BG_UPPER_X1 = OFFSET_X
BG_UPPER_Y1 = OFFSET_Y

BG_UPPER_X2 = WINDOW_WIDTH - OFFSET_X
BG_UPPER_Y2 = OFFSET_Y

BG_UPPER_X3 = WINDOW_CENTER_X
BG_UPPER_Y3 = WINDOW_CENTER_Y

# Lower Triangle:
BG_LOWER_X1 = OFFSET_X
BG_LOWER_Y1 = WINDOW_HEIGHT - OFFSET_Y

BG_LOWER_X2 = WINDOW_WIDTH - OFFSET_X
BG_LOWER_Y2 = WINDOW_HEIGHT - OFFSET_Y

BG_LOWER_X3 = WINDOW_CENTER_X
BG_LOWER_Y3 = WINDOW_CENTER_Y


# BorderSize is the size (in pixels) of the hourglass 'outline' only for triangles
def DrawUpperHourGlass(borderSize):
    # As triangles (is old code before I started using lines)
    # canvas.setColor("black")
    # canvas.drawPolygon(BG_UPPER_X1 , BG_UPPER_Y1 , BG_UPPER_X2 , BG_UPPER_Y2, BG_UPPER_X3, BG_UPPER_Y3)
    # canvas.setColor("white")
    # canvas.drawPolygon(BG_UPPER_X1 + borderSize, BG_UPPER_Y1 + borderSize, BG_UPPER_X2 - borderSize, BG_UPPER_Y2 + borderSize, BG_UPPER_X3, BG_UPPER_Y3 - borderSize)
    # As lines
    canvas.setColor("black")
    canvas.drawLine(BG_UPPER_X1, BG_UPPER_Y1, BG_UPPER_X2, BG_UPPER_Y2)
    canvas.drawLine(BG_UPPER_X1, BG_UPPER_Y1, BG_UPPER_X3, BG_UPPER_Y3)
    canvas.drawLine(BG_UPPER_X2, BG_UPPER_Y2, BG_UPPER_X3, BG_UPPER_Y3)
    return;


# BorderSize is the size (in pixels) of the hourglass 'outline' only for triangles
def DrawLowerHourGlass(borderSize):
    # As triangles
    # canvas.setColor("black")
    # canvas.drawPolygon(BG_LOWER_X1 , BG_LOWER_Y1 , BG_LOWER_X2 , BG_LOWER_Y2, BG_LOWER_X3, BG_LOWER_Y3)
    # canvas.setColor("white")
    # canvas.drawPolygon(BG_LOWER_X1 + borderSize, BG_LOWER_Y1 - borderSize, BG_LOWER_X2 - borderSize, BG_LOWER_Y2 - borderSize, BG_LOWER_X3, BG_LOWER_Y3 + borderSize)
    # As lines
    canvas.setColor("black")
    canvas.drawLine(BG_LOWER_X1, BG_LOWER_Y1, BG_LOWER_X2, BG_LOWER_Y2)
    canvas.drawLine(BG_LOWER_X1, BG_LOWER_Y1, BG_LOWER_X3, BG_LOWER_Y3)
    canvas.drawLine(BG_LOWER_X2, BG_LOWER_Y2, BG_LOWER_X3, BG_LOWER_Y3)
    return;


# DRAW Background Hourglass

DrawUpperHourGlass(3)
DrawLowerHourGlass(3)
# canvas.drawPolygon(BG_UPPER_X1, BG_UPPER_Y1, BG_UPPER_X2, BG_UPPER_Y2, BG_UPPER_X3, BG_UPPER_Y3)

triangleBase = WINDOW_WIDTH - 2 * OFFSET_X
triangleHeight = (WINDOW_HEIGHT // 2) - OFFSET_Y
triangleSurface = triangleBase * triangleHeight / 2
triangleSideLength = math.sqrt(math.pow(triangleBase, 2) + math.pow(triangleHeight, 2))
triangleThetaRad = math.atan(float(triangleBase / 2) / float(triangleHeight))
triangleThetaDeg = math.degrees(triangleThetaRad)

print("Triangle base: %i , Triangle height: %i " % (triangleBase, triangleHeight))
print("Triangle surface: %i" % triangleSurface)
print("Theta rad: %i.2 , Theta deg: %i.2" % (triangleThetaRad, triangleThetaDeg))

minutes = int(input("Please enter minutes: "))
seconds = int(input("Please enter seconds: "))

MAX_MINUTES = 8
MAX_SECONDS = 0
MAX_SECONDS = MAX_MINUTES * 60 + MAX_SECONDS
totalSeconds = minutes * 60 + seconds
percentage = 0.0

if totalSeconds >= MAX_SECONDS:
    percentage = 1.0
elif totalSeconds == 0:
    percentage = 0.0  # even though percentage is initialized as 0.0 this line improves readability.
else:
    percentage = float(totalSeconds / MAX_SECONDS)


#
# We know that as time progresses more sand slips through the hourglass and thus over time the height gets adjusted. We can precisely test the surface area looping the height (from max to 0)
# so that we can find a base for the 'fill' triangle so that we get a percentage of the original surface.
#
def CalculateUpperBase(p):
    p = 1 - p

    if p == 0.0:
        return 0
    elif p == 1.0:
        return  triangleHeight

    targetSurface = triangleSurface * p
    for i in range(int(triangleHeight), 0,
                   -1):  # I use a for instead of a while to avoid 'getting stuck' which shouldn't happen.
        tmpHeight = i
        tmpBase = tmpHeight * math.tan(triangleThetaRad)
        tmpSurface = tmpHeight * tmpBase / 2 * 2
        if targetSurface >= tmpSurface:
            return tmpHeight;

    return float(triangleHeight);  # a 'failsafe' should the function fail just return the base height


upperFilledTriangleHeight = CalculateUpperBase(percentage)
upperFilledTriangleWidth = upperFilledTriangleHeight * math.tan(triangleThetaRad) * 2
upperFilledOffsetX = OFFSET_X + (triangleBase - upperFilledTriangleWidth) / 2
upperFilledOffsetY = OFFSET_Y + (triangleHeight - upperFilledTriangleHeight)

lowerFilledTriangleHeight = CalculateUpperBase(1 - percentage)  # Calculate the complement of 100% for the lower triangle
lowerFilledTriangleWidth = lowerFilledTriangleHeight * math.tan(triangleThetaRad) * 2
lowerFilledOffsetX = OFFSET_X + (triangleBase - lowerFilledTriangleWidth) / 2
lowerFilledOffsetY = WINDOW_CENTER_Y + (triangleHeight - lowerFilledTriangleHeight)

canvas.setColor("blue")
canvas.drawPolygon(upperFilledOffsetX, upperFilledOffsetY, WINDOW_WIDTH - upperFilledOffsetX, upperFilledOffsetY,
                   BG_UPPER_X3, BG_UPPER_Y3)
canvas.drawPolygon(lowerFilledOffsetX, WINDOW_HEIGHT - OFFSET_Y, WINDOW_WIDTH - lowerFilledOffsetX,
                   WINDOW_HEIGHT - OFFSET_Y, WINDOW_CENTER_X, lowerFilledOffsetY)

window.wait()
