from tkinter import *
import speedtest
import threading


#Create a Fuction named Speed Test
def speedcheck():
    sp= speedtest.Speedtest()
    sp.get_servers()
    
    # Calculating speeds
    down=str(round(sp.download()/(10**6),2)) +" Mbps"
    up=str(round(sp.upload()/(10**6),2)) +" Mbps"
    
    # Updating labels
    lab_down.config(text=down)
    lab_up.config(text=up)


# Running the speedtest in a background thread prevents the GUI from freezing
def start_test_thread():
    thread = threading.Thread(target=speedcheck)
    thread.daemon = True        # Ensures thread closes if the app is closed (Very Important)
    thread.start()



#Creating TKinter GUI Interface

sp = Tk()
sp.title(" Internet Speed Test ")          # GUI Title
sp.geometry("500x500")                   # GUI Box Measurements
sp.config(bg="Blue")                    # GUI Box Background Color

# Title Label
lab=Label(sp, text=" Internet Speed Test ", font=("Sans Serif",19,"bold"),bg="white",fg="red")
lab.place(x=30,y=50,height=50,width=435)


# For Downloading Speed
lab=Label(sp, text="Downloading Speed", font=("Sans Serif",17,"bold"),bg="white",fg="red")
lab.place(x=30,y=130,height=50,width=435)

lab_down=Label(sp, text="00", font=("Sans Serif",17,"bold"),bg="white",fg="red")
lab_down.place(x=30,y=170,height=40,width=435)




#For Uploading Speed
lab=Label(sp, text="Uploading Speed", font=("Sans Serif",17,"bold"),bg="white",fg="red")
lab.place(x=30,y=230,height=50,width=435)

lab_up=Label(sp, text="00", font=("Sans Serif",17,"bold"),bg="white",fg="red")
lab_up.place(x=30,y=270,height=40,width=435)


# Creating Functioning Button And Remember To Call The Fuction in our Case its Speedcheck Thats Comprised in Thread**//

button=Button(sp,text="CHECK SPEED", font=("sans serif",30,"bold"),relief=RAISED,command=start_test_thread)
button.place(x=30,y=330,height=40,width=435)




sp.mainloop()