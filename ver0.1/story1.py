import pygame, sys
# ลบการ import NameInputPage ที่ไม่จำเป็นแล้ว
# from input_name import NameInputPage

WIDTH, HEIGHT = 1000, 700

class StoryPage:
    def __init__(self, screen, character):
        self.screen = screen
        self.character = character
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
            self.draw_text_center("เริ่มการผจญภัย", 50, self.font_title)
            story_text = (
            'ไพน์บลู๊ค ซึ่งเป็นชุมชนเล็กๆ ใกล้ตีนเทือกเขา "กระดูกสันหลังของโลก"\n'
            'วันนี้เป็นตาของทีมคุณที่ต้องออกลาดตระเวนแม้ปกติจะเจอแค่สัตว์ป่า \n'
            'แต่ล่าสุดมีข่าวลือแปลกๆ แพร่สะพัด บ้างก็ว่ามีมังกรเงิน\n'
            'ที่เป็นมิตรมาสร้างรังบนภูเขาใกล้ๆ แต่ที่น่ากังวลคือเมื่อวานนี้หน่วย\n'
            'ลาดตระเวนชุดก่อนหน้าได้พบรอยเท้าของFrost Troll ขนาดใหญ่\n'
            'การลาดตระเวนในวันนี้ นำโดยหัวหน้ารักษาความปลอดภัยของ\n'
            'หมู่บ้านกัปตันเอ็มม่าจีน โคล เธอมองเข้าไปในเส้นทางป่าอย่างเป็นกังวล\n'
            'ก่อนจะหันมาพูดกับพวกคุณ"ข้าไม่เคยลาดตระเวนกับเจ้ามาก่อนเลย"\n'
            'เธอกล่าว\n'
            )
            self.draw_multiline_text(story_text, start_y=150, font=self.font_text)
            self.draw_highlight_text("บอกชื่อของเจ้าให้ข้าทีสิ", start_y=550,font=self.font_text)
            self.draw_text_center("กด ENTER เพื่อไปต่อ / ESC เพื่อออก", 600, self.font_text, (255,0,0))

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
