from psychopy import visual, event, core
import random
import math
file = open("D:\Text.txt","a")
win = visual.Window(units='pix',size=(1920, 1080),fullscr=1, color='black')
win.mouseVisible=False
for j in range (24):
 d0=(j+1)*165 #pseudo random for std degree (165=180-sampling interval)
 while d0>270:
       d0=d0-360
 while d0<=-90:
       d0=d0+360
 file.write(str(d0-90)+'\n')
 r0=math.radians(d0)
 limit=0.8 #time duration
 g=7050
 h=0.5*g
 list=[[300,2820],[300,2820],[300,2820],[300,2820],[300,2820],[-300,2820],[-300,2820],[-300,2820],[-300,2820],[-300,2820]]
 #initial vx and vy list
 random.shuffle(list) 
 for i in range (10):
  d1=random.randint(-180,180) #randomrize initial calibration degree
  r1=math.radians(d1)
  polygon = visual.ShapeStim(win=win,size=15,vertices='circle',lineColor=(0,255,255),fillColor=(0,255,255))
  #stimuli defination
  border = visual.ShapeStim(win=win,size=1000,vertices='circle',lineColor=(255,0,255))
  polygon0= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[0,0],lineColor=(255,0,255),fillColor=(255,0,255))
  #center defination
  polygon1= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[500*math.cos(r1),500*math.sin(r1)],lineColor=(255,0,255),fillColor=(255,0,255))
  #calibration defination
  end= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[list[i][0]*limit*math.cos(r0)-(list[i][1]*limit-h*limit**2)*math.sin(r0)-list[i][0]*list[i][1]*math.cos(r0)/g+150*math.sin(r0),
     list[i][0]*limit*math.sin(r0)+(list[i][1]*limit-h*limit**2)*math.cos(r0)-list[i][0]*list[i][1]*math.sin(r0)/g-150*math.cos(r0)],
     lineColor=(0,255,255),fillColor=(0,255,255))
  timer = core.CountdownTimer(0.82)
  #0.01s extension preventing illusion effect
  #stimuli loop start
  while 0.82-timer.getTime()>0:
    t=0.81-timer.getTime()
    border.draw()
    polygon0.draw()
    polygon1.draw()
    #response control flow start
    if event.getKeys('escape'):
     win.close()
     file.write('\n')
    if event.mouseWheelRel[1]<0:
      d1=d1-1
      r1=math.radians(d1)
      polygon1.pos=(500*math.cos(r1),500*math.sin(r1))
      event.mouseWheelRel[1]=0
    if event.mouseWheelRel[1]>0:
      d1=d1+1
      r1=math.radians(d1)
      polygon1.pos=(500*math.cos(r1),500*math.sin(r1))
      event.mouseWheelRel[1]=0
    if event.mouseButtons[0]==1:
      event.mouseButtons[0]=0
      while d1-d0>90:
       d1=d1-360
      while d1-d0<-270:
       d1=d1+360
      #metric degrees conversion
      file.write(str(d1)+',')
      break
    #response control flow end
    if 0>t:
     polygon.pos = (-list[i][0]*list[i][1]*math.cos(r0)/g+150*math.sin(r0),-list[i][0]*list[i][1]*math.sin(r0)/g-150*math.cos(r0))
     polygon.draw()
    if 0<t<limit:
     polygon.pos = (list[i][0]*t*math.cos(r0)-(list[i][1]*t-h*t**2)*math.sin(r0)-list[i][0]*list[i][1]*math.cos(r0)/g+150*math.sin(r0),
     list[i][0]*t*math.sin(r0)+(list[i][1]*t-h*t**2)*math.cos(r0)-list[i][0]*list[i][1]*math.sin(r0)/g-150*math.cos(r0))
     polygon.draw()
    if 0.81>t>limit:
     end.draw()
    win.flip()
  #stimuli loop end
 file.write('\n') #new line for next std degree
win.close()
core.quit()
