class Wand:
    """
    class where all information about player's wand are stored.
    """
    def __init__(self,core,lenght):
        """
        set core,lenght,start position,tab with information about wand.
        """
        self.core=core
        self.lenght=lenght
        self.pos=[1,0,0,0]
        self.tab=["Dlugość różdżki: " + str(self.lenght) + " cali.",
                  "Rdzeń różdżki: " + self.core]