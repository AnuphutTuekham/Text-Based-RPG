import pygame, sys

WIDTH, HEIGHT = 1000, 700

class StoryPage7:
    def __init__(self, screen, character, sfx, action):
        self.action = action              # รับ action มาจากหน้าก่อน
        self.screen = screen
        self.character = character
        self.sfx = sfx
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.Font("asset/ZFTERMIN__.ttf", 60)
        self.font_text = pygame.font.Font("asset/ZFTERMIN__.ttf", 30)

        # ตัวเลือกเริ่มต้น
        self.menu_options = [
            "A. Orn Dragon",
            "B. Orn Darastrix",
            "C. ไม่สนใจปริศนา ทุบกระจกมันให้แตกไปเลย!!"
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
        # เปลี่ยนเนื้อเรื่องตาม action จากหน้าเก่า
        if self.action == "A":
            story_text = (
                'เพราะคุณปีนขึ้นมาแบบทุลักทุเล\n'
                'คุณมองเห็นเงาสะท้อนของมังกรที่ดูอ่อนแรงเล็กน้อยในกระจก\n'
                'บาฮามุทถามด้วยเสียงทรงพลัง...\n'
                '"สิ่งมีชีวิตสองพยางค์ที่พวกเจ้าพากลับบ้านมานี้คือสิ่งใด?"\n'
            )
        elif self.action == "B":
            story_text = (
                'ด้วยการปีนที่มั่นคงและปลอดภัย\n'
                'คุณก้าวเข้ามาเบื้องหน้ากระจกน้ำแข็งที่เปล่งประกายสว่างไสว\n'
                'บาฮามุทผู้ทรงเกียรติถามปริศนา...\n'
                '"สิ่งมีชีวิตสองพยางค์ที่พวกเจ้าพากลับบ้านมานี้คือสิ่งใด?"\n'
            )
        else:
            story_text = (
                'คุณเดินมาเจอแผ่นน้ำแข็งแปลกประหลาด\n'
                'มันสะท้อนภาพมังกรเงินพร้อมเสียงคำรามก้องกังวาน...\n'
                '"สิ่งมีชีวิตสองพยางค์ที่พวกเจ้าพากลับบ้านมานี้คือสิ่งใด?"\n'
            )
        
        while True:
            self.screen.fill((0,0,0))
            self.draw_text_center("กระจกน้ำแข็งลงอาคม", 50, self.font_title)
            self.draw_multiline_text(story_text, 150, self.font_text)

            # วาดตัวเลือกแนวตั้ง
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
                        elif self.selected == 2:
                            return "C"

            self.clock.tick(30)


# ==========================
# Run standalone
# ==========================
class Character:
    def __init__(self, name, job):
        self.name = name
        self.job = job

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ทดสอบ StoryPage7")

    hero = Character("Henry", "Knight")
    sfx = pygame.mixer.Sound("asset/one_beep-99630.mp3")

    # ลองส่ง action = "A" หรือ "B"
    story_page = StoryPage7(screen, hero, sfx, action="B")
    choice = story_page.run()
    print(f"ผู้เล่นเลือก: {choice}")
