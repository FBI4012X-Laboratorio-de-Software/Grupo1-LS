from tkinter import Label, Toplevel, Tk, Button, Entry
from PIL import ImageTk, Image
from tratar_dados.tratamento_dados_cadastro import tratamento_registro_cadastro
from internal.get_filhos import get_filhos

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
            
            if res != "Sucesso":
                resultado = Toplevel(cadastro)
                resultado.geometry("300x80")

                resposta = Label(resultado, text = res, font = 25, padx = 25, pady = 10)
                ok = Button(resultado, text = "Confirmar", font = 25, command = resultado.destroy)

                resposta.pack()
                ok.pack()
            else:
                sucesso = Toplevel(cadastro)
                sucesso.geometry("300x80")

                nome.delete(0, 'end')
                cnpj.delete(0, 'end') 
                contato.delete(0, 'end')
                nf.delete(0, 'end')
                pai.delete(0, 'end')
                pecas.delete(0, 'end')

                cadsuc = Label(sucesso, text = "Cadastro feito com sucesso!", font = 25, padx = 25, pady = 10)
                ok2 = Button(sucesso, text = "Confirmar", font = 25, command = sucesso.destroy)

                cadsuc.pack()
                ok2.pack()
            return

        cadastro = Toplevel(root)
        cadastro.geometry("520x500")
        cadastro.title("Cadastro")

        mens1 = Label(cadastro, text = "Nome Real", font = 25, padx = 50, pady = 25)
        mens2 = Label(cadastro, text = "CNPJ", font = 25, padx = 50, pady = 25)
        mens3 = Label(cadastro, text = "Contato", font = 25, padx = 50, pady = 25)
        mens4 = Label(cadastro, text = "Nível de Formação", font = 50, padx = 25, pady = 25)
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

        confirmar = Button(cadastro, text = "Confirmar", font = 25, command = confi)
        confirmar.grid(row = 6, column = 0)

        volt1 = Button(cadastro, text = "Voltar", font = 25, command = cadastro.destroy)
        volt1.grid(row = 6, column = 1)

    def vis():

        def confirm():
            labels = []
            cn = get_filhos(cnpjf.get().upper())
            
            visu = Toplevel(visualizar)
            
            del labels[:] # remove any previous labels from if the callback was called before

            if not cn:
                visu.geometry("400x70")
                nomeNulo = Label(visu, text = "Nome em branco ou nenhuma relação encontrada.", font = 25)
                nomeNulo.pack()
                volt2 = Button(visu, text = "Voltar", font = 25, command = visu.destroy)
                volt2.pack()
                return
            
            newList = []
            
            nomehead = Label(visu, text = "Nome", font = 20, padx = 10, pady =10)
            cnpjhead = Label(visu, text = "CNPJ", font = 20, padx = 10, pady =10)
            contatohead = Label(visu, text = "Contato", font = 20, padx = 10, pady =10)
            nivelhead = Label(visu, text = "Nível", font = 20, padx = 10, pady =10)
            paihead = Label(visu, text = "Pai", font = 20, padx = 10, pady =10)
            pecashead = Label(visu, text = "Peças", font = 20, padx = 10, pady =10)

            nomehead.grid(row = 0, column = 0, sticky = "W" )
            cnpjhead.grid(row = 0, column = 1, sticky = "W" )
            contatohead.grid(row = 0, column = 2, sticky = "W" )
            nivelhead.grid(row = 0, column = 3, sticky = "W" )
            paihead.grid(row = 0, column = 4, sticky = "W" )
            pecashead.grid(row = 0, column = 5, sticky = "W" )

            for i in cn:
                newList.append(str(i).split(","))

            rowk = 1

            for i in newList:

                column = 0

                for j in i:
                    labels = Label(visu, text = j)
                    labels.grid(row = rowk, column = column, padx = 10, pady =10, sticky = "W")
                    column +=1
                rowk += 1

            xiao = Button(visu, text = "Confirmar", font = 20, command = visu.destroy)
            xiao.grid(row = rowk, column = 2)
                            
        visualizar = Toplevel(root)
        visualizar.geometry("500x120")
        visualizar.title("Visualizar Distribuidor")
        
        mens7 = Label(visualizar, text = "Informe o CNPJ ou nome", font = 25, padx = 50, pady = 25)
        mens7.grid(row = 0, column = 0)
        cnpjf = Entry(visualizar, width = 20, font = 25)
        cnpjf.grid(row = 0, column = 1)

        volt = Button(visualizar, text = "Voltar", font = 25, command = visualizar.destroy)
        volt.grid(row = 1, column = 0)

        conf = Button(visualizar, text = "Confirmar", font = 25, command = confirm)
        conf.grid(row = 1, column = 1)

    def alt():
        altCadastro = Toplevel(root)
        altCadastro.geometry("500x500")
        altCadastro.title("Alterar Cadastro")
        
    def gerar():
        gera = Toplevel(root)
        gera.geometry("500x500")
        gera.title("Gerar Relatório")



    Cadas_Dist = Button(root, text = "Cadastrar Distribuidor", font = 25, command = cad)
    Alt_Dist = Button(root, text = "Alterar Distribuidor", font = 25, command = alt)
    Ger_Rel = Button(root, text = "Gerar Relatório", font = 25, command = gerar)
    Vis_Dist = Button(root, text = "Visualizar Distribuidor", font = 25, command = vis)

    Cadas_Dist.grid(row = 0, column = 0, padx = 50, pady = 50)
    Alt_Dist.grid(row = 0, column = 1, padx = 50, pady = 50)

    lg.grid(row = 1, column = 0, columnspan = 2)

    Ger_Rel.grid(row = 2, column = 0, padx = 50, pady = 50)
    Vis_Dist.grid(row = 2, column = 1, padx = 50, pady = 50)


    root.mainloop()