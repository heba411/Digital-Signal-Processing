import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import filedialog, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Shift_Fold_Signal import Shift_Fold_Signal
from comparesignals import SignalSamplesAreEqual1
from comparesignal2 import SignalSamplesAreEqual2

class Task6:
    def __init__(self, frame):
        self.frame = frame
        self.windowSize = tk.Entry(frame, width=40)
        self.constK = tk.Entry(frame, width=40)
        self.win_label = tk.Label(frame, text="Enter The Window Size",width=37, font=("Bold", 11))
        self.const_label = tk.Label(frame, text="Enter The Number Of Steps",width=37, font=("Bold", 11))
        self.show_button = tk.Button(frame, text="Show", command=self.done,width=26,font=("Bold",11),fg="white",bg="#31B587")
        self.combo_box = ttk.Combobox(frame,width=37,height=30)
        self.combo_box['values'] = ('smoothing', 'sharpening','shift by k','folding','shift folded','remove dc')
        self.selected_operation = None
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

    def show_signal(self, X1, Y1,title1,X2,Y2,title2):
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
            self.canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True, padx=10, pady=10)
            self.canvas.get_tk_widget().config(width=500, height=300)
        else:
            self.figure.clear()

        first_plot = self.figure.add_subplot(121)
        first_plot.plot(X1, Y1)
        first_plot.set_title(title1)
        first_plot.grid(True)

        second_plot = self.figure.add_subplot(122)
        second_plot.plot(X2, Y2)
        second_plot.set_title(title2)
        second_plot.grid(True)

        self.canvas.draw()

    def smoothing(self):
        if self.signal:
            X = [float(row[0]) for row in self.signal]
            Y = [float(row[1]) for row in self.signal]

            moving_avg = []
            window_size = int(self.windowSize.get())
            for i in range(window_size - 1, len(Y)):
                average = sum(Y[i - window_size + 1:i + 1]) / window_size
                moving_avg.append(average)       #its size = N - window size + 1
            indices = list(range(len(moving_avg)))
            self.show_signal(X, Y, "Before Smoothing",indices, moving_avg,"After Smoothing")
            SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 6/TestCases/Moving Average/OutMovAvgTest1.txt", indices,moving_avg)

    def DerivativeSignal(self):
        InputSignal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                       75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
                       99, 100]
        expectedOutput_first = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        expectedOutput_second = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        """
        Write your Code here:
        Start
        """
        FirstDrev = []
        SecondDrev = []

        for i in range(1, len(InputSignal)):
            difference1 = InputSignal[i] - InputSignal[i - 1]
            FirstDrev.append(difference1)

        for i in range(1, len(InputSignal) - 1):
            difference2 = InputSignal[i + 1] - 2 * InputSignal[i] + InputSignal[i - 1]
            SecondDrev.append(difference2)

        indices1 = list(range(len(FirstDrev)))
        indices2 = list(range(len(SecondDrev)))
        self.show_signal(indices1,FirstDrev,"First Derivative",indices2, SecondDrev,"Second Derivative")

        """
        End
        """

        """
        Testing your Code
        """
        if ((len(FirstDrev) != len(expectedOutput_first)) or (len(SecondDrev) != len(expectedOutput_second))):
            print("mismatch in length")
            return
        first = second = True
        for i in range(len(expectedOutput_first)):
            if abs(FirstDrev[i] - expectedOutput_first[i]) < 0.01:
                continue
            else:
                first = False
                print("1st derivative wrong")
                return
        for i in range(len(expectedOutput_second)):
            if abs(SecondDrev[i] - expectedOutput_second[i]) < 0.01:
                continue
            else:
                second = False
                print("2nd derivative wrong")
                return
        if (first and second):
            print("Derivative Test case passed successfully")
        else:
            print("Derivative Test case failed")
        return

    def shiftByConst(self):
        if self.signal:
            X = [float(row[0]) for row in self.signal]
            Y = [float(row[1]) for row in self.signal]

            shifted_signal = [(float(x) + float(self.constK.get()), float(y)) for x, y in self.signal]
            X_result = [float(row[0]) for row in shifted_signal]
            Y_result = [float(row[1]) for row in shifted_signal]

            self.show_signal(X, Y,"Before Shifting",X_result,Y_result,"After Shifting")

    def folding(self):
        if self.signal:
            X = [float(row[0]) for row in self.signal]
            Y = [float(row[1]) for row in self.signal]

            folded_signal = Y[::-1]
            self.show_signal(X,Y,"Before Folding",X,folded_signal,"After Folding")
            Shift_Fold_Signal("D:/Materials_4th/DSP/Labs/Lab 6/TestCases/Shifting and Folding/Output_fold.txt",X,folded_signal)

    def shiftFolded(self):
        if self.signal:
            X = [float(row[0]) for row in self.signal]
            Y = [float(row[1]) for row in self.signal]
            folded_signal = Y[::-1]
            shifted_signal = [(float(x) + float(self.constK.get()), float(y)) for x, y in self.signal]
            X_result = [float(row[0]) for row in shifted_signal]

            self.show_signal(X, Y,"Before Shift Folded Signal",X_result,folded_signal,"After Shift Folded Signal")
            Shift_Fold_Signal("D:/Materials_4th/DSP/Labs/Lab 6/TestCases/Shifting and Folding/Output_ShiftFoldedby-500.txt",X_result,folded_signal)

    def dft(self,Y, sign, factor):
        N = len(Y)
        res = np.array([])
        for k in range(0, N):
            Xk = np.complex(0, 0)
            for n in range(0, N):
                exp = np.exp(sign * 2 * math.pi * k * n * 1j / N)
                Xk += np.complex(Y[n]) * exp
            res = np.append(res, [factor * Xk])

        return res

    def removeDC(self):
        if self.signal:
            X = [float(row[0]) for row in self.signal]
            Y = [float(row[1]) for row in self.signal]

            resDFT = self.dft(Y,-1,1)
            resDFT[0] = 0
            # print(resDFT)
            resIDFT = self.dft(resDFT, 1, 1 / len(resDFT))
            # print(resIDFT.real)
            self.show_signal(X, Y,"Before Removing DC",X,resIDFT,"After Removing DC")
            SignalSamplesAreEqual2("D:/Materials_4th/DSP/Labs/Lab 5/Task files/Remove DC component/DC_component_output.txt",resIDFT)

    def done(self):
        selected_operation = self.combo_box.get()
        if selected_operation:
            if selected_operation == "smoothing":
                self.smoothing()
            if selected_operation == "shift by k":
                self.shiftByConst()
            if selected_operation == "shift folded":
                self.shiftFolded()

    def perform(self):
        self.selected_operation = self.combo_box.get()
        if self.selected_operation:
            if self.selected_operation == "smoothing":
                self.show_button.pack_forget()
                self.win_label.pack(pady=5)
                self.windowSize.pack()
                self.show_button.pack(pady=5)
                self.const_label.pack_forget()
                self.constK.pack_forget()

            if self.selected_operation == "sharpening":
                self.win_label.pack_forget()
                self.windowSize.pack_forget()
                self.const_label.pack_forget()
                self.constK.pack_forget()
                self.show_button.pack_forget()
                self.DerivativeSignal()

            if self.selected_operation == "shift by k":
                self.win_label.pack_forget()
                self.windowSize.pack_forget()
                self.show_button.pack_forget()

                self.const_label.pack(pady=5)
                self.constK.pack()
                self.show_button.pack(pady=5)

            if self.selected_operation == "folding":
                self.win_label.pack_forget()
                self.windowSize.pack_forget()
                self.show_button.pack_forget()
                self.const_label.pack_forget()
                self.constK.pack_forget()

                self.folding()

            if self.selected_operation == "shift folded":
                self.win_label.pack_forget()
                self.windowSize.pack_forget()
                self.show_button.pack_forget()


                self.const_label.pack(pady=5)
                self.constK.pack()
                self.show_button.pack(pady=5)

            if self.selected_operation == "remove dc":
                self.win_label.pack_forget()
                self.windowSize.pack_forget()
                self.show_button.pack_forget()
                self.const_label.pack_forget()
                self.constK.pack_forget()

                self.removeDC()












