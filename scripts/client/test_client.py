#!/usr/bin/python3

import os
import socket
import struct

def send_file(sck: socket.socket, fileName):
    print("Sending data...")
    filesize = os.path.getsize(fileName)
    sck.sendall(struct.pack("<Q", filesize))
    with open(fileName, "rb") as f:
        while read_bytes := f.read(1024):
            sck.sendall(read_bytes)
#try:
if(__name__ == '__main__'):
    with socket.create_connection(("172.16.1.100", 5555)) as conn:
        print("Connecting to the server...")
        send_file(conn, "data.txt")
        print("Sended.")
    print("Connection closed.")
#except:
    #print("There were some troubles!")