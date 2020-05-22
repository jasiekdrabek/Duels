class Spell:
    """
    class where all information about spells are stored.
    """
    def  __init__(self,name,dmg,heal,cost,efect):
        """
        set name,demage,heal,cost and effect.
        """
        self.name=name
        self.dmg=dmg
        self.heal=heal
        self.cost=cost
        self.efect = efect
        
        