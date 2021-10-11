import pygame
#define size of window
windowSize=(900,500)
win=pygame.display.set_mode(windowSize)

#set title on window
pygame.display.set_caption("Frog Game") 

#look in same folder as script for images
frog=pygame.image.load('frog.png')
pond=pygame.image.load('pond.png')

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)


def draw_window(frogInfo):
    blueBackground=(0, 255, 0) # red, green, blue tuple
    win.fill(blueBackground)

    #blit puts one image on another
    win.blit(pond, (700, 300))
    win.blit(frog, (frogInfo.x, frogInfo.y))
    if frogInfo.x > 700 and frogInfo.y >300:
        #print('You Win')
        msg= myfont.render('You Win', False, (0,0,0))
        
    else:
        msg= myfont.render('Move Frog to Pond(w,a,s,d)', False, (0,0,0))
    win.blit(msg, (200,50))
    pygame.display.update() #update the display


def main():
    #upper left corner of pygame window is (0,0)
    frogInfo = pygame.Rect(0,0, 50, 50)  #x,y,width,height

    run= True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('User quit game')
                run=False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: #a to go left
            frogInfo.x -= 1
        elif keys_pressed[pygame.K_d]: #d to go right
            frogInfo.x += 1
        elif keys_pressed[pygame.K_w]: #w to go up
            frogInfo.y -= 1
        elif keys_pressed[pygame.K_s]: #s to go down
            frogInfo.y += 1
                
        draw_window(frogInfo)        
                
    pygame.quit()

main()
    
