from PlentifyMessageProcessor.PacketOps.Packet import Packet

class Message:
        packet = None
        type = None
        version = None
        energyUsed = None
        timeDrift = None
        flags = None
        isGeyserWarm = None
        isGeyserDrawingPower = None

        def __init__(self) -> None:
                pass

        def packMessage(self, packet, type, version, energyUsed, timeDrift, flags, isGeyserWarm, isGeyserDrawingPower):
                pass

        def unpackMessage(self, hexData):
                self.packet = Packet(hexData=hexData)
                self.type = self.packet.getData("PACKET_TYPE")
                self.version = self.packet.getData("PACKET_VERSION")
                self.energyUsed = self.packet.getData("ENERGY_USED")
                self.timeDrift = self.packet.getData("TIME_DRIFT")
                self.flags = self.packet.getData("FLAGS")
                self.isGeyserWarm = self.flags & 1
                self.isGeyserDrawingPower = self.flags & 2
