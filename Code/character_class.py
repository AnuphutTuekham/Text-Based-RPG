# character_class.py
import random

# ==============================
# Classes (คลาสสำหรับไอเทมและอุปกรณ์)
# ==============================
class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    def __str__(self):
        return f"{self.name} (ATK: {self.attack_power})"

class Armor:
    def __init__(self, name, defense_power):
        self.name = name
        self.defense_power = defense_power

    def __str__(self):
        return f"{self.name} (DEF: {self.defense_power})"

class Food:
    def __init__(self, name, hp_restore):
        self.name = name
        self.hp_restore = hp_restore

    def __str__(self):
        return f"{self.name} (ฟื้นฟู {self.hp_restore} HP)"

# ==============================
# Base Character Class
# ==============================
class Character:
    def __init__(self, job, name, hp, mp):
        self.job = job
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.weapon = None
        self.armor = None
        self.inventory = {potion: 2}
        self.skill1_name = "Skill 1"
        self.skill2_name = "Skill 2"
        self.is_player = False

    def equip_weapon(self, weapon):
        self.weapon = weapon
    
    def equip_armor(self, armor):
        self.armor = armor

    def add_item(self, item, quantity=1):
        self.inventory[item] = self.inventory.get(item, 0) + quantity

    def use_item(self, item):
        if self.inventory.get(item, 0) > 0:
            if isinstance(item, Food):
                heal = item.hp_restore
                self.hp = min(self.max_hp, self.hp + heal)
                self.inventory[item] -= 1
                if self.inventory[item] == 0:
                    del self.inventory[item]
                return heal
        return 0

    def take_damage(self, amount):
        defense = self.armor.defense_power if self.armor else 0
        actual_damage = max(0, amount - defense)
        self.hp -= actual_damage
        if self.hp <= 0:
            self.hp = 0

    def attack(self, target):
        base_atk = self.weapon.attack_power if self.weapon else 5
        damage = random.randint(int(base_atk * 0.8), int(base_atk * 1.2))
        target.take_damage(damage)
        return damage

    def show_status(self):
        pass

# ==============================
# อาชีพต่างๆ
# ==============================
sword = Weapon("ดาบเหล็ก", 20)
dagger = Weapon("มีดสั้น", 18)
staff = Weapon("คฑา", 15)
heavy_armor = Armor("เกราะหนัก", 5)
leather_armor = Armor("เกราะหนัง", 4)
cloak = Armor("เสื้อคลุม", 3)
potion = Food("Potion", 50)

class Fighter(Character):
    def __init__(self, name):
        super().__init__(job="Fighter", name=name, hp=130, mp=30)
        self.is_player = True
        self.skill1_name = "Power Strike"
        self.skill2_name = "Wound Healing(10 MP)"
        self.equip_weapon(sword)
        self.equip_armor(heavy_armor)

    def use_skill1(self, target):
        cost_mp = 10
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(40, 60)
            target.take_damage(damage)
            return damage
        else:
            return "MPไม่พอ"

    def use_skill2(self, target=None):
        cost_mp = 10
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            healing = random.randint(30, 40)
            self.hp = min(self.max_hp, self.hp + healing)  
            return healing
        else:
            return "MPไม่พอ"

class Wizard(Character):
    def __init__(self, name):
        super().__init__(job="Wizard", name=name, hp=80, mp=120)
        self.is_player = True
        self.skill1_name = "Fireball(20 MP)"
        self.skill2_name = "Magic Missile(30 MP)"
        self.equip_weapon(staff)
        self.equip_armor(cloak)

    def use_skill1(self, target):
        cost_mp = 20
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(50, 60)
            target.take_damage(damage)
            return damage
        else:
            return "MPไม่พอ"

    def use_skill2(self, target):
        cost_mp = 30
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = 70
            target.take_damage(damage)
            return damage
        else:
            return "MPไม่พอ"

class Rogue(Character):
    def __init__(self, name):
        super().__init__(job="Rogue", name=name, hp=100, mp=50)
        self.is_player = True
        self.skill1_name = "Backstab(10 MP)"
        self.skill2_name = "Quick Kill(50 MP)"
        self.equip_weapon(dagger)
        self.equip_armor(leather_armor)

    def use_skill1(self, target):
        cost_mp = 10
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(30, 40)
            target.take_damage(damage)
            return damage
        else:
            return "MPไม่พอ"

    def use_skill2(self, target):
        cost_mp = 50
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = 150
            target.take_damage(damage)
            return damage
        else:
            return "MPไม่พอ"