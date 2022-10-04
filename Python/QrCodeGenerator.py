import time
import pyqrcode
import png
import threading

done=False
def load():
	j=0
	while True:
		if not done:
  	 	 b = "Processing" + "."*(j%4)+" "*(3-(j%4))
  	 	 print (b,end="\r")
  	 	 time.sleep(1)
		else:
			  break;
		j+=1
  
t = threading.Thread(target=load)
	  
str=input("Enter message to be encoded : ")

scl=int(input("Enter the scaling value( numerical value) : "))
url=pyqrcode.create(str)

t.start()

url.png('qr.png',scl)
done=True
print("QR code generated successfully !!!")

input("Press any key to EXIT---")
