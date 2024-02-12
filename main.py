from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from task_1 import Task1
from task_2 import Task2
from task_3 import Task3
from task_4 import Task4
from task_5 import Task5
from task_6 import Task6
from task_7 import Task7
from task_8 import Task8
from task_9 import Task9

task1_initialized = False
task2_initialized = False
task3_initialized = False
task4_initialized = False
task5_initialized = False
task6_initialized = False
task7_initialized = False
task8_initialized = False
task9_initialized = False

def first_task():
    global task1_initialized
    if not task1_initialized:
        task2_frame.pack_forget()
        task3_frame.pack_forget()
        task4_frame.pack_forget()
        task5_frame.pack_forget()
        task6_frame.pack_forget()
        task7_frame.pack_forget()
        task8_frame.pack_forget()
        task9_frame.pack_forget()
        task1 = Task1(task1_frame)
        browse_button = tk.Button(task1_frame, text="Browse For a Signal File", command=task1.browse_file, width=18,
                                  font=("Bold", 11), fg="white", bg="#31B587")

        button_test = tk.Button(task1_frame, text='Test', command=task1.test, width=18, font=("Bold", 11), fg="white",
                                bg="#31B587")

        # Create radio buttons
        cos_button = tk.Radiobutton(task1_frame, text="Cos", variable=task1.option, value="cos", width=16,
                                    font=("Bold", 11), fg="white", bg="#31B587", selectcolor='#31B587')
        sin_button = tk.Radiobutton(task1_frame, text="Sin", variable=task1.option, value="sin", width=16,
                                    font=("Bold", 11), fg="white", bg="#31B587", selectcolor='#31B587')

        label1 = tk.Label(task1_frame, text="Enter The Amplitude:", width=23, font=("Bold", 9))
        label2 = tk.Label(task1_frame, text="Enter The Analog Frequency:", width=23, font=("Bold", 9))
        label3 = tk.Label(task1_frame, text="Enter The Sampling Frequency:", width=24, font=("Bold", 9))
        label4 = tk.Label(task1_frame, text="Enter The Phase Shift:", width=23, font=("Bold", 9))

        submit_button = tk.Button(task1_frame, text="Show", command=task1.submit, width=18, font=("Bold", 11),
                                  fg="white", bg="#31B587")

        browse_button.pack()
        button_test.pack(pady=10)
        cos_button.pack()
        sin_button.pack()
        label1.pack()
        task1.entry1.pack()
        label2.pack()
        task1.entry2.pack()
        label3.pack()
        task1.entry3.pack()
        label4.pack()
        task1.entry4.pack()
        submit_button.pack(pady=10)
        task1_initialized = True
    task2_frame.pack_forget()
    task3_frame.pack_forget()
    task4_frame.pack_forget()
    task5_frame.pack_forget()
    task6_frame.pack_forget()
    task7_frame.pack_forget()
    task8_frame.pack_forget()
    task9_frame.pack_forget()
    image_label.destroy()
    task1_frame.pack()

def second_task():
    global task2_initialized
    if not task2_initialized:
        task1_frame.pack_forget()
        task3_frame.pack_forget()
        task4_frame.pack_forget()
        task5_frame.pack_forget()
        task6_frame.pack_forget()
        task7_frame.pack_forget()
        task8_frame.pack_forget()
        task9_frame.pack_forget()
        task2 = Task2(task2_frame)
        browse1_button = tk.Button(task2_frame, text="Browse For The First Signal File", command=task2.browse_signal_1,
                                   width=26,
                                   font=("Bold", 11), fg="white", bg="#31B587")
        browse2_button = tk.Button(task2_frame, text="Browse For The Second Signal File", command=task2.browse_signal_2,
                                   width=26,
                                   font=("Bold", 11), fg="white", bg="#31B587")
        # Create a combo box
        combo_box = ttk.Combobox(task2_frame, width=37, height=30)
        combo_box['values'] = (
            'Add', 'Subtract', 'Squaring', 'Multiply By Constant', 'Shift By Constant', 'Normalization', 'Accumulation')

        perform_button = tk.Button(task2_frame, text="Perform Operation", command=lambda: task2.perform(), width=26,
                                   font=("Bold", 11),
                                   fg="white", bg="#31B587")
        browse1_button.pack()
        browse2_button.pack(pady=10)
        task2.combo_box.pack()
        perform_button.pack(pady=10)
        task2_initialized = True

    task1_frame.pack_forget()
    task3_frame.pack_forget()
    task4_frame.pack_forget()
    task5_frame.pack_forget()
    task6_frame.pack_forget()
    task7_frame.pack_forget()
    task8_frame.pack_forget()
    task9_frame.pack_forget()
    image_label.destroy()
    task2_frame.pack()

def third_task():
    global task3_initialized
    if not task3_initialized:
        task1_frame.pack_forget()
        task2_frame.pack_forget()
        task4_frame.pack_forget()
        task5_frame.pack_forget()
        task6_frame.pack_forget()
        task7_frame.pack_forget()
        task8_frame.pack_forget()
        task9_frame.pack_forget()
        task3 = Task3(task3_frame)
        browse_button = tk.Button(task3_frame, text="Browse For The Signal File", command=task3.browse_signal, width=26,
                                  font=("Bold", 11), fg="white", bg="#31B587")

        label1 = tk.Label(task3_frame, text="Enter The Number of Levels:", width=37, font=("Bold", 11))
        label2 = tk.Label(task3_frame, text="Enter The Number of Bits:", width=37, font=("Bold", 11))

        quantize_button = tk.Button(task3_frame, text="Quantize", command=task3.quantize_signal, width=26,
                                    font=("Bold", 11), fg="white", bg="#31B587")

        browse_button.pack(pady=10)
        label1.pack()
        task3.levels.pack()
        label2.pack()
        task3.bits.pack()

        quantize_button.pack(pady=10)
        task3_initialized = True
    task1_frame.pack_forget()
    task2_frame.pack_forget()
    task4_frame.pack_forget()
    task5_frame.pack_forget()
    task6_frame.pack_forget()
    task7_frame.pack_forget()
    task8_frame.pack_forget()
    task9_frame.pack_forget()
    image_label.destroy()
    task3_frame.pack()

def fourth_task():
    global task4_initialized
    if not task4_initialized:
        task1_frame.pack_forget()
        task2_frame.pack_forget()
        task3_frame.pack_forget()
        task5_frame.pack_forget()
        task6_frame.pack_forget()
        task7_frame.pack_forget()
        task8_frame.pack_forget()
        task9_frame.pack_forget()
        task4 = Task4(task4_frame)

        label1 = tk.Label(task4_frame, text="Enter The Sampling Frequency:", width=37, font=("Bold", 11))
        label1.pack()
        task4.Fs.pack()
        dftBtn = tk.Button(task4_frame, text="DFT", command=task4.dftCalc,width=26,font=("Bold", 11), fg="white",
                           bg="#31B587")
        dftBtn.pack(pady=5)
        idftBtn = tk.Button(task4_frame, text="IDFT", command=task4.idftCalc,width=26, font=("Bold", 11), fg="white",
                            bg="#31B587")
        idftBtn.pack()
        lbl = tk.Label(task4_frame, text="New Amplitude", width=37, font=("Bold", 11))
        lbl.pack()
        task4.ampEntry.pack()
        lbl = tk.Label(task4_frame, text="New Phase Shift", width=37, font=("Bold", 11))
        lbl.pack()
        task4.psEntry.pack()
        lbl = tk.Label(task4_frame, text="Entry index",width=37, font=("Bold", 11))
        lbl.pack()
        task4.indxEntry.pack()
        modBtn = tk.Button(task4_frame, text="Modify", command=task4.modify, width=26, font=("Bold", 11), fg="white",
                           bg="#31B587")
        modBtn.pack(pady=5)
        task4_initialized = True

    task1_frame.pack_forget()
    task2_frame.pack_forget()
    task3_frame.pack_forget()
    task5_frame.pack_forget()
    task6_frame.pack_forget()
    task7_frame.pack_forget()
    task8_frame.pack_forget()
    task9_frame.pack_forget()
    image_label.destroy()
    task4_frame.pack()

def fifth_task():
    global task5_initialized
    if not task5_initialized:
        task1_frame.pack_forget()
        task2_frame.pack_forget()
        task3_frame.pack_forget()
        task4_frame.pack_forget()
        task6_frame.pack_forget()
        task7_frame.pack_forget()
        task8_frame.pack_forget()
        task9_frame.pack_forget()
        task5 = Task5(task5_frame)

        browse_button = tk.Button(task5_frame, text="Browse For The Signal File", command=task5.browse_signal, width=26,
                                  font=("Bold", 11), fg="white", bg="#31B587")

        dct_button = tk.Button(task5_frame, text="DCT", command=task5.DCT,width=26,font=("Bold", 11), fg="white",
                           bg="#31B587")
        dcRemove_button = tk.Button(task5_frame, text="DC Removal", command=task5.Remove_DC,width=26,font=("Bold", 11), fg="white",
                           bg="#31B587")
        lbl = tk.Label(task5_frame, text="Enter Number of Coefficients",width=37, font=("Bold", 11))
        browse_button.pack()
        lbl.pack(pady=5)
        task5.numCoeff.pack()
        dct_button.pack(pady=5)
        dcRemove_button.pack()
        task5_initialized = True

    task1_frame.pack_forget()
    task2_frame.pack_forget()
    task3_frame.pack_forget()
    task4_frame.pack_forget()
    task6_frame.pack_forget()
    task7_frame.pack_forget()
    task8_frame.pack_forget()
    task9_frame.pack_forget()
    image_label.destroy()
    task5_frame.pack()

def sixth_task():
    global task6_initialized
    if not task6_initialized:
        task1_frame.pack_forget()
        task2_frame.pack_forget()
        task3_frame.pack_forget()
        task4_frame.pack_forget()
        task5_frame.pack_forget()
        task7_frame.pack_forget()
        task8_frame.pack_forget()
        task9_frame.pack_forget()
        task6 = Task6(task6_frame)

        browse_button = tk.Button(task6_frame, text="Browse For The Signal File", command=task6.browse_signal, width=26,
                                  font=("Bold", 11), fg="white", bg="#31B587")
        perform_button = tk.Button(task6_frame, text="Perform Operation", command=lambda: task6.perform(), width=26,
                                   font=("Bold", 11),
                                   fg="white", bg="#31B587")


        browse_button.pack()
        task6.combo_box.pack(pady=5)
        perform_button.pack()
        task6_initialized = True

    task1_frame.pack_forget()
    task2_frame.pack_forget()
    task3_frame.pack_forget()
    task4_frame.pack_forget()
    task5_frame.pack_forget()
    task7_frame.pack_forget()
    task8_frame.pack_forget()
    task9_frame.pack_forget()
    image_label.destroy()
    task6_frame.pack()

def seventh_task():
    global task7_initialized
    if not task7_initialized:
        task1_frame.pack_forget()
        task2_frame.pack_forget()
        task3_frame.pack_forget()
        task4_frame.pack_forget()
        task5_frame.pack_forget()
        task6_frame.pack_forget()
        task8_frame.pack_forget()
        task9_frame.pack_forget()
        task7 = Task7(task7_frame)

        browse_button1 = tk.Button(task7_frame, text="Browse For The First Signal", command=task7.browse_signal1, width=26,
                                  font=("Bold", 11), fg="white", bg="#31B587")
        browse_button2 = tk.Button(task7_frame, text="Browse For The Second Signal", command=task7.browse_signal2, width=26,
                                  font=("Bold", 11), fg="white", bg="#31B587")
        convolve_button = tk.Button(task7_frame, text="Convolve Signals", command=task7.convolution, width=26,
                                   font=("Bold", 11),fg="white", bg="#31B587")

        browse_button1.pack()
        browse_button2.pack(pady=5)
        convolve_button.pack()
        task7_initialized = True

    task1_frame.pack_forget()
    task2_frame.pack_forget()
    task3_frame.pack_forget()
    task4_frame.pack_forget()
    task5_frame.pack_forget()
    task6_frame.pack_forget()
    task8_frame.pack_forget()
    task9_frame.pack_forget()
    image_label.destroy()
    task7_frame.pack()

def eighth_task():
    global task8_initialized
    if not task8_initialized:
        task1_frame.pack_forget()
        task2_frame.pack_forget()
        task3_frame.pack_forget()
        task4_frame.pack_forget()
        task5_frame.pack_forget()
        task6_frame.pack_forget()
        task7_frame.pack_forget()
        task9_frame.pack_forget()
        task8 = Task8(task8_frame)

        browse_button1 = tk.Button(task8_frame, text="Browse For The First Signal", command=task8.browse_signal1, width=26,
                                  font=("Bold", 11), fg="white", bg="#31B587")
        browse_button2 = tk.Button(task8_frame, text="Browse For The Second Signal", command=task8.browse_signal2, width=26,
                                  font=("Bold", 11), fg="white", bg="#31B587")
        correlate_button = tk.Button(task8_frame, text="Correlation", command=task8.correlation, width=26,
                                   font=("Bold", 11),fg="white", bg="#31B587")

        browse_button1.pack()
        browse_button2.pack(pady=5)
        correlate_button.pack()
        task8_initialized = True

    task1_frame.pack_forget()
    task2_frame.pack_forget()
    task3_frame.pack_forget()
    task4_frame.pack_forget()
    task5_frame.pack_forget()
    task6_frame.pack_forget()
    task7_frame.pack_forget()
    task9_frame.pack_forget()
    image_label.destroy()
    task8_frame.pack()

def ninth_task():
    global task9_initialized
    if not task9_initialized:
        task1_frame.pack_forget()
        task2_frame.pack_forget()
        task3_frame.pack_forget()
        task4_frame.pack_forget()
        task5_frame.pack_forget()
        task6_frame.pack_forget()
        task7_frame.pack_forget()
        task8_frame.pack_forget()
        task9 = Task9(task9_frame)

        browse_button1 = tk.Button(task9_frame, text="Browse For The First Signal", command=task9.browse_signal1, width=26,
                                  font=("Bold", 11), fg="white", bg="#31B587")
        browse_button2 = tk.Button(task9_frame, text="Browse For The Second Signal", command=task9.browse_signal2, width=26,
                                  font=("Bold", 11), fg="white", bg="#31B587")
        fast_conv_button = tk.Button(task9_frame, text="Fast Convolution", command=task9.fast_convolution, width=26,
                                   font=("Bold", 11),fg="white", bg="#31B587")
        fast_corr_button = tk.Button(task9_frame, text="Fast Correlation", command=task9.fast_correlation, width=26,
                                   font=("Bold", 11),fg="white", bg="#31B587")

        browse_button1.pack()
        browse_button2.pack(pady=5)
        fast_conv_button.pack()
        fast_corr_button.pack(pady=5)
        task9_initialized = True

    task1_frame.pack_forget()
    task2_frame.pack_forget()
    task3_frame.pack_forget()
    task4_frame.pack_forget()
    task5_frame.pack_forget()
    task6_frame.pack_forget()
    task7_frame.pack_forget()
    task8_frame.pack_forget()
    image_label.destroy()
    task9_frame.pack()

########################################################################################################################
#GUI Tkinter
root = tk.Tk()
root.title("Digital Signal Processing")
root.geometry("800x565")

options_frame = tk.Frame(root)
main_frame = tk.Frame(root)
task1_frame = tk.Frame(main_frame)
task2_frame = tk.Frame(main_frame)
task3_frame = tk.Frame(main_frame)
task4_frame = tk.Frame(main_frame)
task5_frame = tk.Frame(main_frame)
task6_frame = tk.Frame(main_frame)
task7_frame = tk.Frame(main_frame)
task8_frame = tk.Frame(main_frame)
task9_frame = tk.Frame(main_frame)
# image
image_path = "D:/Downloads/signalment.jpg"
image = Image.open(image_path)
image = image.resize((900, 750))
photo = ImageTk.PhotoImage(image) # Convert the image to Tkinter-compatible format
image_label = tk.Label(main_frame, image=photo)
image_label.place(x=0, y=0)

task1_button = tk.Button(options_frame,text="Task 1",width=12,font=("Bold",15),fg="white",bg="#31B587",command=first_task)
task1_button.place(x=30, y=20)
task2_button = tk.Button(options_frame,text="Task 2",width=12,font=("Bold",15),fg="white",bg="#31B587",command=second_task)
task2_button.place(x=30, y=80)
task3_button = tk.Button(options_frame,text="Task 3",width=12,font=("Bold",15),fg="white",bg="#31B587",command=third_task)
task3_button.place(x=30, y=140)
task4_button = tk.Button(options_frame,text="Task 4",width=12,font=("Bold",15),fg="white",bg="#31B587",command=fourth_task)
task4_button.place(x=30, y=200)
task5_button = tk.Button(options_frame,text="Task 5",width=12,font=("Bold",15),fg="white",bg="#31B587",command=fifth_task)
task5_button.place(x=30, y=260)
task6_button = tk.Button(options_frame,text="Task 6",width=12,font=("Bold",15),fg="white",bg="#31B587",command=sixth_task)
task6_button.place(x=30, y=320)
task7_button = tk.Button(options_frame,text="Task 7",width=12,font=("Bold",15),fg="white",bg="#31B587",command=seventh_task)
task7_button.place(x=30, y=380)
task8_button = tk.Button(options_frame,text="Task 8",width=12,font=("Bold",15),fg="white",bg="#31B587",command=eighth_task)
task8_button.place(x=30, y=440)
task9_button = tk.Button(options_frame,text="Task 9",width=12,font=("Bold",15),fg="white",bg="#31B587",command=ninth_task)
task9_button.place(x=30, y=500)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(height=565,width=200)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=565,width=800)

root.mainloop()