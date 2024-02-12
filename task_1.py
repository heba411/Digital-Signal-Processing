from tkinter import messagebox, filedialog
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from comparesignals import SignalSamplesAreEqual1


class Task1:
    def __init__(self,frame):
        self.frame = frame
        self.entry1 = tk.Entry(frame, width=28)
        self.entry2 = tk.Entry(frame, width=28)
        self.entry3 = tk.Entry(frame, width=28)
        self.entry4 = tk.Entry(frame, width=28)
        self.option = tk.StringVar()
        self.figure = plt.figure()
        self.canvas = None
        self.Type = []
        self.Amplitude = []
        self.Analog_Freq = []
        self.Sampling_Freq = []
        self.Phase_Shift = []
        self.test_file_path = "D:/Materials_4th/DSP/Labs/Lab 1/Signals/Sin_Cos/Inputs.txt"

    def browse_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                for i in range(3):
                    next(file)
                signal = [line.strip().split() for line in file]

        # Separate the columns into two lists
        X = [float(row[0]) for row in signal]
        Y = [float(row[1]) for row in signal]
        self.show_signal(X, Y)

    def show_signal(self, X, Y):
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
            self.canvas.get_tk_widget().pack()
        else:
            self.figure.clear()
        plt.plot(X, Y)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Signal [1] Plot')
        plt.grid(True)
        plt.scatter(X, Y, color='red')
        self.canvas.draw()

    def test(self):
        test_file_path = "D:/Materials_4th/DSP/Labs/Lab 1/Signals/Sin_Cos/Inputs.txt"
        Type = []
        Amplitude = []
        Analog_Freq = []
        Sampling_Freq = []
        Phase_Shift = []
        with open(test_file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith('type'):
                Type.append(line.split('=')[1].strip())
            elif line.startswith('AnalogFrequency'):
                Analog_Freq.append(float(line.split('=')[1].strip()))
            elif line.startswith('A'):
                Amplitude.append(float(line.split('=')[1].strip()))
            elif line.startswith('SamplingFrequency'):
                Sampling_Freq.append(float(line.split('=')[1].strip()))
            elif line.startswith('PhaseShift'):
                Phase_Shift.append(float(line.split('=')[1].strip()))

        t_cos = np.arange(0, 1, 1 / Sampling_Freq[1])  # for only 1 second
        t_sin = np.arange(0, 1, 1 / Sampling_Freq[0])
        signal_cos = Amplitude[1] * np.cos(2 * np.pi * Analog_Freq[1] * t_cos + Phase_Shift[1])
        signal_sin = Amplitude[0] * np.sin(2 * np.pi * Analog_Freq[0] * t_sin + Phase_Shift[0])
        indices = []
        SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 1/Signals/Sin_Cos/CosOutput.txt", indices, signal_cos)
        SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 1/Signals/Sin_Cos/SinOutput.txt", indices, signal_sin)

    def generate_sin(self, amp, analog_freq, samp_freq, shift):
        amp = float(amp)
        analog_freq = float(analog_freq)
        samp_freq = float(samp_freq)
        shift = float(shift)
        t = np.arange(0, 1, 1 / samp_freq)
        signal = amp * np.sin(2 * np.pi * (analog_freq / samp_freq) * t + shift)
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
            self.canvas.get_tk_widget().pack()
        else:
            self.figure.clear()
        cont_plot = self.figure.add_subplot(121)
        cont_plot.plot(t, signal)  # Continuous
        cont_plot.set_title("Continuous Sin Signal")
        cont_plot.grid(True)
        discr_plot = self.figure.add_subplot(122)
        discr_plot.stem(t, signal, use_line_collection=True)
        discr_plot.set_title("Discrete Sin Signal")
        plt.tight_layout()
        self.canvas.draw()

    def generate_cos(self, amp, analog_freq, samp_freq, shift):
        amp = float(amp)
        analog_freq = float(analog_freq)
        samp_freq = float(samp_freq)
        shift = float(shift)
        t = np.arange(0, 1, 1 / samp_freq)
        signal = amp * np.cos(2 * np.pi * analog_freq * t + shift)
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
            self.canvas.get_tk_widget().pack()
        else:
            self.figure.clear()
        cont_plot = self.figure.add_subplot(121)
        cont_plot.plot(t, signal)  # Continuous
        cont_plot.set_title("Continuous Cos Signal")
        cont_plot.grid(True)
        discr_plot = self.figure.add_subplot(122)
        discr_plot.stem(t, signal, use_line_collection=True)
        discr_plot.set_title("Discrete Cos Signal")
        plt.tight_layout()
        self.canvas.draw()

    def submit(self):
        amplitude = float(self.entry1.get())
        analog = float(self.entry2.get())
        sampling = float(self.entry3.get())
        shift = float(self.entry4.get())
        selected_option = self.option.get()
        if sampling >= 2 * analog:
            if selected_option == "cos":
                self.generate_cos(amplitude, analog, sampling, shift)
            elif selected_option == "sin":
                self.generate_sin(amplitude, analog, sampling, shift)
        else:
            messagebox.showerror("Error!", "Sampling frequency should be at least twice the Analog frequency.")
            return