from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    damage: int
    stamina: int


ferocious_kick = Skill(name='Сильный удар', damage=12, stamina=6)
powerful_thust = Skill(name='Крепкий щипок', damage=15, stamina=5)
