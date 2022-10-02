from tkinter import*
from tkinter.font import BOLD
import time

root = Tk()
root.title('Digi Clock')
root.geometry('1350x700+5+5')
root.config(bg='#0D1117')


def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))

    if int(h)>int(12):
        h = str(int(h)//12)
        lbl_noon.config(text='PM')
        lbl_noon2.config(text='Noon')
    
    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    lbl_hr.after(200,clock)


#hours

lbl_hr = Label(root,text='12',font=("times new roman",50,"bold"),bg="#0faada",fg='white')
lbl_hr.place(x=350,y=200,width=150,height=150)

lbl_hr2 = Label(root,text='Hours',font=("Comic Sans MS",20,"bold"),bg="#0faada",fg='white')
lbl_hr2.place(x=350,y=360,width=150,height=50)

#mins

lbl_min = Label(root,text='12',font=("times new roman",50,"bold"),bg="#CA4959",fg='white')
lbl_min.place(x=530,y=200,width=150,height=150)

lbl_min2 = Label(root,text='Minutes',font=("Comic Sans MS",20,"bold"),bg="#CA4959",fg='white')
lbl_min2.place(x=530,y=360,width=150,height=50)

#sec

lbl_sec = Label(root,text='12',font=("times new roman",50,"bold"),bg="#D98F43",fg='white')
lbl_sec.place(x=710,y=200,width=150,height=150)

lbl_sec2 = Label(root,text='Seconds',font=("Comic Sans MS",20,"bold"),bg="#D98F43",fg='white')
lbl_sec2.place(x=710,y=360,width=150,height=50)

# noon

lbl_noon = Label(root,text='AM',font=("Comic Sans MS",50),bg="#0DAC72",fg='white')
lbl_noon.place(x=890,y=200,width=150,height=150)

lbl_noon2 = Label(root,text='Morning',font=("Comic Sans MS",20,"bold"),bg="#0DAC72",fg='white')
lbl_noon2.place(x=890,y=360,width=150,height=50)

clock()

root.mainloop()