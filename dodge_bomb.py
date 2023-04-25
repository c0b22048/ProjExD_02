import pygame as pg #練習問題２までは。vx,vyの場所がわからない
import random
import sys


delta = {
    pg.K_UP: (0, -1),  #移動量の上
    pg.K_DOWN: (0, +1),  #移動量の下
    pg.K_LEFT: (-1, 0),  #移動量の左
    pg.K_RIGHT: (+1, 0)  #移動量の右
        }



def check_bound(scr_rect:pg.Rect,obj_rect:pg.Rect) -> tuple[bool,bool]:  #引数にpg.Rectを付け加えると関数内でrectクラスの.topとかが認識される。
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引数１：画面surfaceのrect
    引数２：こうかとん、または爆弾surfaceのrect
    戻り値：横方向、縦方向のはみだし判定結果(画面内：True/画面外:False)
    """
    yoko, tate = True, True
    if obj_rect.left < scr_rect.left or scr_rect.right < obj_rect.right :
        yoko = False
    if obj_rect.top < scr_rect.top or scr_rect.bottom  < obj_rect.bottom :
        tate = False
    return yoko, tate
    


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0

    bom_screen = pg.Surface((20, 20))    #爆弾の作成
    vx, vy = +1, +1
    bom_screen.set_colorkey(0)
    pg.draw.circle(bom_screen,(255, 0, 0), (10, 10), 10)
    bx = random.randint(160, 1420)
    by = random.randint(90, 790)
    bb_rect = bom_screen.get_rect()
    bb_rect.center=bx, by  #爆弾の初期位置をx,yに設定
    kk_rect=kk_img.get_rect()  #こうかとんをsurfaceからrectに変化
    kk_rect.center=900, 400  #こうかとんの初期位置の値





    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_list = pg.key.get_pressed()
        for k , mv in delta.items():
            if key_list[k]:
                kk_rect.move_ip(mv)

        if check_bound(screen.get_rect(),kk_rect) != (True,True):  ##（True,True）ははみ出てない状態
            for k , mv in delta.items():
                if key_list[k]:
                    kk_rect.move_ip(-mv[0], -mv[1])  #逆向きにするため-mvにする




        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)

        bb_rect.move_ip(vx, vy)

        yoko, tate = check_bound(screen.get_rect(), bb_rect)
        if not yoko:  #横方向に爆弾がはみ出たら
            vx *= -1
        if not tate:  #縦方向に爆弾がはみ出たら
            vy *= -1

        screen.blit(bom_screen,bb_rect)

        #if kk_rect.colliderect(bb_rect):  #==書かない
            #return 


     
    
        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()