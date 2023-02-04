import struct

import PlentifyMessageProcessor.CoreOps.PacketOps.Constants as constants
from PlentifyMessageProcessor.CoreOps.ErrorHandling.Exceptions import BadDataError, BadPacketError

'''
This class is used to perform core bitwise manipulations on packet data.

It provides a layer of abstraction to the Message class present in Message.py.
'''

class Packet:
        hexData = None
        isValid = False
        byteorder = constants.BYTE_ORDER

        def __init__(self, hexData = None) -> None:
                self.hexData = hexData
                self.validatePacket()

        def validatePacket(self):
                if self.hexData is not None and len(self.hexData) == 22:
                        self.isValid = True
                return self.isValid

        def getData(self, dataType=None):
                if self.isValid:
                        if dataType in constants.HEX_CONFIGS.keys():
                                # If this is a known data type, unpack it according to the hex_configs in constants.py

                                hexRequestedPacketData = self.hexData[constants.HEX_CONFIGS[dataType][0]:constants.HEX_CONFIGS[dataType][1]+1]
                                requestedData = struct.unpack(self.byteorder + constants.HEX_CONFIGS[dataType][2], bytes.fromhex(hexRequestedPacketData))[0]
                                return requestedData
                        raise BadDataError(message="The requested data type was not found in the packet")
                raise BadPacketError

        def setData(self, dataType=None, data=None):
                if self.isValid:
                        if dataType in constants.HEX_CONFIGS.keys() and data:
                                # If this is a known data type, pack it according to the hex_configs in constants.py
                                
                                self.hexData = self.hexData[0:max(0, constants.HEX_CONFIGS[dataType][0])] + struct.pack(self.byteorder + constants.HEX_CONFIGS[dataType][2], data).hex() + self.hexData[constants.HEX_CONFIGS[dataType][1]+1:]
                                return self.hexData
                        raise BadDataError(message="The supplied data type cannot be encoded in the packet, or the data is invalid")
                raise BadPacketError
