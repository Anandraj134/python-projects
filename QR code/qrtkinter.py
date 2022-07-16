import pyqrcode
from tkinter import *
from tkinter import messagebox


def generateQR():
    ipstring = enterTextField.get()
    scale = enterScaleField.get()
    if len(scale):
        try:
            scale = int(scale)
        except:
            messagebox.showerror("Error",
                                 "Scale should be integer values.")
            return
    else:
        scale = 5
    if len(ipstring):
        qrCode = pyqrcode.create(ipstring)
        qrCode.svg("qrcode.svg", scale=scale)
        messagebox.showinfo('Sucess',
                            'Your QR code is generated and save in the current folder')
    else:
        messagebox.showerror('Error', "Text field is empty")


def clearAll():
    enterTextField.delete(0, END)
    enterTextField.focus_set()


if __name__ == "__main__":
    window = Tk()
    window.configure(background='Light blue')
    window.geometry("1280x720")
    window.title("QR CODE GENERSTOR")
    enterTextLabel = Label(window, text="Enter Text", fg= 'black', font=("Arial", 20))
    enterTextLabel.grid(row=2, column=1, sticky="E", padx="10", pady="50")
    enterScaleLabel = Label(window, text="Enter Scale", fg= 'black', font=("Arial", 20))
    enterScaleLabel.grid(row=4, column=1, sticky="E", padx="10", pady="10")
    enterTextField = Entry(window,font="Arial 30", width=20)
    enterTextField.grid(row=2, column=2, sticky="E", padx="10", pady="10")
    enterScaleField = Entry(window,font="Arial 30", width=20)
    enterScaleField.grid(row=4, column=2, sticky="E", pady="10")
    generateButton = Button(window, text="Generate", bg="red", fg="black", command=generateQR, font=30)
    clearButton = Button(window, text="Clear", bg="red", fg="black", command=clearAll, font=30)
    generateButton.grid(row=8, column=2, padx="20", pady="20")
    clearButton.grid(row=10, column=2, pady="5")
    window.mainloop()

