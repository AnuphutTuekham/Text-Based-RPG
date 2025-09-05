import pygame, sys


WIDTH, HEIGHT = 1000, 700

class StoryPage3C:
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
            self.draw_text_center("มังกรน้อยระแวงคุณ", 50, self.font_text)
            story_text = (
            'ลูกมังกรตกใจและส่งเสียงร้องแหลม มันถอยกลับไปแอบหลังต้นไม้ \n'
            'กัปตันโคลมองคุณอย่างตำหนิ "เก็บอาวุธซะ! เราไม่ควรทำร้ายมัน \n'
            '"ถ้าแม่มันมาเห็นเข้า หมู่บ้านเราจะเดือดร้อน" คุณจะต้องใช้เวลาสักพัก\n'
            'เพื่อทำให้ลูกมังกรเชื่อใจอีกครั้ง จากนั้น กัปตันโคลยืนยันว่านี่คือลูก\n'
            'มังกรเงินที่เพิ่งเกิดใหม่ และมอบหมายภารกิจให้คุณพามันกลับไปที่รังบนภูเขา \n'
            'เธอให้หน้ากระดาษที่มีคำศัพท์ภาษามังกรแก่คุณก่อนจะแยกตัวกลับไป \n'
            'มังกรน้อยร้องว่า"Nytha"ก่อนจะเดินตามคุณอยู่ห่างๆ\n'
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
    story_page = StoryPage3C(screen, move_sfx)
    choice = story_page.run()
    print(f"ผู้เล่นเลือก: {choice}")
