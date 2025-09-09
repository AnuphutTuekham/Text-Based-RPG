import pygame, sys

WIDTH, HEIGHT = 1000, 700

class ending:
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
    
    def draw_extra_center(self, text, y, font, color=(255,0,0)):
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
                'แม่มังกรจะสงบลงอย่างรวดเร็วและซาบซึ้งใจอย่างสุดซึ้ง เธอจะมอบเพชรเม็ดงาม \n'
                'ให้ทุกคนและเสนอให้คุณรับเลี้ยงลูกมังกรตัวแรกของเธอ \n'
                'เพื่อเป็นการแลกเปลี่ยนกับการที่เธอจะคอยปกป้องดินแดนไพน์บลู๊ค\n'
            )
            ending_text =("ฉากจบ A ปกป้องไข่ได้สองใบ")
        elif self.action == "B":
            story_text = ('การกระทำของคุณช่างโง่เขลา!แม่มังกรใช้ลมหายใจเยือกแข็งของเธอแช่แข็ง\n'
                          'พวกคุณให้หยุดนิ่งโดยไม่ได้รับบาดเจ็บ จากนั้นเธอจะนำพวกคุณไปทิ้งไว้นอกภูเขา \n'
                          
            )
            ending_text =("ท้าทายแม่มังกร")
            extra_text =('คุณล้มเหลวในภารกิจ')

        elif self.action == "C":
            story_text = (
                'มีไข่แตกไปหนึ่งใบ แม่มังกรจะเสียใจอย่างมาก แต่เธอก็ยังขอบคุณที่คุณช่วยชีวิต\n'
                'ลูกคนแรกและไข่ที่เหลือไว้ได้ เธอยังคงให้รางวัลเป็นอัญมณีสีหม่นดูไม่ค่อยส่องประกาย\n'
                'และเสนอให้คุณรับเลี้ยงลูกมังกรก็จะฟังดูเหมือนเป็นการวิงวอนมากกว่าข้อเสนอ\n'
            )
            ending_text =("ฉากจบ C ปกไข่ได้หนึ่งใบ")

        elif self.action == "D":
            story_text = ("คุณตายในการต่อสู้"
            )
            ending_text = "คุณตายในการต่อสู้"

        running = True
        while running:
            self.screen.fill((0,0,0))
            if ending_text:
                self.draw_highlight_text(ending_text, start_y=50, font=self.font_title)
            if extra_text:
                self.draw_extra_center(extra_text, y=500, font=self.font_text,)
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
                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        return True
            self.clock.tick(30)


# ==========================
# Run standalone (ทดสอบ)
# ==========================
