import pygame, sys
from select_class import SelectClass
from story1 import StoryPage
from story2 import StoryPage2
from story3AB import StoryPage3A
from story3C import StoryPage3C
from story4 import StoryPage4
from story5 import StoryPage5
from story6 import StoryPage6
from story7 import StoryPage7
from story8 import StoryPage8
from story9 import StoryPage9
from story10 import StoryPage10
from story11 import StoryPage11
from ending import ending
from credit import Credit
from battle1 import Battle
from enemy_class import IceGolem, EggSnatchers
from input_name import NameInputPage


WIDTH, HEIGHT = 1000, 700

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ภัยอันตรายในไพรบลู๊ค")
    clock = pygame.time.Clock()

    Titlefont = pygame.font.Font("asset/ZFTERMIN__.ttf", 100)
    font = pygame.font.Font("asset/ZFTERMIN__.ttf", 80)
    move_sfx = pygame.mixer.Sound("asset/one_beep-99630.mp3")

    current_state = "MENU"
    selected_character = None
    
    # Initialize variables to prevent UnboundLocalError
    last_choice = ""
    last_choice_9 = ""  
    enemy_count_for_battle = 0
    ending_action = ""

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
            else:
                current_state = "MENU"

        elif current_state == "STORY":
            story_page = StoryPage(screen, selected_character)
            proceed = story_page.run()
            if proceed:
            
                if selected_character.name == selected_character.job:
                    current_state = "INPUT_NAME"
                else:
                    current_state = "GAME_START_SUMMARY"
            else: 
                current_state = "SELECT_CLASS"

        elif current_state == "INPUT_NAME":
            name_page = NameInputPage(screen, selected_character)
            final_character = name_page.run()
            if final_character:
                selected_character = final_character 
                current_state = "STORY2"
            else:
                current_state = "STORY"


        elif current_state == "STORY2":
            story_page2 = StoryPage2(screen, selected_character, move_sfx)
            action = story_page2.run()
            if action == "A":
                current_state = "STORY3A"
            elif action == "C":
                current_state = "STORY3C"


        elif current_state == "STORY3A":
            story_page3A = StoryPage3A(screen, selected_character, move_sfx)
            proceed = story_page3A.run()
            current_state = "STORY4"

        elif current_state == "STORY3C":
            story_page3C = StoryPage3C(screen, selected_character, move_sfx)
            proceed = story_page3C.run()
            current_state = "STORY4"

        elif current_state == "STORY4":
            story_page4 = StoryPage4(screen, selected_character, move_sfx)
            proceed = story_page4.run()
            current_state = "BATTLE1"

        elif current_state == "BATTLE1":
            enemy1 = IceGolem("Ice Golem 1")
            enemy2 = IceGolem("Ice Golem 2")
            enemies_in_battle = [enemy1, enemy2]

            battle1 = Battle(screen, selected_character, enemies_in_battle, move_sfx)
            result = battle1.run()
            if result == "WIN":
                current_state = "STORY5"
            elif result == "LOSE":
                current_state = "CREDIT"

        elif current_state == "STORY5":
            story_page5 = StoryPage5(screen, selected_character, move_sfx)
            last_choice = story_page5.run()
            if last_choice in ("A", "B", "C"):
                current_state = "STORY6"

        elif current_state == "STORY6":
            story_page6 = StoryPage6(screen, selected_character, move_sfx, action=last_choice)
            proceed = story_page6.run()
            if proceed:
                current_state = "STORY7"

        elif current_state == "STORY7":
            story_page7 = StoryPage7(screen, selected_character, move_sfx, action=last_choice)
            last_choice = story_page7.run()
            if last_choice in ("A", "B", "C"):
                current_state = "STORY8"
        
        elif current_state == "STORY8":
            story_page8 = StoryPage8(screen, selected_character, move_sfx, action=last_choice)
            proceed = story_page8.run()
            if proceed:
                current_state = "STORY9"

        elif current_state == "STORY9":
            story_page9 = StoryPage9(screen, selected_character, move_sfx, action=last_choice)
            last_choice_9 = story_page9.run()
            current_state = "STORY10"

        elif current_state == "STORY10":
            story_page10 = StoryPage10(screen, selected_character, move_sfx, action=last_choice_9)
            battle_info = story_page10.run()
            if battle_info["next"] == "BATTLE":
                current_state = "BATTLE2"
                enemy_count_for_battle = battle_info["enemies"]

        elif current_state == "BATTLE2":
            enemies_in_battle = []
            for i in range(enemy_count_for_battle):
                enemies_in_battle.append(EggSnatchers(f"Egg Snatchers {i+1}"))

            battle2 = Battle(screen, selected_character, enemies_in_battle, move_sfx)
            result = battle2.run()
            if result == "WIN":
                current_state = "STORY11"
            elif result == "LOSE":
                ending_action = "B"
                current_state = "ENDING"
        
        elif current_state == "STORY11":
            story_page11 = StoryPage11(screen, selected_character, move_sfx, action=last_choice_9)
            proceed = story_page11.run()
            if proceed:
                if proceed  == "A":
                    if last_choice_9 == "A":
                        ending_action = "A" 
                    elif last_choice_9 == "B":
                        ending_action = "C" 
                elif proceed  == "B":
                    ending_action = "B"
                current_state = "ENDING"

        
        elif current_state == "ENDING":
            ending_page = ending(screen, selected_character, move_sfx, action=ending_action)
            proceed = ending_page.run()
            if proceed:
                current_state = "CREDIT"

        elif current_state == "CREDIT":
            credits = Credit(screen, selected_character, move_sfx, action=ending_action)
            proceed = credits.run()
            if proceed:
                current_state = "MENU"

    pygame.quit()
    sys.exit()


def draw_text_center(screen, text, y, font, color=(255,255,255)):
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


# python3 -m pip install -U pygame==2.6.0

# pip install -U pyinstaller
# python -m PyInstaller --onefile main.py