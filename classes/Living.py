class Living:
    # os atributos com o prefixo "_r" são atributos reais
    # atributos reais são a referência para buffs e debuffs
    __slots__= [
        _name,
        _level,
        _gender,
        _maxhealth,
        _rmaxhealth,
        _health,
        _strength,
        _rstrength,
        _dexterity,
        _rdexterity,
        _sense,
        _rsense,
        _intel,
        _rintel,
        _alive,
        _revivable
    ]
    def __init__(self,name,level,gender,health,strength,dexterity,sense,intel):
        self._name = name
        self._level = level
        self._gender = gender
        self._maxhealth = health
        self._rmaxhealth = health
        self._health = health
        self._strength = strength
        self._rstrength = strength
        self._dexterity = dexterity
        self._rdexterity = dexterity
        self._sense = sense
        self._rsense = sense
        self._intel = intel
        self._rintel = intel
        self._alive = True
        self._revivable = False

    @property
    def name(self):
        return self._name

    @property
    def gender(self):
        return self._gender

    @property
    def maxhealth(self):
        return self._maxhealth

    @property
    def health(self):
        return self._health

    @property
    def strength(self):
        return self._strength

    @property
    def dexterity(self):
        return self._dexterity

    @property
    def sense(self):
        return self._sense

    @property
    def intel(self):
        return self._intel

    def get_damage(self,value):
        self._health -= value
        self.check_death()

    def check_death(self):
        if(self._health<0):
            self._alive = False