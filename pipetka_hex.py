import pyautogui
import time
import pyperclip

print('you have 5 sec')
time.sleep(5)# задержка в 0.1 с, чтобы питон не сходил с ума
x, y = pyautogui.position()#получаем в x, y координаты мыши
r, g, b = pyautogui.pixel(x, y)

r = ['0'+str(hex(r)[2:]) if len(hex(r)[2:])==1 else hex(r)[2:]][0]
g = ['0'+str(hex(g)[2:]) if len(hex(g)[2:])==1 else hex(g)[2:]][0]
b = ['0'+str(hex(b)[2:]) if len(hex(b)[2:])==1 else hex(b)[2:]][0]

col = f'#{r}{g}{b}'

pyperclip.copy(col)
print('done')