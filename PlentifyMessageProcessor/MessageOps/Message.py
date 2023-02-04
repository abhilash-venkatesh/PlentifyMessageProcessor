from PlentifyMessageProcessor.CoreOps.PacketOps.Packet import Packet

'''
This class interacts with the user to provide a programming interface 
and maintains packet structure information.
'''

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

        def __str__(self) -> str:
                return "Type = " + str(self.type) + "; Version = " + str(self.version) + "; Energy Used (Wh) = " + str(self.energyUsed) + "; Time Drift (ms) = " + str(self.timeDrift) + "; Geyser Is Warm = " + str(self.isGeyserWarm) + "; Geyser Is Drawing Power = " + str(self.isGeyserDrawingPower) + ";"

        def unpackMessage(self, hexData):
                self.packet = Packet(hexData=hexData)
                self.type = self.packet.getData("PACKET_TYPE")
                self.version = self.packet.getData("PACKET_VERSION")
                self.energyUsed = self.packet.getData("ENERGY_USED")
                self.timeDrift = self.packet.getData("TIME_DRIFT")
                self.flags = self.packet.getData("FLAGS")
                self.isGeyserWarm = (self.flags & 1) == 1
                self.isGeyserDrawingPower = (self.flags >> 1 & 1) == 1

        def packMessage(self, type: int, version: int, energyUsed: int, timeDrift: int, flags = None):
                self.packet = Packet(hexData="0000000000000000000000") # Initialize packet with all zeroes to pass Packet.isValid()
                self.packet.setData("PACKET_TYPE", type)
                self.packet.setData("PACKET_VERSION", version)
                self.packet.setData("ENERGY_USED", energyUsed)
                self.packet.setData("TIME_DRIFT", timeDrift)
                self.packet.setData("FLAGS", flags)
                self.unpackMessage(self.packet.hexData) # Run unpack to repopulate variables of self

