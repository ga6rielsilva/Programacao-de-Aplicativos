import tkinter as tk

janela = tk.Tk()

promotion = tk.IntVar()
checkboxPromotion = tk.Checkbutton(text="Deseja receber e-mails promocionais?", variable=promotion)
checkboxPromotion.grid(row=0, column=0)

termsPrivacy = tk.IntVar()
checkboxTerms = tk.Checkbutton(text="Aceitar os Termos de Uso e Políticas de Privacidade", variable=termsPrivacy)
checkboxTerms.grid(row=1, column=0)

def send():
    if promotion.get():
        print("O usuário deseja receber e-mails promocionais!", promotion.get())
    else:
        print("O usuário não deseja receber e-mails promocionais!", promotion.get())
    if termsPrivacy.get():
        print("O usuário aceitou os Termos de Uso e Políticas de Privacidade!", termsPrivacy.get())
    else:
        print("O usuário não aceitou os Termos de Uso e Políticas de Privacidade!", termsPrivacy.get())

sendPromotionButton = tk.Button(text="Enviar", command=send)
sendPromotionButton.grid(row=2, column=0)

janela.mainloop()