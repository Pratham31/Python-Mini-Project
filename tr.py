from tkinter import *
from PIL import Image,ImageTk
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import tkinter.messagebox as tmsg

prath_root = Tk()

prath_root.geometry("844x890")
prath_root.title("CROP PREDICTION")
prath_root.maxsize(1280,768)

heading = Label(prath_root, text="Welcome!!!\nLets Help FOOD PROVIDER", font=("cooper black",40,"bold"), fg="steelblue").pack() 

def nat():
    print("LETS SEE NATURAL RESOURCES>>>")
    if (searchTerm.get()=="rice"):
        slices=[14,17]
        activities=['Hot Weather','Water']
        cols=['orange','blue']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
        plt.title("Natural Resource Requirements")
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="wheat"):
        slices=[17,10]
        activities=['Warm Climate','Cold Climate']
        cols=['orange','blue']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
        plt.title("Natural Resource Requirements")
        plt.legend()
        plt.show()

    elif(searchTerm.get()=="tea"):
        slices=[10,19]
        activities=['Sloppy Area','High Rainfall']
        cols=['brown','blue']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
        plt.title("Natural Resource Requirements")
        plt.legend()
        plt.show()

    elif(searchTerm.get()=="sugarcane"):
        slices=[14,17]
        activities=['Hot Weather','Water']
        cols=['orange','blue']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
        plt.title("Natural Resource Requirements")
        plt.legend()
        plt.show()

    elif(searchTerm.get()=="cotton"):
        slices=[17,10]
        activities=['Hot Weather','Water']
        cols=['orange','blue']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
        plt.title("Natural Resource Requirements")
        plt.legend()
        plt.show()

    elif(searchTerm.get()=="coffee"):
        slices=[17,10]
        activities=['Two-Tier shade','Sea-Level']
        cols=['grey','blue']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
        plt.title("Natural Resource Requirements")
        plt.legend()
        plt.show()

    else:
        tmsg.showinfo("Natural Resources","Sorry..We don't have required crop,will add soon :)")

def av():
    print("\nAverage Rainfall Plotting..")
    if (searchTerm.get()=="rice"):
        plt.title('Average Rainfall for RICE')
        plt.ylabel('Rainfall in mm')
        plt.xlabel('MONTHS')
        gas=pd.read_csv('newr.csv')
        plt.plot(gas.month, gas.rice,'b.-')
        plt.show()
        
    elif(searchTerm.get()=="wheat"):
        plt.title('Average Rainfall for WHEAT')
        plt.ylabel('Rainfall in mm')
        plt.xlabel('MONTHS')
        gas=pd.read_csv('newr.csv')
        plt.plot(gas.month,gas.wheat,'r.-')
        plt.show()
        
    elif(searchTerm.get()=="tea"):
        plt.title('Average Rainfall for TEA')
        plt.ylabel('Rainfall in mm')
        plt.xlabel('MONTHS')
        gas=pd.read_csv('newr.csv')
        plt.plot(gas.month,gas.tea,'g.-')
        plt.show()
        
    elif(searchTerm.get()=="sugarcane"):
        plt.title('Average Rainfall for SUGARCANE')
        plt.ylabel('Rainfall in mm')
        plt.xlabel('MONTHS')
        gas=pd.read_csv('newr.csv')
        plt.plot(gas.month,gas.sugarcane,'y.-')
        plt.show()
        
    elif(searchTerm.get()=="cotton"):
        plt.title('Average Rainfall for COTTON')
        plt.ylabel('Rainfall in mm')
        plt.xlabel('MONTHS')
        gas=pd.read_csv('newr.csv')
        plt.plot(gas.month,gas.cotton,'o.-')
        plt.show()
        
    elif(searchTerm.get()=="coffee"):
        plt.title('Average Rainfall for COFFEE')
        plt.ylabel('Rainfall in mm')
        plt.xlabel('MONTHS')
        gas=pd.read_csv('newr.csv')
        plt.plot(gas.month,gas.coffee,'y.-')
        plt.show()
        
    else:
        tmsg.showinfo("Avg. Rainfall","Sorry..We don't have data for required crop,will add soon :)")    


def see():
    print("\nSowing Crop Plotiing..")
    if (searchTerm.get()=="rice"):
        plt.title('Sowding Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.sr,label="Possibility")
        #plt.hist(gas.sr)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="wheat"):
        plt.title('Sowing Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.sw,label="Possibility")
        #plt.hist(gas.sw)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="tea"):
        plt.title('Sowing Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.st,label="Possibility")
        #plt.hist(gas.st)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="sugarcane"):
        plt.title('Sowing Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.ss,label="Possibility")
        #plt.hist(gas.ss)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="cotton"):
        plt.title('Sowing Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.scot,label="Possibility")
        #plt.hist(gas.scot)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="coffee"):
        plt.title('Sowing Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.sc,label="Possibility")
        #plt.hist(gas.sc)
        plt.legend()
        plt.show()
        
    else:
        tmsg.showinfo("Sowing Crop","Sorry..We don't have data for required crop,will add soon :)")        

def har():
    print("\nHarvesting Crop Plotting..")
    if (searchTerm.get()=="rice"):
        plt.title('Harvesting Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.hr,label="Possibility")
        #plt.hist(gas.hr)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="wheat"):
        plt.title('Harvesting Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.hw,label="Possibility",color="green")
        #plt.hist(gas.hw)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="tea"):
        plt.title('Harvesting Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.ht,label="Possibility",color="brown")
        #plt.hist(gas.ht)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="sugarcane"):
        plt.title('Harvesting Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.hs,label="Possibility",color="grey")
        #plt.hist(gas.hs)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="cotton"):
        plt.title('Harvesting Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.hcot,label="Possibility",color="orange")
        #plt.hist(gas.hcot)
        plt.legend()
        plt.show()
        
    elif(searchTerm.get()=="coffee"):
        plt.title('Harvesting Crop Period')
        plt.ylabel('Possibility')
        plt.xlabel('Months')
        gas=pd.read_csv('newsh.csv')
        plt.bar(gas.month,gas.hc,label="Possibility",color="red")
        #plt.hist(gas.hc)
        plt.legend()
        plt.show()
        
    else:
        tmsg.showinfo("Harvesting Crop","Sorry..We don't have data for required crop,will add soon :)")        


def sta():
    if (searchTerm.get()=="rice"):
        slices=[19,12,6,3]
        activities=['West Bengal','Orissa','Haryana','Tamil Nadu']
        cols=['yellow','blue','red','orange']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0,0,0.1),autopct='%1.1f%%')
        plt.title("Highest Producing States")
        plt.legend()
        plt.show()
    
    elif (searchTerm.get()=="wheat"):
        slices=[19,12,6,2]
        activities=['Uttar Pradesh','Bihar','Maharastra','West Bengal']
        cols=['yellow','blue','red','orange']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0,0,0.1),autopct='%1.1f%%')
        plt.title("Highest Producing States")
        plt.legend()
        plt.show()
    
    elif (searchTerm.get()=="tea"):
        slices=[20,18,4,3]
        activities=['Assam','Meghalaya','Kerala','Tamil Nadu']
        cols=['yellow','blue','red','orange']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0,0,0.1),autopct='%1.1f%%')
        plt.title("Highest Producing States")
        plt.legend()
        plt.show()
    
    elif (searchTerm.get()=="sugarcane"):
        slices=[29,22,16,5]
        activities=['Uttar Pradesh','Maharastra','Kerala','Punjab']
        cols=['yellow','blue','red','orange']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0,0,0.1),autopct='%1.1f%%')
        plt.title("Highest Producing States")
        plt.legend()
        plt.show()
    
    elif (searchTerm.get()=="cotton"):
        slices=[30,18,11,5]
        activities=['Gujarat','Maharastra','Andhra Pradesh','Tamil Nadu']
        cols=['yellow','red','blue','orange']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0,0,0.1),autopct='%1.1f%%')
        plt.title("Highest Producing States")
        plt.legend()
        plt.show()
    
    elif (searchTerm.get()=="coffee"):
        slices=[5,3,9,19]
        activities=['Assam','Meghalaya','Kerala','Karnataka']
        cols=['yellow','blue','red','orange']
        plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0.1,0,0),autopct='%1.1f%%')
        plt.title("Highest Producing States")
        plt.legend()
        plt.show()
    
    else:
        tmsg.showinfo("States","Sorry..We don't have data for required crop,will add soon :)")    
        

        
label2 = Label(prath_root, text="To those who works in ACRES not in HOURS ", font=("arial",40,"bold"), fg="black").pack()
label1 = Label(prath_root, text="\nEnter the Crop to Analyze ", font=("arial",20,"bold"), fg="black").place(x=30,y=200)

searchTerm = StringVar()
entry_box = Entry(prath_root, textvariable=searchTerm, width=30, bg="lightgreen").place(x=400,y=240)

work = Button(text="Sowing Crop",width=22,height=5,bg="black",fg="white",command=see).place(x=310,y=300)
work1 = Button(text="Avg. Rainfall",width=22,height=5,bg="black",fg="white",command=av).place(x=160,y=300)
work2 = Button(text="Natural Resources",width=22,height=5,bg="black",fg="white",command=nat).place(x=10,y=300)
work3 = Button(text="Harvesting Crop",width=22,height=5,bg="black",fg="white",command=har).place(x=460,y=300)
work4 = Button(text="States",width=22,height=5,bg="black",fg="white",command=sta).place(x=610,y=300)
image=Image.open("qw.jpg")
photoe=ImageTk.PhotoImage(image)

varl_label=Label(image=photoe)
varl_label.pack(side=RIGHT,anchor="se")


image=Image.open("xx.jpg")
photow=ImageTk.PhotoImage(image)

varw_label=Label(image=photow)
varw_label.pack(side=RIGHT,padx=10,anchor="se")

image=Image.open("vv.jpg")
photov=ImageTk.PhotoImage(image)

varv_label=Label(image=photov)
varv_label.pack(side=RIGHT,padx=1,anchor="se")


image=Image.open("aa.jpg")
photol=ImageTk.PhotoImage(image)

varl_label=Label(image=photol)
varl_label.pack(side=RIGHT,padx=9,anchor="se")

image=Image.open("uu.jpg")
photoo=ImageTk.PhotoImage(image)

varo_label=Label(image=photoo)
varo_label.pack(side=LEFT,anchor="sw")
prath_root.mainloop()