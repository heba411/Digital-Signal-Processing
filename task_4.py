import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Task4:
    def __init__(self,frame):
        self.frame = frame
        self.Fs = tk.Entry(frame, width=40)
        self.win = tk.Toplevel(self.frame)
        self.win.title("DFT")
        self.entryTable = None
        self.ampEntry = tk.Entry(frame, width=40)
        self.psEntry = tk.Entry(frame, width=40)
        self.indxEntry = tk.Entry(frame, width=40)
        self.figure = plt.figure()
        self.canvas = None

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

    def readSignalsFromFile(self):
        time = []
        x_t = []
        filePath = filedialog.askopenfilename(initialdir="C:\\Users\\Tech",title="Open File",)
        with open(filePath, 'r') as file:
            for i, line in enumerate(file):
                if i >= 3:
                    num1, num2 = line.split()
                    time.append(float(num1))
                    x_t.append(float(num2))
        return x_t, time

    def plot(self, f, amp,phase):
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
            self.canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True, padx=10, pady=10)
            self.canvas.get_tk_widget().config(width=600, height=500)
        else:
            self.figure.clear()

        plt1 = self.figure.add_subplot(121)
        plt1.bar(f, amp)
        plt1.set_xlabel("Frequency")
        plt1.set_ylabel("Amplitude")

        plt2 = self.figure.add_subplot(122)
        plt2.bar(f, phase)
        plt2.set_xlabel("Frequency")
        plt2.set_ylabel("Phase")
        plt2.set_ylim(min(phase), max(phase))
        plt2.axhline(0, color='black')
        self.create_table(len(table), 3, table)
        self.canvas.draw()

    def readPolarSignalFromFile(self):
        freq = list()
        filePath = filedialog.askopenfilename(initialdir="C:\\Users\\Tech",
                                              title="Open File")
        with open(filePath, 'r') as file:
            for i, line in enumerate(file):
                if i >= 3:
                    num1, num2 = line.strip().split(',')
                    # print(num1,num2)
                    if num1[len(num1) - 1] == 'f':
                        num1 = num1[:-1]
                    if num2[len(num2) - 1] == 'f':
                        num2 = num2[:-1]
                    amp = float(num1)
                    phase_shift = float(num2)
                    real = amp * np.cos(phase_shift)
                    img = amp * np.sin(phase_shift)
                    f = real + 1j * img
                    freq.append(f)
        return freq

    def create_table(self,total_rows, total_columns, lst):
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.entryTable = Entry(self.win, width=20, fg='black')
                self.entryTable.grid(row=i, column=j)
                self.entryTable.insert(END, lst[i][j])

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

    def dftCalc(self):
        x, t = self.readSignalsFromFile()
        fs = int(self.Fs.get())
        result = self.dft(x, -1, 1)
        ts = 1 / fs
        omega = 2 * np.pi / (len(result) * ts)
        c = omega
        global f
        f = list()
        for i in range(len(result)):
            f.append(c)
            c = c + omega
        amp = list()
        phase = list()
        for x in result:
            amp.append(np.sqrt(x.real ** 2 + x.imag ** 2))
            phase.append(math.atan2(x.imag, x.real))
        n = np.arange(len(result))
        n = [x + 1 for x in n]
        global table
        table = [n, amp, phase]
        table = list(map(list, zip(*table)))
        print(table)
        self.plot(f, amp, phase)

        with open("dftOutput.txt", 'w') as file:
            file.write("0\n")
            file.write("1\n")
            file.write("%s\n" % len(amp))
            for i in range(len(amp)):
                file.write("%s" % amp[i])
                file.write(" ")
                file.write("%s\n" % phase[i])


    def idftCalc(self):
        x = self.readPolarSignalFromFile()
        result = self.dft(x, 1, 1 / len(x))
        print(result.real)
        print(result.imag)
        indicices = []
        with open("idftOutput.txt", 'w') as file:
            file.write("0\n")
            file.write("0\n")
            file.write("%s\n" % len(result))
            for i in range(len(result)):
                file.write("%s" % (i + 1))
                file.write(" ")
                file.write("%s\n" % int(round(result[i].real)))
                indicices.append(i)
        self.show_signal(indicices,result.real)

    def modify(self):
        amp = float(self.ampEntry.get())
        phase = float(self.psEntry.get())
        i = int(self.indxEntry.get())
        # print(table)
        table[i - 1][1] = amp
        table[i - 1][2] = phase
        # print(table)
        # print(table[:1])
        t = list(map(list, zip(*table)))
        self.plot(f, t[1], t[2])
        with open("dftOutput.txt", 'r') as file:
            lines = file.readlines()
        with open("dftOutput.txt", 'w') as file:
            file.writelines(lines[:i + 2])
            file.write("%s %s\n" % (amp, phase))
            file.writelines(lines[i + 3:])