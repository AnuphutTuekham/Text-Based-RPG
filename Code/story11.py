import pygame, sys

WIDTH, HEIGHT = 1000, 700

class StoryPage11:
    def __init__(self, screen, character, sfx, action):
        self.action = action
        self.screen = screen
        self.character = character
        self.sfx = sfx
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.Font("asset/ZFTERMIN__.ttf", 60)
        self.font_text = pygame.font.Font("asset/ZFTERMIN__.ttf", 30)


        # ตัวเลือกเริ่มต้น
        self.menu_options = [
            "A.อธิบายทุกอย่างตามความจริงอย่างใจเย็นและแสดงความเคารพ",
            "B.ชักดาบโจมตีแม่มังกร! ชั้นจะเป็น dragons slayer!!"
        ]
        self.selected = 0

    def draw_text_center(self, text, y, font, color=(255,255,255)):
        img = font.render(text, True, color)
        rect = img.get_rect(center=(WIDTH//2, y))
        self.screen.blit(img, rect)
    
    def draw_choice_left(self, text, y, font, color=(255,255,255)):
        img = font.render(text, True, color)
        rect = img.get_rect(topleft=(100, y))
        self.screen.blit(img, rect)

    def draw_multiline_text(self, text, start_y, font, line_height=40, color=(255,255,255)):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            y = start_y + i * line_height
            self.draw_text_center(line, y, font, color)

    def run(self):
        self.draw_text_center("การพิพากษาของแม่มังกร", 100, self.font_text)
        story_text = ('หลังจากคุณจัดการ ตัวขโมยใข่ได้สำเร็จทันใดนั้น ตูมมมม! \n'
                      'แม่มังกรเงิน ฮิส-วี-รอน กลับมายังรังของเธอ\n'
                      'เธอเห็นสภาพความวุ่นวายและคำรามด้วยความโกรธ\n'
        )
        
        while True:
            self.screen.fill((0,0,0))
            self.draw_multiline_text(story_text, 100, self.font_text)
            self.draw_text_center("คุณจะทำอย่างไร?", 400, self.font_text, (255,0,0))

            start_y = 450
            line_height = 60
            for i, option in enumerate(self.menu_options):
                color = (255, 255, 0) if i == self.selected else (255, 255, 255)
                self.draw_choice_left(option, start_y + i * line_height, self.font_text, color)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_UP:
                        self.sfx.play()
                        self.selected = (self.selected - 1) % len(self.menu_options)
                    elif event.key == pygame.K_DOWN:
                        self.sfx.play()
                        self.selected = (self.selected + 1) % len(self.menu_options)
                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        self.sfx.play()
                        if self.selected == 0:
                            return "A"
                        elif self.selected == 1:
                            return "B"

            self.clock.tick(30)
