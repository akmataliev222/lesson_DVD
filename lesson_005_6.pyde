
def setup():
    size(1000, 800)
    
names = ("ABU")

        
x = 0
y = 0        

speedX = 3
speedY = 3             

def draw():
    global names, x, y, speedX, speedY
    background(0)
    x = x + speedX
    y = y + speedY  
    textSize(35)
    text(names, 50 + x, 100 + y)
    ellipse(80 + x, 130 + y, 150, 40)
    
    if y > height - 150:
        speedY = -speedY
        fill(random(0,255), random(0,255), random(0,255))    
    if x > width - 150:
        speedX = -speedX
        fill(random(0,255), random(0,255), random(0,255))
    if y < 0 - 80:
       speedY = -speedY 
       fill(random(0,255), random(0,255), random(0,255))
    if x < 0 - 10:
       speedX = -speedX 
       fill(random(0,255), random(0,255), random(0,255))
    
