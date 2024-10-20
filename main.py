import tkinter
import customtkinter
from PIL import Image 

# System Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.title("Form")

# Define the window size
width = 480
height = 600
app.geometry(f"{width}x{height}")

# Calculate the position to center the window.
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

app.geometry(f"{width}x{height}+{x}+{y}")
app.maxsize(480, 600)
app.minsize(480, 600)

app.iconbitmap("./images/logo.ico")

# Functions
showing_password = False

def show_password():
    global showing_password
    showing_password = not showing_password 

    if showing_password:
        show_p.configure(image=eye_off) 
        password.configure(show='') 
        show_p.configure(text="Hide password")
    else:
        show_p.configure(image=eye)
        password.configure(show='*')
        show_p.configure(text="Show password")


# Part of the top
frame = customtkinter.CTkFrame(app, fg_color="transparent")
frame.pack(fill="both", expand="true", padx=20, pady=10)

title = customtkinter.CTkLabel(frame, text="Login", font=("Arial", 40, "bold"))
title.pack(side="top", pady="5")

# images
eye_off_image = Image.open("./images/eye-off.png")
eye_off = customtkinter.CTkImage(eye_off_image)

eye_image = Image.open("./images/eye.png")
eye = customtkinter.CTkImage(eye_image)

# input
inputs = customtkinter.CTkFrame(frame, fg_color="transparent")
inputs.pack(fill="both", expand="true", padx="10", pady="50")

name = customtkinter.CTkEntry(inputs, placeholder_text="Name", font=("Arial", 15), corner_radius=20)
name.pack(side="top", fill="x", pady="10")

email = customtkinter.CTkEntry(inputs, placeholder_text="Email", font=("Arial", 15), corner_radius=20)
email.pack(side="top", fill="x", pady="10")

password = customtkinter.CTkEntry(inputs, placeholder_text="Password", font=("Arial", 15), show="*", corner_radius=20)
password.pack(side="top", fill="x", pady="10")

# show password
show_p = customtkinter.CTkButton(inputs,text="Show password", image=eye, fg_color="transparent", compound="left", hover="false", command=show_password)
show_p.pack(side="top", anchor="w")

# Login button
login = customtkinter.CTkButton(inputs, text="Login", font=("Arial", 25, "bold"))
login.pack(side="top", fill="x",pady="30", padx="30")

# Run app
app.mainloop()
