
# Features should be added in future:
"""
1). designes   # Shows designes you can use just now without making your own ones
2). default_style   # Constructor where you can make/choose designes for different classes or establish a built-in design pack
"""





######################################################################################

default_size_of_display = (1600, 900)

######################################################################################





import pygame, types
pygame.init()

class DisplayError(Exception):
    2 + 2 == 4

class NummerError(Exception):
    2 + 2 == 4

class DesignError(Exception):
    2 + 2 == 4



class NoLimitsTypeHere:
    2 + 2 == 4

class AutoTypeHere:
    2 + 2 == 4



display_for_sps = None
display_size = None
nolimits = NoLimitsTypeHere()
auto = AutoTypeHere()



def select_display(*display):
    global display_for_sps, display_size
    if len(display) == 0:
        if display_for_sps is not None:
            raise DisplayError('Display already initialized, cannot create a new one')
        display_for_sps = pygame.display.set_mode(default_size_of_display)   # Established the display with default simple_panels size
        display_size = default_size_of_display
    elif len(display) == 1:
        if isinstance(display[0], pygame.Surface):
            display_for_sps = display[0]
            display_size = display[0].get_size()
        else:
            raise DisplayError(f'select_display() function requires a pygame.Surface object, but {type(display[0])} ones have passed')
    else:
        raise DisplayError(f'select_display() function requires one argument, but {len(display)} ones have passed')



class nummer:   # The panel fixed on a some place that shows some text when user interacts with some simple_panels object
    exist = False
    coordinates = None   # Top-left point
    width = None   # The same value for width along x and width along y
    font = None

    @classmethod
    def set(cls, coordinates, width, design):
        if not display_size:
            raise DisplayError('Display wasn\'t detected')
        if type(coordinates) is not tuple and type(coordinates) is not list and type(coordinates):
            raise TypeError(f'The {type(coordinates)} type had passed, but a tuple or list expected')
        if type(width) is not int and type(width) is not AutoTypeHere:
            raise TypeError(f'The {type(width)} type had passed, but int was expected')
        if len(coordinates) != 2:
            raise ValueError(f'{len(coordinates)} arguments had passed, but 2 ones (x, y) was expected')
        for i in range(2):
            if type(coordinates[i]) is not int:
                raise TypeError(f'The {type(coordinates)} type was passed for {i} position in the coordinates, but int was expected')
        if type(width) is AutoTypeHere:
            if display_size[0] - coordinates[0] < 15 or display_size[1] - coordinates[1] < 15:
                raise ValueError(f'The width of a nummer can\'t be smaller that 15. The coordinatates passed don\'t fit within the remaining space up to the boundaries of the display')
            else:
                io = display_size[0] - coordinates[0]
                if display_size[1] - coordinates[1] < io:
                    io = display_size[1] - coordinates[1]
                width = io
        else:
            if width < 15:
                raise ValueError(f'{width} is too small value. You can only use 15 and bigger')
        if not (type(design).__qualname__.split('.')[0] == 'design'):
            raise TypeError(f'The design type was expected, but {type(design)} had passed')   # These is a design type for every class of interactive object but all of them located in the design class
        elif len(type(design).__qualname__.split('.')) == 1:
            raise TypeError('You have passed the design class, but it\'s must be a class object')
        elif len(type(design).__qualname__.split('.')) > 2:
            raise TypeError(f'The design type was expected, but {type(design)} had passed')
        elif not (type(design).__qualname__.split('.')[1] == 'NummerDesign'):
            raise DesignError('You have passed the design, which doesn\'t designed for nummer. Check how you was created it')
        cls.exist = True
        cls.coordinates = tuple(coordinates)
        cls.font = pygame.font.SysFont(design.font_type, design.font_size)
        cls.font_color = design.font_color
        cls.width = width
        cls.border_radius = design.border_radius
        cls.carcas = pygame.surface.Surface((cls.width, cls.width), pygame.SRCALPHA)










        # Some testing code

        pygame.draw.rect(cls.carcas, design.inside_color, (0, 0, width, width), border_radius = design.border_radius)
        pygame.draw.rect(cls.carcas, design.edges_color, (0, 0, width, width), 5, design.border_radius)









        
    @classmethod
    def pict(cls, text):
        if not display_size:
            raise DisplayError('simple_panels is not seen the display')
        display_for_sps.blit(cls.carcas, (cls.coordinates[0], cls.coordinates[1]))
        rend = cls.font.render(str(text), True, cls.font_color)
        display_for_sps.blit(rend, (round(cls.coordinates[0] + cls.width / 2) - rend.get_size()[0] / 2, round(cls.coordinates[1] + cls.width / 2) - rend.get_size()[1] / 2))
            


class design:
    @classmethod
    def slider(cls, inside_color = (255, 0, 0), edges_color = (0, 0, 0), separators_exist = None, notes_exist = None, /):
        return design.SliderDesign(inside_color, edges_color, separators_exist, notes_exist)
    
    @classmethod
    def nummer(cls, border_radius = 0, inside_color = (255, 0, 0), edges_color = (0, 0, 0), font_color = (255, 255, 255), font_size = 16, font_type = 'centurygothic'):
        return design.NummerDesign(border_radius, inside_color, edges_color, font_color, font_size, font_type)
    
    @classmethod
    def button(self, text, border_radius = 0, color_doesnt_downed = (255, 0, 0), color_downed = (255, 125, 125), text_color_doesnt_downed = (255, 255, 255), text_color_downed = (125, 0, 0), font_type = ('centurygothic'), font_size = 16, edges_color = (0, 0, 0), change_time_ticks = 0):
        return design.ButtonDesign(text, border_radius, color_doesnt_downed, color_downed, text_color_doesnt_downed, text_color_downed, font_type, font_size, edges_color, change_time_ticks)

    class SliderDesign:
        def __init__(self, inside_color, edges_color, separators_exist, notes_exist):
            if type(inside_color) is not tuple and type(inside_color) is not list:
                if inside_color is None:
                    raise ValueError(f'The color choosing is necessarily, None is impossible')
                else:
                    raise TypeError(f'Tuple or list type was expected, but {type(inside_color)} had passed')
            if type(edges_color) is not tuple and type(edges_color) is not list:
                if edges_color is None:
                    raise ValueError(f'The color choosing is necessarily, None is impossible')
                else:
                    raise TypeError(f'Tuple or list type was expected, but {type(edges_color)} had passed')
            if type(separators_exist) is not tuple and type(separators_exist) is not list and type(separators_exist) is not None:
                raise TypeError(f'Tuple or list or None was expected, but {type(separators_exist)} had passed')
            if type(notes_exist) is not bool and type(notes_exist) is not None:
                raise TypeError(f'None or bool type was expected, but {type(type(notes_exist))} had passed')
            self.inside_color = inside_color
            self.edges_color = edges_color
            self.separators_exist = separators_exist
            self.notes_exist = notes_exist
    
    class NummerDesign:
        def __init__(self, border_radius, inside_color, edges_color, font_color, font_size, font_type):
            if type(border_radius) is not int:
                raise TypeError(f'The int object was expected, but {type(border_radius)} had passed')
            elif border_radius < 0:
                raise ValueError('The nummer less than 0 had passed')
            if type(inside_color) is not tuple and type(inside_color) is not list:
                if inside_color is None:
                    raise ValueError(f'The color choosing is necessarily, None is impossible')
                else:
                    raise TypeError(f'Tuple or list type was expected, but {type(inside_color)} had passed')
            if type(edges_color) is not tuple and type(edges_color) is not list:
                if edges_color is None:
                    raise ValueError(f'The color choosing is necessarily, None is impossible')
                else:
                    raise TypeError(f'Tuple or list type was expected, but {type(edges_color)} had passed')
            if type(font_color) is not tuple and type(font_color) is not list:
                raise TypeError(f'Tuple or list on RGB was expected, but {type(font_color)} had passed')
            elif len(font_color) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(font_color)} elements had passed')
            else:
                for i in range(3):
                    if type(font_color[i]) is not int:
                        raise TypeError(f'None-int had passed as {i}th color element')
                    elif font_color[i] < 0 or font_color[i] > 255:
                        raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if type(font_size) is not int:
                raise TypeError(f'Font size is not int')
            elif font_size < 1:
                raise ValueError(f'Invalide size of font (<1)')
            try:
                pygame.font.SysFont(font_type, font_size)
            except:
                raise ValueError('This font is not found')
            self.border_radius = border_radius
            self.inside_color = inside_color
            self.edges_color = edges_color
            self.font_color = font_color
            self.font_size = font_size
            self.font_type = font_type
    
    class ButtonDesign:
        def __init__(self, text, border_radius, color_doesnt_downed, color_downed, text_color_doesnt_downed, text_color_downed, font_type, font_size, edges_color, change_time_ticks):
            try:
                text = str(text)
            except:
                raise TypeError(f'Impossible to transform the value to the str type')
            if type(border_radius) is not int:
                raise TypeError(f'int type was expected, but {type(border_radius)} had passed')
            elif border_radius < 0:
                raise ValueError(f'Invalide border_radius (<0)')
            if not (type(color_doesnt_downed) is tuple or type(color_doesnt_downed) is list):
                raise TypeError(f'Tuple or list type was expected, but {type(color_doesnt_downed)} had passed')
            elif len(color_doesnt_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(color_doesnt_downed)} elements had passed')
            for i in range(len(color_doesnt_downed)):
                if type(color_doesnt_downed[i]) is not int:
                    raise TypeError(f'int type was expected, but {type(color_doesnt_downed[i])} had passed')
                if color_doesnt_downed[i] < 0 and color_doesnt_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not (type(color_downed) is tuple or type(color_downed) is list):
                raise TypeError(f'Tuple or list type was expected, but {type(color_downed)} had passed')
            elif len(color_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(color_downed)} elements had passed')
            for i in range(len(color_downed)):
                if type(color_downed[i]) is not int:
                    raise TypeError(f'int type was expected, but {type(color_downed[i])} had passed')
                if color_downed[i] < 0 and color_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not (type(text_color_doesnt_downed) is tuple or type(text_color_doesnt_downed) is list):
                raise TypeError(f'Tuple or list type was expected, but {type(text_color_doesnt_downed)} had passed')
            elif len(text_color_doesnt_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(text_color_doesnt_downed)} elements had passed')
            for i in range(len(text_color_doesnt_downed)):
                if type(text_color_doesnt_downed[i]) is not int:
                    raise TypeError(f'int type was expected, but {type(text_color_doesnt_downed[i])} had passed')
                if text_color_doesnt_downed[i] < 0 and text_color_doesnt_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not (type(text_color_downed) is tuple or type(text_color_downed) is list):
                raise TypeError(f'Tuple or list type was expected, but {type(text_color_downed)} had passed')
            elif len(text_color_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(text_color_downed)} elements had passed')
            for i in range(len(text_color_downed)):
                if type(text_color_downed[i]) is not int:
                    raise TypeError(f'int type was expected, but {type(text_color_downed[i])} had passed')
                if text_color_downed[i] < 0 and text_color_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')

            if type(font_size) is not int:
                raise TypeError(f'int type was expected, but {type(font_size)} had passed')
            elif font_size < 1:
                raise ValueError(f'Indalid value (less than 1)')
            
            try:
                self.font = pygame.font.SysFont(font_type, font_size)
            except:
                raise ValueError('This font is not found')

            if not (type(edges_color) is tuple or type(edges_color) is list):
                raise TypeError(f'Tuple or list type was expected, but {type(edges_color)} had passed')
            elif len(edges_color) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(edges_color)} elements had passed')
            for i in range(len(edges_color)):
                if type(edges_color[i]) is not int:
                    raise TypeError(f'int type was expected, but {type(edges_color[i])} had passed')
                if edges_color[i] < 0 and edges_color[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if type(change_time_ticks) is not int:
                raise TypeError(f'int type was expected, but {type(change_time_ticks)} had passed')
            elif change_time_ticks < 0:
                raise ValueError('Invalide value (less than 0 or bigger than 255)')
            self.text = text
            self.border_radius = border_radius
            self.color_doesnt_downed = color_doesnt_downed
            self.color_downed = color_downed
            self.text_color_doesnt_downed = text_color_doesnt_downed
            self.text_color_downed = text_color_downed
            self.font_type = font_type
            self.font_size = font_size
            self.edges_color = edges_color
            self.change_time_ticks = change_time_ticks



class RelateSlider:
    def __init__(self, dependent_variable_as_list: list, coordinates: tuple | list, min_value: int | float, max_value: int | float, k_steps: int, live_level: int, design):
        if type(min_value) is not int and type(min_value) is not float:
            raise TypeError(f'Int or float type was expected, but {type(min_value)} had passed')
        if type(max_value) is not int and type(max_value) is not float:
            raise TypeError(f'Int or float type was expected, but {type(max_value)} had passed')
        if type(k_steps) is not int:
            raise TypeError(f'Int type was expected, but {type(k_steps)} had passed')
        if type(coordinates) is not tuple and type(coordinates) is not list:
            raise TypeError(f'Tuple or list type was expected, but {type(coordinates)} had passed')
        else:
            if len(coordinates) != 4:
                raise ValueError(f'coordinates must contain 4 element (x, y, width and height), but is {len(coordinates)}')
            else:
                if type(coordinates[0]) is not int:
                    raise TypeError(f'x coordinate must be int type, but {type(coordinates[0])} had passed')
                elif type(coordinates[1]) is not int:
                    raise TypeError(f'y coordinate must be int type, but {type(coordinates[1])} had passed')
                elif type(coordinates[2]) is not int:
                    raise TypeError(f'width must be int type, but {type(coordinates[2])} had passed')
                elif type(coordinates[3]) is not int:
                    raise TypeError(f'height must be int type, but {type(coordinates[3])} had passed')
        if type(dependent_variable_as_list) is not list:
            raise TypeError(f'dependent_valiable must be lists of 1 entry, but {type(k_steps)} had passed')
        else:
            if len(dependent_variable_as_list) != 1:
                raise ValueError(f'dependent_variable must contain 1 element, but is {len(dependent_variable_as_list)}')
        if k_steps < 1:
            raise ValueError(f'k_steps must be >= 1, but is {k_steps}')
        if type(live_level) is not int:
            raise TypeError(f'Int object was expected, but {type(live_level)} had passed')
        else:
            if live_level > k_steps or live_level < 0:
                raise ValueError(f'Had passed the impossible live_level. It\'s the {live_level}, but a one from 0 to {k_steps} was expected')
#        if type(design) is not SliderDesign:
#            raise ValueError(f'A design type object has passed, which doesn\'t intended for the Sliders. Check whereby it was created')
        values_tuple = []
        one_step = (max_value - min_value) / k_steps
        for i in range(k_steps):
            values_tuple.append(min_value + one_step * i)
        values_tuple.append(max_value)
        values_tuple = tuple(values_tuple)
        self.design = design
        self.coordinates = coordinates
        self.level = live_level
        self.xchunk = round(coordinates[2] / k_steps)
        self.dependent_variable_as_list = dependent_variable_as_list
        
    def pict(self):
        pass

class Incut:
    def create():
        pass
    
class TapButton:
    def __init__(self, rect, function, design):
        if type(rect) is not tuple and type(rect) is not list:
            raise TypeError(f'rect argument must be a list or tuple type')
        elif len(rect) != 4:
            raise ValueError(f'rect require 4 arguments (x, y, width, height), but {len(rect)} had passed')
        if type(function) is not types.FunctionType:
            raise TypeError(f'function type was expected, but {type(function)} had passed')
        if not (type(design).__qualname__.split('.')[0] == 'design'):
            raise TypeError(f'The design type was expected, but {type(design)} had passed')
        elif len(type(design).__qualname__.split('.')) == 1:
            raise TypeError('You have passed the design class, but it\'s must be a class object')
        elif len(type(design).__qualname__.split('.')) > 2:
            raise TypeError(f'The design type was expected, but {type(design)} had passed')
        elif not (type(design).__qualname__.split('.')[1] == 'ButtonDesign'):
            raise DesignError('You have passed the design, which doesn\'t designed for button. Check how you created this')
        self.rect = rect
        self.function = function
        self.border_radius = design.border_radius
        self.color_doesnt_downed = design.color_doesnt_downed
        self.color_downed = design.color_downed
        self.edges_color = design.edges_color
        self.change_time_ticks = design.change_time_ticks
        self.text_color_doesnt_downed = design.text_color_doesnt_downed
        self.text_color_downed = design.text_color_downed
        self.I_am_doesnt_downed = pygame.surface.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
        pygame.draw.rect(self.I_am_doesnt_downed, self.color_doesnt_downed, (0, 0, self.rect[2], self.rect[3]), border_radius = self.border_radius)
        pygame.draw.rect(self.I_am_doesnt_downed, self.edges_color, (0, 0, self.rect[2], self.rect[3]), 5, self.border_radius)
        text_surface_by_downed = pygame.font.SysFont(design.font_type, design.font_size).render(design.text, True, design.text_color_doesnt_downed)
        self.I_am_doesnt_downed.blit(text_surface_by_downed, ((io := self.I_am_doesnt_downed.get_size())[0] / 2 - (io0 := text_surface_by_downed.get_size())[0] / 2, io[1] / 2 - io0[1] / 2))
        self.I_am_downed = pygame.surface.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
        pygame.draw.rect(self.I_am_downed, self.color_downed, (0, 0, self.rect[2], self.rect[3]), border_radius = self.border_radius)
        pygame.draw.rect(self.I_am_downed, self.edges_color, (0, 0, self.rect[2], self.rect[3]), 5, self.border_radius)
        text_surface_by_doesnt_downed = pygame.font.SysFont(design.font_type, design.font_size).render(design.text, True, design.text_color_downed)
        self.I_am_downed.blit(text_surface_by_doesnt_downed, ((io := self.I_am_downed.get_size())[0] / 2 - (io0 := text_surface_by_doesnt_downed.get_size())[0] / 2, io[1] / 2 - io0[1] / 2))

        self.downed = False
    
    def pict(self):
        if self.downed is False:
            display_for_sps.blit(self.I_am_doesnt_downed, (self.rect[0], self.rect[1]))
        else:
            display_for_sps.blit(self.I_am_downed, (self.rect[0], self.rect[1]))
