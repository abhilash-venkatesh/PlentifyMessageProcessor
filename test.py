from PlentifyMessageProcessor.PacketOps.Packet import Packet

p = Packet("0100c8110000d307000002")
print(p.validatePacket())
print(p.getData("PACKET_TYPE"), p.getData("PACKET_VERSION"), p.getData("ENERGY_USED"), p.getData("TIME_DRIFT"), p.getData("FLAGS"))