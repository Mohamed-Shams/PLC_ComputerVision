import tkinter as tk
from tkinter import ttk
import webbrowser

# Function to open a Python script using OpenCV
def open_cv():
    # Replace 'your_opencv_script.py' with the actual filename
    # and path of your OpenCV script.
    import subprocess
    subprocess.Popen(["python", "HandTrackingModule.py"])

# Function to open IIOT webpage
def open_iiot():
    # Replace 'http://your_node_red_webpage.com' with the actual URL
    # of your Node-RED webpage.
    url = 'http://127.0.0.1:1880/ui/#!/0?socketid=keNK5QyB_AjIWVHKAAD1'
    webbrowser.open(url)

# Function to go back to the main menu
def back_to_menu():
    frame_main_menu.tkraise()

# Function to open the Local Control page
def open_local_control():
    frame_local_control.tkraise()

# Function to control elevator based on the button clicked
def elevator_control(elevator_number):
    # Replace this function with your elevator control logic.
    print(f"Elevator {elevator_number} is selected.")

# Create the main window
root = tk.Tk()
root.title("GUI with Gradient Background")

# Create a style for the background gradient
style = ttk.Style()
style.configure("TFrame", background="linear-gradient(300deg, #967643, #271f12, #15110a, #000000)")

# Create a frame with the gradient background for the main menu
frame_main_menu = ttk.Frame(root, style="TFrame")
frame_main_menu.place(relwidth=1, relheight=1)

# Create a frame with the gradient background for the Local Control page
frame_local_control = ttk.Frame(root, style="TFrame")

# Create buttons with text for the main menu
open_cv_button = ttk.Button(frame_main_menu, text="Open CV", command=open_cv)
open_cv_button.place(relx=0.1, rely=0.2)

open_iiot_button = ttk.Button(frame_main_menu, text="Open IIOT", command=open_iiot)
open_iiot_button.place(relx=0.4, rely=0.2)

local_control_button = ttk.Button(frame_main_menu, text="Local Control", command=open_local_control)
local_control_button.place(relx=0.7, rely=0.2)

# Create elevator buttons and back/exit buttons for the Local Control page
elevator_buttons = []
for i in range(1, 7):
    elevator_button = ttk.Button(frame_local_control, text=f"Elevator {i}", command=lambda i=i: elevator_control(i))
    elevator_buttons.append(elevator_button)

back_button = ttk.Button(frame_local_control, text="Back to Main Menu", command=back_to_menu)
exit_button = ttk.Button(frame_local_control, text="Exit", command=root.destroy)

# Place the elevator buttons and other buttons on the Local Control page
for i, button in enumerate(elevator_buttons):
    button.place(relx=0.1, rely=0.1 + i * 0.1)

back_button.place(relx=0.1, rely=0.8)
exit_button.place(relx=0.4, rely=0.8)

# Raise the main menu frame initially
frame_main_menu.tkraise()

# Start the main loop
root.mainloop()
