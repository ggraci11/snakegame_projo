def drawGrid (w,rows,surface):
    
    pass


def redrawWindow (surface):
    global rows, width
    win.fill((0,0,0))
    drawGrid(surface)
    pygame.display.update



def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((225,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock() 

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)

    pass


