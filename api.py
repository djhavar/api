from tkinter import *
import requests 
import json

root=Tk()
root.overridedirect(True)
root.title("My Weather App")
root.geometry("600x300")
root.config(bg="black")

cnl=Label(root,text="city name",font=("Helvetica",16,'bold'),bg="black",fg="white")
cnl.place(relx=0.5,rely=0.15,anchor=CENTER)
ce=entry(root)
ce.place(relx=0.5,rely=0.35,anchor=CENTER)
wil=Label(root,font=("Helvetica",16),bg="black",fg="white")
cnl.place(relx=0.5,rely=0.38,anchor=CENTER)
wil=Label(root,font=("bold",16),bg="black",fg="white")
cnl.place(relx=0.5,rely=0.5,anchor=CENTER)

def cn():
    
api_request =requests.get("https://api.openweathermap.org/data/2.5/weather?q=
"+ce.get()+"&appid=2"+"1cab08deb7b27f4c2b55f3e2df28ea4
")