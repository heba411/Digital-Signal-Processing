import matplotlib.pyplot as plt
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ConvTest import ConvTest

class Task7:
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

    def convolution(self):
        if self.signal1 and self.signal2:
            X1 = [int(row[0]) for row in self.signal1]
            Y1 = [int(row[1]) for row in self.signal1]
            X2 = [int(row[0]) for row in self.signal2]
            Y2 = [int(row[1]) for row in self.signal2]

            X_result = []
            Y_result = []

            for i in range(X1[0] + X2[0], X1[-1] + X2[-1] + 1):
                convolution_sum = 0
                for j in range(len(Y1)):
                    for k in range(len(Y2)):
                        if i == X1[j] + X2[k]:
                            convolution_sum += Y1[j] * Y2[k]

                X_result.append(i)
                Y_result.append(convolution_sum)
            print(Y_result)
            print(X_result)
            ConvTest(X_result,Y_result)
            self.show_signal(X_result,Y_result,"Convolved Signal")

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



