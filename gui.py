import eel
import bluetooth
import struct
from enum import Enum
from pprint import pprint


"""------------------------------------------------------------------------------------
Bluetooth communication stuff
------------------------------------------------------------------------------------"""
class PacketType(Enum):
    GAME_MOVE:  int     = 0     # TODO Light that was clicked
    GAME_BOARD: int     = 1     # TODO String of 1's and 0's that show which lights are currently on
                                # or off. 16 bits long
    NEW_GAME:   int     = 2     # TODO Signals that we want to start a new game.
    GAME_WON:   int     = 3     # TODO Signals that the game is over

def connect():
    skt = bluetooth.BluetoothSocket()
    skt.connect(('98:DA:60:04:F6:D1', 1))
    return skt


def packet_decode(packet):
	unp = struct.unpack("!i60s", packet)
	return (unp[0], unp[1])


"""------------------------------------------------------------------------------------
Eel functions
------------------------------------------------------------------------------------"""
@eel.expose
def lightChoice_py(light):
	global sock
	sock.send(struct.pack("!i60s", PacketType.GAME_MOVE.value, light.encode(encoding="ascii")))
	ptype, lightStr = packet_decode(sock.recv(64))
	if ptype == PacketType.GAME_BOARD.value:
		return lightStr[:16].decode()
	else:
		print(f"Error: lightPress function. Packet returned: {ptype} {lightStr}")
		return None


@eel.expose
def startNewGame_py():
	global sock
	sock.send(struct.pack("!i60s", PacketType.NEW_GAME.value, b""))
	pkt = sock.recv(64);
	ptype, lightStr = packet_decode(pkt)
	if ptype == PacketType.GAME_BOARD.value:
		test = lightStr[:16].decode()
		return lightStr[:16].decode()
	else:
		print(f"Error: startNewGame function: Packet returned: {ptype} {lightStr}")
		return None


"""------------------------------------------------------------------------------------
Eel functions
------------------------------------------------------------------------------------"""
if __name__ == "__main__":
	global sock
	sock = connect()

	eel.init('index')
	eel.start("index.html", size=(800, 600))
