from tkinter import *

class Projeto:
    def __init__(self, master=None):
        self.master = master
        self.usuarios = Frame(master)
        self.fontePadrao = ('Arial', 12)
        self.usuarios.pack()

        self.usu = Button(self.usuarios, text='Usuários', font=self.fontePadrao)
        self.usu.pack(side=LEFT)

        self.cid = Button(self.usuarios, text='Cidades', font=self.fontePadrao)
        self.cid.pack(side=LEFT)

        self.cli = Button(self.usuarios, text='Clientes', font=self.fontePadrao)
        self.cli.pack(side=LEFT)

        self.fec = Button(self.usuarios, text='Fechar', font=self.fontePadrao, command=self.master.quit)
        self.fec.pack(side=LEFT)

root = Tk()
Projeto(root)
root.state("zoomed")
root.mainloop()
