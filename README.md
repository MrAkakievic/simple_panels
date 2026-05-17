# SIMPLE_PANELS

## About
<a name = "about-anchor"></a>
This python library designed for embedding intuitive buttons, sliders, windows and other types of interactive elements with basic customization and functionality features into pygame projects

Tags: python, pygame, UI, simplify

## Table of content
<a name = "table-of-content-anchor"></a>
- [About](#about-anchor)
- [Table of content](#table-of-content-anchor)
- [Features](#features-anchor)
- [Installation & Connection](#installation-and-connection-anchor)
- [Documentation](#documentation-anchor)
- - [What is simple panels? The necessarly items you should embed into your simple_panels program](#before-consuming)

## Features
<a name = "features-anchor"></a>
- __ __ __

## Installation & Connection
<a name = "installation-and-connection-anchor"></a>
Unavaivable yet

## Documentation
<a name = "documentation-anchor"></a>
### The necessary items you should embed before consuming simple_panels
<a name = "before-consuming"></a>
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
* sps.update() - this function reports sps that the tick ended and sps prepares for the next turn. If you don't called this then sps think the program is in the previos tick. But if calld this function twice, sps will overtake the main loop at 1 tick. This function is necessary to call before pygame.time.Clock().tick() (the end of the tick) or before the code of the main loop. I recommend the firs approach:
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





























