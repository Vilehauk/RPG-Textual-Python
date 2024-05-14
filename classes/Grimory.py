import classes.Spell as Spell

class Firebolt(Spell):
    __name="firebolt"
    __description="atira um projétil de fogo no oponente"
    __cooldown_time=6
    __mana_cost=1
    
    __slots__=[
        _caster,
        _cooling,
        _mana_cost
    ]
    
    def __init__(self,caster):
        self._caster = caster
        self._cooling = self.__class__.__cooldown_time
        self._mana_cost = self.__class__.__mana_cost

    def check_availability(self, f):
        self.check_availability(f)


    @check_availability
    def cast(self, target):
        self._cooling = 0
        target.get_damage(self._caster.intel)
