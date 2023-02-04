from PlentifyMessageProcessor.MessageOps.Message import Message

packetData = "0100c8110000d307000002"
m1 = Message()
print("The Tool Is About To Unpack The Following Data:", packetData)
m1.unpackMessage(packetData)
print("\nKey-Value Pair of The Packet Is :")
print(m1)

print("\n----")
m2 = Message()
print("The tool is now packing the following data:\nType = 3; Version = 2; Energy Used (Wh) = 8915; Time Drift (ms) = 2554; Geyser Is Warm = True; Geyser Is Drawing Power = True;")
m2.packMessage(type=3, version=2, energyUsed=8915, timeDrift=2554, flags=3)
print("\nThe Packed Data Is:")
print(m2.packet.hexData)
