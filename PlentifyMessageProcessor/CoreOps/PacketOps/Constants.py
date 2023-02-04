# This is a constants file used to reconfigure the application dynamically as per the changes in data encoding formats used

BYTE_ORDER = "<"
'''
Each tuple within each value of the dictionary represents the following information:
(START POSITION, END POSITION, STRUCT MODULE ENCODING FORMAT)

To understand struct encoding formats, refer to https://docs.python.org/3/library/struct.html
'''
HEX_CONFIGS = {"PACKET_TYPE": (0, 1, "B"), "PACKET_VERSION": (2, 3, "B"), "ENERGY_USED": (4, 11, "I"), "TIME_DRIFT": (12, 19, "i"), "FLAGS": (20, 21, "B")}
FLAG_POS = {"GEYSER_WARM": 0, "GEYSER_POWER": 1}

