# Simple Project - Practice with Pygame Text Input
# Textbox Class
# Supports Clicking inside/outside the textbox

import pygame
# Using pygame_textinput from github/nearoo
import pygame_textinput as pyti

pygame.init

s_width = 800
s_height = s_width / 2

# Button Variables
b_width = s_width / 5
b_height = s_width / 10

spacing = (s_width - 3 * b_width) / 3

xl_pos = spacing                                    # Left Button Position
xr_pos = s_width - spacing - b_width                # Right Button Position
xc_pos = (s_width - b_width) / 2                    # Center Button Position

yd_pos = s_height - spacing / 2 - b_height          # Lower Button Position
yu_pos = spacing                                    # Upper Button Position

y2_pos = (s_height - spacing / 4) / 2 - b_height    # Top 2 Position
y3_pos = (s_height + spacing / 4) / 2               # Top 3 Position
y1_pos = y2_pos - b_height - spacing / 4            # Top 1 Position
y4_pos = y3_pos + b_height + spacing / 4            # Top 4 Position

fc_radius = 2

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()

bg_color = (232, 228, 218)      # Light Creme
light_color = (196, 183, 164)   # Dark Creme
text_color = (40, 54, 24)       # Dark Green
comp_1 = (96, 108, 56)          # Green
comp_2 = (165, 63, 43)          # Red

# Create TextInput-object
textinput = pyti.TextInputVisualizer()
textinput.font_color = text_color
font_size_large = 40
font_size_small = 20
font_name = 'yugothicuisemibold'
large_font = pygame.font.SysFont(font_name, font_size_large)
small_font = pygame.font.SysFont(font_name, font_size_small)
blink_interval = 400

# Pygame now allows natively to enable key repeat:
pygame.key.set_repeat(200, 25)


# Textbox Varibles
tb_width = s_width - (2*spacing)
tb_height = b_height
tb_x_pos = (s_width - tb_width)/2
tb_font = large_font
tb_font_height = tb_font.get_height()
tb_spacing = (tb_height - tb_font.get_height()) / 2
tb_font_x_pos = tb_x_pos + tb_spacing
tb_manager = pyti.TextInputManager(validator=lambda input: 
                                   (tb_font.render(input, 1, text_color).get_size()[0] +
                                    textinput.cursor_width < (tb_width - 2*tb_spacing)))
stop_type = pyti.TextInputManager(validator=lambda input: False)

# Text Input Class
class Textbox:
    def __init__(self, name, y_pos):
        self.name = name
        self.bg_color = light_color
        self.t_color = text_color
        self.y_pos = y_pos
        self.font_y_pos = self.y_pos + tb_spacing
        self.rect = pygame.Rect(tb_x_pos, self.y_pos, tb_width, tb_height)
        self.textinput = pyti.TextInputVisualizer()
        self.textinput.manager = tb_manager
        self.textinput.cursor_visible = False
        self.textinput.cursor_width = 4
        self.textinput.font_color = text_color
        self.textinput.font_object = large_font
        self.value = ''
        self.on = True
    
    def draw(self):
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=fc_radius)

    def empty_draw(self):
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=fc_radius)
        screen.blit(large_font.render(self.name, 1, bg_color), 
                    (tb_font_x_pos, self.font_y_pos))
        
    def tb_box_show(self):
        if self.textinput.value == '' and self.value == '':
            self.empty_draw()
        else:
            self.draw()

    def tb_text_show(self):
        if self.on:
            screen.blit(self.textinput.surface, 
                        (tb_font_x_pos, self.font_y_pos))
        else:
            screen.blit(large_font.render(self.value, 1, text_color), 
                        (tb_font_x_pos, self.font_y_pos))
            
    def clear(self):
        self.value = ''
        self.textinput.value = ''

    def tb_click(self, mouse_pos):
        # Click Inside Textbox
        if self.rect.collidepoint(mouse_pos):
            if not self.on:
                self.textinput.value = self.value
                self.textinput.manager = tb_manager
                self.textinput.cursor_visible = True
                self.on = True
        # Click Outside Textbox
        else:
            if self.on:
                if self.textinput.value != '':
                    self.value = self.textinput.value
                self.textinput.manager = stop_type
                self.textinput.cursor_visible = False
                self.on = False

# Button Class
class Button:
    def __init__(self, name, bg_color, t_color, x_pos, y_pos):
        self.name = name
        self.bg_color = bg_color
        self.t_color = t_color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = pygame.Rect(self.x_pos, self.y_pos, b_width, b_height)
        self.font = pygame.font.SysFont(font_name, font_size_small)

    def draw(self):
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=fc_radius)
        button_surf = self.font.render(self.name, 1, self.t_color)
        text_width, text_height = button_surf.get_size()
        x_center = self.x_pos + (b_width - text_width) / 2
        y_center = self.y_pos + (b_height - text_height) / 2
        screen.blit(button_surf, (x_center, y_center))

    def hover_draw(self):
        if self.bg_color == light_color:
            pygame.draw.rect(screen, self.bg_color, self.rect, 2, border_radius=fc_radius)
            button_surf = self.font.render(self.name, 1, self.t_color)
        else:
            pygame.draw.rect(screen, self.bg_color, self.rect, 2, border_radius=fc_radius)
            button_surf = self.font.render(self.name, 1, self.bg_color)
        text_width, text_height = button_surf.get_size()
        x_center = self.x_pos + (b_width - text_width) / 2
        y_center = self.y_pos + (b_height - text_height) / 2
        screen.blit(button_surf, (x_center, y_center))

    def interact(self, mouse_pos=pygame.mouse.get_pos()):
        if self.rect.collidepoint(mouse_pos):
            self.hover_draw()
        else:
            self.draw()

# Buttons
conf_b = Button('Confirm', comp_1, bg_color, xr_pos, yd_pos)
back_b = Button('Back', light_color, text_color, xc_pos, yd_pos)
clear_b = Button('Clear', comp_2, bg_color, xl_pos, yd_pos)

# Textboxes
tb_1 = Textbox("Textbox 1", yu_pos)

def complete(user_input):
    global screen
    while True:
        screen.fill(bg_color)
        text = large_font.render(user_input, 1, text_color)
        if user_input == '1234':
            text = large_font.render('You guessed the secret code.', 1, text_color)
        text_width = text.get_size()[0]
        x_center = (s_width - text_width) / 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # Mouse Click Options
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_b.rect.collidepoint(event.pos):
                    return 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return 0
        # Show Buttons
        back_b.interact(pygame.mouse.get_pos())
        # Show Input Text
        screen.blit(text, (x_center, yu_pos))
        pygame.display.update()
        

while True:
    screen.fill(bg_color)
    events = pygame.event.get()
    # User Inputs
    tb_1.textinput.update(events)

    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            complete(tb_1.textinput.value)
        # Mouse Click Options
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if conf_b.rect.collidepoint(event.pos):
                complete(tb_1.textinput.value)
            if clear_b.rect.collidepoint(event.pos):
                tb_1.clear()
            # Click inside/outside Textbox 1
            tb_1.tb_click(event.pos)
    # Show Buttons
    conf_b.interact(pygame.mouse.get_pos())
    clear_b.interact(pygame.mouse.get_pos())
    # Show Textbox
    tb_1.tb_box_show()
    tb_1.tb_text_show()
    # Update Screen
    pygame.display.update()
    clock.tick(30)