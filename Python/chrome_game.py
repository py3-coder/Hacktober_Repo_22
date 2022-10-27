import pyautogui
import pyttsx3
import time
from PIL import Image,ImageGrab 

engine = pyttsx3.init('sapi5')
announce = engine.getProperty('voices')
engine.setProperty('voice',announce[0].id)


def press(key):
    pyautogui.keyDown(key)
    return

def speak(a):
    engine.say(a)
    engine.runAndWait()

def isCollide(data):
    # for trees
    for i in range(510, 550): #it increases the length
        for j in range(230, 255):#it increases the height
            if data[i, j] < 100:
                press("up")
                return

    for i in range(500, 511):
        for j in range(215, 230):
            if data[i, j] < 100:
                press("down")
                return

    return
    
if __name__ == '__main__':
    
    time.sleep(3)
    #speak("the game will start in 3 seconds")
    
    while True:
        
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        
        '''
        #for trees
        for i in range(520, 531): #it increases the length
            for j in range(233, 270):#it increases the height
                data[i, j] = 0
        
        #for birds
        for i in range(500, 511):
            for j in range(215, 233):
                data[i, j] = 150
            
        image.show()
        break
        '''
