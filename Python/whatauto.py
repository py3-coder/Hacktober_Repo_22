import webbrowser
#import pywhatkit
import pyautogui
import time

person_name=input("enter name")
my_msg=input("enter message")

webbrowser.open('https://web.whatsapp.com/')

time.sleep(10)
print(pyautogui.position())

pyautogui.click(187,187)
pyautogui.typewrite(person_name)

time.sleep(10)

pyautogui.click(163,319)

time.sleep(5)

pyautogui.typewrite(my_msg)

time.sleep(2)

pyautogui.click(1332,692)
#pywhatkit.sendwhatmsg("+91 99611 72845","Aron automatic msg",20,34)