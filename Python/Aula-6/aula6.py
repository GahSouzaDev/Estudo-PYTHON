import tkinter as tk

# Crie uma janela
janela = tk.Tk()
janela.title("Meu Programa")

# Crie um label
label = tk.Label(janela, text="Olá, mundo!")
label.pack()

# Crie um botão
botao = tk.Button(janela, text="Clique aqui", command=lambda: print("Você clicou!"))
botao.pack()

# Inicie a janela
janela.mainloop()
