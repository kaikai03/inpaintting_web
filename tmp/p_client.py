# -*- coding:utf-8 -*-
__author__ = 'kk'

import websocket
from threading import Thread
import time
import sys


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, code, msg):
    print("### closed ###",code,msg)


def on_open(ws):
    def run(*args):
        for i in range(3):
            # send the message, then wait
            # so thread doesn't exit and socket
            # isn't closed
            if i == 0:
                ws.send("login://%s" % '193.QQ')
            else:
                ws.send("Hello %d" % i)
            time.sleep(1)

        time.sleep(1)
        # ws.close()
        print("Thread terminating...")
        # time.sleep(5)

    Thread(target=run).start()


if __name__ == "__main__":
    websocket.enableTrace(True)
    host = "ws://192.168.1.21:11303/"
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()