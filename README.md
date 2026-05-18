# SIMPLE_PANELS

<a name = "about-anchor"></a>
## About
This python library designed for embedding intuitive buttons, sliders, windows and other types of interactive elements with basic customization and functionality features into pygame projects

Tags: python, pygame, UI, simplify

<a name = "table-of-content-anchor"></a>
## Table of content
- [About](#about-anchor)
- [Table of content](#table-of-content-anchor)
- [Features](#features-anchor)
- [Installation & Connection](#installation-and-connection-anchor)
- [Documentation](#documentation-anchor)
  - [Examples](#examples)
  - [The necessary items you should embed before consuming simple_panels](#before-consuming)
  - [The quick start](#the-quick-start)
  - [About UI elements](#about-UI-elements)

<a name = "features-anchor"></a>
## Features
- __ __ __

<a name = "installation-and-connection-anchor"></a>
## Installation & Connection
Unavaivable yet

<a name = "documentation-anchor"></a>
## Documentation
<a name = examples></a>
### Examples
These are some examples of simple_panels usage. You can copy, past, play and try these examples. Don't forget to import simple_panels

___ ___ ___ No examples yet
<a name = "before-consuming"></a>
### The necessary items you should embed before consuming simple_panels
>[!NOTE]
>The sps literal uses for represent simple_panels insted of simple_panels throughout the Documentation in the code. This is represents the tacit line "import simple_panels as sps" in the header of the code

simple_panels created as an application tool with the one aim: to shorter losing time on creating interactive elements that often needed in small projects like simulation when you use pygame. simple_panels offers the regular interactive elements: <ins>Buttons</ins> that can service regular functions. simple_panels does that pygame routine for you. But this means simple_panels is deeply interconnected with pygame. To ensure their coordinated activity you should embed some items into your regular program with simple_panels:
* sps.handle(events) - this function handles all events came the last call of this function itself: clicks on the buttons, moves of the sliders and other, but this function can't track that events itself, you should pass them to this function as well as you handle these events in your program out of simple_panels. The most mere case is to save events each turn and pass them into simple_panels via sps.handle(events) then handle these events in your part of program. I recommend exacly this approach due to if you call sps.handle(events) before your general handling of events you will operate with the situation of current time so simple_panels got handled all clicks and actions, but in opposite side if you call sps.handle(events) at the end of the main loop your program will operate with that situation was actual one tick earlier

That approach I recommend:
```
import pygame, simple_panels as sps
pygame.init()

while True:
    events = pygame.events.get()
    sps.handle(events)               # sps handling
    for event in events:             # Your handling, you're just working with the fresh data
        ...                          # Your handling
```
* sps.update() --- This function reports sps that the tick ended and sps prepares for the next turn. If you don't called this then sps think the program is in the previos tick. But if calld this function twice, sps will overtake the main loop at 1 tick. This function is necessary to call before pygame.time.Clock().tick() (the end of the tick) or before the code of the main loop. I recommend the firs approach:
>[!NOTE]
>sps.update() requires no parameters such FPS

```
import pygame, simple_panels as sps
pygame.init()
cl = pygame.time.Clock()

FPS = 60

while True:
    
    ...                      # Your code

    sps.update()             # sps update
    cl.tick(FPS)             # pygame tick
```
* sps.select_display(display) --- sps don't know about display you made via pygame before you report about it. sps.select_display(display) is that function that give sps the link on display. In your program you should save pygame display as a variable then pass it into sps
```
import pygame, simple_panels as sps
pygame.init()

screen = pygame.display.set_mode((1600, 900))
sps.select_display(screen)
```
* sps.pict() --- pict() is a class of functions that map sps objects onto a display, but the sps.pict() maps all sps objects onto a display. Call it then call pygame.display.flip() or pygame.display.update()
```
import pygame, simple_panels as sps
pygame.init()

screen = pygame.display.set_mode((1600, 900))
sps.select_display(screen)

pygame.draw.circle(screen, (255, 0, 0), (200, 200), 100)                # <--------- a pygame object
pygame.display.flip()                                                   # <--------- this objects is showed on the display

sps.TapButton('Tap Me', (400, 200, 100, 100), lambda: print('hello'))   # <--------- some sps object
sps.pict()                                                              # <--------- pygame.display.flip() can't show sps objects without it
pygame.display.flip()                                                   # <--------- now let's call .flip()
```
These 4 items are necessary to get normal behavior of sps. After you have cared about that you can use all fetures of sps freely

<a name = "the-quick-start"></a>
### The quick start
There is a minimal starting code you can extend:
```
import pygame, simple_panels as sps
pygame.init()

DISPLAY_SIZE = (1600, 900)
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode(DISPLAY_SIZE)
sps.select_display(screen)

while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    sps.handle(events)
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        #   Some your handling
    #   Some your code
    sps.pict()
    sps.update()
    pygame.display.flip()
    clock.tick(FPS)
```
<a name = about-UI-elements></a>
### About UI elements
Here you can get how to create UI elements and how to use them

To create a button for openers you should choose the type you want to utilize. There are 2 types of the button: TapButton and .... The difference is that TapButton is designes for triggering on the click but ... designed for tracking the hold of the button
The difference in customization between 2 types is minimal: both require 3 necessary arguments: text, rect and function. To create TapButton use sps.TapButton() and to create ... use sps.....

text is a parameter contains what the note will placed on your button

rect is a position of your button on the display as (x, y, width, high) or [x, y, width, high]

function is that module will executed each time the user click on the button. For ... it also be executed each tick the button hold down
```
def func():                      # Logic when button clicked
    ...
button = sps.TapButton('Tap Me', (100, 100, 100, 100), func)
```
the launchable code:
```
import pygame, simple_panels as sps
pygame.init()

DISPLAY_SIZE = (1600, 900)
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode(DISPLAY_SIZE)
sps.select_display(screen)

def func():                                                      # <--- the code we added
    ...                                                          # <--- the code we added
button = sps.TapButton('Tap Me', (300, 300, 300, 200), func)     # <--- the code we added

while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    sps.handle(events)
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    sps.pict()
    sps.update()
    pygame.display.flip()
    clock.tick(FPS)
```
the result:





















