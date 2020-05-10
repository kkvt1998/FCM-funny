from __future__ import division, print_function
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import tkinter as tk
from fcmeans import FCM
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from seaborn import scatterplot as scatter


def Var():
    colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
    T2 = []

    app = Toplevel()
    app.title("Tạo bảng số liệu ")
    app.geometry("320x140")
    app.configure(bg="gray")

    lbl1 = Label(app, text = "Nhập m",width = 20, height = 1, bg = "blue", fg ="white").grid(row = 0, column = 0)
    lbl2 = Label(app, text = "Nhập n",width = 20, height = 1, bg = "blue", fg ="white").grid(row = 1, column = 0)
    lbl3 = Label(app, text = "Nhập số cụm ",width = 20, height = 1, bg = "blue", fg ="white").grid(row = 2, column = 0)

    e1_m = StringVar()
    e2_n = StringVar()
    e3_a = StringVar()
    

    e1=Entry(app, text = e1_m).grid(row = 0, column = 1)
    e2=Entry(app, text = e2_n).grid(row = 1, column = 1)
    e3=Entry(app, text = e3_a).grid(row = 2, column = 1)

    def create():
        root = Toplevel()
        root.title("Nhập số liệu")
        m = int(e1_m.get())
        n = int(e2_n.get())
        a = int(e3_a.get())
    
        class SimpleTableInput(tk.Frame):
            def __init__(self, parent, rows, columns):
                tk.Frame.__init__(self, parent)
                self._entry = {}
                self.rows = rows
                self.columns = columns

        # register a command to use for validation
                vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
                for row in range(self.rows):
                    for column in range(self.columns):
                        index = (row, column)
                        e = tk.Entry(self, validate="key", validatecommand=vcmd)
                        e.grid(row=row, column=column, stick="w")
                        self._entry[index] = e
        # adjust column weights so they all expand equally
                for column in range(self.columns):
                    self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
                self.grid_rowconfigure(rows, weight=1)

            def get(self):
                global result

                result = []
                for row in range(self.rows):
                    current_row = []
                    for column in range(self.columns):
                        index = (row, column)
                        current_row.append(self._entry[index].get())
                    result.append(current_row)
                return result

            def _validate(self, P):

                if P.strip() == "":
                    return True

                try:
                    f = float(P)
                except ValueError:              
                    self.bell()
                    return False
                return True

        class Example(tk.Frame):
            def __init__(self, parent):
                tk.Frame.__init__(self, parent)
                self.table = SimpleTableInput(self, m, n)
                self.submit = tk.Button(self, text="Phân cụm", command=self.on_submit)
                self.table.pack(side="top", fill="both", expand=True)
                self.submit.pack(side="bottom")

            def on_submit(self):
                print(self.table.get())
                T2 = [list(map(int, x)) for x in result]
                print(T2)
     
                n_samples = 500
                n_bins = 4  # use 3 bins for calibration_curve as we have 3 clusters here
                centers = T2

                X,_ = make_blobs(n_samples=n_samples, n_features=2, cluster_std=1.0,
                     centers=centers, shuffle=False, random_state=42)

# fit the fuzzy-c-means
                fcm = FCM(n_clusters=a)
                fcm.fit(X)

# outputs
                fcm_centers = fcm.centers
                fcm_labels  = fcm.u.argmax(axis=1)


# plot result

                f, axes = plt.subplots(1, 2, figsize=(11,5))
                scatter(X[:,0], X[:,1], ax=axes[0])
                scatter(X[:,0], X[:,1], ax=axes[1], hue=fcm_labels)
                scatter(fcm_centers[:,0], fcm_centers[:,1], ax=axes[1],marker="D",s=200)

                plt.show()
            
        Example(root).pack(side="top", fill="both", expand=True)
        root.mainloop()
    btn = Button(app, text = "Tạo bảng",bg = "green",fg="yellow", command = create).grid(row = 4, column = 0)

    app.mainloop()