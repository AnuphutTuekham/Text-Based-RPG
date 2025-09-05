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
        self.inventory = {}
        self.skill1_name = "Skill 1"
        self.skill2_name = "Skill 2"

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} สวมใส่ {weapon.name}!")

    def equip_armor(self, armor):
        self.armor = armor
        print(f"{self.name} สวมใส่ {armor.name}!")

    def add_item(self, item, quantity=1):
        self.inventory[item] = self.inventory.get(item, 0) + quantity
        print(f"ได้รับ {item.name} x{quantity}")

    def use_item(self, item):
        if self.inventory.get(item, 0) > 0:
            if isinstance(item, Food):
                self.hp = min(self.max_hp, self.hp + item.hp_restore)
                print(f"{self.name} ใช้ {item.name}, ฟื้นฟู {item.hp_restore} HP! (HP: {self.hp}/{self.max_hp})")
                self.inventory[item] -= 1
                if self.inventory[item] == 0:
                    del self.inventory[item]
        else:
            print(f"ไม่มี {item.name} ในช่องเก็บของ")

    def take_damage(self, amount):
        defense = self.armor.defense_power if self.armor else 0
        actual_damage = max(0, amount - defense)
        self.hp -= actual_damage
        print(f"{self.name} ได้รับความเสียหาย {actual_damage}! (HP: {self.hp}/{self.max_hp})")
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} พ่ายแพ้แล้ว...")

    def attack(self, target):
        base_atk = self.weapon.attack_power
        damage = random.randint(int(base_atk * 0.8), int(base_atk * 1.2))
        print(f"{self.name} โจมตี {target.name}!")
        target.take_damage(damage)

    def show_status(self):
        print("\n" + "="*20)
        print(f"ชื่อ: {self.name} ({self.__class__.__name__})")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"MP: {self.mp}/{self.max_mp}")
        weapon_name = self.weapon if self.weapon else "ไม่มี"
        armor_name = self.armor if self.armor else "ไม่มี"
        print(f"อาวุธ: {weapon_name}")
        print(f"เกราะ: {armor_name}")
        print("="*20 + "\n")

    def show_detail(self):
        print("\n" + "◇"*20)
        print(f"รายละเอียดตัวละคร : {self.name}")
        print(f"คลาส : {self.job}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"MP: {self.mp}/{self.max_mp}")
        weapon_name = self.weapon if self.weapon else "ไม่มี"
        armor_name = self.armor if self.armor else "ไม่มี"
        print(f"อาวุธ: {weapon_name}")
        print(f"เกราะ: {armor_name}")

# ==============================
# อาชีพต่างๆ
# ==============================
class Fighter(Character):
    def __init__(self, name):
        super().__init__(job="Fighter", name=name, hp=130, mp=30)
        self.skill1_name = "Power Strike"
        self.skill2_name = "Wound Healing"
        self.weapon = sword
        self.armor = heavy_armor

    def use_skill1(self, target):
        cost_mp = 5
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(15, 25)
            print(f"Fighter {self.name} ใช้ {self.skill1_name} โจมตี {target.name}!")
            target.take_damage(damage)
        else:
            print(f"MP ไม่เพียงพอสำหรับ {self.skill1_name}")

    def use_skill2(self, target=None):
        cost_mp = 10
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            healing = random.randint(30, 40)
            self.hp = min(self.max_hp, self.hp + healing)  
            print(f"Fighter {self.name} ใช้ {self.skill2_name} ฟื้นฟูตัวเอง {healing} HP! (HP: {self.hp}/{self.max_hp}, MP: {self.mp})")
        else:
            print(f"MP ไม่เพียงพอสำหรับ {self.skill2_name}")


    def show_detail(self):
        super().show_detail()
        print(f"Skill:")
        print(f"  - {self.skill1_name}: การโจมตีที่รุนแรง")
        print(f"  - {self.skill2_name}: การโจมตีด้วยโล่")

class Wizard(Character):
    def __init__(self, name):
        super().__init__(job="Wizard", name=name, hp=80, mp=120)
        self.skill1_name = "Fireball"
        self.skill2_name = "Lightning Bolt"
        self.weapon = staff
        self.armor = cloak


    def use_skill1(self, target):
        cost_mp = 20
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(30, 40)
            print(f"Wizard {self.name} ร่าย {self.skill1_name} ใส่ {target.name}!")
            target.take_damage(damage)
        else:
            print(f"MP ไม่เพียงพอสำหรับ {self.skill1_name}")

    def use_skill2(self, target):
        cost_mp = 30
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(30, 40)
            print(f"Wizard {self.name} ร่าย {self.skill2_name} ใส่ {target.name}!")
            target.take_damage(damage)
        else:
            print(f"MP ไม่เพียงพอสำหรับ {self.skill2_name}")

    def show_detail(self):
        super().show_detail()
        print(f"Skill:")
        print(f"  - {self.skill1_name}: โจมตีด้วยลูกไฟ")
        print(f"  - {self.skill2_name}: โจมตีด้วยสายฟ้า")

class Rogue(Character):
    def __init__(self, name):
        super().__init__(job="Rogue", name=name, hp=100, mp=50)

        self.skill1_name = "Backstab"
        self.skill2_name = "Poison Dart"
        self.weapon = dagger
        self.armor = leather_armor


    def use_skill1(self, target):
        cost_mp = 10
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(20, 30)
            print(f"Rogue {self.name} ใช้ {self.skill1_name} ลอบโจมตี {target.name}!")
            target.take_damage(damage)
        else:
            print(f"MP ไม่เพียงพอสำหรับ {self.skill1_name}")

    def use_skill2(self, target):
        cost_mp = 15
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(10, 15)
            print(f"Rogue {self.name} โจมตี {target.name} ด้วย {self.skill2_name}!")
            target.take_damage(damage)
        else:
            print(f"MP ไม่เพียงพอสำหรับ {self.skill2_name}")

    def show_detail(self):
        super().show_detail()
        print(f"Skill:")
        print(f"  - {self.skill1_name}: โจมตีรวดเร็วและรุนแรง")
        print(f"  - {self.skill2_name}: สร้างความเสียหายด้วยพิษ")


class littledragon(Character):
    def __init__(self, name):
        super().__init__(job="dragon", name=name, hp=100, mp=50)
        self.skill1_name = "dragon breath"

    def use_skill1(self, target):
        cost_mp = 20
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(30, 40)
            print(f"มังกรน้อย ใช้ {self.skill1_name} โจมตี {target.name}!")
            target.take_damage(damage)
        else:
            print(f"MP ไม่เพียงพอสำหรับ {self.skill1_name}")

    def use_skill2(self, target):
        cost_mp = 15
        if self.mp >= cost_mp:
            self.mp -= cost_mp
            damage = random.randint(10, 15)
            print(f"Rogue {self.name} โจมตี {target.name} ด้วย {self.skill2_name}!")
            target.take_damage(damage)
        else:
            print(f"MP ไม่เพียงพอสำหรับ {self.skill2_name}")

    def show_detail(self):
        super().show_detail()
        print(f"Skill:")
        print(f"  - {self.skill1_name}: โจมตีรวดเร็วและรุนแรง")
        print(f"  - {self.skill2_name}: สร้างความเสียหายด้วยพิษ")

# ==============================
# สร้างไอเทมพื้นฐาน (พร้อมใช้)
# ==============================
sword = Weapon("ดาบเหล็ก", 10)
dagger = Weapon("มีดสั้น", 8)
staff = Weapon("คฑา", 6)
heavy_armor = Armor("เกราะหนัก", 6)
leather_armor = Armor("เกราะหนัง", 4)
cloak = Armor("เสื้อคลุม", 2)
potion = Food("ยาฟื้นฟู", 40)

# ==============================
# Test ตัวละคร (run เมื่อไฟล์นี้ main เท่านั้น)
# ==============================
if __name__ == "__main__":
    print("=== การสร้างตัวละครและแสดงรายละเอียด ===")
    my_fighter = Fighter("Leon")
    my_wizard = Wizard("Merlin")
    my_rogue = Rogue("Shadowstrike")

    my_fighter.show_detail()
    my_wizard.show_detail()
    my_rogue.show_detail()

    print("\n=== การต่อสู้จำลอง ===")
    turn = 1
    while my_fighter.hp > 0 and my_wizard.hp > 0:
        print(f"\n--- เทิร์น {turn} ---")
        # Fighter โจมตี Wizard
        if turn % 2 == 1:
            my_fighter.use_skill1(my_wizard)
        else:
            my_wizard.use_skill1(my_fighter)

        # แสดงสถานะปัจจุบัน
        my_fighter.show_status()
        my_wizard.show_status()

        turn += 1

        # ถ้าใครตาย เกมจบ
        if my_fighter.hp <= 0 or my_wizard.hp <= 0:
            break

    print("\n=== จบการต่อสู้ ===")
    if my_fighter.hp > 0:
        print(f"🎉 {my_fighter.name} ชนะ!")
    else:
        print(f"🎉 {my_wizard.name} ชนะ!")