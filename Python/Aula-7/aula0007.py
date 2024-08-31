import tkinter as tk

root = tk.Tk()
root.title("Raiz Quadrada")


num = int(input('Digite um numero: '))
from math import sqrt
raiz = sqrt(num)

label = tk.Label(root, text=f'A raiz quadrada de {num} e {raiz}')
label.pack()

root.mainloop()
