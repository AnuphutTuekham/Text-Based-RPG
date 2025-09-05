import pygame, sys

WIDTH, HEIGHT = 1000, 700

class StoryPage2:
    def __init__(self, screen, sfx):
        self.screen = screen
        self.sfx = sfx
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.Font("asset/ZFTERMIN__.ttf", 60)  
        self.font_text = pygame.font.Font("asset/ZFTERMIN__.ttf", 30)

        # ตัวเลือกเริ่มต้น
        self.menu_options = [
            "A ค่อยๆ เข้าไปหามันอย่างเป็นมิตร",
            "B หยิบเสบียง ออกมา แล้วโยนให้มันอย่างช้าๆ",
            "C ชักอาวุธออกมา เตรียมพร้อมหากมันจู่โจม"
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
        story_text = (
            'หลังจากที่คุณแนะนำตัว กัปตันโคลก็พยักหน้ารับฟัง "เอาล่ะ ถึงเวลาลาดตระเวน"\n'
            'เธอกล่าว "ข้าพร้อมที่จะสู้ถ้ามันจำเป็น" พวกคุณเดินตามเส้นทางในป่าไป\n'
            'ประมาณสิบห้านาที ทันใดนั้น กัปตันโคลก็ยกมือขึ้นเป็นสัญญาณให้หยุด\n'
            '"พวกเจ้าได้ยินไหม?" เธอถามเสียงเบามีเสียงกรอบแกรบดังมาจากพุ่มไม้\n'
            'ข้างทางเดิน เงาหนึ่งค่อยๆ คลานออกมา มันคือลูกมังกร ตัวเล็กมาก \n'
            'มีเกล็ดสีฟ้าเทาแวววาวราวกับโลหะ และยังมีเศษเปลือกไข่สีเงินติดอยู่บนหัว \n'
            'มันพยายามขู่ฟ่อใส่พวกคุณ แต่เสียงที่ออกมากลับเหมือนลูกแมวตัวน้อยๆ เท่านั้น\n'
            'กัปตันโคลมองอย่างสับสน ลูกมังกรดูอ่อนแรงและหิวโหย \n'
        )

        while True:
            self.screen.fill((0,0,0))
            self.draw_multiline_text(story_text, 100, self.font_text)

            # วาดตัวเลือกแนวตั้ง ชิดซ้าย
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
                        # ✅ เล่นเสียงอีกครั้งตอนเลือกเสร็จ
                        self.sfx.play()
                        pygame.time.delay(100)  # หน่วงเล็กน้อยให้เสียงดังทัน

                        if self.selected == 0:
                            return "A"
                        elif self.selected == 1:
                            return "B"
                        elif self.selected == 2:
                            return "C"

            self.clock.tick(30)

# ==========================
# Run standalone (ทดสอบเอง)
# ==========================
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ทดสอบ StoryPage2")

    move_sfx = pygame.mixer.Sound("asset/one_beep-99630.mp3")
    story_page = StoryPage2(screen, move_sfx)
    choice = story_page.run()
    print(f"ผู้เล่นเลือก: {choice}")
