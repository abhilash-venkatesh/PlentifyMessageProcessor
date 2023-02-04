class BadPacketError(Exception):
    """Exception raised if input hex data is invalud.

    Attributes:
        message -- Error message explanation
    """

    def __init__(self, message="Packet is not valid"):
        self.message = message
        super().__init__(self.message)

class BadDataError(Exception):
    """Exception raised if unknown data is requested from valid packet.

    Attributes:
        message -- Error message explanation
    """

    def __init__(self, message="The requested data type is not found in this packet"):
        self.message = message
        super().__init__(self.message)