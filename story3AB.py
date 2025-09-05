import pygame, sys


WIDTH, HEIGHT = 1000, 700

class StoryPage3A:
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
            self.draw_text_center("มังกรน้อยเชื่อใจคุณ", 50, self.font_text)
            story_text = (
            'ลูกมังกรลังเลในตอนแรก แต่เมื่อเห็นว่าคุณไม่มีท่าทีคุกคาม มันค่อยๆ \n'
            'คลานเข้ามาหาคุณอย่างระมัดระวัง และเริ่มดมกลิ่นคุณหรือกินอาหารที่ \n'
            'คุณให้มันดูเชื่อใจคุณเป็นพิเศษจากนั้น กัปตันโคลจะยืนยันว่านี่ \n'
            'คือลูกมังกรเงินที่เพิ่งเกิดใหม่ และมอบหมายภารกิจให้คุณพามันกลับ \n'
            'ไปที่รังบนภูเขาเธอให้หน้ากระดาษที่มีคำศัพท์ภาษามังกรแก่คุณ \n'
            'ก่อนจะแยกตัวกลับไปเมื่อมันกินอิ่มมันก็พูดออกมาได้คำเดียวว่า  \n'
            '"Nytha" และเดินตามคุณต้อยๆ มันเข้ามาคลอเคลียที่ขาของคุณ\n'
            'คุณกับมังกรน้อย มุ่งหน้าขึ้นไปบนภูเขาตามเส้นทาง\n'
            )
            self.draw_multiline_text(story_text, start_y=150, font=self.font_text)
            self.draw_highlight_text("กัปตันโคลออกจากปาตี้", start_y=500,font=self.font_text)
            self.draw_highlight_text("มังกรน้อยเข้าร่วมปาตี้", start_y=550,font=self.font_text)
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
                        return True 
            self.clock.tick(30)

# ==========================
# Run standalone (ทดสอบเอง)
# ==========================
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ทดสอบ StoryPage2")

    move_sfx = pygame.mixer.Sound("asset/one_beep-99630.mp3")
    story_page = StoryPage3A(screen, move_sfx)
    choice = story_page.run()
    print(f"ผู้เล่นเลือก: {choice}")
