# Pygame Textbox Class Test
## Description
This program intakes user text and allows the user to clear their input or confirm.
Confirming outputs the text, or if there is no text input, states `No Text Was Input.'
The program only allows the user to input text to the extent that the length of the text fits within the textbox.
When the user starts the program, the user can start inputting text right away.
If the user clicks outside the textbox, the user cannot type in the textbox. 
The program only allows the user to further input text if the user clicks inside of the textbox. 

## Textbox Class
### Initialization
When initializing a Textbox, the following need to be initialized:
- name: (string) shown in the Textbox when no text is input while the user is clicked outside the textbox
- y_pos: (int) y-position of the Textbox
```
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
        self.textinput.cursor_width = 4
        self.textinput.font_color = text_color
        self.textinput.font_object = large_font
        self.value = ''
        self.on = True
```
### Functions
The Textbox class has many functions including:
- `tb_box_draw` which draws the rectangle for the textbox itself
- `tb_text_show` blits text into the textbox
  - If clicked inside textbox: shows typed text and cursor
  - If clicked outside textbox: shows the typed text without cursor
  - If clicked outside textbox and no text is input: shows `name`
- `tb_draw` draws the textbox and approprate text by calling `tb_box_draw` and `tb_text_show`
- `clear` clears any text input
- `value_update` updates the value in the textbox from textinput[^1] (text input by user)
- `tb_click` if the user clicks inside the textbox, allows user to input text, if the user clicks outside the textbox, does not let the user input text

[^1]: [Pygame Text Input Module](https://github.com/Nearoo/pygame-text-input) by [Nearoo](https://github.com/Nearoo/)

## Acknowledgements
The Textbox Class relies on [Pygame Text Input Module](https://github.com/Nearoo/pygame-text-input) by [Nearoo](https://github.com/Nearoo/).
