from tkinter.filedialog import askopenfilename
import pandas as pd

archiveDirectory = askopenfilename(title="Selecione um arquivo excel para abrir")
df = pd.read_excel(archiveDirectory)

print(df)