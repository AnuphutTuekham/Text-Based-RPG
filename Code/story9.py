import pygame, sys

WIDTH, HEIGHT = 1000, 700

class StoryPage9:
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
            "A.ปกป้องไข่! เอาตัวไปบังไข่ไว้ปกป้องไข่สุดชีวิต! \n",
            "B.ใช้ไข่เป็นตัวล่อปล่อยให้มันเอาไข่ไป พอมือมันไม่ว่างแล้วค่อยเข้าโจมตี!\n"
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
        
        story_text = ('คุณมาถึงห้องโถงฟักไข่ ที่มีไข่สีเงินอีกสองฟองวางอยู่ แต่แล้ว\n'
                    'Egg Snatchers สองตัวก็ปรากฏตัวขึ้น! พุ่งตรงไปยังไข่หวังขโมยมันไปทันที!\n'
        )
        
        while True:
            self.screen.fill((0,0,0))
            self.draw_multiline_text(story_text, 150, self.font_text)
            self.draw_text_center("ตัวขโมยไข่", 50, self.font_title)

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

# ==========================
# ตัวอย่าง Character class + Run standalone
# ==========================
class Character:
    def __init__(self, name, job):
        self.name = name
        self.job = job

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ทดสอบ StoryPage2")

    # สร้างตัวละครจำลอง
    hero = Character("Henry", "Knight")

    sfx = pygame.mixer.Sound("asset/one_beep-99630.mp3")
    story_page = StoryPage9(screen, hero, sfx)
    choice = story_page.run()
    print(f"ผู้เล่นเลือก: {choice}")
