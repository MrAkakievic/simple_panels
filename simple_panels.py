
# Features should be added in future:
"""
1). Design.show_designs()   # Shows designs you can use just now without making your own ones
2). Design.set_default()   # Constructor where you can make/choose designs for different classes or establish a built-in design pack
performed   --->   3). To deal with animation_time so make that color changed gradually
4). All simple_panels interactive objects should be not fixed ones, but should be remaked as movable ones that can be freely relocated. And they should be able to give theirselves as pygame.surface.Surface()
5). Classes in design kits. Should be maked that in kits of design it would be able to design several designes for one type of interactive object like checklist with one type of design, sub-checklist with different one
"""





import pygame, types, math
from typing import Union
from enum import Enum, StrEnum
pygame.init()



####################################################################################################################################

DEFAULT_DISPLAY_SIZE = (1600, 900)
STANDART_BUTTON_BORDER_WIDTH = 5
STANDART_INTENSITY = 2
STANDART_SLASHING_INTENSITY = 4



class Animation(StrEnum):   # This class created for using it's attributes as arguments in press_animation and release_animation parameters by the user
    NO_ANIMATION = 'NO_ANIMATION'
    LINEAR = 'LINEAR'
    EASE = 'EASE'
    SLASHING_EASE = 'SLASHING_EASE'



class Function():   # Translator from Animation() arguments passed my the user to functions performing these animations
    class Button:
        In = {'NO_ANIMATION': None, 'LINEAR': lambda x: x, 'EASE': lambda x: math.pow(x, STANDART_INTENSITY), 'SLASHING_EASE': lambda x: math.pow(x, STANDART_SLASHING_INTENSITY)}
        Out = {'NO_ANIMATION': None, 'LINEAR': lambda x: 1 - x, 'EASE': lambda x: 1 - math.pow(1 - x, STANDART_INTENSITY), 'SLASHING_EASE': lambda x: 1 - math.pow(1 - x, STANDART_SLASHING_INTENSITY)}



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


display = None
display_size = None
NoLimits = NoLimits()
Auto = Auto()

####################################################################################################################################





def is_in(point: tuple[int, int] | list[int, int], area: tuple[int, int, int, int] | list[int, int, int, int]) -> bool:   # Checks is a point in some area
    return True if   (     area[0] <= point[0] and area[0] + area[2] >= point[0] and area[1] <= point[1] and area[1] + area[3] >= point[1]     )   else False

def get_intermediate_color(color_0, color_1, percent_of_1):
    blended_color = [0, 0, 0]
    for channel in range(3):
        this_channel_result = round(color_0[channel] * (1 - percent_of_1) + color_1[channel] * percent_of_1)
        if this_channel_result > 255:
            this_channel_result = 255
        blended_color[channel] = this_channel_result
    return blended_color




def select_display(*given_display):
    global display, display_size
    if len(given_display) == 0:
        if display is not None:
            raise DisplayError('Display already initialized, cannot create a new one')
        display = pygame.display.set_mode(DEFAULT_DISPLAY_SIZE)   # Established the display with default simple_panels size
        display_size = DEFAULT_DISPLAY_SIZE
    elif len(given_display) == 1:
        if isinstance(given_display[0], pygame.Surface):
            display = given_display[0]
            display_size = given_display[0].get_size()
        else:
            raise DisplayError(f'select_display() function requires a pygame.Surface object, but {type(given_display[0])} have passed')
    else:
        raise DisplayError(f'select_display() function requires one argument, but {len(given_display)} ones have passed')


class Design:   # The general class containing designs for all types of interactive objects. Exists only for containing different types of designs, it's planned that a user thinks only one class for design exists
    # The different design classes are created via @classmethod functions for a user, not via constructors
    
    @classmethod
    def slider(cls, inside_color: tuple[int, int, int] | list[int, int, int] = (255, 0, 0), edges_color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0), separators_exist: tuple[int, int, int] | list[int, int, int] = None, notes_exist: bool = None, animation_time: int = 0, animation = None, /):
        return Design.SliderDesign(inside_color, edges_color, separators_exist, notes_exist, animation_time, animation)
    
    @classmethod
    def nummer(cls, border_radius: int = 0, inside_color: tuple[int, int, int] | list[int, int, int] = (255, 0, 0), edges_color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0), font_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255), font_size: int = 16, font_type: str = 'centurygothic', /):
        return Design.NummerDesign(border_radius, inside_color, edges_color, font_color, font_size, font_type)
    
    @classmethod
    def button(cls, border_radius: int = 0, color_not_downed: tuple[int, int, int] | list[int, int, int] = (255, 0, 0), color_downed: tuple[int, int, int] | list[int, int, int] = (255, 125, 125), text_color_not_downed: tuple[int, int, int] | list[int, int, int] = (255, 255, 255), text_color_downed: tuple[int, int, int] | list[int, int, int] = (125, 0, 0), font_type: str = ('centurygothic'), font_size: int = 16, edges_color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0), animation_time: int = 0, press_animation: str = Animation.NO_ANIMATION, release_animation: str = Animation.NO_ANIMATION):
        return Design.ButtonDesign(border_radius, color_not_downed, color_downed, text_color_not_downed, text_color_downed, font_type, font_size, edges_color, animation_time, press_animation, release_animation)

    def show_designs(cls):   # Must show all available built-in designs as a tuple
        pass
    
    def set_default(cls, design_kit, for_objects = None):   # Sets the defaul design kits for types of objects (Buttons, sliders, etc.) from this for_objects. Design kit is a set of designes designed for every type of interactive object in simple_panels or at least for that types of interactive objects noted in for_objects. A kit of design can be chosen fromin ones and can be creates as a now one from custom designes
        pass                                                # defauld designes should be substitited Automatically when specified that design=simple_panels.Auto or design=simple_panels_default (needed to choose is needed the new magic number in simple_panels)
    
    class SliderDesign:
        def __init__(self, inside_color: tuple[int, int, int] | list[int, int, int], edges_color, separators_exist, notes_exist, animation_time, animation):
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
            #   if animation ...
            self.inside_color = inside_color
            self.edges_color = edges_color
            self.separators_exist = separators_exist
            self.notes_exist = notes_exist
            self.animation_time = animation_time
            self.animation = animation
    
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
        def __init__(self, border_radius, color_not_downed, color_downed, text_color_not_downed, text_color_downed, font_type, font_size, edges_color, animation_time, press_animation, release_animation):   # animation_time is how long time animation of pressing a button and animation of releasing of it play
            if not isinstance(border_radius, int):
                raise TypeError(f'int type was expected, but {type(border_radius)} had passed')
            elif border_radius < 0:
                raise ValueError(f'Invalide border_radius (<0)')
            if not isinstance(color_not_downed, (tuple, list)):
                raise TypeError(f'Tuple or list type was expected, but {type(color_not_downed)} had passed')
            elif len(color_not_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(color_not_downed)} elements had passed')
            for i in range(len(color_not_downed)):
                if not isinstance(color_not_downed[i], int):
                    raise TypeError(f'int type was expected, but {type(color_not_downed[i])} had passed')
                if color_not_downed[i] < 0 and color_not_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not isinstance(color_downed, (tuple, list)):
                raise TypeError(f'Tuple or list type was expected, but {type(color_downed)} had passed')
            elif len(color_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(color_downed)} elements had passed')
            for i in range(len(color_downed)):
                if not isinstance(color_downed[i], int):
                    raise TypeError(f'int type was expected, but {type(color_downed[i])} had passed')
                if color_downed[i] < 0 and color_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not isinstance(text_color_not_downed, (tuple, list)):
                raise TypeError(f'Tuple or list type was expected, but {type(text_color_not_downed)} had passed')
            elif len(text_color_not_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(text_color_not_downed)} elements had passed')
            for i in range(len(text_color_not_downed)):
                if not isinstance(text_color_not_downed[i], int):
                    raise TypeError(f'int type was expected, but {type(text_color_not_downed[i])} had passed')
                if text_color_not_downed[i] < 0 and text_color_not_downed[i] > 255:
                    raise ValueError(f'{i}st color argument is less than 0 or bigger than 255')
            if not isinstance(text_color_downed, (tuple, list)):
                raise TypeError(f'Tuple or list type was expected, but {type(text_color_downed)} had passed')
            elif len(text_color_downed) != 3:
                raise ValueError(f'Tuple or list with 3 elements (RGB) was expected, but {len(text_color_downed)} elements had passed')
            for i in range(len(text_color_downed)):
                if not isinstance(text_color_downed[i], int):
                    raise TypeError(f'int type was expected, but {type(text_color_downed[i])} had passed')
                if text_color_downed[i] < 0 and text_color_downed[i] > 255:
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
            if not isinstance(animation_time, int):
                raise TypeError(f'int type was expected, but {type(animation_time)} had passed')
            elif animation_time < 0:
                raise ValueError('Invalide value (less than 0 or bigger than 255)')
            if not type(press_animation) == Animation:
                raise TypeError(f'Animation type had expected but {type(press_animation)} was passed')
            if not type(release_animation) == Animation:
                raise TypeError(f'Animation type had expected but {type(release_animation)} was passed')

            self.border_radius = border_radius
            self.color_not_downed = color_not_downed
            self.color_downed = color_downed
            self.text_color_not_downed = text_color_not_downed
            self.text_color_downed = text_color_downed
            self.font_type = font_type
            self.font_size = font_size
            self.edges_color = edges_color
            self.animation_time = animation_time
            self.press_animation = press_animation
            self.release_animation = release_animation



####################################################################################################################################

DEFAUL_NUMMER_DESING = Design.nummer()
DEFAUL_BUTTON_DESING = Design.button()
DEFAUL_SLIDER_DESING = Design.slider()

####################################################################################################################################



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
        display.blit(cls.preset, (cls.coordinates[0], cls.coordinates[1]))
        rend = cls.font.render(str(text), True, cls.font_color)
        display.blit(rend, (round(cls.coordinates[0] + cls.width / 2) - rend.get_size()[0] / 2, round(cls.coordinates[1] + cls.width / 2) - rend.get_size()[1] / 2))


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
        self.color_not_downed = design.color_not_downed
        self.color_downed = design.color_downed
        self.edges_color = design.edges_color
        self.font = pygame.font.SysFont(design.font_type, design.font_size)

        self.animation_time = design.animation_time
        self.press_animation = design.press_animation
        self.release_animation = design.release_animation

        self.text_color_not_downed = design.text_color_not_downed
        self.text_color_downed = design.text_color_downed

        self.surface_not_downed = pygame.surface.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
        pygame.draw.rect(self.surface_not_downed, self.color_not_downed, (0, 0, self.rect[2], self.rect[3]), border_radius = self.border_radius)
        pygame.draw.rect(self.surface_not_downed, self.edges_color, (0, 0, self.rect[2], self.rect[3]), STANDART_BUTTON_BORDER_WIDTH, self.border_radius)
        text_surface_not_downed = self.font.render(text, True, design.text_color_not_downed)
        self.surface_not_downed.blit(text_surface_not_downed, ((io := self.surface_not_downed.get_size())[0] / 2 - (io0 := text_surface_not_downed.get_size())[0] / 2, io[1] / 2 - io0[1] / 2))
        
        self.surface_downed = pygame.surface.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
        pygame.draw.rect(self.surface_downed, self.color_downed, (0, 0, self.rect[2], self.rect[3]), border_radius = self.border_radius)
        pygame.draw.rect(self.surface_downed, self.edges_color, (0, 0, self.rect[2], self.rect[3]), STANDART_BUTTON_BORDER_WIDTH, self.border_radius)
        text_surface_downed = self.font.render(text, True, design.text_color_downed)
        self.surface_downed.blit(text_surface_downed, ((io := self.surface_downed.get_size())[0] / 2 - (io0 := text_surface_downed.get_size())[0] / 2, io[1] / 2 - io0[1] / 2))

        self.press_animation_function = Function.Button.In[design.press_animation]
        self.release_animation_function = Function.Button.In[design.release_animation]
        self.phases = math.ceil(design.animation_time / 2)   # How much frames in ticks in one half of animation (1 half is press and 1 half is release of button)
        self.current_phase = None   # from -self.phase to 0 it's press animation and from 0 to self.phase it's release animation. None if no animation just now
        self.animation_playing = False

    def pict(self):
        if self.current_phase is None:
            display.blit(self.surface_not_downed, (self.rect[0], self.rect[1]))
        elif self.current_phase == 0 or (self.press_animation_function is None and self.current_phase < 0) or (self.release_animation_function is None and self.current_phase > 0):
            display.blit(self.surface_downed, (self.rect[0], self.rect[1]))
        elif self.current_phase < 0:
            current_surface = pygame.surface.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
            pygame.draw.rect(current_surface, get_intermediate_color(self.color_not_downed, self.color_downed, self.press_animation_function(1 + self.current_phase / self.phases)), (0, 0, self.rect[2], self.rect[3]), border_radius = self.border_radius)
            pygame.draw.rect(current_surface, self.edges_color, (0, 0, self.rect[2], self.rect[3]), STANDART_BUTTON_BORDER_WIDTH, self.border_radius)
            note = self.font.render(self.text, True, get_intermediate_color(self.text_color_not_downed, self.text_color_downed, self.press_animation_function(1 + self.current_phase / self.phases)))
            current_surface.blit(note, ((io := current_surface.get_size())[0] / 2 - (io0 := note.get_size())[0] / 2, io[1] / 2 - io0[1] / 2))
            display.blit(current_surface, (self.rect[0], self.rect[1]))
        elif self.current_phase > 0:
            current_surface = pygame.surface.Surface((self.rect[2], self.rect[3]), pygame.SRCALPHA)
            pygame.draw.rect(current_surface, (get_intermediate_color(self.color_downed, self.color_not_downed, self.release_animation_function(self.current_phase / self.phases))), (0, 0, self.rect[0], self.rect[1]), border_radius = self.border_radius)
            pygame.draw.rect(current_surface, self.edges_color, (0, 0, self.rect[2], self.rect[3]), STANDART_BUTTON_BORDER_WIDTH, self.border_radius)
            note = self.font.render(self.text, True, get_intermediate_color(self.text_color_downed, self.text_color_not_downed, self.release_animation_function(self.current_phase / self.phases)))
            current_surface.blit(note, ((io := current_surface.get_size())[0] / 2 - (io0 := note.get_size())[0] / 2, io[1] / 2 - io0[1] / 2))
            display.blit(current_surface, (self.rect[0], self.rect[1]))

    def handle_some_click(self, event: pygame.event.Event):   # The subsidiary function for the global function handle() that call it
        if is_in(event.pos, self.rect):
            self.current_phase = -self.phases
            self.animation_playing = True
            self.function()
    
    def update(self):   # The subsidiary function for the global function update() that call it
        if self.current_phase == self.phases:
            self.current_phase = None
            self.animation_playing = False
        elif self.animation_playing:
            self.current_phase += 1

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
