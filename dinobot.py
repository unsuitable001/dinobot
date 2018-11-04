import time
import cv2
import numpy as np
import mss
from pynput.keyboard import Key, Controller

keyboard = Controller()

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 130, "left": 420, "width": 90, "height": 115} #has to be tweaked as per your screen size and res. This worked fine for my monitor. details of my monitor is in github repo.
    #Defining the game sprite color properties
    lowerBound=np.array([0,0,83])
    upperBound=np.array([0,0,83])

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        #convert RGB to HSV
        imgHSV= cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
        #Create the mask
        mask=cv2.inRange(imgHSV,lowerBound,upperBound)
        #Filtering the mask - morphological operation
        kernelOpen=np.ones((5,5))
        kernelClose=np.ones((20,20))

        maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
        maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

        #Drawing contours
        _,conts,h=cv2.findContours(maskClose.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        if(len(conts)>1):
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        else:
            pass
            
        # Display the picture - just for debuging
        cv2.imshow("OpenCV/Numpy normal", img)

        #fps counter for nerds and number crunchers
        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break