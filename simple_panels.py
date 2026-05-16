
# Features should be added in future:
"""
1). Design.show_designs()   # Shows designs you can use just now without making your own ones
2). Design.set_default()   # Constructor where you can make/choose designs for different classes or establish a built-in design pack
3). To deal with change_time_in_ticks so make that color changed gradually
4). All simple_panels interactive objects should be not fixed ones, but should be remaked as movable ones that can be freely relocated. And they should be able to give theirselves as pygame.surface.Surface()
5). Classes in designe kits. Should be maked that in kits of design it would be able to design several designes for one type of interactive object like checklist with one type of design, sub-checklist with different one
"""





######################################################################################

DEFAULT_SIZE_OF_DISPLAY = (1600, 900)

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



class NoLimits:
    2 + 2 == 4

class Auto:
    2 + 2 == 4



display_for_simple_panels = None
display_size = None
NoLimits = NoLimits()
Auto = Auto()


def is_in(point: tuple[int, int] | list[int, int], area: tuple[int, int, int, int] | list[int, int, int, int]) -> bool:   # Checks is a point in some area
    return True if   (     area[0] <= point[0] and area[0] + area[2] >= point[0] and area[1] <= point[1] and area[1] + area[3] >= point[1]     )   else False





def select_display(*display):
    global display_for_simple_panels, display_size
    if len(display) == 0:
        if display_for_simple_panels is not None:
            raise DisplayError('Display already initialized, cannot create a new one')
        display_for_simple_panels = pygame.display.set_mode(DEFAULT_SIZE_OF_DISPLAY)   # Established the display with default simple_panels size
        display_size = DEFAULT_SIZE_OF_DISPLAY
    elif len(display) == 1:
        if isinstance(display[0], pygame.Surface):
            display_for_simple_panels = display[0]
            display_size = display[0].get_size()
        else:
            raise DisplayError(f'select_display() function requires a pygame.Surface object, but {type(display[0])} have passed')
    else:
        raise DisplayError(f'select_display() function requires one argument, but {len(display)} ones have passed')
            


class Design:   # The general class containing designs for all types of interactive objects. Exists only for containing different types of designs, it's planned that a user thinks only one class for design exists
    # The different design classes are created via @classmethod functions for a user, not via constructors
    
    @classmethod
    def slider(cls, inside_color: tuple[int, int, int] | list[int, int, int] = (255, 0, 0), edges_color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0), separators_exist: tuple[int, int, int] | list[int, int, int] = None, notes_exist: bool = None, /):
        return Design.SliderDesign(inside_color, edges_color, separators_exist, notes_exist)
    
    @classmethod
    def nummer(cls, border_radius: int = 0, inside_color: tuple[int, int, int] | list[int, int, int] = (255, 0, 0), edges_color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0), font_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255), font_size: int = 16, font_type: str = 'centurygothic'):
        return Design.NummerDesign(border_radius, inside_color, edges_color, font_color, font_size, font_type)
    
    @classmethod
    def button(cls, border_radius: int = 0, color_when_does_not_downed: tuple[int, int, int] | list[int, int, int] = (255, 0, 0), color_when_downed: tuple[int, int, int] | list[int, int, int] = (255, 125, 125), text_color_when_does_not_downed: tuple[int, int, int] | list[int, int, int] = (255, 255, 255), text_color_when_downed: tuple[int, int, int] | list[int, int, int] = (125, 0, 0), font_type: str = ('centurygothic'), font_size: int = 16, edges_color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0), change_time_in_ticks: int = 0):
        return Design.ButtonDesign(border_radius, color_when_does_not_downed, color_when_downed, text_color_when_does_not_downed, text_color_when_downed, font_type, font_size, edges_color, change_time_in_ticks)

    def show_designs(cls):   # Must show all available built-in designs as a tuple
        pass
    
    def set_default(cls, design_kit, for_objects = None):   # Sets the defaul design kits for types of objects (Buttons, sliders, etc.) from this for_objects. Design kit is a set of designes designed for every type of interactive object in simple_panels or at least for that types of interactive objects noted in for_objects. A kit of design can be chosen fromin ones and can be creates as a now one from custom designes
        pass                                                # defauld designes should be substitited Automatically when specified that design=simple_panels.Auto or design=simple_panels_default (needed to choose is needed the new magic number in simple_panels)
    
    class SliderDesign:
        def __init__(self, inside_color: tuple[int, int, int] | list[int, int, int], edges_color, separators_exist, notes_exist):
            if not isinstance(inside_color, (tuple, list)):
                if inside_color is None:
                    raise ValueError(f'The color choosing is necessarily, None is impossible')
                else:
                    raise TypeError(f'Tuple or list type was expected, but {type(inside_color)} had passed')
            if not isinstance(edges_color, (tuple, list)):
                if edges_color is None:
                    raise ValueError(f'The color choosing is necessarily, None is impossible')
                else:
                    raise TypeError(f'Tuple or list type was expected, but {type(edges_color)} had passed')
            if separators_exist is not None and not isinstance(separators_exist, (tuple, list)):
                raise TypeError(f'Tuple or list or None was expected, but {type(separators_exist)} had passed')
            if notes_exist is not None and not isinstance(notes_exist, bool):
                raise TypeError(f'None or bool type was expected, but {type(notes_exist)} had passed')
            self.inside_color = inside_color
            self.edges_color = edges_color
            self.separators_exist = separators_exist
            self.notes_exist = notes_exist
    
    class NummerDesign:
        def __init__(self, border_radius, inside_color, edges_color, font_color, font_size, font_type):
            if not isinstance(border_radius, int):
                raise TypeError(f'The int object was expected, but {type(border_radius)} had passed')
            elif border_radius < 0:
                raise ValueError('The nummer less than 0 had passed')
            if not isinstance(inside_color, (tuple, list)):
                if inside_color is None:
                    raise ValueError(f'The color choosing is necessarily, None is impossible')
                else:
                    raise TypeError(f'Tuple or list type was expected, but {type(inside_color)} had passed')
            if not isinstance(edges_color, (tuple, list)):
                if edges_color is None:
                    raise ValueError(f'The color choosing is necessarily, None is impossible')
                else:
                    raise TypeError(f'Tuple or list type was expected, but {type(edges_color)} had passed')
            if not isinstance(font_color, (tuple, list)):
                raise TypeError(f'Tuple or list on RGB was expected, but {type(font_color)} had passed')
            elif len(font_color) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(font_color)} elements had passed')
            else:
                for i in range(3):
                    if not isinstance(font_color[i], int):
                        raise TypeError(f'None-int had passed as {i}th color element')
                    elif font_color[i] < 0 or font_color[i] > 255:
                        raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not isinstance(font_size, int):
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
        def __init__(self, border_radius, color_when_does_not_downed, color_when_downed, text_color_when_does_not_downed, text_color_when_downed, font_type, font_size, edges_color, change_time_in_ticks):   # change_time_in_ticks is how long time animation of pressing a button and animation of releasing of it play
            if not isinstance(border_radius, int):
                raise TypeError(f'int type was expected, but {type(border_radius)} had passed')
            elif border_radius < 0:
                raise ValueError(f'Invalide border_radius (<0)')
            if not isinstance(color_when_does_not_downed, (tuple, list)):
                raise TypeError(f'Tuple or list type was expected, but {type(color_when_does_not_downed)} had passed')
            elif len(color_when_does_not_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(color_when_does_not_downed)} elements had passed')
            for i in range(len(color_when_does_not_downed)):
                if not isinstance(color_when_does_not_downed[i], int):
                    raise TypeError(f'int type was expected, but {type(color_when_does_not_downed[i])} had passed')
                if color_when_does_not_downed[i] < 0 and color_when_does_not_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not isinstance(color_when_downed, (tuple, list)):
                raise TypeError(f'Tuple or list type was expected, but {type(color_when_downed)} had passed')
            elif len(color_when_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(color_when_downed)} elements had passed')
            for i in range(len(color_when_downed)):
                if not isinstance(color_when_downed[i], int):
                    raise TypeError(f'int type was expected, but {type(color_when_downed[i])} had passed')
                if color_when_downed[i] < 0 and color_when_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not isinstance(text_color_when_does_not_downed, (tuple, list)):
                raise TypeError(f'Tuple or list type was expected, but {type(text_color_when_does_not_downed)} had passed')
            elif len(text_color_when_does_not_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(text_color_when_does_not_downed)} elements had passed')
            for i in range(len(text_color_when_does_not_downed)):
                if not isinstance(text_color_when_does_not_downed[i], int):
                    raise TypeError(f'int type was expected, but {type(text_color_when_does_not_downed[i])} had passed')
                if text_color_when_does_not_downed[i] < 0 and text_color_when_does_not_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not isinstance(text_color_when_downed, (tuple, list)):
                raise TypeError(f'Tuple or list type was expected, but {type(text_color_when_downed)} had passed')
            elif len(text_color_when_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(text_color_when_downed)} elements had passed')
            for i in range(len(text_color_when_downed)):
                if not isinstance(text_color_when_downed[i], int):
                    raise TypeError(f'int type was expected, but {type(text_color_when_downed[i])} had passed')
                if text_color_when_downed[i] < 0 and text_color_when_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')

            if not isinstance(font_size, int):
                raise TypeError(f'int type was expected, but {type(font_size)} had passed')
            elif font_size < 1:
                raise ValueError(f'Indalid value (less than 1)')
            
            try:
                self.font = pygame.font.SysFont(font_type, font_size)
            except:
                raise ValueError('This font is not found')

            if not isinstance(edges_color, (tuple, list)):
                raise TypeError(f'Tuple or list type was expected, but {type(edges_color)} had passed')
            elif len(edges_color) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(edges_color)} elements had passed')
            for i in range(len(edges_color)):
                if not isinstance(edges_color[i], int):
                    raise TypeError(f'int type was expected, but {type(edges_color[i])} had passed')
                if edges_color[i] < 0 and edges_color[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not isinstance(change_time_in_ticks, int):
                raise TypeError(f'int type was expected, but {type(change_time_in_ticks)} had passed')
            elif change_time_in_ticks < 0:
                raise ValueError('Invalide value (less than 0 or bigger than 255)')
            self.border_radius = border_radius
            self.color_when_does_not_downed = color_when_does_not_downed
            self.color_when_downed = color_when_downed
            self.text_color_when_does_not_downed = text_color_when_does_not_downed
            self.text_color_when_downed = text_color_when_downed
            self.font_type = font_type
            self.font_size = font_size
            self.edges_color = edges_color
            self.change_time_in_ticks = change_time_in_ticks

DEFAUL_NUMMER_DESING = Design.nummer()
DEFAUL_BUTTON_DESING = Design.button()
DEFAUL_SLIDER_DESING = Design.slider()


class Nummer:   # The panel fixed on a some place that shows some text when user interacts with some simple_panels object
    exist = False
    coordinates = None   # Top-left point
    width = None   # The same value for width along x and for width along y
    font = None

    @classmethod
    def set(cls, coordinates: tuple | list, width: Union[int, Auto], design = DEFAUL_NUMMER_DESING):
        if not display_size:
            raise DisplayError('Display wasn\'t detected')
        if not isinstance(coordinates, (tuple, list)):
            raise TypeError(f'The {type(coordinates)} type had passed, but a tuple or list expected')
        if not isinstance(width, int) and not type(width) == Auto:
            raise TypeError(f'The {type(width)} type had passed, but int was expected')
        if len(coordinates) != 2:
            raise ValueError(f'{len(coordinates)} arguments had passed, but 2 ones (x, y) was expected')
        for i in range(2):
            if not isinstance(coordinates[i], int):
                raise TypeError(f'The {type(coordinates[i])} type was passed for {i} position in the coordinates, but int was expected')
        if type(width) == Auto:
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
        if not (type(design).__qualname__.split('.')[0] == 'Design'):
            raise TypeError(f'The design type was expected, but {type(design)} had passed')   # These is a design type for every class of interactive object but all of them located in the Design class
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
        cls.preset = pygame.surface.Surface((cls.width, cls.width), pygame.SRCALPHA)
        pygame.draw.rect(cls.preset, design.inside_color, (0, 0, width, width), border_radius = design.border_radius)
        pygame.draw.rect(cls.preset, design.edges_color, (0, 0, width, width), 5, design.border_radius)
    
    @classmethod
    def pict(cls, text):   # Very function nummer exists to implement. Any interactive element can show some text it wants over nummer.pict()
        if not display_size:
            raise DisplayError('simple_panels is not seen the display')
        display_for_simple_panels.blit(cls.preset, (cls.coordinates[0], cls.coordinates[1]))
        rend = cls.font.render(str(text), True, cls.font_color)
        display_for_simple_panels.blit(rend, (round(cls.coordinates[0] + cls.width / 2) - rend.get_size()[0] / 2, round(cls.coordinates[1] + cls.width / 2) - rend.get_size()[1] / 2))


class RelateSlider:   # The type of slider in which the value it represents varyes between tips-values, and middle points-values are between that two tip values. Like here: *1* 2 3 4 *5* when 1 pinned as a start point and 5 pinned as an end point
    def __init__(self, dependent_variable_as_list: list, coordinates: tuple | list, min_value: int | float, max_value: int | float, k_steps: int, live_level: int, design = DEFAUL_SLIDER_DESING):   # dependent_variable_as_list is a list of 1 element   # live_level is a point where the slider on is in the start of a simulation
        if not isinstance(min_value, (int, float)):
            raise TypeError(f'Int or float type was expected, but {type(min_value)} had passed')
        if not isinstance(max_value, (int, float)):
            raise TypeError(f'Int or float type was expected, but {type(max_value)} had passed')
        if not isinstance(k_steps, int):
            raise TypeError(f'Int type was expected, but {type(k_steps)} had passed')
        if not isinstance(coordinates, (tuple, list)):
            raise TypeError(f'Tuple or list type was expected, but {type(coordinates)} had passed')
        else:
            if len(coordinates) != 4:
                raise ValueError(f'coordinates must contain 4 element (x, y, width and height), but is {len(coordinates)}')
            else:
                if not isinstance(coordinates[0], int):
                    raise TypeError(f'x coordinate must be int type, but {type(coordinates[0])} had passed')
                elif not isinstance(coordinates[1], int):
                    raise TypeError(f'y coordinate must be int type, but {type(coordinates[1])} had passed')
                elif not isinstance(coordinates[2], int):
                    raise TypeError(f'width must be int type, but {type(coordinates[2])} had passed')
                elif not isinstance(coordinates[3], int):
                    raise TypeError(f'height must be int type, but {type(coordinates[3])} had passed')
        if not isinstance(dependent_variable_as_list, list):
            raise TypeError(f'dependent_valiable must be lists of 1 entry, but {type(k_steps)} had passed')
        else:
            if len(dependent_variable_as_list) != 1:
                raise ValueError(f'dependent_variable must contain 1 element, but is {len(dependent_variable_as_list)}')
        if k_steps < 1:
            raise ValueError(f'k_steps must be >= 1, but is {k_steps}')
        if not isinstance(live_level, int):
            raise TypeError(f'Int object was expected, but {type(live_level)} had passed')
        else:
            if live_level > k_steps or live_level < 0:
                raise ValueError(f'Had passed the impossible live_level. It\'s the {live_level}, but a one from 0 to {k_steps} was expected')

        if not (type(design).__qualname__.split('.')[0] == 'Design'):
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

class Incut:   # A interactive thing pops up when some interctive object requests some input like text (clipdoard)
    def create():
        pass
    
class TapButton:
    instances = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.instances.append(instance)
        return instance

    def __init__(self, text: str, rect: tuple[int, int, int, int] | list[int, int, int, int], function: types.FunctionType, design = DEFAUL_BUTTON_DESING):   # rect is a rect within which the button fits
        try:
            text = str(text)
        except:
            raise TypeError(f'Impossible to transform the value to the str type')
        if not isinstance(rect, (tuple, list)):
            raise TypeError(f'rect argument must be a list or tuple type')
        elif len(rect) != 4:
            raise ValueError(f'rect require 4 arguments (x, y, width, height), but {len(rect)} had passed')
        for i in range(len(rect)):
            if not isinstance(rect[i], int):
                raise TypeError(f'The {rect[i]}th element of coordinates is not int')
        if not isinstance(function, types.FunctionType):
            raise TypeError(f'function type was expected, but {type(function)} had passed')
        if not (type(design).__qualname__.split('.')[0] == 'Design'):
            raise TypeError(f'The design type was expected, but {type(design)} had passed')
        elif len(type(design).__qualname__.split('.')) == 1:
            raise TypeError('You have passed the design class, but it\'s must be a class object')
        elif len(type(design).__qualname__.split('.')) > 2:
            raise TypeError(f'The design type was expected, but {type(design)} had passed')
        elif not (type(design).__qualname__.split('.')[1] == 'ButtonDesign'):
            raise DesignError('A design type object has passed, which doesn\'t intended for the Buttons. Check whereby it was created')
        self.text = text
        self.rect = rect
        self.function = function
        self.border_radius = design.border_radius
        self.color_when_does_not_downed = design.color_when_does_not_downed
        self.color_when_downed = design.color_when_downed
        self.edges_color = design.edges_color
        self.change_time_in_ticks = design.change_time_in_ticks
        self.text_color_when_does_not_downed = design.text_color_when_does_not_downed
        self.text_color_when_downed = design.text_color_when_downed
        self.surface_not_downed = pygame.surface.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
        pygame.draw.rect(self.surface_not_downed, self.color_when_does_not_downed, (0, 0, self.rect[2], self.rect[3]), border_radius = self.border_radius)
        pygame.draw.rect(self.surface_not_downed, self.edges_color, (0, 0, self.rect[2], self.rect[3]), 5, self.border_radius)
        text_surface_downed = pygame.font.SysFont(design.font_type, design.font_size).render(text, True, design.text_color_when_does_not_downed)
        self.surface_not_downed.blit(text_surface_downed, ((io := self.surface_not_downed.get_size())[0] / 2 - (io0 := text_surface_downed.get_size())[0] / 2, io[1] / 2 - io0[1] / 2))
        self.surface_downed = pygame.surface.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
        pygame.draw.rect(self.surface_downed, self.color_when_downed, (0, 0, self.rect[2], self.rect[3]), border_radius = self.border_radius)
        pygame.draw.rect(self.surface_downed, self.edges_color, (0, 0, self.rect[2], self.rect[3]), 5, self.border_radius)
        text_surface_not_downed = pygame.font.SysFont(design.font_type, design.font_size).render(text, True, design.text_color_when_downed)
        self.surface_downed.blit(text_surface_not_downed, ((io := self.surface_downed.get_size())[0] / 2 - (io0 := text_surface_not_downed.get_size())[0] / 2, io[1] / 2 - io0[1] / 2))

        self.is_downed = False
    
    def pict(self):
        if self.is_downed is False:
            display_for_simple_panels.blit(self.surface_not_downed, (self.rect[0], self.rect[1]))
        else:
            display_for_simple_panels.blit(self.surface_downed, (self.rect[0], self.rect[1]))
    
    def handle_some_click(self, event: pygame.event.Event):
        if is_in(event.pos, self.rect):
            self.is_downed = not self.is_downed
            self.function()
    
    def update(self):
        self.is_downed = False

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

def update():   # Serves all processes simple_panels must handle each tick of the main loop. MUST be called for every pygame.time.Clock().tick(...) tick in the main loop in that program using simple_panels
    for tapbutton in TapButton.instances:
        tapbutton.update()
