import pygame
from pygame.locals import *
import sys
import backgroundClass


FPS = 100
fpsClock = pygame.time.Clock()
all_elements_list = pygame.sprite.LayeredUpdates()
screen = pygame.display.set_mode((600, 400), RESIZABLE, WINDOWMAXIMIZED)
screen.fill((0, 200, 0))

sprites = []

sprites.append(backgroundClass.Sprite())

all_elements_list.add(sprites)
all_elements_list.draw(screen)
# def createElements(cnt):
#     for i in range(cnt):
#         createdElement = element('bitmapa.png', 0.9, 'numer ' + str(i + 1), (23, 23, 23))
#         createdElement.ID = i
#         sprites.append(createdElement)
#
# def createSlots(cnt):
#     for i in range(cnt):
#         createdElement = elementSlot('bitmapa1.png', 1, 'slot ' + str(i + 1), (155, 155, 155))
#         createdElement.ID = i
#         slots.append(createdElement)
#
# def placeElements():
#     for s in sprites:
#         x = (pygame.display.get_window_size()[0]/(sprites.__len__()+1)) * (s.ID+1) - s.image.get_size()[0]/2
#         y = (pygame.display.get_window_size()[1]/20)*3 # - s.image.get_size()[1]/4
#         pos = [x, y]
#         s.initialPosition = pos
#         s.updateSprite(pos)
# def placeSlots():
#     for s in slots:
#         x = (pygame.display.get_window_size()[0]/(slots.__len__()+1)) * (s.ID+1) - s.image.get_size()[0]/2
#         y = (pygame.display.get_window_size()[1]/20)*12 # - s.image.get_size()[1]/4
#         pos = [x, y]
#         s.position = pos
#         s.initialPosition = pos
#         s.updateSprite(pos)
# #////////////////////////////////////////////////////////////////////////
#
# def init():
#     pygame.init()
#     global bg
#
#     bg = pygame.image.load('obr.jpg')
#     screen.blit(bg, (0,0))
#     createSlots(objCnt)
#     createElements(objCnt)
#     placeSlots()
#     placeElements()
#
#     all_elements_list.add(sprites)
#     all_elements_list.draw(screen)
#     all_slots_list.add(slots)
#     all_slots_list.draw(screen)
#
# init()
#
#
#
#
#
def closeEventHandler():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#
# def eventHandlerMouseCoursor(element = None):
#     #print(element)
#     if element != None:
#         pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
#     if element == None:
#         pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
#
#
# def checkCollision():
#     global dropped
#     global currentElement
#     global MD
#     MD = pygame.mouse.get_pressed()[0]
#     cnt = 0
#     if currentElement == None:
#         for i in sprites:
#             if i != None:
#                 if i.rect.collidepoint(pygame.mouse.get_pos()):
#                     currentElement = i
#                     break
#             cnt += 1
#
#     eventHandlerMouseCoursor(currentElement)
#
#
#     #print(currentElement)
#
#
#
#     if MD == True and currentElement != None:
#         #print('kliknięty')
#         drag()
#
#     if MD == False and currentElement != None:
#         if currentElement.lifted == True:
#             print('drop')
#             drop()
#             currentElement = None
#
#
#     if cnt == sprites.__len__() or MD == False:
#
#         currentElement = None
#     # cnt = -1
#     # checkSlotCollision()
#     # for i in sprites:
#     #     cnt += 1
#     #     if i.rect.collidepoint(pygame.mouse.get_pos()) and MD == MOUSEBUTTONDOWN:# and pygame.mouse.get_pressed()[0] == True:
#     #         currentElement = i
#     #         eventHandlerDragAndDrop(i)
#     #         break
#
#
# def checkSlotCollision():
#     global currentSlot
#     currentSlot = None
#     for i in slots:
#         if currentElement != None and i != None:
#             if i.rect.colliderect(currentElement.rect):
#                 currentSlot = i
#                 break
#     return currentSlot
#
# def getBackToStartPosition():
#     global dropped
#     global currentElement
#     el=currentElement
#     print('going to start position')
#     screen.blit(bg, (0, 0))
#     sprites[el.ID].updateSprite(el.initialPosition)
#     #sprites[el.ID].xy = position
#     all_slots_list.draw(screen)
#     all_elements_list.draw(screen)
#     currentElement.lifted = False
#     dropped = False
#
# def putInSlot():
#     print('put in slot')
#     global dropped
#     global currentElement
#     global currentSlot
#     if currentSlot.full == False:
#         currentSlot.full = True
#         currentElement.slotId = currentSlot.ID
#         el = currentElement
#         screen.blit(bg, (0, 0))
#         sprites[el.ID].updateSprite(currentSlot.position)
#         # sprites[el.ID].xy = position
#         all_slots_list.draw(screen)
#         all_elements_list.draw(screen)
#         print()
#
#         currentElement.lifted = False
#         sprites[currentElement.ID] = None
#         slots[currentSlot.ID] = None
#         currentElement = None
#         currentSlot = None
#         dropped = False
#
#
#
# def drag():
#     global currentElement
#     el=currentElement
#     currentElement.lifted = True
#     if currentElement.slotId != -1:
#         slots[currentElement.slotId].full = False
#
#     tempRect = pygame.Rect(sprites[el.ID].getRect()[0], sprites[el.ID].getRect()[1], sprites[el.ID].image.get_rect()[2],
#                            sprites[el.ID].image.get_rect()[3])
#     position = [0, 0]
#     position[0] = round(pygame.mouse.get_pos()[0] - tempRect[0])  # / 200)
#     position[1] = round(pygame.mouse.get_pos()[1] - tempRect[1])  # / 200)
#     screen.blit(bg, (0, 0))
#     #screen.fill((255, 255, 0))
#     all_elements_list.move_to_front(sprites[el.ID])
#     sprites[el.ID].updateSprite(position)
#     sprites[el.ID].xy = position
#
#     all_slots_list.draw(screen)
#     all_elements_list.draw(screen)
#
#


running = True
while running:

    #getBackToStartPosition()

    # checkCollision()
    closeEventHandler()

    pygame.display.update()
    fpsClock.tick(FPS)