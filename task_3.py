import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from QuanTest1 import QuantizationTest1
from QuanTest2 import QuantizationTest2
from tkinter import messagebox, filedialog, ttk
import numpy as np
import matplotlib.pyplot as plt

class Task3:
    def __init__(self,frame):
        self.frame = frame
        self.levels = tk.Entry(frame, width=40)
        self.bits = tk.Entry(frame, width=40)
        self.figure = plt.figure()
        self.canvas = None
        self.signal = []
        self.numLevels = 0

    def browse_signal(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                for i in range(3):
                    next(file)
                self.signal = [line.strip().split() for line in file]

    def quantize_signal(self):
        if self.signal:
            X = [float(row[0]) for row in self.signal]
            Y = [float(row[1]) for row in self.signal]

            quantized_signal = np.zeros_like(Y)
            encoded_values = []
            encoded_values_binary = []

            max_amp = np.max(Y)
            min_amp = np.min(Y)

            if self.levels.get() is not None and self.levels.get().strip():
                self.numLevels = int(self.levels.get())
            elif self.bits.get() is not None and self.bits.get().strip():
                self.numLevels = 2 ** int(self.bits.get())


            delta = (max_amp - min_amp) / self.numLevels
            midpoints = min_amp + delta / 2 + delta * np.arange(self.numLevels)

            for i, sample in enumerate(Y):
                nearest_index = np.abs(midpoints - sample).argmin()
                quantized_signal[i] = midpoints[nearest_index]
                encoded_values.append(nearest_index + 1)
                encoded_values_binary.append(np.binary_repr(nearest_index, width=int(np.log2(self.numLevels))))

            quantization_error = quantized_signal - Y
            print("Quantized Signal:", quantized_signal)
            print("Quantization Error:", quantization_error)
            print("Encoded Values:", encoded_values)
            print("Encoded Values Binary:", encoded_values_binary)

            self.show_signal(X,quantized_signal)
            QuantizationTest1("D:/Materials_4th/DSP/Labs/Lab 3/Task 3 + (UPDATED) Files/Test 1/Quan1_Out.txt",encoded_values_binary,quantized_signal)
            QuantizationTest2("D:/Materials_4th/DSP/Labs/Lab 3/Task 3 + (UPDATED) Files/Test 2/Quan2_Out.txt",encoded_values,encoded_values_binary,quantized_signal,quantization_error)

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
