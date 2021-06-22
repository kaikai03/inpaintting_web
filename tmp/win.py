import win32gui, win32con, win32api
import win32clipboard as w
from array import array
import time
import xmltodict
import re


class Q:
    def __init__(self, window_name="S1韭菜跟车群"):
        self.window_name = window_name
        self.handle = 0
        self.last_row = None

    def get_handle(self):
        handle = win32gui.FindWindow('TXGuiFoundation', self.window_name)
        if handle == 0:
            print('get handle errrrrrrrrrrrrrrrrrrror')
        else:
            self.handle = handle
            print('get handle success',win32gui.GetWindowText(handle),win32gui.GetClassName(handle))

    def handle_check(self):
        win32gui.ShowWindow(self.handle, win32con.SW_SHOW)
        win32gui.ShowWindow(self.handle, win32con.SW_HIDE)

    def process(self):
        self.select_copy_ctr()
        data = self.read_clip_board()
        if data is not None:
            new_data = self.parse_clip_board(data)
            print(new_data)

    def select_copy_ctr(self):
        win32gui.SendMessage(self.handle, win32con.WM_ACTIVATE, 0, 0)
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0);
        time.sleep(0.8)
        win32gui.SendMessage(self.handle, win32con.WM_KEYDOWN, 0x00000041, 0x401E0001)
        win32gui.SendMessage(self.handle, win32con.WM_CHAR, 0x00000001, 0x001E0001)
        time.sleep(0.5)
        win32gui.SendMessage(self.handle, win32con.WM_KEYDOWN, 0x00000043, 0x002E0001)
        win32gui.SendMessage(self.handle, win32con.WM_CHAR, 0x00000003, 0x002E0001)
        time.sleep(0.3)
        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

    def read_clip_board(self):
        # 富文本49860  文本13
        w.OpenClipboard()
        check_data = w.GetClipboardData(49860)
        if check_data[0:len('<QQRichEditFormat>')]==b'<QQRichEditFormat>':
            data = w.GetClipboardData(13)
        else:
            data = None
            print('未get到QQ数据')
        w.CloseClipboard()
        return data

    def read_clip_board_back_up(self):
        format_ = None
        # while True:
        w.OpenClipboard()
        if format_ is None:
            format_ = w.EnumClipboardFormats()
        else:
            format_ = w.EnumClipboardFormats(format_)
        data = w.GetClipboardData(format_)
        print(format_)
        print(data)
        w.CloseClipboard()

    def parse_clip_board(self,data):
        tmp = None
        res = []
        if data is None: return None

        for row in data.split('\r\n\r\n')[::-1]:
            ###！！！ 注意，倒序的。
            if len(row) < 3:
                continue
            ti = re.findall(r"(\d{1,2}:\d{1,2}:\d{1,2})", row)
            if len(ti) == 0:
                tmp = row
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
                if len(at_users) > 0:
                    for at in at_users:
                        content = content.replace(at.replace('@', ''), '')
                        content = content.replace('@', '')
                tmp = None

            if self.last_row == '+'.join((user, ti, content)):
                print('匹配末尾，退出')
                break
            res.append((user, ti, content))

        if len(res) > 0:  # 返回前改回正序
            res.reverse()
            self.last_row = '+'.join(res[-1])

        return res


if __name__ == '__main__':
    q = Q('S1韭菜跟车群')
    q.get_handle()
    while 1:
        q.process()
        time.sleep(15)
    pass






# 富文本 0: 文本  1: 图片[imagebiztype="0(新图),1(表情包.jpg),2(热图),7(表情包.gif)"] 2: 小表情 5: 来自表情商城 6: Emoji
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
