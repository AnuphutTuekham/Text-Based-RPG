import pygame, sys

WIDTH, HEIGHT = 1000, 700

class NameInputPage:
    def __init__(self, screen, character):
        self.screen = screen
        self.character = character
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.Font("asset/ZFTERMIN__.ttf", 60)
        self.font_text = pygame.font.Font("asset/ZFTERMIN__.ttf", 40)
        self.input_text = character.job  # Set initial name to class name

    def draw_text_center(self, text, y, font, color=(255,255,255)):
        img = font.render(text, True, color)
        rect = img.get_rect(center=(WIDTH//2, y))
        self.screen.blit(img, rect)

    def run(self):
        while True:
            self.screen.fill((0,0,0))
            self.draw_text_center("กรุณาใส่ชื่อตัวละครของคุณ", 100, self.font_title)
            # Create a blinking cursor effect
            cursor = "|"
            self.draw_text_center(self.input_text + cursor, 300, self.font_text)
            self.draw_text_center("กด ENTER เพื่อยืนยัน", 600, self.font_text, (255,0,0))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if self.input_text.strip(): # Make sure name is not empty
                            self.character.name = self.input_text.strip()
                            return self.character
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        # Add typed character if it's printable and within length limit
                        if len(self.input_text) < 12 and event.unicode.isprintable():
                            self.input_text += event.unicode
            self.clock.tick(30)
