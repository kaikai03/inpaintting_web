import win32gui,win32con,win32api
import win32clipboard as w
from array import array
import time
import xmltodict


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
# x1,y1,x2,y2 = win32gui.GetWindowRect(handle)
# win32api.SetCursorPos((x2-int((x2-x1)/2),y2-int((y2-y1)/2)))
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
# windows = []
# win32gui.EnumChildWindows(handle, lambda hwnd,param: param.append(hwnd), windows)


# 0: 文本  1: 图片[imagebiztype="0(新图),1(表情包.jpg),2(热图),7(表情包.gif)"] 2: 小表情 5: 来自表情商城 6: Emoji
handle = win32gui.FindWindow('TXGuiFoundation', "满朝文武第四次哭蜀国")
win32gui.GetWindowText(handle)
win32gui.GetClassName(handle)

win32gui.ShowWindow(handle,win32con.SW_SHOW)
win32gui.ShowWindow(handle,win32con.SW_HIDE)





text = array('b', b'\x00\x00' * 99)
text_len = win32gui.SendMessage(handle, win32con.WM_GETTEXT, 99, text)
win32gui.PyGetString(text.buffer_info()[0], 99 - 1).lower()

win32gui.SendMessage(handle, win32con.WM_ACTIVATE, 0, 0)
win32api.keybd_event(win32con.VK_CONTROL,0,0,0);
time.sleep(1)
win32gui.SendMessage(handle, win32con.WM_KEYDOWN, 0x00000041, 0x401E0001)
win32gui.SendMessage(handle, win32con.WM_CHAR, 0x00000001, 0x001E0001)
time.sleep(1)
win32gui.SendMessage(handle, win32con.WM_KEYDOWN, 0x00000043, 0x002E0001)
win32gui.SendMessage(handle, win32con.WM_CHAR, 0x00000003, 0x002E0001)
time.sleep(1)
win32api.keybd_event(win32con.VK_CONTROL,0,win32con.KEYEVENTF_KEYUP,0)


win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)

# 49860
format=None
w.OpenClipboard()
# if format is None:
#     format = w.EnumClipboardFormats()
# else:
#     format = w.EnumClipboardFormats(format)
data = w.GetClipboardData(49860)
print(format)
print(data)
w.CloseClipboard()


ele = xmltodict.parse(data.decode('utf-8'))
for item in ele['QQRichEditFormat']['EditElement']:
    print("key:",item.keys())
    # print("item:",item)
    print(item['@type'])
    # if int(item['@type']) == 0 and '#text' in item.keys():
    #     print(item['#text'])



