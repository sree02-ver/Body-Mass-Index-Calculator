from tkinter import *

root = Tk()
root.geometry("1350x650+0+0")
root.resizable(0, 0)
root.title("BMI CALCULATOR")

# Custom colors
bg_color = "#3498db"
label_color = "white"
button_color = "#e74c3c"

def BMI_Cal():
    Bheight = float(var2.get())
    Bweight = float(var1.get())
    BMI = Bweight / (Bheight * Bheight)
    labelBMIResult.config(text=f"BMI: {BMI:.2f}")

var1 = DoubleVar()
var2 = DoubleVar()

Tops = Frame(root, width=1350, height=50, bd=8, relief="raise", bg=bg_color)
Tops.pack(side=TOP)

f1 = Frame(root, width=600, height=600, bd=8, relief="raise", bg=bg_color)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, bd=8, relief="raise", bg=bg_color)
f2.pack(side=RIGHT)

f1a = Frame(f1, width=600, height=200, bd=20, relief="raise", bg=bg_color)
f1a.pack(side=TOP)
f1b = Frame(f1, width=600, height=600, bd=20, relief='raise', bg=bg_color)
f1b.pack(side=TOP)

label1Title = Label(Tops, text="BODY MASS INDEX", padx=16, pady=16, bd=16, fg=label_color,
                    font=("arial", 54, 'bold'), bg=bg_color, relief='raise', width=32, height=1)
label1Title.pack()

labelweight = Label(f1a, text="Select Weight in Kilograms", font=('arial', 20, 'bold'), bd=20, bg=bg_color, fg=label_color)
labelweight.grid(row=0, column=0)
Bodyweight = Scale(f1a, variable=var1, from_=1, to=500, length=880, tickinterval=30, orient=HORIZONTAL)
Bodyweight.grid(row=1, column=0)

labelheight = Label(f1b, text="Enter Height in Meters Square", font=('arial', 20, 'bold'), bd=20, bg=bg_color, fg=label_color)
labelheight.grid(row=0, column=0)
textheight = Entry(f1b, textvariable=var2, font=('arial', 16, 'bold'), bd=16, width=22, justify='center')
textheight.grid(row=1, column=0)

labelBMIResult = Label(f1b, padx=16, pady=16, bd=16, fg=label_color, font=('arial', 30, 'bold'), bg=bg_color,
                       relief='sunk', width=34, height=1)
labelBMIResult.grid(row=2, column=0)

labelBMITable = Label(f2, font=("arial", 20, 'bold'), text='BMI Table', bg=bg_color, fg=label_color)
labelBMITable.grid(row=0, column=0)
txtlabelBMITable = Text(f2, height=12, width=38, bd=16, font=("arial", 12, 'bold'))
txtlabelBMITable.grid(row=1, column=0)

txtlabelBMITable.insert(END, 'Meaning \t\t' + "BMI \n\n")
txtlabelBMITable.insert(END, 'Normal weight \t\t' + "19-24 \n\n")
txtlabelBMITable.insert(END, 'Overweight \t\t' + "25-29.9 \n\n")
txtlabelBMITable.insert(END, 'Obesity level I \t\t' + "30-34.9 \n\n")
txtlabelBMITable.insert(END, 'Obesity level II \t\t' + "35-39.9\n\n")
txtlabelBMITable.insert(END, 'Obesity level III \t\t' + ">= 40\n\n")

btnBMI = Button(f2, text="Click to\nCheck Your\nBMI", padx=8, pady=8, bd=12, width=21, font=("arial", 20, 'bold'),
                height=3, command=BMI_Cal, bg=button_color, fg=label_color)
btnBMI.grid(row=2, column=0)

root.mainloop()
