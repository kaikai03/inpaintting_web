import sys
from random import choice, randrange
from string import ascii_letters

import pygame as pg

import win32api
import win32con
import win32gui


def random_letters(n):
    """Pick n random letters."""
    return ''.join(choice(ascii_letters) for _ in range(n))


def main():
    info = pg.display.Info()
    # screen = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN)
    screen = pg.display.set_mode((200, 100), pg.NOFRAME) #pg.NOFRAME
    screen_rect = screen.get_rect()
    font = pg.font.Font(None, 25)
    clock = pg.time.Clock()
    color = (randrange(256), randrange(256), randrange(256))
    txt = font.render(random_letters(randrange(5, 21)), True, color)
    timer = 10
    done = False
    show_frame = False
    show_ctr = False

    fuchsia = (255, 0, 128)
    ctr_tip = (50, 200, 50)
    hwnd = pg.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)


    while not done:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True
                if event.key == pg.K_SPACE:
                    if show_frame:
                        show_frame = False
                        screen = pg.display.set_mode((200, 100), pg.NOFRAME)
                    else:
                        show_frame = True
                        screen = pg.display.set_mode((200, 100), 0)
                # if event.key == pg.K_LCTRL or event.key == pg.K_RCTRL:
                #     show_ctr = True

            # if event.type == pg.KEYUP:
            #     if event.key == pg.K_LCTRL or event.key == pg.K_RCTRL:
            #         show_ctr = False



        timer -= 1
        show_ctr = win32api.GetKeyState(win32con.VK_CONTROL) & 0x8000
        # Update the text surface and color every 10 frames.
        if timer <= 0:
            timer = 10
            color = (randrange(256), randrange(256), randrange(256))
            txt = font.render(random_letters(randrange(5, 21)), True, color)


        # screen.fill((130, 130, 130))
        if show_ctr:
            screen.fill(ctr_tip)
        else:
            screen.fill(fuchsia)

        screen.blit(txt, txt.get_rect(center=screen_rect.center))

        pg.display.flip()
        clock.tick(30)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,
                              0, 0, 0, 0,
                              win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE| win32con.SWP_NOMOVE)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()