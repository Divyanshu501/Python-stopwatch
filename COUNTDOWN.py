# Importing all necessary library for the Project
import time
from tkinter import *
from tkinter import messagebox
 
# Creating background with title
Clock=Tk() 
Clock.geometry("400x300")
Clock.title("CountDown Timer")

# Declaring varible to store time value
hour=StringVar()
minute=StringVar()
second=StringVar()
# Creating class for performing all feature

class Count1:
    a=1 # Creating counter for reset
    b=0 # Creating counter for pause
    def reset(self):
        # Setting to reset value
        hour.set("00")
        minute.set("00")
        second.set("00")
        self.a+=1
        if self.b==1:
            self.b=0
            self.a+=1
        self.__init__()
        #  Method for pausing 
    def pause(self):
        self.b=1
          #  Method for resume
    def reume(self):
        self.b=0
        self.submit()
          # Construtor for setting default value
    def __init__(self):
            hour.set("00")
            minute.set("00")
            second.set("00")
            hourEntry= Entry(Clock, width=3, font=("Arial",24,""),
				textvariable=hour)
            hourEntry.place(x=110,y=20)
            minuteEntry= Entry(Clock, width=3, font=("Arial",24,""),
				textvariable=minute)
            minuteEntry.place(x=160,y=20)
            secondEntry= Entry(Clock, width=3, font=("Arial",24,""),
				textvariable=second)
            secondEntry.place(x=210,y=20)
            # Method for Countdown value 
    def submit(self):
        try:
		# the input provided by the user is
		# stored in here :temp
           
                temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while ((temp >-1)and (self.a%2!=0)and self.b==0):
            mins,secs = divmod(temp,60)

		# Converting the input entered in mins or secs to hours,
		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
		# 50min: 0sec)
            hours=0
            if mins >60:
			
			# divmod(firstvalue = temp//60, secondvalue
			# = temp%60)
                hours, mins = divmod(mins, 60)
		
		# using format () method to store the value up to
		# two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

		# updating the GUI window after decrementing the
		# temp value every time
            Clock.update()
            time.sleep(1)

		# when temp value = 0; then a messagebox pop's up
		# with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
		
		# after every one sec the value of temp will be decremented
		# by one
            temp -= 1
        if self.b==0 and (self.a%2==0):
            self.reset()
# Creating object for class for countdown.
excute=Count1() 
#Creating buttons and there comment
btn = Button(Clock, text='START', bd='5',
			command=excute.submit) #Creating buttons and there comment
btn1 = Button(Clock, text='RESET', bd='5',
			command=excute.reset)
btn2 = Button(Clock, text='PAUSE', bd='5',
			command=excute.pause)
btn3 = Button(Clock, text='RESUME', bd='5',
			command=excute.reume)
btn.place(x = 70,y = 130)
btn1.place(x = 70,y = 160)
btn2.place(x = 230,y = 130)
btn3.place(x = 230,y = 160)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
Clock.mainloop()
        
    