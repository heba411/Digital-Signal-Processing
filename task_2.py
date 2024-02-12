from tkinter import messagebox, filedialog, ttk
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn import preprocessing
from comparesignals import SignalSamplesAreEqual1

class Task2:
    def __init__(self,frame):
        self.option = tk.StringVar()
        self.label1 = tk.Label(frame, text="Enter The Constant To Multiply The Signal:",width=37,font=("Bold",10))
        self.entry1 = tk.Entry(frame,width=40)
        self.label2 = tk.Label(frame, text="Enter The Constant To Shift The Signal By:",width=37,font=("Bold",10))
        self.entry2 = tk.Entry(frame,width=40)
        self.from0to1_button = tk.Radiobutton(frame, text="From 0 To 1", variable=self.option, value="From 0 To 1",width=16,
                                         font=("Bold",11),fg="white",bg="#31B587",selectcolor='#31B587')
        self.fromNeg1to1_button = tk.Radiobutton(frame, text="From -1 To 1", variable=self.option, value="From -1 To 1",width=16,
                                            font=("Bold",11),fg="white",bg="#31B587",selectcolor='#31B587')
        self.show_button = tk.Button(frame, text="Show", command=self.done,width=26,font=("Bold",11),fg="white",bg="#31B587")
        self.combo_box = ttk.Combobox(frame,width=37,height=30)
        self.combo_box['values'] = ('Add', 'Subtract','Squaring','Multiply By Constant','Shift By Constant','Normalization','Accumulation')
        self.selected_operation = None
        self.frame = frame
        self.figure = plt.figure()
        self.canvas = None
        self.signal1 = []
        self.signal2 = []

    def browse_signal_1(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                for i in range(3):
                    next(file)
                self.signal1 = [line.strip().split() for line in file]

    def browse_signal_2(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                for i in range(3):
                    next(file)
                self.signal2 = [line.strip().split() for line in file]

    def add_signals(self):
        if self.signal1 and self.signal2:
            X1 = [float(row[0]) for row in self.signal1]
            Y1 = [float(row[1]) for row in self.signal1]
            X2 = [float(row[0]) for row in self.signal2]
            Y2 = [float(row[1]) for row in self.signal2]
            len1 = len(X1)
            len2 = len(X2)

            max_len = max(len1, len2)
            X_result = np.zeros(max_len)
            Y_result = np.zeros(max_len)

            X_result[:len1] = X1
            X_result[:len2] += X2

            Y_result[:len1] = Y1
            Y_result[:len2] += Y2

            self.show_signal(X_result, Y_result)
            SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 2/Task 2 + Files/output signals/Signal1+signal2.txt",
                                  X_result, Y_result)

    def subtract_signals(self):
        if self.signal1 and self.signal2:
            X1 = [float(row[0]) for row in self.signal2]
            Y1 = [float(row[1]) for row in self.signal2]
            X2 = [float(row[0]) for row in self.signal1]
            Y2 = [float(row[1]) for row in self.signal1]
            len1 = len(X1)
            len2 = len(X2)

            max_len = max(len1, len2)
            X_result = np.zeros(max_len)
            Y_result = np.zeros(max_len)

            X_result[:len1] = X1
            X_result[:len2] -= X2

            Y_result[:len1] = Y1
            Y_result[:len2] -= Y2

            self.show_signal(X_result, Y_result)
            SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 2/Task 2 + Files/output signals/signal1-signal2.txt",
                                  X_result, Y_result)

    def multiply_signal(self):
        multiplied_signal = [(x, float(y) * float(self.entry1.get())) for x, y in self.signal1]
        X_result = [float(row[0]) for row in multiplied_signal]
        Y_result = [float(row[1]) for row in multiplied_signal]
        self.show_signal(X_result,Y_result)
        SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 2/Task 2 + Files/output signals/MultiplySignalByConstant-Signal1 - by 5.txt",
                              X_result, Y_result)

    def square_signal(self):
        squared_signal = [[float(row[0]) ** 2, float(row[1]) ** 2] for row in self.signal1]
        X_result = [float(row[0]) for row in squared_signal]
        Y_result = [float(row[1]) for row in squared_signal]
        self.show_signal(X_result, Y_result)
        SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 2/Task 2 + Files/output signals/Output squaring signal 1.txt",
                              X_result, Y_result)

    def shift_signal(self):
        shifted_signal = [(float(x) + float(self.entry2.get()), float(y)) for x, y in self.signal1]
        X_result = [float(row[0]) for row in shifted_signal]
        Y_result = [float(row[1]) for row in shifted_signal]
        self.show_signal(X_result, Y_result)
        SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 2/Task 2 + Files/output signals/output shifting by add 500.txt",
                              X_result, Y_result)

    def fromzeroToOne_normalization(self):
        min_max_scaler = preprocessing.MinMaxScaler()
        normalized_signal = min_max_scaler.fit_transform(self.signal1)
        X_result = [float(row[0]) for row in normalized_signal]
        Y_result = [float(row[1]) for row in normalized_signal]
        self.show_signal(X_result, Y_result)
        SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 2/Task 2 + Files/output signals/normlize signal 2 -- output.txt",
                              X_result, Y_result)

    def fromNegOneToOne_normalization(self):
        scaler = preprocessing.MinMaxScaler(feature_range=(-1, 1))
        normalized_signal = scaler.fit_transform(self.signal1)
        X_result = [float(row[0]) for row in normalized_signal]
        Y_result = [float(row[1]) for row in normalized_signal]
        self.show_signal(X_result, Y_result)
        SignalSamplesAreEqual1(
            "D:/Materials_4th/DSP/Labs/Lab 2/Task 2 + Files/output signals/normalize of signal 1 -- output.txt",
            X_result, Y_result)

    def accumulative_signal(self):
        X_result = [float(row[0]) for row in self.signal1]
        Y_result = [sum(X_result[:i + 1]) for i in range(len(X_result))]
        self.show_signal(X_result, Y_result)
        SignalSamplesAreEqual1("D:/Materials_4th/DSP/Labs/Lab 2/Task 2 + Files/output signals/output accumulation for signal1.txt",
                              X_result, Y_result)

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

    def perform(self):
        self.selected_operation = self.combo_box.get()
        if self.selected_operation:
            if self.selected_operation == "Add":
                self.add_signals()
                self.show_button.pack_forget()
                self.label2.pack_forget()
                self.entry2.pack_forget()
                self.label1.pack_forget()
                self.entry1.pack_forget()
                self.from0to1_button.pack_forget()
                self.fromNeg1to1_button.pack_forget()
            elif self.selected_operation == "Subtract":
                self.subtract_signals()
                self.show_button.pack_forget()
                self.label2.pack_forget()
                self.entry2.pack_forget()
                self.label1.pack_forget()
                self.entry1.pack_forget()
                self.from0to1_button.pack_forget()
                self.fromNeg1to1_button.pack_forget()
            elif self.selected_operation == "Squaring":
                self.square_signal()
                self.show_button.pack_forget()
                self.label2.pack_forget()
                self.entry2.pack_forget()
                self.label1.pack_forget()
                self.entry1.pack_forget()
                self.from0to1_button.pack_forget()
                self.fromNeg1to1_button.pack_forget()
            elif self.selected_operation == "Accumulation":
                self.accumulative_signal()
                self.show_button.pack_forget()
                self.label2.pack_forget()
                self.entry2.pack_forget()
                self.label1.pack_forget()
                self.entry1.pack_forget()
                self.from0to1_button.pack_forget()
                self.fromNeg1to1_button.pack_forget()
            elif self.selected_operation == "Multiply By Constant":
                self.show_button.pack_forget()
                self.label2.pack_forget()
                self.entry2.pack_forget()
                self.from0to1_button.pack_forget()
                self.fromNeg1to1_button.pack_forget()

                self.label1.pack()
                self.entry1.pack(pady=10)
                self.show_button.pack()
            elif self.selected_operation == "Shift By Constant":
                self.show_button.pack_forget()
                self.label1.pack_forget()
                self.entry1.pack_forget()
                self.from0to1_button.pack_forget()
                self.fromNeg1to1_button.pack_forget()

                self.label2.pack()
                self.entry2.pack(pady=10)
                self.show_button.pack()
            elif self.selected_operation == "Normalization":
                self.show_button.pack_forget()
                self.label1.pack_forget()
                self.entry1.pack_forget()
                self.label2.pack_forget()
                self.entry2.pack_forget()
                self.from0to1_button.pack()
                self.fromNeg1to1_button.pack()
                self.show_button.pack(pady=10)
        else:
            messagebox.showerror("Error!","You Have To Choose an Operation..")
            return

    def done(self):
        selected_operation = self.combo_box.get()
        selected_normalization = self.option.get()
        if selected_operation:
            if selected_operation == "Multiply By Constant":
                self.multiply_signal()
            elif selected_operation == "Shift By Constant":
                self.shift_signal()
            elif selected_operation == "Normalization":
                if selected_normalization == "From 0 To 1":
                    self.fromzeroToOne_normalization()
                elif selected_normalization == "From -1 To 1":
                    self.fromNegOneToOne_normalization()

