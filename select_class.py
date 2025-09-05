import pygame
import sys
from character_class import Fighter, Wizard, Rogue

WIDTH, HEIGHT = 1000, 700

class SelectClass:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.title_font = pygame.font.Font("asset/ZFTERMIN__.ttf", 60)
        self.text_font = pygame.font.Font("asset/ZFTERMIN__.ttf", 30)
        self.move_sfx = pygame.mixer.Sound("asset/one_beep-99630.mp3")
        self.class_names = ["Fighter", "Wizard", "Rogue"]
        self.selected = 0
        self.class_objects = {
            "Fighter": Fighter("Fighter"),
            "Wizard": Wizard("Wizard"),
            "Rogue": Rogue("Rogue")
        }

    def draw_text(self, text, x, y, font, color=(255,255,255)):
        img = font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.draw_text("เลือกคลาสของคุณ", 50, 30, self.title_font)

            for i, cls_name in enumerate(self.class_names):
                color = (255, 255, 0) if i == self.selected else (255, 255, 255)
                self.draw_text(cls_name, 100, 150 + i * 100, self.text_font, color)

            character = self.class_objects[self.class_names[self.selected]]
            self.draw_text(f"คลาส: {character.job}", 600, 150, self.text_font, (0,200,255))
            self.draw_text(f"HP: {character.hp}/{character.max_hp}", 600, 220, self.text_font)
            self.draw_text(f"MP: {character.mp}/{character.max_mp}", 600, 280, self.text_font)
            self.draw_text(f"อาวุธ: {character.weapon}", 600, 340, self.text_font)
            self.draw_text(f"เกราะ: {character.armor}", 600, 400, self.text_font)
            self.draw_text(f"Skill 1: {character.skill1_name}", 600, 460, self.text_font)
            self.draw_text(f"Skill 2: {character.skill2_name}", 600, 520, self.text_font)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.class_names)
                        self.move_sfx.play()
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.class_names)
                        self.move_sfx.play()
                    elif event.key == pygame.K_RETURN:
                        self.move_sfx.play()
                        return self.class_objects[self.class_names[self.selected]]

            self.clock.tick(30)
