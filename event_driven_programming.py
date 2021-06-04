#Event driven programming handles one event at a time, in the order the events occur.
#Event handlers should execute as quickly as possible to avoid making other events wait.

import tkinter #built-in module to create GUI (graphical user interface)
import time

#event handler : code that is executed when an event occurs
#handler for timer event (do sth when the timer goes off)
def alarm ():
    print('calling pizza company')

#handler for ringing doorbell (do sth when the doorbell rings)
def doorbell():
    print('ding dong')
    time.sleep(4) #add a delay of 4s. after door bell rings, wait for 4s before opneing the door
    print('opening the door') #before opening the door.
   

#handler for when the phone rings (do sth when the phone rings)
def phonecall():
    print('answering the phone')

#create buttons and assign callbacks
root = tkinter.Tk() #creates a new GUI window named root
#create 2 buttons inside the root window :
tkinter.Button(root,text='ring doorbell', command = doorbell).pack()
tkinter.Button(root,text='call phone', command = phonecall).pack()

#set a timer for 4s
root.after(4000,alarm) #when alarm function is called, it will be executed after 4000 ms

#kickstart the tkinter module
root.mainloop()
