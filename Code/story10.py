import pygame, sys

WIDTH, HEIGHT = 1000, 700

class StoryPage10:
    def __init__(self, screen, character, sfx, action):
        self.action = action
        self.screen = screen
        self.character = character
        self.sfx = sfx
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.Font("asset/ZFTERMIN__.ttf", 60)
        self.font_text = pygame.font.Font("asset/ZFTERMIN__.ttf", 30)

    def draw_text_center(self, text, y, font, color=(255,255,255)):
        img = font.render(text, True, color)
        rect = img.get_rect(center=(WIDTH//2, y))
        self.screen.blit(img, rect)

    def draw_multiline_text(self, text, start_y, font, line_height=40, color=(255,255,255)):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            y = start_y + i*line_height
            self.draw_text_center(line, y, font, color)

    def draw_highlight_text(self, text, start_y, font, line_height=40, color=(255,255,0)):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            y = start_y + i*line_height
            self.draw_text_center(line, y, font, color)

    def run(self):
        if self.action == "A":
            story_text = (
                'คุณปกป้องไข่เอาไว้ได้ทั้งสองใบ Egg Snatchers \n'
                'สองตัวขู่ฟ่อใส่คุณมันเข้าโจมตีคุณอย่างเกรี้ยวกราด\n'
            )
            highlight = "Egg Snatchers สองตัวพุ่งเข้าโจมตี!"
            enemy_count = 2
        elif self.action == "B":
            story_text = (
                'Egg Snatchers ตัวหนึ่งเอาไข่ไปได้หนึ่งใบและวิ่่งหนีไป\n'
                'คุณปกป้องไข่ไว้ได้เพียงใบเดียว Egg Snatchers อีกตัวหนึ่ง\n'
                'ที่เหลือพุ่งเข้าโจมตีคุณ\n'
            )
            highlight = "Egg Snatchers หนึ่งตัวพุ่งเข้าโจมตี!"
            enemy_count = 1

        while True:
            self.screen.fill((0,0,0))
            self.draw_multiline_text(story_text, start_y=150, font=self.font_text)
            self.draw_highlight_text(highlight, start_y=400, font=self.font_text)
            self.draw_text_center("สู้", 550, self.font_title, (255,0,0))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        return {"next": "BATTLE", "enemies": enemy_count}

            self.clock.tick(30)


# ==========================
# Run standalone (ทดสอบ)
# ==========================
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ทดสอบ StoryPage10")

    class DummyChar:
        def __init__(self):
            self.name = "Hero"
            self.hp = 100
            self.max_hp = 100

    dummy = DummyChar()
    move_sfx = pygame.mixer.Sound("asset/one_beep-99630.mp3")

    # ลองเปลี่ยน "A" → "B"
    story_page = StoryPage10(screen, dummy, move_sfx, action="A")
    result = story_page.run()
    print("ส่งต่อไป:", result)
