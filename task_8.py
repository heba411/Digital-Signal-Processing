import matplotlib.pyplot as plt
from tkinter import filedialog
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from CompareSignal import Compare_Signals

class Task8:
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

    def correlation(self):
        if self.signal1 and self.signal2:
            X1 = [int(row[0]) for row in self.signal1]
            Y1 = [int(row[1]) for row in self.signal1]
            X2 = [int(row[0]) for row in self.signal2]
            Y2 = [int(row[1]) for row in self.signal2]

            N = len(Y1)
            sum_squares_Y1 = sum(x ** 2 for x in Y1)
            sum_squares_Y2 = sum(x ** 2 for x in Y2)
            factor = np.sqrt(sum_squares_Y1 * sum_squares_Y2) / N  #the dominator

            correlation_result = []

            for j in range(N):
                sum_product = 0
                for n in range(N):
                    sum_product += Y1[n] * Y2[(n + j) % N]
                    corr = sum_product/N
                correlation_result.append(corr/factor)
                print(sum_product)

            print(correlation_result)
            Compare_Signals('D:/Materials_4th/DSP/Labs/Lab 8/Correlation/CorrOutput.txt', X1, correlation_result)
            self.show_signal(X1,correlation_result, "Correlation")

# Y1                2 1 0 0 3
# Y2 at lag 0       3 2 1 1 5
# Y2 at lag 1       2 1 1 5 3
# Y2 at lag 2       1 1 5 3 2
# Y2 at lag 3       1 5 3 2 1
# Y2 at lag 4       5 3 2 1 1




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



