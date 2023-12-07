import tkinter as tk 

def soma ():
    a = 10
    b = 5 
    print(a + b)

janela = tk.Tk()
janela.title ("Janela")
janela.geometry("500x500")

label = tk.Label(janela, text = "Text")
label.pack()

btn = tk.Button(janela, text = "clique aqui", command= soma)
btn.pack()

janela.mainloop()

