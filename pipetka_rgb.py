import pyautogui
import time
import pyperclip

print('you have 5 sec')
time.sleep(5)# задержка в 0.1 с, чтобы питон не сходил с ума
x, y = pyautogui.position()#получаем в x, y координаты мыши
r, g, b = pyautogui.pixel(x, y)

col = f'rgb({r},{g},{b})'

pyperclip.copy(col)