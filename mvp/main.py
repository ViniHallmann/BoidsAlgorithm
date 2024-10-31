import pygame as pg
from canvas import Canvas
from universe import Universe

def main():
    canvas = Canvas()
    universe = Universe()
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        canvas.clear()
        universe.update()
        universe.draw(canvas.screen)
        canvas.update()

    pg.quit()

if __name__ == "__main__":
    main()
