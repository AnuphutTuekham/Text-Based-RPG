# enemy_class.py
import random
from character_class import Character, Weapon, Armor

class IceGolem(Character):
    def __init__(self, name="Ice Golem"):
        super().__init__(job="Golem", name=name, hp=150, mp=30)
        self.skill1_name = "พุ่งกระแทก"
        self.equip_weapon(Weapon("แขนหิน", 8))
        self.equip_armor(Armor("เกราะน้ำแข็ง", 8))

    def use_skill1(self, target):
        cost_mp = 15
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(10, 20)
            target.take_damage(damage)
            return damage
        else:
            return "MPไม่พอ"
        
class EggSnatchers(Character):
    def __init__(self, name="Egg Snatchers"):
        super().__init__(job="Snatchers", name=name, hp=100, mp=40)
        self.skill1_name = "พุ่งกัด"
        self.equip_weapon(Weapon("กรงเล็บ", 12))
        self.equip_armor(Armor("หนังหนา", 4))

    def use_skill1(self, target):
        cost_mp = 10
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(15, 25)
            target.take_damage(damage)
            return damage
        else:
            return "MPไม่พอ"