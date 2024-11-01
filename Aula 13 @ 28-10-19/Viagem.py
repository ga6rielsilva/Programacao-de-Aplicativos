import tkinter as tk

janela = tk.Tk()

plane = tk.StringVar()

economicClass = tk.Radiobutton(text="Classe Econômica", value="Classe Econômica")
executiveClass = tk.Radiobutton(text="Classe Executiva", value="Classe Executiva")
firstClass = tk.Radiobutton(text="Primeira Classe", value="Primeira Classe")

economicClass.grid(row=0, column=0)
executiveClass.grid(row=0, column=1)
firstClass.grid(row=0, column=2)

def send():
    if plane.get():
        print(f"O usuário escolheu a opção: {plane.get()}")
    else:
        print("Por favor selecione uma das três opções!")

sendButton = tk.Button(text="Enviar", command=send)
sendButton.grid(row=1, column=1)

tk.mainloop()