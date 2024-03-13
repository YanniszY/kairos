# to-do list v1.0
# author Yvixx | https://github.com/YanniszY
# made in UA🇺🇦

import tkinter
import customtkinter
from customtkinter import *


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


app = customtkinter.CTk()
app.title("kairos")
app.geometry("1920x1080")


frame_1 = customtkinter.CTkFrame(master=app, width=250, height=100)
frame_1.pack(side=LEFT ,ipadx=100, ipady=100, padx=900, pady=300)
frame_1.pack(side=LEFT)




app.mainloop()