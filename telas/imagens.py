from tkinter import Label, Toplevel, Tk, Button, Entry
from PIL import ImageTk, Image
from tratar_dados.tratamento_dados_cadastro import tratamento_registro_cadastro
global tupla

def front():
    root = Tk()
    root.geometry("550x500")
    root.title('Pleno Sono')

    logo = ImageTk.PhotoImage(Image.open("logo.png"))
    lg = Label(image = logo)


    def cad():

        def confi():

            res = tratamento_registro_cadastro(
                nome.get().upper(),
                cnpj.get().upper(),
                contato.get().upper(),
                nf.get().upper(),
                pai.get().upper(),
                pecas.get().upper()
            )
            print(res)
            resultado = Toplevel(cadastro)
            resposta = Label(resultado, text = res, font = 25, padx = 25, pady = 10)
            ok = Button(resultado, text = "Confirmar", command = resultado.destroy)

            resposta.pack()
            ok.pack()
            

        cadastro = Toplevel(root)
        cadastro.geometry("500x500")
        cadastro.title("Cadastro")

        mens1 = Label(cadastro, text = "Nome Real", font = 25, padx = 50, pady = 25)
        mens2 = Label(cadastro, text = "CNPJ", font = 25, padx = 50, pady = 25)
        mens3 = Label(cadastro, text = "Contato", font = 25, padx = 50, pady = 25)
        mens4 = Label(cadastro, text = "Niível de Formação", font = 50, padx = 25, pady = 25)
        mens5 = Label(cadastro, text = "Nome do Pai", font = 25, padx = 50, pady = 25)
        mens6 = Label(cadastro, text = "Peças vendidas", font = 25, padx = 50, pady = 25)

        mens1.grid(row = 0, column = 0)
        mens2.grid(row = 1, column = 0)
        mens3.grid(row = 2, column = 0)
        mens4.grid(row = 3, column = 0)
        mens5.grid(row = 4, column = 0)
        mens6.grid(row = 5, column = 0)

        nome = Entry(cadastro, width = 30, font = 25)
        cnpj = Entry(cadastro, width = 30, font = 25)
        contato = Entry(cadastro, width = 30, font = 25)
        nf = Entry(cadastro, width = 30, font = 25)
        pai = Entry(cadastro, width = 30, font = 25)
        pecas = Entry(cadastro, width = 30, font = 25)

        nome.grid(row = 0, column = 1)
        cnpj.grid(row = 1, column = 1)
        contato.grid(row = 2, column = 1)
        nf.grid(row = 3, column = 1)
        pai.grid(row = 4, column = 1)
        pecas.grid(row = 5, column = 1)

        confirmar = Button(cadastro, text = "Confirmar", font = 20, command = confi)

        confirmar.grid(row = 6, column = 0)

    def alt():
        altCadastro = Toplevel(root)
        altCadastro.geometry("500x500")
        altCadastro.title("Alterar Cadastro")
        
    def gerar():
        gera = Toplevel(root)
        gera.geometry("500x500")
        gera.title("Gerar Relatório")

    def vis():
        visualizar = Toplevel(root)
        visualizar.geometry("500x500")
        visualizar.title("Visualizar Distribuidor")

    Cadas_Dist = Button(root, text = "Cadastrar Distribuidor", font = 20, command = cad)
    Alt_Dist = Button(root, text = "Alterar Distribuidor", font = 20, command = alt)
    Ger_Rel = Button(root, text = "Gerar Relatório", font = 20, command = gerar)
    Vis_Dist = Button(root, text = "Visualizar Distribuidor", font = 20, command = vis)

    Cadas_Dist.grid(row = 0, column = 0, padx = 50, pady = 50)
    Alt_Dist.grid(row = 0, column = 1, padx = 50, pady = 50)

    lg.grid(row = 1, column = 0, columnspan = 2)

    Ger_Rel.grid(row = 2, column = 0, padx = 50, pady = 50)
    Vis_Dist.grid(row = 2, column = 1, padx = 50, pady = 50)


    root.mainloop()