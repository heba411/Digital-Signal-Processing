import matplotlib.pyplot as plt
from tkinter import filedialog
import numpy as np
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from CompareSignal import Compare_Signals
from ConvTest import ConvTest


class Task9:
    def __init__(self, frame):
        self.frame = frame
        self.figure = plt.figure()
        self.canvas = None
        self.signal1 = []
        self.signal2 = []

    def browse_signal1(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                for i in range(3):
                    next(file)
                self.signal1 = [line.strip().split() for line in file]

    def browse_signal2(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                for i in range(3):
                    next(file)
                self.signal2 = [line.strip().split() for line in file]

    def dft(self,x, sign, factor):
        N = len(x)
        X = np.array([])
        for k in range(0, N):
            Xk = np.complex(0, 0)
            for n in range(0, N):
                exp = np.exp(sign * 2 * math.pi * k * n * 1j / N)
                Xk += np.complex(x[n]) * exp
            X = np.append(X, [factor * Xk])
        return X


    def fast_convolution(self):
        X1 = [int(row[0]) for row in self.signal1]
        Y1 = [int(row[1]) for row in self.signal1]
        X2 = [int(row[0]) for row in self.signal2]
        Y2 = [int(row[1]) for row in self.signal2]
        size = len(X1) + len(X2) - 1
        num_zeros1 = size - len(X1)
        Y1 = Y1 + [0] * num_zeros1

        num_zeros2 = size - len(X2)
        Y2 = Y2 + [0] * num_zeros2

        Y1DFT = self.dft(Y1, -1, 1)
        Y2DFT = self.dft(Y2, -1, 1)

        result = Y1DFT * Y2DFT
        conv_result = self.dft(result, 1, 1 / size)
        conv_result = [round(x) for x in conv_result.real]

        X_result = []
        for i in range(X1[0] + X2[0], X1[-1] + X2[-1] + 1):
            X_result.append(i)

        # print(conv_result)
        # print(X_result)
        ConvTest(X_result,conv_result)
        self.show_signal(X_result,conv_result,"Fast Convolution")

    def fast_correlation(self):
        X1 = [int(row[0]) for row in self.signal1]
        Y1 = [int(row[1]) for row in self.signal1]
        X2 = [int(row[0]) for row in self.signal2]
        Y2 = [int(row[1]) for row in self.signal2]

        Y1DFT = self.dft(Y1, -1, 1)
        Y2DFT = self.dft(Y2, -1, 1)

        Y1DFT = np.conjugate(Y1DFT)

        res = Y1DFT * Y2DFT
        corr_result = self.dft(res, 1, 1 / len(res))
        corr_result = [round(x) / len(X1) for x in corr_result.real]
        print(corr_result)
        Compare_Signals("D:/Materials_4th/DSP/Labs/Lab 9/Practical Task/Task Files/Fast Correlation/Corr_Output.txt",X1,corr_result)
        self.show_signal(X1,corr_result,"Fast Correlation")


    def show_signal(self, X, Y, title):
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
            self.canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True, padx=10, pady=10)
            self.canvas.get_tk_widget().config(width=500, height=300)
        else:
            self.figure.clear()

        first_plot = self.figure.add_subplot(111)
        first_plot.plot(X, Y)
        first_plot.set_title(title)
        first_plot.grid(True)
        self.canvas.draw()