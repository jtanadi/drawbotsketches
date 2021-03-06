PAGESIZE = 600
SQUARE = 40
FRAMES = 60

def drawSlash(x, y):
    line((x, y), (x + SQUARE, y + SQUARE))


for frame in range(FRAMES):
    newPage(PAGESIZE, PAGESIZE)

    factor = sin(2 * pi * frame / FRAMES)

    fill(0)
    rect(0, 0, PAGESIZE, PAGESIZE)

    fill(None)
    stroke(1)
    strokeWidth(10)
    lineCap("square")

    for y in range(0, PAGESIZE, SQUARE):
        save()
        for x in range(PAGESIZE // SQUARE):
            save()
            translate(SQUARE / 2, SQUARE / 2)
            rotate(randint(1, 2) * 180 * factor)
            translate(-SQUARE / 2, -SQUARE / 2)
            drawSlash(0, 0)
            restore()
            translate(SQUARE, 0)
        restore()
        translate(0, SQUARE)

saveImage("_gifs/slash_rotate.gif")