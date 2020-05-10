from tkinter import *
from LOAD_DATA.VARIABLE import *
from LOAD_IMAGE.IMAGE_MAIN import *
from file_path_manager import FilePathManager
from PIL import ImageTk,Image
import cv2
from EXCel.aircraft import *

fcm = Tk()
fcm.title("Phần mềm phân cụm - H2D")
fcm.geometry("500x340")
fcm.configure(bg = "skyblue")

my_menu = Menu(fcm,tearoff = 0 )
fcm.config(menu=my_menu)
#
file_menu = Menu(my_menu,tearoff = 0)
my_menu.add_cascade(label = "Phân cụm ", menu = file_menu)
file_menu.add_command(label = "Phân cụm hình ảnh", command = IMA)
file_menu.add_command(label = "Phân cụm số", command = Var)
file_menu.add_command(label = "Phân cụm dữ liệu excel", command = Ex)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = fcm.quit)
#
help_menu = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label ="Information")

fcm.mainloop()