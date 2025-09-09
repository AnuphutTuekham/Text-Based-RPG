import pygame, sys
# ลบการ import NameInputPage ที่ไม่จำเป็นแล้ว
# from input_name import NameInputPage

WIDTH, HEIGHT = 1000, 700

class Credit:
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
        lines = text.split('\n')  # แยกบรรทัดด้วย \n
        for i, line in enumerate(lines):
            y = start_y + i*line_height
            self.draw_text_center(line, y, font, color)

    def draw_highlight_text(self, text, start_y, font, line_height=40, color=(255,255,0)):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            y = start_y + i*line_height
            self.draw_text_center(line, y, font, color)

    def run(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
            self.draw_text_center("ผู้จัดทำ", 50, self.font_title)
            story_text = ('นายอนุภัทร ตื้อคำ 67022995\n'
                          'นางสาวอนัญญา โพธิคำปา 67022984\n'
                          'นายธนดล เทศเเก้ว 67022636\n'
            )
            self.draw_multiline_text(story_text, start_y=150, font=self.font_text)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        return True # คืนค่า True เพื่อไปต่อ
            self.clock.tick(30)