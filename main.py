import bluetooth
from pprint import pprint 
import struct
import sys
import time

bt_name = 'tims_bt'
sleep_time = 0.500


# def scan():
#     print("Scanning for bluetooth devices:")
#     devices = bluetooth.discover_devices(lookup_names = True, flush_cache=True, lookup_class = True)
#     number_of_devices = len(devices)
#     print(number_of_devices,"devices found")
#     pprint(devices)
#     return devices

# def filter_results(devices, device_name):
#     i = 0
#     for _, name, _ in devices:
#         if name == device_name:
#             break
#         i += 1
#     if i < len(devices):
#         return {"addr":devices[i][0], "name":devices[i][1], "class":devices[i][2]}
#     else:
#         None

# my_bluetooth = filter_results(scan(), bt_name)

# if my_bluetooth is not None:
#     print("Device:")
#     print(f"\tDevice Name: {my_bluetooth['name']}")
#     print(f"\tDevice MAC Address: {my_bluetooth['addr']}")
#     print(f"\tDevice Class: {my_bluetooth['class']}")
# else:
#     print(f"No bluetooth found matching {bt_name}")

# services = bluetooth.find_service(address=my_bluetooth['addr'])[0]

# pprint(services)

'''
elloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhell
'''

def connect(addr, port):
    sock = bluetooth.BluetoothSocket()
    sock.connect((addr, port))
    return sock

# sock = connect(my_bluetooth["addr"], services["port"])
# if __name__ == '__main__':
#     sock = connect('98:DA:60:04:F6:D1', 1)
#     for i in range(20):
#         result = sock.recv(64)
#         print(result)
#     sock.close()


if __name__ == '__main__':
    try:
        sock = connect('98:DA:60:04:F6:D1', 1)
        sock.send(struct.pack('64s', b'LIGHT0'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT1'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT2'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT3'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT4'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT5'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT6'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT7'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT8'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT9'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT10'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT11'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT12'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT13'))
        result = sock.recv(64)
        print(result)
        print()
        sock.send(struct.pack('64s', b'LIGHT14'))
        result = sock.recv(64)
        print(result)
        print()
    except:
        print("Whoops!")

    sock.close()
# while True:
    # sock.send(b"LIGHT1\0")
    # print("Sent!")
    # result = sock.recv(256)
    # print(result)
    # time.sleep(sleep_time)
    # sock.send(b"LIGHT1\0")
    # result = sock.recv(256)
    # print(result)
    # sock.send(b"LIGHT2\0")
    # result = sock.recv(256)
    # print(result)
    # time.sleep(sleep_time)
    # sock.send(b"LIGHT2\0")
    # result = sock.recv(256)
    # print(result)
    # sock.send(b"LIGHT3\0")
    # result = sock.recv(256)
    # print(result)
    # time.sleep(sleep_time)
    # sock.send(b"LIGHT3\0")
    # result = sock.recv(256)
    # print(result)
    # sock.send(b"LIGHT4\0")
    # result = sock.recv(256)
    # print(result)
    # time.sleep(sleep_time)
    # sock.send(b"LIGHT4\0")
    # result = sock.recv(256)
    # print(result)
    # sock.send(b"LIGHT\0")
    # result = sock.recv(256)
    # print(result)
    # time.sleep(sleep_time)



# print("\n")
