import win32gui,win32con,win32api
import win32clipboard as w
from array import array
import time
import ctypes

PBYTE256 = ctypes.c_ubyte * 256
_user32 = ctypes.WinDLL("user32")
GetKeyboardState = _user32.GetKeyboardState
SetKeyboardState = _user32.SetKeyboardState
PostMessage = win32api.PostMessage
SendMessage = win32gui.SendMessage
FindWindow = win32gui.FindWindow
IsWindow = win32gui.IsWindow
GetCurrentThreadId = win32api.GetCurrentThreadId
GetWindowThreadProcessId = _user32.GetWindowThreadProcessId #it is very important to take the function from the dll, since Python wrapper (win32process.GetWindowThreadProcessId) gives incorrect values
AttachThreadInput = _user32.AttachThreadInput

MapVirtualKeyA = _user32.MapVirtualKeyA
MapVirtualKeyW = _user32.MapVirtualKeyW

def PostKeyEx( hwnd, key, shift, specialkey):

    MakeLong = win32api.MAKELONG
    w = win32con  # so short entry
    ThreadId = GetWindowThreadProcessId(hwnd, None)

    lparam = MakeLong(0, MapVirtualKeyA(key, 0))
    msg_down=w.WM_KEYDOWN
    msg_up=w.WM_KEYUP

    if specialkey:
        lparam = lparam | 0x1000000

    if len(shift) > 0: #If there are modifiers - use PostMessage and AttachThreadInput
        pKeyBuffers = PBYTE256()
        pKeyBuffers_old = PBYTE256()

    SendMessage(hwnd, w.WM_ACTIVATE, w.WA_ACTIVE, 0)
    AttachThreadInput(GetCurrentThreadId(), ThreadId, True)
    GetKeyboardState( ctypes.byref(pKeyBuffers_old ))

    for modkey in shift:
        if modkey == w.VK_MENU:
            lparam = lparam | 0x20000000
            msg_down=w.WM_SYSKEYDOWN
            msg_up=w.WM_SYSKEYUP
            pKeyBuffers[modkey] |= 128


    SetKeyboardState( ctypes.byref(pKeyBuffers) )
    time.sleep(0.01)
    PostMessage( hwnd, msg_down, key, lparam)
    time.sleep(0.01)
    PostMessage( hwnd, msg_up, key, lparam | 0xC0000000)
    time.sleep(0.01)
    SetKeyboardState( ctypes.byref(pKeyBuffers_old) )
    time.sleep(0.01)
    AttachThreadInput(GetCurrentThreadId(), ThreadId, False)



# #打开剪贴板
# w.OpenClipboard()
# #清空剪贴板
# w.EmptyClipboard()
# #设置剪贴板内容
# w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
# #获取剪贴板内容
# date = w.GetClipboardData()
# #关闭剪贴板
# w.CloseClipboard()

# #显示窗口
# win32gui.ShowWindow(handle,win32con.SW_SHOW)
# #把剪切板内容粘贴到qq窗口
# win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
# #按下后松开回车键，发送消息
# win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
# win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
# 关闭窗口
# win32gui.PostMessage(win32lib.findWindow(classname, titlename), win32con.WM_CLOSE, 0, 0)
# def click1(x,y): #第一种
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
# win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600, 300, 600, 600, win32con.SWP_SHOWWINDOW)

handle = win32gui.FindWindow('TXGuiFoundation', "满朝文武第四次哭蜀国")
win32gui.GetWindowText(handle)
win32gui.GetClassName(handle)
x1,y1,x2,y2 = win32gui.GetWindowRect(handle)
win32api.SetCursorPos((x2-int((x2-x1)/2),y2-int((y2-y1)/2)))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

win32gui.ShowWindow(handle,win32con.SW_SHOW)
win32gui.ShowWindow(handle,win32con.SW_HIDE)

windows = []
win32gui.EnumChildWindows(handle, lambda hwnd,param: param.append(hwnd), windows)

win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
win32gui.SendMessage(handle, win32con.WM_COPY, 0, 0)


text = array('b', b'\x00\x00' * 99)
text_len = win32gui.SendMessage(handle, win32con.WM_GETTEXT, 99, text)
win32gui.PyGetString(text.buffer_info()[0], 99 - 1).lower()

win32gui.PostMessage(handle, win32con.WM_CHAR, ord('a'), 0xF0001)

win32gui.PostMessage(handle, win32con.WM_KEYDOWN, win32con.VK_CONTROL, 0xF0001)
win32gui.PostMessage(handle, win32con.WM_KEYUP, ord('v'), 0xF0001)

win32gui.SendMessage(handle, win32con.WM_KEYDOWN, 0x00000011, 0x401D0001)
win32gui.SendMessage(handle, win32con.WM_KEYDOWN, 0x00000041, 0x401E0001)
win32gui.PostMessage(handle, win32con.WM_KEYUP, 0x00000041, 0x401E0001)
win32gui.PostMessage(handle, win32con.WM_KEYUP, 0x00000011, 0x401D0001)
win32gui.PostMessage(handle, win32con.WM_CHAR, 0x00000001, 0x401E0001)



PostKeyEx(handle,ord('A'),[win32con.VK_CONTROL],False)
