import pygame




pygame.init()


dpw=800
dph=600


black=(0,0,0)
white=(255,255,255)
red=(55,0,0)
bred=(255,0,0)
green=(0,55,0)
bgreen=(0,255,0)
blue=(0,0,255)
bblue=(27,196,255)


gd=pygame.display.set_mode((dpw,dph))
pygame.display.set_caption('new trial 002 ')

clock=pygame.time.Clock()
gd.fill(bblue)
#pygame.draw.rect(gd,blue,[x-r,y-r,r+r,r+r])

pygame.display.update()

def bal(xn,yn):
    
    pygame.draw.circle(gd,white,(xn,yn),25)
    pygame.display.update()
    #pygame.display.update()

def gml():
    
    
    g=0
    x=dpw-24
    y=300
    pygame.draw.circle(gd,white,(x,y),25)
    pygame.display.update()
    while g==0:
        mus=pygame.mouse.get_pos()
        print(mus)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      
        
        if x<27:
            for i in range(25,dpw-25):
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         pygame.quit()
                         quit() 
           
            
                a=i*i
                x=x+1
                gd.fill(bblue)
                bal(x,y)
                print(x,y)
                clock.tick(245)
        elif x>dpw-25:
            
            for j in range(25,dpw-25):
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         pygame.quit()
                         quit() 
                
                a=j*j
                x=x-1
                gd.fill(bblue)
                bal(x,y)
                #pygame.display.update()       
                clock.tick(245)

            
             
            
                  
            
gml()               
pygame.quit()
quit()
