import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Cotação de Moedas")
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

title = tk.Label(text="Sistema de busca de cotação de Moedas", fg="white", bg="black", width=35, height=5)
title.grid(row=0, column=0, columnspan=2, sticky="nsew")

selectCurrency = tk.Label(text="Selecione a moeda desejada")
selectCurrency.grid(row=1, column=0)

dictionaryQuotation = {
    'Dólar': 5.40,
    'Euro': 6.30,
    'Bitcoin': 30000
}

# currencySearchBar = tk.Entry()
# currencySearchBar.grid(row=1, column=1)

currencyDropdown = list(dictionaryQuotation.keys())
currencyDropdown = ttk.Combobox(janela, values=currencyDropdown)
currencyDropdown.grid(row=1, column=1)

def searchQuotation():
    filledCurrency = currencyDropdown.get()
    currencyQuotation = dictionaryQuotation.get(filledCurrency)

    quotationResultMessage = tk.Label(text="Cotação não encontrada", fg='red')
    quotationResultMessage.grid(row=3, column=0)
    
    if currencyQuotation:
        quotationResultMessage["text"] = f"A cotação do {filledCurrency} é R$ {currencyQuotation}"
        quotationResultMessage["fg"] = 'black'

search = tk.Button(text="Buscar cotação", command=searchQuotation)
search.grid(row=2, column=1)

janela.mainloop()
