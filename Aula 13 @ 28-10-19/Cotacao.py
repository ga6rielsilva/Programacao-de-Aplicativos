import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Cotação de Moedas")
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

title = tk.Label(text="Sistema de busca de cotação de Moedas", fg="white", bg="black", width=35, height=5)
title.grid(row=0, column=0, columnspan=2, sticky="nsew")

selectCurrencyMessage = tk.Label(text="Selecione a moeda desejada")
selectCurrencyMessage.grid(row=1, column=0)

dictionaryQuotation = {
    'Dólar': 5.78,
    'Euro': 6.32,
    'Bitcoin': 378000.75
}

def searchQuotation():
    filledCurrency = currencyDropdown.get()
    currencyQuotation = dictionaryQuotation.get(filledCurrency)

    quotationResultMessage = tk.Label(text="Cotação não encontrada", fg='red')
    quotationResultMessage.grid(row=3, column=0, sticky="nsew")

    if currencyQuotation:
        quotationResultMessage["text"] = f"A cotação do {filledCurrency} é R$ {currencyQuotation}"
        quotationResultMessage["fg"] = "black"

# currencySearchBar = tk.Entry()
# currencySearchBar.grid(row=1, column=1)

currencyDropdown = list(dictionaryQuotation.keys())
currencyDropdown = ttk.Combobox(janela, values=currencyDropdown)
currencyDropdown.grid(row=1, column=1)

search = tk.Button(text="Buscar cotação", command=searchQuotation)
search.grid(row=2, column=1)

def searchMultipleQuotations():
    filledCurrencies = multipleQuotationBar.get("1.0", tk.END)
    listCurrencies = filledCurrencies.split("\n")
    quotationMessage = []

    for currency in listCurrencies:
        if currency:
            currencyQuotation = dictionaryQuotation.get(currency)
            if currencyQuotation:
                quotationMessage.append(f"A cotação do {currency} é R$ {currencyQuotation}")
            else:
                quotationMessage.append(f"A cotação do \"{currency}\" não foi encontrada")

    multipleQuotationResultMessage = tk.Label(text="\n".join(quotationMessage), fg='red')
    multipleQuotationResultMessage.grid(row=6, column=1, sticky="nsew")

multipleQuotationMessage = tk.Label(text="Informe mais de uma cotação ao mesmo tempo abaixo")
multipleQuotationMessage.grid(row=4, column=0, columnspan=2, sticky="nsew")

multipleQuotationBar = tk.Text(width=10, height=5)
multipleQuotationBar.grid(row=5, column=0, sticky="nswe")

searchMultiple = tk.Button(text="Buscar cotações", command=searchMultipleQuotations)
searchMultiple.grid(row=5, column=1)

janela.mainloop()
