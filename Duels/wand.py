class Wand:
    def __init__(self,core,lenght):
        self.core=core
        self.lenght=lenght
        self.pos=[1,0,0,0]
        self.tab=["Dlugość różdżki: " + str(self.lenght) + " cali.",
                  "Rdzeń różdżki: " + self.core]