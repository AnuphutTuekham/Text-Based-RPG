import pygame, sys
from select_class import SelectClass
from story1 import StoryPage
from story2 import StoryPage2
from story3AB import StoryPage3A
from story3C import StoryPage3C
from input_name import NameInputPage

WIDTH, HEIGHT = 1000, 700

def main():
    """
    Main function to run the game flow.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ภัยอันตรายในไพรบลู๊ค")
    clock = pygame.time.Clock()

    Titlefont = pygame.font.Font("asset/ZFTERMIN__.ttf", 100)
    font = pygame.font.Font("asset/ZFTERMIN__.ttf", 80)
    move_sfx = pygame.mixer.Sound("asset/one_beep-99630.mp3")

    # --- Game States ---
    current_state = "MENU"
    selected_character = None

    while True:
        if current_state == "MENU":
            menu = Menu(screen, Titlefont, font, move_sfx, clock)
            action = menu.run()
            if action == "START":
                current_state = "SELECT_CLASS"
            elif action == "EXIT":
                break

        elif current_state == "SELECT_CLASS":
            class_selector = SelectClass(screen)
            selected_character = class_selector.run()
            if selected_character:
                current_state = "STORY"
            else: # Player closed the window or pressed ESC
                current_state = "MENU"

        elif current_state == "STORY":
            story_page = StoryPage(screen, selected_character)
            proceed = story_page.run()
            if proceed:
             # ถ้าชื่อตัวละครยังเป็นชื่อคลาส ให้ไปหน้าเขียนชื่อ
                if selected_character.name == selected_character.job:
                    current_state = "INPUT_NAME"
                else:
                    current_state = "GAME_START_SUMMARY"
            else:  # Player closed the window or pressed ESC
                current_state = "SELECT_CLASS"

        elif current_state == "INPUT_NAME":
            # จะเข้ามาที่นี่เฉพาะครั้งแรกที่ยังไม่ได้ตั้งชื่อ
            name_page = NameInputPage(screen, selected_character)
            final_character = name_page.run()
            if final_character:
                selected_character = final_character 
                current_state = "STORY2"
            else:
                current_state = "STORY"


        elif current_state == "STORY2":
            story_page2 = StoryPage2(screen, move_sfx)
            action = story_page2.run()
            if action == "A":
                current_state = "STORY3A"
            elif action == "C":
                current_state = "STORY3C"


        elif current_state == "STORY3A":
            story_page3A = StoryPage3A(screen, selected_character)
            proceed = story_page3A.run()

        elif current_state == "STORY3C":
            story_page3C = StoryPage3C(screen, selected_character)
            proceed = story_page3C.run()

    pygame.quit()
    sys.exit()

def draw_text_center(screen, text, y, font, color=(255,255,255)):
    """Helper function to draw centered text."""
    img = font.render(text, True, color)
    rect = img.get_rect(center=(WIDTH//2, y))
    screen.blit(img, rect)

class Menu:
    def __init__(self, screen, title_font, text_font, sfx, clock):
        self.screen = screen
        self.title_font = title_font
        self.text_font = text_font
        self.move_sfx = sfx
        self.clock = clock
        self.menu_options = ["Start", "Exit"]
        self.selected = 0

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            draw_text_center(self.screen, "ภัยอันตรายในไพรบลู๊ค", 150, self.title_font)

            for i, option in enumerate(self.menu_options):
                color = (255, 255, 0) if i == self.selected else (255, 255, 255)
                draw_text_center(self.screen, option, 300 + i * 150, self.text_font, color)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "EXIT"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.menu_options)
                        self.move_sfx.play()
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.menu_options)
                        self.move_sfx.play()
                    elif event.key == pygame.K_RETURN:
                        self.move_sfx.play()
                        if self.menu_options[self.selected] == "Start":
                            return "START"
                        elif self.menu_options[self.selected] == "Exit":
                            return "EXIT"
            self.clock.tick(30)

if __name__ == "__main__":
    main()
