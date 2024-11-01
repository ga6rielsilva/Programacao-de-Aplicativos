import tkinter as tk

def openWindow():
    newWindow = tk.Toplevel()
    newWindow.title("Nova janela")
    closeButton = tk.Button(newWindow, text="Fechar", command=newWindow.destroy)
    closeButton.grid(row=1, column=0)

window = tk.Tk()
openButton = tk.Button(window, text="Abrir uma janela nova", command=openWindow)
openButton.grid(row=2, column=3)

window.mainloop()