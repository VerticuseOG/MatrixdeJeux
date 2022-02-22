import pygame
import pygame_menu
from subprocess import call

pygame.init()
surface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Matrix de Jeux")

#Play Functions
def play_tictactoe():
    call(["python", "Tic Tac Toe.py"])

def play_chess():
    call(["python", "Chess.py"])

#Fonts and Colors
bahnschrifttitle=pygame.font.Font('fonts/Bahnschrift.ttf',120)
bahnschriftwidget=pygame.font.Font('fonts/Bahnschrift.ttf',72)
BG_COLOR = (50, 50, 50)
Focus=(40, 180, 90)

#Cutom Theme Creation
Matrixtheme = pygame_menu.themes.THEME_BLUE.copy()

Matrixtheme.title_font_shadow=False
Matrixtheme.title_font=bahnschrifttitle
Matrixtheme.background_color=BG_COLOR
Matrixtheme.widget_font=bahnschriftwidget
Matrixtheme.selection_color=Focus

#Drawing the Menu
menu = pygame_menu.Menu('Matrix de Jeux', 1280, 720,
                       theme=Matrixtheme)

menu.add.text_input('Name :', default='Username')
menu.add.button('Chess', play_chess)
menu.add.button('Tic Tac Toe', play_tictactoe)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface) #Displays the menu