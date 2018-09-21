import pygame 
import random

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

pygame.display.set_caption('BOUNCY  ')
ico=pygame.image.load("pon.png")
pygame.display.set_icon(ico)
paused=False

beat=pygame.mixer.Sound("p.wav")
a=open("x25.txt","w")
a.close
b=open("xdpw-25.txt","w")
b.close()
c=open("y25.txt","w")
c.close()
d=open("ydph-25.txt","w")
d.close()
clock=pygame.time.Clock()
bimg=pygame.image.load("bkj.png")

def qtg():
    pygame.quit()
    quit()
def cntin():
    global paused
    paused=False
def pause():
    
        
        txt=pygame.font.SysFont('bellmt',90)
        TextSurface,TextRect=text_objects("PAUSED",txt,bgreen)
        TextRect.center=((dpw/2),(dph/2))
        gd.blit(TextSurface,TextRect)
        pady=525

        while paused:
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                                quit()

                # btn(bx,by,bw,bh,txt,txcl,ic,ac,action):
                ##            mus=pygame.mouse.get_pos()
                ##            clk=pygame.mouse.get_pressed()
                btn(150,420,90,80,"CONTINUE",black,white,bgreen,cntin)
                btn(550,420,90,80,"QUIT",black,white,bred,qtg)
                pygame.draw.line(gd,bred,(0,pady),(dpw,pady))
                pygame.display.update()
                clock.tick(65)

        
       
   

def pad(xp,yp,wp,hp):
    pygame.draw.rect(gd,white,(xp,yp,wp,hp))
def mrk(cnt):
    
    font=pygame.font.SysFont('bellmt',21)
    text=font.render("SCORE: "+str(cnt), True,bblue)
    gd.blit(text,(0,0))
    s=open("his.txt","r")
    q=s.read()
    s.close()
    font=pygame.font.SysFont('bellmt',23)
    text=font.render("HI_SCORE: "+str(q), True,bblue)
    gd.blit(text,(0,20))
    int(cnt)
    int(q)
    if int(cnt)>int(q):
        s=open("his.txt","w")
        s.write(str(cnt))
        s.close()
        font=pygame.font.SysFont('bellmt',23)
        text=font.render("HI_SCORE: "+str(q), True,bblue)
        gd.blit(text,(0,20))
    
    

def ball(xn,yn):
    pygame.draw.circle(gd,white,(xn,yn),25)
def text_objects(text,font,color):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()  
def over():
    pady=525
    largeText=pygame.font.SysFont('bellmt',80)
    TextSurf,TextRect=text_objects('GAME OVER',largeText,bred)
    TextRect.center=((dpw/2),(150))
    gd.blit(TextSurf,TextRect)
   
    while True:
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        btn(150,450,95,40,"PLAY AGAIN",black,white,bgreen,gm)
        btn(550,450,90,40,"QUIT",black,white,bred,qtg)
        pygame.draw.line(gd,bred,(0,pady),(dpw,pady))
        pygame.display.update()
        clock.tick(60)
def btn(bx,by,bw,bh,txt,txcl,ic,ac,action):
    mus=pygame.mouse.get_pos()
    
    clk=pygame.mouse.get_pressed()
  
   
       
    if bx+bw>mus[0]>bx and by+bh>mus[1]>by :
      pygame.draw.rect(gd,ac,[bx,by,bw,bh])
      if clk[0]==1:
           action()
    else:
         pygame.draw.rect(gd,ic,[bx,by,bw,bh])
  
    stxt=pygame.font.SysFont('bellmt',22)
    TextSurf,TextRect=text_objects(txt,stxt,txcl)
    TextRect.center=(bx+(bw/2),by+(bh/2))
    gd.blit(TextSurf,TextRect)


def intro():
    intr=True
    #pxr=pygame.PixelArray(gd)
    
    while intr:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
        gd.fill(black)
        
##        xe=random.randrange(0,dpw)
##        ye=610
##        pxr[xe][ye]=white
##        ye=ye-10
        mus=pygame.mouse.get_pos()
        
##        xe=random.randrange(5,dpw-6)
##        ye=605
##        while ye>0:
##            gd.fill(black)
##            pygame.draw.circle(gd,white,(xe,ye),5)
##            gd.fill(black)
##            pygame.display.update()
##            
##            ye=ye-1
        txt=pygame.font.SysFont("broadway",120)
        TextSurf,TextRect=text_objects('BOUNCY',txt,white)
        TextRect.center=((dpw/2),(200))
        gd.blit(TextSurf,TextRect)
        txt=pygame.font.SysFont("calibri",15)
        TextSurf,TextRect=text_objects("Velocity of Ball INCREASE's Each Time When It hit the PADDLE ",txt,white)
        TextRect.center=((dpw/2),(350))
        gd.blit(TextSurf,TextRect)
        
        btn(150,450,90,80,"PLAY",black,white,bgreen,gm)
        btn(550,450,90,80,"quit",black,white,bred,qtg)
        xe=random.randrange(5,dpw-6)
        ye=605
        
        pygame.display.update()
        clock.tick(100)
                                
            
        



def gm():
    global paused
    x=random.randrange(200,550)
    y=random.randrange(150,450)
    padx=275
    pady=525
    padw=250
    padh=40
    pad(padx,pady,padw,padh)
    dirsx=-3
    dirsy=-1
    xcp=0
    cmr=0
    i=0
    ch=0
    gd.fill(black)
    ball(x,y)
    g=0
    
    while g==0:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        xcp=-5
                        
                    elif event.key==pygame.K_RIGHT:
                        xcp=5
                        
                    elif event.key==pygame.K_SPACE:
                        paused=True
                        pause()
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        xcp=0
                      
        x=x+dirsx
        y=y+dirsy
        padx=padx+xcp
        if padx<=0:
            padx=0
        if padx>=dpw-padw:
            padx=dpw-padw
        gd.blit(bimg,(0,0))
        mrk(cmr)
        pad(padx,pady,padw,padh)
        
        
        if x<25:
            print(x,y)
            a=open("x25.txt","a")
            a.write(str(x)+"  "+str(y)+"\n")
            a.close()
            dirsx=dirsx*-1
            i=1
        if x>dpw-25:
            print(x,y)
            b=open("xdpw-25.txt","a")
            b.write(str(x)+"   "+str(y)+"\n")
            b.close()
            dirsx=dirsx*-1
            i=2
        if y<25:
            print(x,y)
            c=open("y25.txt","a")
            c.write(str(x)+"   "+str(y)+"\n")
            c.close()
            dirsy=dirsy*-1
            
        if y+25>pady+3:
            if (padx-4<=x and padx+padw+5>=x):
                print(x,y)
                cmr=cmr+1
                pygame.mixer.Sound.play(beat)
                d=open("ydph-25.txt","a")
                d.write(str(x)+"   "+str(y)+"\n")
                d.close()
                dirsy=dirsy*-1
                dirsy=dirsy-1
                if i==1:
                    dirsx=dirsx+1
                elif i==2:
                    dirsx=dirsx-1
                
##            elif x+25==padx:
##                    dirsy=dirsy*-1
##                    dirsx=dirsx*-1
##                    dirsy=dirsy-1
##                    dirsx=dirsy-1
##            elif x-25==(padx+padw)+7:
##                    dirsy=dirsy*-1
##                    dirsx=dirsx*-1
##                    dirsy=dirsy-1
##                    dirsx=dirsx+1
            else:
                ball(x,y)
                over()
                    

  #           if y+26>pady+padh/2:
##                ball(x,y)
##                over()



            
                
                
                
        pygame.draw.line(gd,bred,(0,pady),(dpw,pady))
        btn(710,5,90,40,"QUIT!",white,black,bred,qtg)        
        ball(x,y)
        txt=pygame.font.SysFont("arial",12)
        TextSurf,TextRect=text_objects('<--- LEFT ARROW KEY',txt,white)
        TextRect.center=((250),(570))
        gd.blit(TextSurf,TextRect)
        txt=pygame.font.SysFont("arial",12)
        TextSurf,TextRect=text_objects('RIGHT ARROW KEY --->',txt,white)
        TextRect.center=((550),(570))
        gd.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(65)
     
               
intro()
gm()
pygame.quit()
quit()



















    
