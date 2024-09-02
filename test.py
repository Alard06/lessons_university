:mport pygame as pg

pg.init()

WIDTH, HEIGHT = 700, 700

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Images')


orig_image = pg.image.load('d2.png')
orig_image = pg.transform.scale(orig_image, (200,200))

def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
        return True


def update():
    pg.display.flip()


while check_events():
54319339:AAEw04HGhXksoWseLr8xbEdAJWeb17FjhwA'
