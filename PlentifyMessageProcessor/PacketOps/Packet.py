import PlentifyMessageProcessor.PacketOps.Constants as constants
from PlentifyMessageProcessor.ErrorHandling.Exceptions import BadDataError, BadPacketError

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
                        if dataType in constants.HEX_POSITIONS.keys():
                                hexRequestedPacketData = self.hexData[constants.HEX_POSITIONS[dataType][0]:constants.HEX_POSITIONS[dataType][1]+1]
                                requestedData = int.from_bytes(bytes.fromhex(hexRequestedPacketData), byteorder=self.byteorder)
                                return requestedData
                        raise BadDataError(message="The requested data type was not found in the packet")
                raise BadPacketError

        def setData(self, dataType=None, data=None):
                if self.isValid:
                        if dataType in constants.HEX_POSITIONS.keys() and data:
                                self.hexData = self.hexData[0:max(0, constants.HEX_POSITIONS[dataType][0])] + data + self.hexData[constants.HEX_POSITIONS[dataType][1]+1:]
                                return self.hexData
                        raise BadDataError(message="The supplied data type cannot be encoded in the packet, or the data is invalid")
                raise BadPacketError

if __name__ == "__main__":
        p = Packet("0100c8110000d307000002")
        print(p.validatePacket())
        print(p.getData("PACKET_TYPE"), p.getData("PACKET_VERSION"), p.getData("ENERGY_USED"), p.getData("TIME_DRIFT"), p.getData("FLAGS"))