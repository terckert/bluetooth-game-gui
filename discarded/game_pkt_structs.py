from dataclasses import dataclass
from enum import Enum
import struct

_ = '''
 This dataclass is a c-style struct. It is intended to be 128 bits long. The data portion is
 in bytes so that it can be further modified with other types of data structures using the
 pack command.

 Websites that were helpful:
 https://stackoverflow.com/questions/35988/c-like-structures-in-python
 https://stackoverflow.com/questions/14928888/creating-packet-using-struct-pack-with-python
 https://docs.python.org/3/library/struct.html
 https://stackoverflow.com/questions/38883476/how-to-remove-those-x00-x00
 https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement

  
 Things I learned that I need to remember:
 -  Pack makes a byte string based on the first parameter. This can be useful when packing 
    structs within structs
 -  The pack string '!iii116s' means that I am packing 3 integers, 1 byte string
 -  I can only reliably receive about 106 bits at a time for some reason.
 
'''
#TODO Pack size needs to be decreased to 64 in all strings. Potentially global variable from now on. >:(

class PacketType(Enum):
    OKAY:       int     = 0     # Acknowledgement of packet received
    MESSAGE:    int     = 1     # Message packet: Can be multiples but working with embedded 
                                # so will attempt to keep them short
    AT_COMMAND: int     = 2     # TODO: Sending an AT command to the bluetooth module. Good for setting
                                # setting name and pin
    GAME_MOVE:  int     = 3     # TODO: Light that was clicked
    GAME_BOARD: int     = 4     # TODO: String of 1's and 0's that show which lights are currently on
                                # or off. 16 bits long
    NEW_GAME:   int     = 5     # Signals that we want to start a new game.

@dataclass
class PacketStruct:
    type:  int          # 4 bytes 
    count: int          # 4 bytes
    outof: int          # 4 bytes
    data:  bytes        # Max: 64 bytes

    def __init__(self, type: int, count: int, outof: int, data: bytes):
        self.type  = type
        self.count = count
        self.outof = outof
        self.data  = data
    
    def __lt__(self, other):
        return self.count < other.count

@dataclass
class Okay:
    def __init__(self):
        pass
    
    def pack(self):
        return struct.pack(
            '!iii116s'
            , PacketType.OKAY.value
            , 1
            , 1
            , ''.encode()
        )

@dataclass
class Message:
    msg:   str          # No maximum, but needs to be broken up into multiple packets
    
    def __init__(self, msg: str | list[PacketStruct] = ''):
        print (type(msg))
        match msg:
            case str():
                self.msg = msg
            case list():
                msg.sort()
                self.msg = ''
                for m in msg:
                    self.msg += m.data.decode().split('\x00', 1)[0]


    def pack(self):
        # Split the data into 116 character chunks for stuffing into packets
        data = [self.msg[i:i+116] for i in range(0, len(self.msg), 116)]
        length = len(data)
        return [
            struct.pack(
                '!iii116s',
                PacketType.MESSAGE.value,
                i+1,
                length,
                data[i].encode()
            ) for i in range(0, length)
        ]

    def message(self):
        return self.msg


def unpackPacket(pkt):
    unp = struct.unpack('!iii116s', pkt)
    return PacketStruct(unp[0], unp[1], unp[2], unp[3])


# testStr = Message('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Consequat mauris nunc congue nisi vitae suscipit. Felis donec et odio pellentesque diam volutpat. Consequat interdum varius sit amet mattis. Vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. Non odio euismod lacinia at quis risus sed vulputate odio. Diam vulputate ut pharetra sit amet aliquam id diam. Tortor condimentum lacinia quis vel eros donec ac odio tempor. Nullam vehicula ipsum a arcu cursus vitae congue. Eu augue ut lectus arcu bibendum at varius. Turpis massa tincidunt dui ut. Arcu dui vivamus arcu felis bibendum ut tristique. Pellentesque pulvinar pellentesque habitant morbi tristique. Ut morbi tincidunt augue interdum velit. A iaculis at erat pellentesque adipiscing commodo elit at imperdiet. Ultricies tristique nulla aliquet enim tortor at auctor urna nunc.

# Praesent tristique magna sit amet purus gravida. Quam elementum pulvinar etiam non quam lacus suspendisse. Faucibus a pellentesque sit amet porttitor eget dolor. Fringilla urna porttitor rhoncus dolor purus non enim praesent elementum. Urna porttitor rhoncus dolor purus non enim praesent elementum facilisis. Massa enim nec dui nunc mattis enim ut tellus. Tellus at urna condimentum mattis. Eu facilisis sed odio morbi. Etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus. Tincidunt lobortis feugiat vivamus at augue eget arcu dictum varius. Convallis convallis tellus id interdum velit laoreet id. Vestibulum morbi blandit cursus risus at. Massa tempor nec feugiat nisl pretium fusce id velit ut. Nibh mauris cursus mattis molestie a iaculis at. Fames ac turpis egestas integer eget aliquet nibh praesent. Fusce ut placerat orci nulla pellentesque dignissim enim sit. Etiam erat velit scelerisque in dictum non consectetur a. Vitae nunc sed velit dignissim sodales ut eu.

# Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus. Fames ac turpis egestas maecenas pharetra convallis posuere morbi leo. Odio ut enim blandit volutpat maecenas volutpat blandit aliquam etiam. Sed viverra tellus in hac habitasse. Integer vitae justo eget magna fermentum iaculis. Tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat. Nulla facilisi etiam dignissim diam quis. Egestas congue quisque egestas diam. Ac turpis egestas sed tempus. Eu mi bibendum neque egestas congue quisque. Eleifend donec pretium vulputate sapien nec sagittis aliquam malesuada bibendum.

# Augue lacus viverra vitae congue. Diam sit amet nisl suscipit adipiscing bibendum est ultricies integer. Orci eu lobortis elementum nibh. Amet risus nullam eget felis eget nunc lobortis mattis. Blandit turpis cursus in hac. Faucibus interdum posuere lorem ipsum dolor sit amet. Posuere ac ut consequat semper. Dignissim convallis aenean et tortor. Eu lobortis elementum nibh tellus molestie nunc. Aenean euismod elementum nisi quis eleifend quam adipiscing vitae proin. Velit laoreet id donec ultrices tincidunt arcu non sodales neque. Volutpat commodo sed egestas egestas fringilla phasellus faucibus. Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Tortor at auctor urna nunc id cursus. Aliquam nulla facilisi cras fermentum odio eu feugiat pretium. In iaculis nunc sed augue lacus viverra.

# Ac turpis egestas maecenas pharetra convallis. Feugiat nibh sed pulvinar proin. Pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Dignissim sodales ut eu sem integer vitae. Ut faucibus pulvinar elementum integer. Blandit massa enim nec dui nunc mattis enim ut tellus. Risus feugiat in ante metus dictum at tempor. Id aliquet lectus proin nibh. Posuere ac ut consequat semper viverra nam libero justo. Sit amet aliquam id diam maecenas ultricies mi eget. Tristique senectus et netus et malesuada fames ac turpis egestas.''')


if __name__ == '__main__':
    # # Testing struct.pack(..) and struct.unpack(..)
    # test = PacketStruct(2, 1, 1, b'hello world');
    # pprint(test)
    # enc = struct.pack('!iii116s', test.type, test.count, test.outof, test.data)
    # pprint(enc)
    # pprint(struct.calcsize('!iii116s'))
    # unp = struct.unpack('!iii116s', enc)
    # print(unp)
    # for u in unp:
        # print(u);
    # test = PacketStruct(unp[0], unp[1], unp[2], unp[3])
    # pprint(test)
    # 
    # # Testing enumerator for splitting values
    # for i in range(4):
    #     match i:
    #         case PacketType.MESSAGE.value:
    #             print ("MESSAGE")
    #         case PacketType.AT_COMMAND.value:
    #             print ('AT_COMMAND')
    #         case PacketType.GAME_MOVE.value:
    #             print ("GAME_MOVE")
    #         case PacketType.GAME_BOARD.value:
    #             print ("GAME_BOARD")

    # # Testing string encoding and decoding for transmission.    
    # enc = testStr.buildPkts()
    # dec = [ unpackPacket(e) for e in enc]
    # msg = Message(dec)
    # og = open('og.txt', 'w')
    # og.write(testStr.message())
    # nw = open('nw.txt', 'w')
    # nw.write(msg.message())
    # if (msg.message() == testStr.message()):
    #     print ("Decoded successfully")
    # else:
    #     print ("I fucked up!")
    pass
