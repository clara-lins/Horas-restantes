from tkinter import *

win= Tk()
win.title("Situação Acadêmica")
win.geometry("700x420")
win.iconbitmap('c:/Users/clara/OneDrive/Área de Trabalho/IMPORTANTE/Interface/brasaoufba.ico')

horas_cumpridas= LabelFrame(win, text= "Horas já cumpridas", padx=100, pady=100)
horas_cumpridas.pack(padx=10, pady=10)

ac_label= Label(horas_cumpridas, text= "Atividade Complementar")
lv_label= Label(horas_cumpridas, text="Componente Livre")
ob_label= Label(horas_cumpridas, text="Componente Obrigatório")
op_label= Label(horas_cumpridas, text="Optativa Grande Área")
oph_label= Label(horas_cumpridas, text="Optativa Humanística")
opa_label= Label(horas_cumpridas, text= "Optativa Artística")

ac= Entry(horas_cumpridas, width=40, borderwidth=2 )
lv=Entry(horas_cumpridas, width=40, borderwidth=2 )
ob=Entry(horas_cumpridas, width=40, borderwidth=2 )
op=Entry(horas_cumpridas, width=40, borderwidth=2 )
oph=Entry(horas_cumpridas, width=40, borderwidth=2 )
opa=Entry(horas_cumpridas, width=40, borderwidth=2 )

ac.insert(0, "0 0 0 0")
lv.insert(0, "0 0 0 0")
ob.insert(0, "0 0 0 0")
op.insert(0, "0 0 0 0")
oph.insert(0, "0 0 0 0")
opa.insert(0, "0 0 0 0")


ac_label.grid(row= 0,column= 0)
ac.grid(row=0, column=1)
lv_label.grid(row=1 ,column=0 )
lv.grid(row=1 ,column= 1)
ob_label.grid(row= 2,column= 0)
ob.grid(row=2 ,column= 1)
op_label.grid(row= 3,column= 0)
op.grid(row= 3,column= 1)
oph_label.grid(row= 4,column= 0)
oph.grid(row= 4,column= 1)
opa_label.grid(row= 5,column= 0)
opa.grid(row= 5,column= 1)
erro= Label(horas_cumpridas, text= "")
erro.grid(row=6, column=0)

def listas(num):
    num= [int(x) for x in num.split()]
    num= sum(num)
    return num

def horas_restantes():
    global erro
    erro.grid_forget()
    ativ_c= listas(ac.get())
    comp_livre= listas(lv.get())
    obrig= listas(ob.get())
    optativa= listas(op.get())
    humanistica= listas(oph.get())
    artistica= listas(opa.get())
    try :
        ativ_c, comp_livre, obrig, optativa, humanistica, artistica= int(ativ_c), int(comp_livre), int(obrig), int(optativa), int(humanistica), int(artistica)
        ativ_c= 360- ativ_c
        comp_livre= 476- comp_livre
        obrig= 476- obrig
        optativa= 816- optativa
        humanistica= 136-humanistica
        artistica=136- artistica
        ativ_c, comp_livre, obrig, optativa, humanistica, artistica= str(ativ_c), str(comp_livre), str(obrig), str(optativa), str(humanistica), str(artistica)
        
        root= Toplevel()
        root.title("Situação Acadêmica")
        root.geometry("500x420")
        root.iconbitmap('c:/Users/clara/OneDrive/Área de Trabalho/IMPORTANTE/Interface/brasaoufba.ico')
        cumpridas= LabelFrame(root, text= "Horas Restantes", padx=100, pady=100)
        cumpridas.pack(padx=10, pady=10)
        ac_label= Label(cumpridas, text= "Atividade Complementar = "+ ativ_c)
        lv_label= Label(cumpridas, text="Componente Livre = " + comp_livre)
        ob_label= Label(cumpridas, text="Componente Obrigatório = " + obrig)
        op_label= Label(cumpridas, text="Optativa Grande Área = " + optativa)
        oph_label= Label(cumpridas, text="Optativa Humanística = "+ humanistica)
        opa_label= Label(cumpridas, text= "Optativa Artística = " + artistica)
        
        ac_label.grid(row=0, column=0)
        lv_label.grid(row=1, column=0)
        ob_label.grid(row=2, column=0)
        op_label.grid(row=3, column=0)
        oph_label.grid(row=4, column=0)
        opa_label.grid(row=5, column=0)



    except ValueError:
        erro= Label(horas_cumpridas, text="Erro no preenchimento", bg= "red")
        erro.grid(row=6, column=0, columnspan=2)
checar= Button(win, text= "Checar", command= horas_restantes)
checar.pack()

win.mainloop()