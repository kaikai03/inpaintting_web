# -*- coding: UTF-8 -*-
import socket
import sys
import time


def connect_Printer(HOST, sock):
    try:
        sock.settimeout(5)
        sock.connect((HOST, 9100))
        print("connect success\n")
    except Exception as e:
        err = str(e)
        print("Connect fail, Reason:\n")
        print(err)

def get_ID(sock):   #打印机型号信息
    try:
        sock.settimeout(5)
        sock.send(b"@PJL INFO ID\r\n")
        time.sleep(1)   #Delay
        rec = sock.recv(256)
        print(rec.decode('utf-8'))
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get ID information fail,Reason:\n")
        print(err)

def get_ENV(sock):  #打印机变量信息
    try:
        sock.settimeout(10)
        sock.send(b"@PJL INFO VARIABLES\r\n")
        time.sleep(2)   #Delay
        rec = sock.recv(40960)
        print(rec.decode('utf-8'))
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get variable information fail,Reason:\n")
        print(err)

def get_CONFIG(sock):   #打印机初始化信息
    try:
        sock.settimeout(3)
        sock.send(b"@PJL INFO CONFIG\r\n")
        time.sleep(2)   #Delay
        rec = sock.recv(40960)
        print(rec.decode('utf-8'))
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get config information fail,Reason:\n")
        print(err)

def get_MEM(sock):  #打印机内存信息
    try:
        sock.settimeout(3)
        sock.send(b"@PJL INFO MEMORY\r\n")
        time.sleep(2)   #Delay
        rec = sock.recv(1024)
        print(rec.decode('utf-8'))
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get memory information fail,Reason:\n")
        print(err)

def get_PAGECOUNT(sock):  #打印计数
    try:
        sock.settimeout(3)
        sock.send(b"@PJL INFO PAGECOUNT\r\n")
        time.sleep(2)   #Delay
        rec = sock.recv(1024)
        print(rec.decode('utf-8'))
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get pagecount information fail,Reason:\n")
        print(err)

def get_STATUS(sock):  #打印机状态
    try:
        sock.settimeout(3)
        sock.send(b"@PJL INFO STATUS\r\n")
        time.sleep(2)   #Delay
        rec = sock.recv(1024)
        print(rec.decode('utf-8'))
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get status information fail,Reason:\n")
        print(err)

def main():
    # HOST = sys.argv[1]
    HOST = '192.168.1.114'
    sock = socket.socket()
    connect_Printer(HOST, sock)
    get_ID(sock)
    get_ENV(sock)
    get_CONFIG(sock)
    get_MEM(sock)
    get_PAGECOUNT(sock)
    get_STATUS(sock)

    sock.close()

if __name__ == '__main__':
    try:
        main()
    # catch CTRL-C
    except (KeyboardInterrupt):
        pass
    finally:
        print("")

# try:
#     sock.settimeout(5)
#     sock.send(b"@PJL INFO ID\r\n")
#     time.sleep(1)  # Delay
#     rec = sock.recv(256)
#     print(rec.decode('utf-8'))
#     sys.stdout.flush()
# except Exception as e:
#     err = str(e)
#     print("Get ID information fail,Reason:\n")
#     print(err)