import sys
from random import choice, randrange
from string import ascii_letters

import pygame as pg

import win32api
import win32con
import win32gui

from tmp import winQ


def random_letters(n):
    """Pick n random letters."""
    return ''.join(choice(ascii_letters) for _ in range(n))


def main():
    q = winQ.Q('S1韭菜群')
    q.get_handle()
    if q.handle == 0:
        raise Exception('handle errorrrr')

    info = pg.display.Info()
    # screen = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN)
    window_size = (info.current_w-200, 30)
    xy = (int(200/2), int(info.current_h - 30 - 12))
    fuchsia = (255, 0, 128)
    ctr_tip = (66, 66, 66)
    txt_color = (180, 180, 180)
    fps = 20
    # color = (randrange(256), randrange(256), randrange(256))

    screen = pg.display.set_mode(window_size, pg.NOFRAME)
    screen_rect = screen.get_rect()
    # font = pg.font.Font('SimHei', 25)

    clock = pg.time.Clock()
    font = pg.font.Font("C:\\Windows\\Fonts\\msyhbd.ttc", 20)
    txt = font.render(random_letters(randrange(5, 21)), True, txt_color)

    timer = 10
    done = False
    show_frame = False
    show_ctr = False


    hwnd = pg.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,xy[0], xy[1], window_size[0], window_size[1],0)

    while not done:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True
                if event.key == pg.K_SPACE:
                    if show_frame:
                        show_frame = False
                        screen = pg.display.set_mode(window_size, pg.NOFRAME)
                    else:
                        show_frame = True
                        screen = pg.display.set_mode(window_size, 0)
                # if event.key == pg.K_LCTRL or event.key == pg.K_RCTRL:
                #     show_ctr = True

            # if event.type == pg.KEYUP:
            #     if event.key == pg.K_LCTRL or event.key == pg.K_RCTRL:
            #         show_ctr = False


        # screen.fill((130, 130, 130))
        if show_ctr:
            screen.fill(ctr_tip)
        else:
            screen.fill(fuchsia)

        timer -= 1
        show_ctr = win32api.GetKeyState(win32con.VK_CONTROL) & 0x8000

        if timer % (fps * 3) == 0:
            msg = q.get_msg()
            if msg:
                print('show:', msg)
                txt = font.render(msg, False, txt_color)

        if timer % (fps * 30) == 0:
            q.process()

        if timer <= 1:
            timer = fps*30 + 1


        screen.blit(txt, txt.get_rect(center=screen_rect.center))

        pg.display.flip()
        clock.tick(fps)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,
                              0, 0, 0, 0,
                              win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE| win32con.SWP_NOMOVE)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()

# font = pg.font.get_fonts()
# for i in font:
#     print(i)
#