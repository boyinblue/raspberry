#!/usr/bin/env python

import socket
import time

SOCKET_PATH = "/var/run/lirc/lircd"

sock = None
sync_mode = True

def init_irw(blocking = False):
    global sock
    global sync_mode

    if blocking == True:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    else:
        sock = socket.socket(socket.AF_UNIX,
                    socket.SOCK_STREAM | socket.SOCK_NONBLOCK)

    sync_mode = blocking

    print ('Connect to lirc socket : ', SOCKET_PATH)
    sock.connect(SOCKET_PATH)

def read_key_async():
    try:
        data = sock.recv(128)
    except BlockingIOError:
        return None
    
    return data

def read_key_sync():
    while True:
        data = sock.recv(128)
    
        if data:
            data = data.strip()
            return data

def read_key():
    '''Get the next key pressed. Return keyname, updown.
    '''
    global sync_mode
    if sync_mode:
        data = read_key_sync()
    else:
        data = read_key_async()

    if data:
        words = data.split()
        return words[2], words[1]

    return '', ''

def main_sync():
    init_irw(blocking = True)

    while True:
        keyname, updown = read_key()
        print('%s (%s)' % (keyname, updown))

def main_async():
    init_irw(blocking = False)

    while True:
        keyname, updown = read_key()
        if keyname == '' and updown == '':
            time.sleep(0.1)
            continue
        print('%s (%s)' % (keyname, updown))

if __name__ == '__main__':
    #main_async()
    main_sync()
