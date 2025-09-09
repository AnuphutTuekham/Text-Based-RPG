import pygame, sys

WIDTH, HEIGHT = 1000, 700

class StoryPage8:
    def __init__(self, screen, character, sfx, action):
        self.screen = screen
        self.character = character
        self.sfx = sfx
        self.action = action
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
                'คุณตอบผิดกระจกแตกออกกลายเป็นเศษน้ำแข็งคมกริบพุ่งกระจายใส่คุณ\n'
            )
            self.character.hp = max(0, self.character.hp - 30)
            extra_text = "คุณได้รับบาดเจ็บเล็กน้อย HP -30"
        elif self.action == "C":
            story_text = ('คุณไม่สนใจปริศนาอละพุ่งเข้าไปทุบกระจกเยิี่ยงคนเถื่อน\n'
                          'กระจกแตกออกกลายเป็นเศษน้ำแข็งคมกริบพุ่งกระจายใส่คุณ\n'
            )
            self.character.hp = max(0, self.character.hp - 80)
            extra_text = "คุณได้รับบาดเจ็บอย่างหนัก HP -80"

        elif self.action == "B":
            story_text = (
                'คุณตอบถูก กระจกจะละลายกลายเป็นละอองแสงสีเงินที่ช่วย\n'
                'รักษาบาดแผลและฟื้นฟูพลังของพวกคุณจนเต็ม นี่คือพรจากบาฮามุท\n'
            )
            self.character.hp = max(0, self.character.hp + (self.character.max_hp - self.character.hp))
            extra_text = "บาดแผลของคุณรักษาหายอย่างสมบูรณ์"

        running = True
        while running:
            self.screen.fill((0,0,0))
            self.draw_multiline_text(story_text, start_y=150, font=self.font_text)
            if extra_text:
                self.draw_highlight_text(extra_text, start_y=500, font=self.font_text)
            self.draw_text_center("กด ENTER เพื่อไปต่อ / ESC เพื่อออก", 650, self.font_text, (255,0,0))

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
                        return True
            self.clock.tick(30)


# ==========================
# Run standalone (ทดสอบ)
# ==========================
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ทดสอบ StoryPage6")

    class DummyChar:
        def __init__(self):
            self.name = "Hero"
            self.hp = 100
            self.max_hp = 100

    dummy = DummyChar()
    move_sfx = pygame.mixer.Sound("asset/one_beep-99630.mp3")

    # ลองเปลี่ยน "A" → "B" เพื่อทดสอบ
    story_page = StoryPage8(screen, dummy, move_sfx, action="A")
    story_page.run()
    print(f"HP หลังเล่นเนื้อเรื่อง: {dummy.hp}")
