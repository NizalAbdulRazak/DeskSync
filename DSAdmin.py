import socket
import pickle
import cv2
import threading
import struct
import numpy
import time
import zlib
from pynput import keyboard

ip = socket.gethostbyname(socket.gethostname())
port = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip, port))

def handler(conn, addr):

    data = b""
    payload_size = struct.calcsize("L")

    def click_event(event, x, y, flags, param):
        conn.send(pickle.dumps(((int((1920*x)/1280),int(((1080*y)/720)), event))))
    
    def keyboard_listener():
        def sender(k):
            conn.send(pickle.dumps(k))
            print(f"sent {k}")
        with keyboard.Listener(on_press=sender) as listen:
            listen.join()

    key_thr = threading.Thread(target=keyboard_listener)
    # key_thr.start()
    
    try:
        while True:
            timeSample = time.time()
            while len(data) < payload_size:
                data += conn.recv(4096)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += conn.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            image = numpy.array(pickle.loads(zlib.decompress(frame_data)).resize((1280, 720)))

            image = cv2.putText(image, f"FPS: {int(1/(time.time() - timeSample))}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            cv2.imshow('frame', image[:,:,::-1])
            cv2.setMouseCallback("frame", click_event)
            cv2.waitKey(1)
    except ConnectionResetError:
        # cv2.destroyAllWindows()
        start_server()

def start_server():
    while True:
        server.listen()
        conn, addr = server.accept()
        print(conn)
        serverThread = threading.Thread(target = lambda: handler(conn, addr))
        serverThread.start()

start_server()
