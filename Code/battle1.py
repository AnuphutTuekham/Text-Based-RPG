# main_game.py
import pygame, sys, random
from pygame.locals import *
from character_class import Fighter, Food, potion, sword, heavy_armor
from enemy_class import IceGolem

# =========================
# Game Configuration
# =========================
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battle Demo")

FONT_PATH = "asset/ZFTERMIN__.ttf"
FONT_SIZE = 30
try:
    FONT = pygame.font.Font(FONT_PATH, FONT_SIZE)
except pygame.error:
    FONT = pygame.font.SysFont("arial", FONT_SIZE)
    print("Warning: ZFTERMIN__.ttf not found. Using Arial font instead.")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

# =========================
# Battle Class (with UI)
# =========================
class Battle:
    def __init__(self, screen, player, enemies, sfx):
        self.screen = screen
        self.player = player
        self.enemies = enemies
        self.sfx = sfx
        self.turn = "PLAYER"
        self.menu = ["โจมตี", "สกิล", "ไอเทม", "หนี"]
        self.selected = 0
        self.submenu_show = False
        self.submenu_options = []
        self.submenu_selected = 0
        self.messages = []
        self.action_done = False
        self.skill_selected = None
        self.target_type = ""
        # New: List to hold only the living enemy objects for targeting
        self.living_enemies_for_target = []

    def draw_text(self, text, x, y, color=WHITE):
        img = FONT.render(text, True, color)
        self.screen.blit(img, (x, y))

    def draw_hp_bar(self, x, y, w, h, hp, max_hp, color):
        ratio = hp / max_hp
        pygame.draw.rect(self.screen, WHITE, (x, y, w, h), 2)
        pygame.draw.rect(self.screen, color, (x, y, w * ratio, h))

    def draw(self):
        self.screen.fill(BLACK)
        # Player Stats
        self.draw_text(f"{self.player.name} HP: {self.player.hp}/{self.player.max_hp} MP: {self.player.mp}/{self.player.max_mp}", 50, 20, GREEN)
        self.draw_hp_bar(50, 50, 200, 20, self.player.hp, self.player.max_hp, GREEN)
        # Enemies Stats
        for i, enemy in enumerate(self.enemies):
            self.draw_text(f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}", 650, 20 + i * 60, RED)
            self.draw_hp_bar(650, 50 + i * 60, 200, 20, enemy.hp, enemy.max_hp, RED)
        # Messages
        for i, msg in enumerate(self.messages[-4:]):
            self.draw_text(msg, 50, 200 + i * 30, YELLOW)
        # Menu and Submenu
        if self.turn == "PLAYER" and not self.action_done:
            if not self.submenu_show:
                for i, opt in enumerate(self.menu):
                    color = YELLOW if i == self.selected else WHITE
                    self.draw_text(opt, 100, 500 + i * 30, color)
                # Show details for selected menu option
                if self.menu[self.selected] == "สกิล":
                    self.draw_text(f"Skill1: {self.player.skill1_name}  Skill2: {self.player.skill2_name}", 300, 500, CYAN)
                elif self.menu[self.selected] == "ไอเทม":
                    inv_items = ", ".join([f"{i.name} x{q}" for i, q in self.player.inventory.items()])
                    self.draw_text(f"คลัง: {inv_items}" if inv_items else "ไม่มีไอเทม", 300, 500, CYAN)
            else: # Submenu is active
                for i, opt in enumerate(self.submenu_options):
                    color = YELLOW if i == self.submenu_selected else WHITE
                    self.draw_text(opt, 300, 500 + i * 30, color)
        pygame.display.flip()

    def handle_input(self, event):
        if self.turn == "PLAYER" and not self.action_done:
            if event.key == K_UP:
                self.sfx.play()
                if self.submenu_show:
                    self.sfx.play()
                    self.submenu_selected = (self.submenu_selected - 1) % len(self.submenu_options)
                else:
                    self.sfx.play()
                    self.selected = (self.selected - 1) % len(self.menu)
            elif event.key == K_DOWN:
                if self.submenu_show:
                    self.sfx.play()
                    self.submenu_selected = (self.submenu_selected + 1) % len(self.submenu_options)
                    self.sfx.play()
                else:
                    self.sfx.play()
                    self.selected = (self.selected + 1) % len(self.menu)
            elif event.key == K_RETURN:
                if self.submenu_show:
                    self.sfx.play()
                    self.perform_action()
                else:
                    self.sfx.play()
                    self.open_submenu()
            elif event.key == K_ESCAPE:
                if self.submenu_show:
                    self.submenu_show = False
                    self.target_type = ""
                    self.skill_selected = None

    def open_submenu(self):
        action = self.menu[self.selected]
        if action == "โจมตี":
            self.submenu_show = True
            self.target_type = "ENEMY"
            self.living_enemies_for_target = [e for e in self.enemies if e.hp > 0]
            self.submenu_options = [f"{e.name}" for e in self.living_enemies_for_target]
            self.submenu_selected = 0
        elif action == "สกิล":
            self.submenu_show = True
            self.target_type = "SKILL"
            self.submenu_options = [self.player.skill1_name, self.player.skill2_name]
            self.submenu_selected = 0
        elif action == "ไอเทม":
            if self.player.inventory:
                self.submenu_show = True
                self.target_type = "ITEM"
                self.submenu_options = [i.name for i in self.player.inventory.keys()]
                self.submenu_selected = 0
            else:
                self.messages.append("ไม่มีไอเทม!")
        elif action == "หนี":
            self.messages.append(f"{self.player.name} หนีออกจากการต่อสู้!")
            self.action_done = True
            return "ESCAPE"

    def perform_action(self):
        action_name = self.menu[self.selected]
        if action_name == "โจมตี":
            target = self.living_enemies_for_target[self.submenu_selected]
            dmg = self.player.attack(target)
            self.messages.append(f"{self.player.name} โจมตี {target.name} สร้างความเสียหาย {dmg}!")
            self.action_done = True
        elif action_name == "สกิล":
            if self.target_type == "SKILL":
                self.skill_selected = self.submenu_options[self.submenu_selected]
                self.target_type = "SKILL_TARGET"
                self.living_enemies_for_target = [e for e in self.enemies if e.hp > 0]
                self.submenu_options = [f"{e.name}" for e in self.living_enemies_for_target]
                self.submenu_selected = 0
                return
            
            elif self.target_type == "SKILL_TARGET":
                target = self.living_enemies_for_target[self.submenu_selected]
                if self.skill_selected == self.player.skill1_name:
                    result = self.player.use_skill1(target)
                elif self.skill_selected == self.player.skill2_name:
                    result = self.player.use_skill2(target)
                
                if result == "MPไม่พอ":
                    self.messages.append(f"{self.player.name} MPไม่พอใช้ {self.skill_selected}!")
                else:
                    self.messages.append(f"{self.player.name} ใช้ {self.skill_selected} โจมตี {target.name} สร้างความเสียหาย {result}!")
                
                self.action_done = True
                self.submenu_show = False
                self.target_type = ""
                self.skill_selected = None
        elif action_name == "ไอเทม":
            item = list(self.player.inventory.keys())[self.submenu_selected]
            heal = self.player.use_item(item)
            if heal > 0:
                self.messages.append(f"{self.player.name} ใช้ {item.name} ฟื้นฟู {heal} HP!")
            self.action_done = True
            self.submenu_show = False
            self.target_type = ""

    def enemy_turn(self):
        for enemy in self.enemies:
            if enemy.hp > 0:
                if enemy.mp >= 15 and random.random() < 0.5:
                    result = enemy.use_skill1(self.player)
                    if result != "MPไม่พอ":
                        self.messages.append(f"{enemy.name} ใช้ {enemy.skill1_name} โจมตี {self.player.name}!")
                else:
                    dmg = enemy.attack(self.player)
                    self.messages.append(f"{enemy.name} โจมตี {self.player.name}!")
                pygame.time.delay(100)
                if self.player.hp <= 0:
                    return "LOSE"
        return "CONTINUE"

    def run(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    self.handle_input(event)

            if self.turn == "PLAYER" and self.action_done:
                living_enemies = [e for e in self.enemies if e.hp > 0]
                if not living_enemies:
                    self.messages.append("คุณชนะการต่อสู้!")
                    self.player.add_item(potion, 1)
                    self.player.mp = max(0, self.player.mp + (self.player.max_mp - self.player.mp))
                    self.messages.append("คุณได้รับรางวัล : (potion) x1!")
                    self.draw()
                    pygame.time.delay(1000)
                    return "WIN"
                
                self.turn = "ENEMY"
                self.action_done = False

            if self.turn == "ENEMY":
                result = self.enemy_turn()
                if result == "LOSE":
                    self.messages.append("คุณแพ้...")
                    return "LOSE"
                self.turn = "PLAYER"
            
            pygame.time.delay(10)

# =========================
# Game Screens
# =========================
def show_end_screen(message):
    while True:
        screen.fill(BLACK)
        draw_text_center(message, 50, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        draw_text_center("กดปุ่มใดๆ เพื่อไปต่อ", 30, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                return "QUIT"
            if event.type == KEYDOWN:
                return "CONTINUE"

def draw_text_center(text, size, x, y):
    font = pygame.font.Font(FONT_PATH, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# =========================
# Main Game Loop
# =========================
def main():
    while True:
        player = Fighter("Arthur")
        player.add_item(potion, 2)
        enemy1 = IceGolem("IceGolem1")
        enemy2 = IceGolem("IceGolem2")
        enemies = [enemy1, enemy2]
        
        battle = Battle(screen, player, enemies, pygame.mixer.Sound("asset/one_beep-99630.mp3"))
        result = battle.run()
        
        if result == "WIN":
            if show_end_screen("คุณชนะ!") == "QUIT":
                break
        elif result == "LOSE":
            if show_end_screen("คุณแพ้...") == "QUIT":
                break
        elif result == "ESCAPE":
            if show_end_screen("คุณหนีรอดมาได้") == "QUIT":
                break
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()