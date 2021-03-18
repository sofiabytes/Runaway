import random

#Move the opponents randomly
def box_update(lefty, righty, leftmove, rightmove):
    if lefty<=5:
        leftmove=random.randint(15, 25)
    elif lefty>=495:
        leftmove=random.randint(15, 25)-40
    if righty<=5:
        rightmove=random.randint(15, 25)
    elif righty>=495:
        rightmove=random.randint(15, 25)-40
    lefty=lefty+leftmove
    righty=righty+rightmove
    return lefty, righty, leftmove, rightmove

def laserres(leftlaser, rightlaser, leftlaserx, leftlasery, leftx, lefty, rightlaserx, rightlasery, rightx, righty, lasernoise):
    if leftlaser==False:    
        leftlaserx=leftx+40
        leftlasery=lefty+24
        leftlaser=True
        lasernoise.play()
    if rightlaser==False:
        rightlaserx=rightx
        rightlasery=righty+24
        rightlaser=True  
        lasernoise.play()			
    leftlaserx+=40
    rightlaserx-=40 
    if leftlaserx>800:
        leftlaser=False
    if rightlaserx<0:
        rightlaser=False
    return leftlaserx, leftlasery, rightlaserx, rightlasery, leftlaser, rightlaser

def dead(plives, rightlives, leftlives):
    game=True
    deathstr=""
    if plives==0:
        deathstr='You Deided!'
        game=False
    if rightlives==0:
        deathstr="Right enemy Died"
        game=False
    if leftlives==0:
        deathstr="left enemy Died!"
        game=False 
    return game, deathstr