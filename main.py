import pyautogui as pg
import time
#print(pg.position())
#pg.click(1241,66)
#pg.typewrite('google.com')
#pg.typewrite(['enter'])

pg.hotkey('winleft')
pg.typewrite('opera\n')
pg.typewrite('www.youtube.com\n')
pg.hotkey('winleft','up')
time.sleep(3)
pg.click(517,362)