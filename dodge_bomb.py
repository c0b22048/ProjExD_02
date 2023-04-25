import pygame as pg #練習問題２までは。vx,vyの場所がわからない
import sys
import random
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0

    bom_screen = pg.Surface((20,20))    #爆弾の作成
    vx = 0
    vy = 0
    bom_screen.set_colorkey(0)
    pg.draw.circle(bom_screen,(255,0,0),(10,10),10)
    bom = bom_screen.get_rect(center=(random.randint(160,1420),random.randint(90,790)))

    kx=0
    ky=0
    key_lst = {pg.K_UP:(1),pg.K_DOWN:(-1),pg.K_LEFT:(-1),pg.K_RIGHT:(1)}




    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bom = bom_screen.get_rect(center=(vx,vy))
        screen.blit(bom_screen,bom)
        vx += 1
        vy += 1 
    
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()