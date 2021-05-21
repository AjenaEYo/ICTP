import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics
import ctypes
from pynput import mouse

ctypes.windll.user32.SetProcessDPIAware()
dc = win32gui.GetDC(0)
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
red = win32api.RGB(255, 0, 0) # Red

past_coordinates = monitor

def draw_rect():
    global past_coordinates
    rect = win32gui.CreateRoundRectRgn(*past_coordinates, 5 , 5)
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
    Mypen = win32gui.CreatePen(win32con.PS_SOLID,5,red)
    OldPen = win32gui.SelectObject(dc,Mypen)

    #win32gui.Rectangle(dc,50,50,100,100)
    win32gui.MoveToEx(dc,m[0],m[1])
    win32gui.LineTo(dc,m[0],m[1]+100)
    win32gui.MoveToEx(dc,m[0],m[1])
    win32gui.LineTo(dc,m[0]+100,m[1])
    win32gui.MoveToEx(dc,n[0],n[1])
    win32gui.LineTo(dc,n[0],n[1]-100)
    win32gui.MoveToEx(dc,n[0],n[1])
    win32gui.LineTo(dc,n[0]-100,n[1])
    win32gui.SelectObject(dc,OldPen)
    win32gui.DeleteObject(Mypen)
    #win32gui.InvalidateRect(hwnd, monitor, True)
    past_coordinates = (m[0]-20, m[1]-20, n[0]+20, n[1]+20)

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
