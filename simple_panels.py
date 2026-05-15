
# Features should be added in future:
"""
1). design.show_designes()   # Shows designes you can use just now without making your own ones
2). design.set_default()   # Constructor where you can make/choose designes for different classes or establish a built-in design pack
"""





######################################################################################

default_size_of_display = (1600, 900)

######################################################################################





import pygame, types
from typing import Union
pygame.init()

class DisplayError(Exception):
    2 + 2 == 4

class NummerError(Exception):
    2 + 2 == 4

class DesignError(Exception):
    2 + 2 == 4



class nolimits:
    2 + 2 == 4

class auto:
    2 + 2 == 4



display_for_simple_panels = None
display_size = None
nolimits = nolimits()
auto = auto()


def is_in(point: tuple[int, int] | list[int, int], area: tuple[int, int, int, int] | list[int, int, int, int]) -> bool:   # Checks is a point in some area
    return True if   (     area[0] <= point[0] and area[0] + area[2] >= point[0] and area[1] <= point[1] and area[1] + area[3] >= point[1]     )   else False



def select_display(*display):
    global display_for_simple_panels, display_size
    if len(display) == 0:
        if display_for_simple_panels is not None:
            raise DisplayError('Display already initialized, cannot create a new one')
        display_for_simple_panels = pygame.display.set_mode(default_size_of_display)   # Established the display with default simple_panels size
        display_size = default_size_of_display
    elif len(display) == 1:
        if isinstance(display[0], pygame.Surface):
            display_for_simple_panels = display[0]
            display_size = display[0].get_size()
        else:
            raise DisplayError(f'select_display() function requires a pygame.Surface object, but {type(display[0])} have passed')
    else:
        raise DisplayError(f'select_display() function requires one argument, but {len(display)} ones have passed')



class nummer:   # The panel fixed on a some place that shows some text when user interacts with some simple_panels object
    exist = False
    coordinates = None   # Top-left point
    width = None   # The same value for width along x and for width along y
    font = None

    @classmethod
    def set(cls, coordinates: tuple | list, width: Union[int, auto], design):
        if not display_size:
            raise DisplayError('Display wasn\'t detected')
        if type(coordinates) is not tuple and type(coordinates) is not list and type(coordinates):
            raise TypeError(f'The {type(coordinates)} type had passed, but a tuple or list expected')
        if type(width) is not int and type(width) is not auto:
            raise TypeError(f'The {type(width)} type had passed, but int was expected')
        if len(coordinates) != 2:
            raise ValueError(f'{len(coordinates)} arguments had passed, but 2 ones (x, y) was expected')
        for i in range(2):
            if type(coordinates[i]) is not int:
                raise TypeError(f'The {type(coordinates)} type was passed for {i} position in the coordinates, but int was expected')
        if type(width) is auto:
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
        pygame.draw.rect(cls.carcas, design.inside_color, (0, 0, width, width), border_radius = design.border_radius)
        pygame.draw.rect(cls.carcas, design.edges_color, (0, 0, width, width), 5, design.border_radius)
    
    @classmethod
    def pict(cls, text):   # Very function nummer exists to implement. Any interactive element can show some text it wants over nummer.pict()
        if not display_size:
            raise DisplayError('simple_panels is not seen the display')
        display_for_simple_panels.blit(cls.carcas, (cls.coordinates[0], cls.coordinates[1]))
        rend = cls.font.render(str(text), True, cls.font_color)
        display_for_simple_panels.blit(rend, (round(cls.coordinates[0] + cls.width / 2) - rend.get_size()[0] / 2, round(cls.coordinates[1] + cls.width / 2) - rend.get_size()[1] / 2))
            


class design:   # The general class containing designes for all types of intecactive objects. Exists only for containing different types of designes, it's planned that a user thinks only one class for design exists
    # The different design classes creates via @classmethod functions for a user, not via constructors
    
    @classmethod
    def slider(cls, inside_color: tuple[int, int, int] | list[int, int, int] = (255, 0, 0), edges_color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0), separators_exist: tuple[int, int, int] | list[int, int, int] = None, notes_exist: bool = None, /):
        return design.SliderDesign(inside_color, edges_color, separators_exist, notes_exist)
    
    @classmethod
    def nummer(cls, border_radius: int = 0, inside_color: tuple[int, int, int] | list[int, int, int] = (255, 0, 0), edges_color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0), font_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255), font_size: int = 16, font_type: str = 'centurygothic'):
        return design.NummerDesign(border_radius, inside_color, edges_color, font_color, font_size, font_type)
    
    @classmethod
    def button(cls, text, border_radius: int = 0, color_doesnt_downed: tuple[int, int, int] | list[int, int, int] = (255, 0, 0), color_downed: tuple[int, int, int] | list[int, int, int] = (255, 125, 125), text_color_doesnt_downed: tuple[int, int, int] | list[int, int, int] = (255, 255, 255), text_color_downed: tuple[int, int, int] | list[int, int, int] = (125, 0, 0), font_type: str = ('centurygothic'), font_size: int = 16, edges_color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0), change_time_ticks: int = 0):
        return design.ButtonDesign(text, border_radius, color_doesnt_downed, color_downed, text_color_doesnt_downed, text_color_downed, font_type, font_size, edges_color, change_time_ticks)

    def show_designes(cls):   # Must show all available built-in designes as a tuple
        pass
    
    def set_default(cls, design_kit, for_objects = None):   # Sets the defaul design kits for types of objects (Buttons, sliders, etc.) from this for_objects. Design kit is a set of designes designed for every type of interactive object in simple_panels or at least for that types of interactive objects noted in for_objects. A kit of design can be chosen fromin ones and can be creates as a now one from custom designes
        pass                                                # defauld designes should be substitited automatically when specified that design=simple_panels.auto or design=simple_panels_default (needed to choose is needed the new magic number in simple_panels)
    
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
        def __init__(self, text, border_radius, color_doesnt_downed, color_downed, text_color_doesnt_downed, text_color_downed, font_type, font_size, edges_color, change_time_ticks):   # change_time_ticks is how long time animation of pressing a button and animation of releasing of it play
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



class RelateSlider:   # The type of slider in which the value it represents varyes between tips-values, and middle points-values are between that two tip values. Like here: *1* 2 3 4 *5* when 1 pinned as a start point and 5 pinned as an end point
    def __init__(self, dependent_variable_as_list: list, coordinates: tuple | list, min_value: int | float, max_value: int | float, k_steps: int, live_level: int, design):   # dependent_variable_as_list is a list of 1 element   # live_level is a point where the slider on is in the start of a simulation
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

        if not (type(design).__qualname__.split('.')[0] == 'design'):
            raise TypeError(f'The design type was expected, but {type(design)} had passed')
        elif len(type(design).__qualname__.split('.')) == 1:
            raise TypeError('You have passed the design class, but it\'s must be a class object')
        elif len(type(design).__qualname__.split('.')) > 2:
            raise TypeError(f'The design type was expected, but {type(design)} had passed')
        elif not (type(design).__qualname__.split('.')[1] == 'SliderDesign'):
            raise DesignError('A design type object has passed, which doesn\'t intended for the Sliders. Check whereby it was created')

        values_tuple = []   # values at all the points
        one_step = (max_value - min_value) / k_steps
        for i in range(k_steps):
            values_tuple.append(min_value + one_step * i)
        values_tuple.append(max_value)
        values_tuple = tuple(values_tuple)
        self.design = design
        self.coordinates = coordinates
        self.level = live_level
        self.xchunk = round(coordinates[2] / k_steps)   # distance between 2 neighboring points
        self.dependent_variable_as_list = dependent_variable_as_list
        
    def pict(self):
        pass

class Incut:   # A interactive thing pops up when some interctive object requests some input
    def create():
        pass
    
class TapButton:
    instances = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.instances.append(instance)
        return instance

    def __init__(self, rect: tuple[int, int, int, int] | list[int, int, int, int], function: types.FunctionType, design):   # rect is a rect within which the button fits
        if type(rect) is not tuple and type(rect) is not list:
            raise TypeError(f'rect argument must be a list or tuple type')
        elif len(rect) != 4:
            raise ValueError(f'rect require 4 arguments (x, y, width, height), but {len(rect)} had passed')
        for i in range(len(rect)):
            if type(rect[i]) is not int:
                raise TypeError(f'The {rect[i]}th element of coordinates is not int')
        if type(function) is not types.FunctionType:
            raise TypeError(f'function type was expected, but {type(function)} had passed')
        if not (type(design).__qualname__.split('.')[0] == 'design'):
            raise TypeError(f'The design type was expected, but {type(design)} had passed')
        elif len(type(design).__qualname__.split('.')) == 1:
            raise TypeError('You have passed the design class, but it\'s must be a class object')
        elif len(type(design).__qualname__.split('.')) > 2:
            raise TypeError(f'The design type was expected, but {type(design)} had passed')
        elif not (type(design).__qualname__.split('.')[1] == 'ButtonDesign'):
            raise DesignError('A design type object has passed, which doesn\'t intended for the Buttons. Check whereby it was created')
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
            display_for_simple_panels.blit(self.I_am_doesnt_downed, (self.rect[0], self.rect[1]))
        else:
            display_for_simple_panels.blit(self.I_am_downed, (self.rect[0], self.rect[1]))
    
    def handle_some_click(self, event: pygame.event.Event):
        if is_in(event.pos, self.rect):
            self.downed = not self.downed
    
    def tick(self):
        self.downed = False

def handle(all_events: tuple | list):   # Must be called for every event causing in pygame
    if not isinstance(all_events, (tuple, list)):
        raise TypeError(f'a list/tuple of pygame.events had expected but {type(all_events)} was passed')
    else:
        for event in all_events:
            if not isinstance(event, pygame.event.Event):
                raise TypeError(f'Impossible to handle {type(event)}, so pygame.event.Event object expected')
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tapbutton_instances_here = TapButton.instances
                    for button_num in range(len(tapbutton_instances_here)):
                        tapbutton_instances_here[button_num].handle_some_click(event)

def tick():   # Serves all processes simple_panels must handle each tick of the main loop. MUST be called for every pygame.time.Clock().tick(...) tick in the main loop in that program using simple_panels
    for tapbutton in TapButton.instances:
        tapbutton.tick()
