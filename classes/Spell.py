# [Spell] é uma classe mãe de todas as spells
# uma nova [Spell] pode ser criada herdando ela, mas ela terá seus próprios atributos e descrições
class Spell:
    __name="Spell_sample"
    __description=""
    __cooldown_time=1
    __mana_cost=0
    __slots__ = [
        _caster, # o lançador que tem a magia em seu grimório
        _cooling,  # tempo de recarga local da magia
        _mana_cost
    ]
    def __init__(self,caster):
        self._caster = caster
        self._cooling = self.__class__.__cooldown_time
        self._mana_cost = self.__class__.__mana_cost

    @classmethod
    def get_description(cls):
        return cls.__description

    @classmethod
    def get_name(cls):
        return cls.__name

    @classmethod
    def get_cooldown_time(cls):
        return cls.__cooldown_time

    @classmethod
    def get_mana_cost(cls):
        return cls.__mana_cost

    @property
    def name(self):
        return self._name

    @property
    def cooling(self):
        return self._cooling

    @property
    def description(self):
        return self._description

    def decrease_mana_cost(self, amount):
        self._mana_cost -= amount
        if(self._mana_cost<0):
            self._mana_cost = 0

    def increase_mana_cost(self, amount):
        self._mana_cost += amount

    def reset_mana_cost(self):
        self._mana_cost = type(self).__name__.__mana_cost

    # pode parecer confuso, mas increase vai reduzir o valor contido em [_cooldown]
    # enquanto que decrease vai aumentar o valor contido em [_cooldown]
    # pois a variável [_cooldown] conta a quantidade de ticks que passaram
    # enquanto que increase e decrease se referem ao aumento e a diminuição dos ticks necessários
    # como se aumentassem ou diminuissem o tempo
    def increase_cooldown(self,amount):
        self._cooling -= amount
        self.limit_cooling()

    def decrease_cooldown(self,amount):
        self._cooling += amount
        self.limit_cooling()

    # não faz sentido o progresso do cooldown passar do objetivo
    def limit_cooling(self):
        if(self._cooling > self.__class__.__cooldown_time):
            self._cooling = self.__class__.__cooldown_time

    def check_availability(self,f): # checa se o feitiço está em cooldown
        return (self._cooling >= Spell.__cooldown_time)

    # [cast] -> toda magia terá e é o que vai colocar a magia em jogo
    @check_availability
    def cast(self,alvo):
        self._cooling = 0
        alvo.get_damage(self._caster.intel) # nesse caso seria uma magia ofensiva

    # [tick] -> será chamado a cada tick do jogo, e será responsável por determinar certas características da magia além da recarga
    def tick(self):
        if(self._cooling < Spell.cooldown_time):
            self._cooling += 1