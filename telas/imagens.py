from tkinter import *
from tkinter import ttk
from datetime import datetime
from PIL import ImageTk, Image
from tratar_dados.tratamento_dados_cadastro import tratamento_registro_cadastro, find_dis
from internal.gera_comissao import gera_comissao
from internal.get_filhos import get_filhos

global tupla

def front():
    root = Tk()
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    positionRight = int(root.winfo_screenwidth()/8 - windowWidth/5)
    positionDown = int(root.winfo_screenheight()/8 - windowHeight/5)

    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.title('Pleno Sono')

    logo = ImageTk.PhotoImage(Image.open("logo.png"))
    lg = Label(image = logo)

    def cad():
        
        def confi():
            res = tratamento_registro_cadastro(
                nome.get().upper(),
                cnpj.get().upper(),
                contato.get().upper(),
                comboExample.get().upper(),
                pai.get().upper(),
                pecas.get().upper()
            )
            
            if res != "Sucesso":
                resultado = Toplevel(cadastro)
                resultado.geometry("+{}+{}".format(positionRight, positionDown))

                resposta = Label(resultado, text = res, font = 25, padx = 25, pady = 10)
                ok = Button(resultado, text = "Confirmar", font = 25, command = resultado.destroy)
                espaco = Label(resultado, text = " ")

                resposta.grid()
                ok.grid()
                espaco.grid()

            else:
                sucesso = Toplevel(cadastro)
                sucesso.geometry("+{}+{}".format(positionRight, positionDown))

                nome.delete(0, 'end')
                cnpj.delete(0, 'end') 
                contato.delete(0, 'end')
                pai.delete(0, 'end')
                pecas.delete(0, 'end')

                cadsuc = Label(sucesso, text = "Cadastro feito com sucesso!", font = 25, padx = 25, pady = 10)
                ok2 = Button(sucesso, text = "Confirmar", font = 25, command = sucesso.destroy)
                espaco900 = Label(sucesso, text = " ")

                cadsuc.grid()
                ok2.grid()
                espaco900.grid()
            return

        cadastro = Toplevel(root)

        cadastro.geometry("+{}+{}".format(positionRight, positionDown))
        cadastro.title("Cadastro")

        comboExample = ttk.Combobox(cadastro, values=[
                                    "Indicador",
                                    "Assistente de Vendedor",
                                    "Vendedor",
                                    "Assistente de Distribuidor",
                                    "Distribuidor",
                                    "Distribuidor Senior",
                                    "Distribuidor de Carreira",
                                    "Distribuidor Nato"], state="readonly") 
        comboExample.current(1)

        mens1 = Label(cadastro, text = "Nome Real", font = 25, padx = 50, pady = 25)
        mens2 = Label(cadastro, text = "CNPJ ou CPF", font = 25, padx = 50, pady = 25)
        mens3 = Label(cadastro, text = "Contato", font = 25, padx = 50, pady = 25)
        mens4 = Label(cadastro, text = "Nível de Formação", font = 50, padx = 25, pady = 25)
        mens5 = Label(cadastro, text = "Nome do Pai", font = 25, padx = 50, pady = 25)
        mens6 = Label(cadastro, text = "Peças vendidas", font = 25, padx = 50, pady = 25)
        espaco360 = Label(cadastro, text = " ")

        mens1.grid(row = 0, column = 0)
        mens2.grid(row = 1, column = 0)
        mens3.grid(row = 2, column = 0)
        mens4.grid(row = 3, column = 0)
        mens5.grid(row = 4, column = 0)
        mens6.grid(row = 5, column = 0)

        nome = Entry(cadastro, width = 40, font = 25)
        cnpj = Entry(cadastro, width = 40, font = 25)
        contato = Entry(cadastro, width = 40, font = 25)
        pai = Entry(cadastro, width = 40, font = 25)
        pecas = Entry(cadastro, width = 40, font = 25)

        nome.grid(row = 0, column = 1)
        cnpj.grid(row = 1, column = 1)
        contato.grid(row = 2, column = 1)
        comboExample.grid(row = 3, column = 1)
        pai.grid(row = 4, column = 1)
        pecas.grid(row = 5, column = 1)
        espaco360.grid(row = 0, column = 2)

        confirmar = Button(cadastro, text = "Confirmar", font = 25, command = confi)
        confirmar.grid(row = 6, column = 1)

        volt1 = Button(cadastro, text = "Voltar", font = 25, command = cadastro.destroy)
        volt1.grid(row = 6, column = 0)

        espaco = Label(cadastro, text = " ")
        espaco.grid(row = 7, column = 0)

    def vis():

        def confirm():
            labels = []
            cn = get_filhos(cnpjf.get().upper())
            
            visu = Toplevel(visualizar)
            
            del labels[:] # remove any previous labels from if the callback was called before

            if not cn:
                visu.geometry("+{}+{}".format(positionRight, positionDown))
                nomeNulo = Label(visu, text = "Nome em branco ou nenhum distribuidor encontrado.", font = 25, padx = 20)
                nomeNulo.grid()
                volt2 = Button(visu, text = "Voltar", font = 25, command = visu.destroy)
                volt2.grid()

                espaco3 = Label(visu, text = " ")
                espaco3.grid()
                return
            
            newList = []
            
            visu.geometry("+{}+{}".format(positionRight, positionDown))

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
            xiao.grid(row = rowk, column = 2, columnspan = 2)

            espaco13 = Label(visu, text = " ")
            espaco13.grid()
                            
        visualizar = Toplevel(root)
        visualizar.geometry("+{}+{}".format(positionRight, positionDown))
        visualizar.title("Visualizar Distribuidor")
        
        mens7 = Label(visualizar, text = "Informe o CNPJ ou nome.", font = 25, padx = 50, pady = 25)
        mens7.grid(row = 0, column = 0)
        cnpjf = Entry(visualizar, width = 40, font = 25)
        cnpjf.grid(row = 0, column = 1)
        espaco4 = Label(visualizar, text = " ")
        espaco4.grid(row = 0, column = 2)

        volt = Button(visualizar, text = "Voltar", font = 25, command = visualizar.destroy)
        volt.grid(row = 1, column = 0)

        conf = Button(visualizar, text = "Confirmar", font = 25, command = confirm)
        conf.grid(row = 1, column = 1)

        espaco1 = Label(visualizar, text = " ")
        espaco1.grid(row = 2, column = 0)

    def gerar():

        def pegadados():
            
            encontrou = find_dis(entrygera.get().upper())
            if encontrou == False:
                find_dis_resultado = Toplevel(gera)
                find_dis_resultado.geometry("+{}+{}".format(positionRight, positionDown))

                aviso_de_erro = Label(find_dis_resultado, text = "Nome, CNPJ ou CPF em branco ou não encontrado.", font = 25, padx = 25, pady = 10)
                aviso_de_erro.pack()

                aviso_conf = Button(find_dis_resultado, text = "Confirmar", font = 25, command = find_dis_resultado.destroy)
                aviso_conf.pack()

                espaco24 = Label(find_dis_resultado, text = " ")
                espaco24.pack()
                return

            distribuidor_seleciona = entrygera.get().upper()

            monthir = str(mes_combo.current()+1)

            if monthir > "10":
                monthir = "0" + monthir
            datainirec = str(dia_combo.get() + "/"  + monthir + "/" + year_combo.get())
            
            try:
                date_time_obj = datetime.strptime(datainirec, '%d/%m/%Y')
            except ValueError :
                aviso = Toplevel(gera)
                aviso.geometry("+{}+{}".format(positionRight, positionDown))

                dataerradai = Label(aviso, text = "Data inicial seleciona inexistente.", font = 25, padx = 25, pady = 10) 
                dataerradai.pack()

                botao_voltar = Button(aviso, text = "Confirmar", font = 25, command = aviso.destroy)
                botao_voltar.pack()

                espaco245 = Label(dataerradai, text = " ")
                espaco245.pack()
                return

            monthfr = str(mes_combof.current()+1)
            if monthir > "10":
                monthir = "0" + monthfr
            datainirec = str(dia_combof.get() + "/"  + monthfr + "/" + year_combof.get())
            try:
                date_time_objf = datetime.strptime(datainirec, '%d/%m/%Y')
            except ValueError :
                aviso1 = Toplevel(gera)
                aviso1.geometry("+{}+{}".format(positionRight, positionDown))

                dataerradaf = Label(aviso1, text = "Data final seleciona inexistente.", font = 25, padx = 25, pady = 10) 
                dataerradaf.pack()

                botao_voltar = Button(aviso1, text = "Confirmar", font = 25, command = aviso1.destroy)
                botao_voltar.pack()

                espaco246 = Label(dataerradaf, text = " ")
                espaco246.pack()
                return

            comissao = gera_comissao(distribuidor_seleciona, date_time_obj, date_time_objf)
            comissao_tela = Toplevel(gera)
            comissao_tela.geometry("+{}+{}".format(positionRight, positionDown))

            ind_comissao = Label(comissao_tela, text = f'Comissão gerada: {comissao}', font = 25, padx = 25, pady = 10)
            ind_comissao.pack()

            destruir_tela = Button(comissao_tela, text = "Confirmar", font = 25, command = comissao_tela.destroy)
            destruir_tela.pack()

            espaco23 = Label(comissao_tela, text = " ")
            espaco23.pack()
            print(comissao)

            return

        gera = Toplevel(root)
        gera.geometry("+{}+{}".format(positionRight, positionDown))
        gera.title("Gerar Relatório")

        nocncp = Label(gera, text = "Digite nome, CNPJ ou CPF do Distribuidor.", font = 25, padx = 50, pady = 25)
        entrygera = Entry(gera, width = 40, font = 25)

        datai = Label(gera, text = "Data Incial", font = 25, padx = 50, pady = 25)
        dataf = Label(gera, text = "Data Final", font = 25, padx = 50, pady = 25)

        nocncp.grid(row = 0, column = 0)
        entrygera.grid(row = 0, column = 1, columnspan = 5)

        ########### DATA INICIAL ###################################

        dia_combo = ttk.Combobox(gera, values=[
                                                "1","2","3","4","5","6",
                                                "7","8","9","10","11","12",
                                                "13","14","15","16","17","18",
                                                "19","20","21","22","23","24",
                                                "25","26","27","28","29","30","31"], state="readonly") 
        dia_combo.current(0)

        mes_combo = ttk.Combobox(gera, values=[
                                                "Janeiro","Fevereiro","Março",
                                                "Abril","Maio","Junho",
                                                "Julho","Agosto","Setembro",
                                                "Outubro","Novembro","Dezembro"], state = "readonly")
    
        mes_combo.current(datetime.today().month - 1)

        currentYear = datetime.today().year

        year = int(currentYear)

        year_combo = ttk.Combobox(gera, values = [f'{year-3}' f'{year-2}', f'{year-1}', f'{year}', f'{year+1}', f'{year+2}' f'{year+3}'
        ], state = "readonly")
        year_combo.current(2)

        ########### DATA FINAL ###################################

        dia_combof = ttk.Combobox(gera, values=[
                                                "1","2","3","4","5","6",
                                                "7","8","9","10","11","12",
                                                "13","14","15","16","17","18",
                                                "19","20","21","22","23","24",
                                                "25","26","27","28","29","30","31"], state="readonly") 
        dia_combof.current(datetime.today().day - 1)

        mes_combof = ttk.Combobox(gera, values=[
                                                "Janeiro","Fevereiro","Março",
                                                "Abril","Maio","Junho",
                                                "Julho","Agosto","Setembro",
                                                "Outubro","Novembro","Dezembro"], state = "readonly")
    
        mes_combof.current(datetime.today().month-1)

        year_combof = ttk.Combobox(gera, values = [f'{year-2}', f'{year-1}', f'{year}', f'{year+1}', f'{year+2}'
        ], state = "readonly")
        year_combof.current(2)

        espaco5 = Label(gera, text = " ")

        datai.grid(row = 1, column = 0)
        dataf.grid(row = 2, column = 0)

        dia_combo.grid(row = 1, column = 1)
        mes_combo.grid(row = 1, column = 2)
        year_combo.grid(row = 1, column = 3)

        dia_combof.grid(row = 2, column = 1)
        mes_combof.grid(row = 2, column = 2)
        year_combof.grid(row = 2, column = 3)

        espaco5.grid(row = 1, column = 4)

        volt1 = Button(gera, text = "Voltar", font = 25, command = gera.destroy)
        volt1.grid(row = 3, column = 0)

        conf1 = Button(gera, text = "Confirmar", font = 25, command = pegadados)
        conf1.grid(row = 3, column = 2)

        espaco2 = Label(gera, text = " ")
        espaco2.grid(row = 4, column = 0)

    def alt():
        altCadastro = Toplevel(root)
        altCadastro.title("Alterar Cadastro")
        
    Cadas_Dist = Button(root, text = "Cadastrar Distribuidor", font = 100, command = cad)
    Alt_Dist = Button(root, text = "Alterar Distribuidor", font = 100, command = alt)
    Ger_Rel = Button(root, text = "Gerar Relatório", font = 100, command = gerar)
    Vis_Dist = Button(root, text = "Visualizar Distribuidor", font = 100, command = vis)
    Sair = Button(root, text = "Sair",  font = 100, command = root.destroy)

    prenche = Label(root, text = "     ")
    prenche2 = Label(root, text = "     ")
    
    Cadas_Dist.grid(row = 0, column = 0, padx = 50, pady = 50)
    Alt_Dist.grid(row = 0, column = 2, padx = 50, pady = 50)

    lg.grid(row = 1, column = 1)

    Ger_Rel.grid(row = 2, column = 0, padx = 50, pady = 50)
    Vis_Dist.grid(row = 2, column = 2, padx = 50, pady = 50)

    Sair.grid(row = 4, column = 1, padx = 50, pady = 50)


    root.mainloop()