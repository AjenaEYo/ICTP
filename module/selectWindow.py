import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics
import ctypes
from pynput import mouse

ctypes.windll.user32.SetProcessDPIAware()
dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
red = win32api.RGB(255, 0, 0) # Red

past_coordinates = monitor

def draw_rect():
    global past_coordinates
    rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
    win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)
    selectwnd=win32gui.WindowFromPoint(win32api.GetCursorPos())
    window_rect = win32gui.GetWindowRect(selectwnd)
    m = window_rect[0],window_rect[1]
    n = window_rect[2],window_rect[3]
    for x in range(100):
        win32gui.SetPixel(dc, m[0]+x, m[1], red)
        win32gui.SetPixel(dc, m[0]+x, m[1]+1, red)
        win32gui.SetPixel(dc, m[0]+x, m[1]+2, red)
        #win32gui.SetPixel(dc, m[0]+x, m[1]+10, red)
        for y in range(100):
            win32gui.SetPixel(dc, m[0], m[1]+y, red)
            win32gui.SetPixel(dc, m[0]+1, m[1]+y, red)
            win32gui.SetPixel(dc, m[0]+2, m[1]+y, red)
            #win32gui.SetPixel(dc, m[0]+10, m[1]+y, red)
    
    for x in range(100):
        win32gui.SetPixel(dc, n[0]-x, n[1], red)
        win32gui.SetPixel(dc, n[0]-x, n[1]+1, red)
        win32gui.SetPixel(dc, n[0]-x, n[1]+2, red)
        #win32gui.SetPixel(dc, m[0]+x, m[1]+10, red)
        for y in range(100):
            win32gui.SetPixel(dc, n[0], n[1]-y, red)
            win32gui.SetPixel(dc, n[0]+1, n[1]-y, red)
            win32gui.SetPixel(dc, n[0]+2, n[1]-y, red)
            #win32gui.SetPixel(dc, m[0]+10, m[1]+y, red)

    past_coordinates = (m[0], m[1], n[0], n[1])


def draw_rect_fast():
    global past_coordinates
    rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
    win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)
    selectwnd=win32gui.WindowFromPoint(win32api.GetCursorPos())
    window_rect = win32gui.GetWindowRect(selectwnd)
    m = window_rect[0],window_rect[1]
    n = window_rect[2],window_rect[3]

    ###m-----------###
    ###|          |
    ###|          |            
    ###|          |
    ###|----------n###
    
    for x in range(100):
        win32gui.SetPixel(dc, m[0]+x, m[1], red)
        win32gui.SetPixel(dc, m[0]+x, m[1]+1, red)
        win32gui.SetPixel(dc, m[0]+x, m[1]+2, red)
        #win32gui.SetPixel(dc, m[0]+x, m[1]+10, red)
        for y in range(100):
            win32gui.SetPixel(dc, m[0], m[1]+y, red)
            win32gui.SetPixel(dc, m[0]+1, m[1]+y, red)
            win32gui.SetPixel(dc, m[0]+2, m[1]+y, red)
            #win32gui.SetPixel(dc, m[0]+10, m[1]+y, red)
    
    for x in range(100):
        win32gui.SetPixel(dc, n[0]-x, n[1], red)
        win32gui.SetPixel(dc, n[0]-x, n[1]+1, red)
        win32gui.SetPixel(dc, n[0]-x, n[1]+2, red)
        #win32gui.SetPixel(dc, m[0]+x, m[1]+10, red)
        for y in range(100):
            win32gui.SetPixel(dc, n[0], n[1]-y, red)
            win32gui.SetPixel(dc, n[0]+1, n[1]-y, red)
            win32gui.SetPixel(dc, n[0]+2, n[1]-y, red)
            #win32gui.SetPixel(dc, m[0]+10, m[1]+y, red)

    past_coordinates = (m[0], m[1], n[0], n[1])

prehwnd = -1

def on_move(x,y):
    global prehwnd 
    print('Position : x:%s, y:%s' %(x,y))
    selectwnd=win32gui.WindowFromPoint(win32api.GetCursorPos())
    if prehwnd != selectwnd:
        prehwnd = selectwnd
        try:
            draw_rect()
        except:
            pass
   

def on_click(x, y, button, pressed):
    print('Button: %s, Position: (%s, %s), Pressed: %s ' %(button, x, y, pressed))
    return False

def on_scroll(x, y, dx, dy):
    print('Scroll: (%s, %s) (%s, %s).' %(x, y, dx, dy))

def on():
    with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
        listener.join()

if __name__ == "__main__":
	on()