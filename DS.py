import pyautogui
import socket
import pickle
import struct
import zlib
import threading

pyautogui.FAILSAFE = False

class socket_code:
    
    def connect():
        
        ip = socket.gethostbyname(socket.gethostname())
        port = 5050

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        thr = threading.Thread(target=lambda:socket_code.click_detect(client))
        
        while True:
            try:
                print("trying to connect")
                client.connect((ip, port))
                print("connected")
                thr.start()
                socket_code.send_image(client)
                break
            except ConnectionRefusedError as e:
                print(e)
                pass

    def send_image(client):
        
        try:
            while True:
                data = zlib.compress(pickle.dumps(pyautogui.screenshot()), level=1)
                client.sendall(struct.pack("L", len(data))+data)
        except ConnectionResetError:
            socket_code.connect()

    def click_detect(client):
        try:
            while True:
                inp = pickle.loads(client.recv(1024))
                try:
                    if inp[2] == 1:
                        pyautogui.click((inp[0], inp[1]))
                        print(inp[0], inp[1])
                    if inp[2] == 7:
                        pyautogui.doubleClick(inp[0], inp[1])
                except Exception as e:
                    inp = str(inp)
                    if "Key" in inp:
                        pyautogui.typewrite(inp)
                    else:
                        pyautogui.typewrite(inp[1])
        except ConnectionResetError:
            pass

socket_code.connect()

