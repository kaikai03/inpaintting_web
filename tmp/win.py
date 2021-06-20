import win32gui, win32con, win32api
import win32clipboard as w
from array import array
import time
import xmltodict
import re

# 0: 文本  1: 图片[imagebiztype="0(新图),1(表情包.jpg),2(热图),7(表情包.gif)"] 2: 小表情 5: 来自表情商城 6: Emoji
handle = win32gui.FindWindow('TXGuiFoundation', "S1韭菜跟车群")
win32gui.GetWindowText(handle)
win32gui.GetClassName(handle)

win32gui.ShowWindow(handle, win32con.SW_SHOW)
win32gui.ShowWindow(handle, win32con.SW_HIDE)

win32gui.SendMessage(handle, win32con.WM_ACTIVATE, 0, 0)
win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0);
time.sleep(0.8)
win32gui.SendMessage(handle, win32con.WM_KEYDOWN, 0x00000041, 0x401E0001)
win32gui.SendMessage(handle, win32con.WM_CHAR, 0x00000001, 0x001E0001)
time.sleep(0.5)
win32gui.SendMessage(handle, win32con.WM_KEYDOWN, 0x00000043, 0x002E0001)
win32gui.SendMessage(handle, win32con.WM_CHAR, 0x00000003, 0x002E0001)
time.sleep(0.3)
win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

# win32gui.SendMessage(handle, win32con.WM_COPY, 0, 0)
# win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)

# 富文本49860  文本13
format = None
w.OpenClipboard()
# if format is None:
#     format = w.EnumClipboardFormats()
# else:
#     format = w.EnumClipboardFormats(format)
data = w.GetClipboardData(13)
print(format)
print(data)
w.CloseClipboard()


tmp = None
for row in data.split('\r\n\r\n')[::-1]:
    print('ortigin--:', row)
    if len(row) < 3:
        continue
    ti = re.findall(r"(\d{1,2}:\d{1,2}:\d{1,2})", row)
    if len(ti) == 0:
        tmp = row
        print('tmmmmp')
        continue

    if row[0:2] == '\r\n':
        row_ = row[2:]
    else:
        row_ = row

    std_row_sp = row_.split('\r\n')
    user = std_row_sp[0].replace(ti[0], '')
    user = user[:-1]
    ti = ti[0]
    if len(std_row_sp) > 1:
        content = std_row_sp[1]
    else:
        content = ''

    if len(content) > 2:
        content = re.sub(r"(@.*? )", '', content)

    if tmp is not None:
        content = content + tmp
        at_users = re.findall(r"(@.*? )", tmp)
        print('at_users:',at_users)
        if len(at_users) > 0:
            for at in at_users:
                content = content.replace(at.replace('@', ''), '')
                content = content.replace('@', '')
        tmp = None



    print('final:--',user, ti, content)
    print('\r\n')

a = '\r\n冥河娃娃 20:00:08\r\n有的哦'
b = '洛西 19:52:53\r\nlazy  '
c = '@lazy 还在'
d = '@围观型青阳子 另附上一小段论述帝国的防务状况的水平，来自基里曼分析五百世界的防御局势时的评论：“如果异形还不够贪婪，多年来的腐败已经掏空了旧军团的遗产。我去过的所有星球，没有一个地方的防御布置，军事资产或者其他任何东西，合乎账目。十分之一是伪造的。相当一部分财政资金被挪用了。许多被直接偷走了，他们不害怕帝国的权威，但是他们会怕的。我已经联系了异端审判庭和法务部，他们的特工和仲裁官会协助我。将会有一场处决，大规模处决。” 作者：rtgghuuggg https://www.bilibili.com/read/cv11630389 出处：bilibili'

re.findall(r"(@.*? )", d)

#
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

# text = array('b', b'\x00\x00' * 99)
# text_len = win32gui.SendMessage(handle, win32con.WM_GETTEXT, 99, text)
# win32gui.PyGetString(text.buffer_info()[0], 99 - 1).lower()

# ele = xmltodict.parse(data.decode('utf-8'))
# for item in ele['QQRichEditFormat']['EditElement']:
#     print("key:",item.keys())
#     # print("item:",item)
#     print(item['@type'])
#     # if int(item['@type']) == 0 and '#text' in item.keys():
#     #     print(item['#text'])
