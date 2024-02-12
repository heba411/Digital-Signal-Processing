import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from comparesignal2 import SignalSamplesAreEqual2


class Task5:
    def __init__(self, frame):
        self.frame = frame
        self.numCoeff = tk.Entry(frame, width=40)
        self.figure = plt.figure()
        self.canvas = None
        self.signal = []

    def browse_signal(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                for i in range(3):
                    next(file)
                self.signal = [line.strip().split() for line in file]

    def DCT(self):
        if self.signal:
            X = [float(row[0]) for row in self.signal]
            Y = [float(row[1]) for row in self.signal]

            N = len(self.signal)
            result = np.zeros(N)

            for k in range(N):
                result[k] = np.sqrt(2 / N) * np.sum(
                    Y * np.cos(np.pi / (4 * N) * (2 * np.arange(N) - 1) * (2 * k - 1)))

            m = int(self.numCoeff.get())

            with open("DCT_Output.txt", 'w') as file:
                file.write("0\n")
                file.write("1\n")
                file.write("%s\n" % m)
                for i in range(m):
                    # file.write("%s" % X[i])
                    # file.write(" ")
                    file.write("%s\n" % result[i])


            self.show_signal(X, result)
            print(result)
            SignalSamplesAreEqual2("D:/Materials_4th/DSP/Labs/Lab 5/Task files/DCT/DCT_output.txt",result)

    def Remove_DC(self):
        if self.signal:
            X = [float(row[0]) for row in self.signal]
            Y = [float(row[1]) for row in self.signal]

            N = len(self.signal)
            after_removal = np.zeros(N)

            avg = np.mean(Y)
            for i in range(N):
                after_removal[i] = Y[i] - avg

            self.show_signal(X, after_removal)
            print(after_removal)
            SignalSamplesAreEqual2("D:/Materials_4th/DSP/Labs/Lab 5/Task files/Remove DC component/DC_component_output.txt",after_removal)


    def show_signal(self, X, Y):
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
            self.canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True, padx=10, pady=10)
            self.canvas.get_tk_widget().config(width=500, height=300)
        else:
            self.figure.clear()

        cont_plot = self.figure.add_subplot(121)
        cont_plot.plot(X, Y)  # Continuous
        cont_plot.set_title("Continuous Signal")
        cont_plot.grid(True)

        discr_plot = self.figure.add_subplot(122)
        discr_plot.stem(X, Y, use_line_collection=True)
        discr_plot.set_title("Discrete Signal")

        self.canvas.draw()


