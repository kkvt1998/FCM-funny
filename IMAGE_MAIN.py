from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.cluster.fcm import fcm
from pyclustering.utils import read_image, draw_image_mask_segments
import cv2
import numpy as np


def IMA():

    window = Toplevel()
    window.title("Phân cụm hình ảnh")

    lbl = Label(window, text = "Nhập giá trị cụm ").grid(row = 0, column = 0)
    c_input = StringVar()
    c = Entry(window, text = c_input).grid(row = 0, column = 1)
    def open():
        global my_image
        window.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select A file", filetypes=(("png files", "*.png"),("all files", "*.*")))
        my_label = Label(window, text=window.filename)
        my_label.grid(row = 1, column = 0)
        
        my_image = ImageTk.PhotoImage(Image.open(window.filename))
        my_image_label = Label(window,image = my_image)
        my_image_label.grid(row = 2, column = 0)
    
        
    def run():
        img = cv2.imread(window.filename)
        Z = img.reshape((-1,3))
        Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = int(c_input.get())
        ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((img.shape))

        cv2.imshow('Clustering images',res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
  
    
    btn = Button(window, text = "Tải hình ảnh",bg = "brown", fg = "yellow", command = open).grid(row =0, column = 4)
    btn1 = Button(window, text = "Chạy",bg = "green", fg = "yellow", command = run).grid(row =0, column =5)


    window.mainloop()