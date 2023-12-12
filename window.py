from tkinter import *
import json
# lista = ['abc','pipas','aque libas','pintoca', 'chapei dois dedos no peito']
# def auau():
#     a = enty_of_append.get()
#     if a == 'pipas':
#         return True
#     else:
#         return a
# def uuu():
#     a = auau()
#     if a == True:
#         label_bg.config(image=img_)
#     else:
#         enty_of_append.delete(0,END)
#         global lista
#         lista.append(a)
#         c = '\n'.join(f'{valor+1}- {item}'for valor,item in enumerate(lista))
#         listas.config(text=c)
#         pipas()


# def pipas():
#     listi_box.delete(0, END)
#     for valor,item in enumerate(lista, start=0):
#         listi_box.insert(END,f'{valor+1}- {item}')
        
# b = '\n'.join(f'{valor+1}- {item}'for valor,item in enumerate(lista))



# window = Tk()
# #configuração da janela
# window.geometry('500x500')
# window.title(f'Super Foco')
# window.resizable(False,False)

# #Imagens adicionadas
# img_bg = PhotoImage(file="img_1\\Adicione metas.png")
# img_bt = PhotoImage(file="img_1\\Adicionar.png")
# img_ = PhotoImage(file="img\\pagina pronta.png")
# #fundo
# label_bg = Label(window,image=img_bg)
# label_bg.pack()


# listas = Label(window,background='#d9d9d9', text=b)
# listas.place(relx=0.08,rely=0.55,relwidth=0.83,relheight=0.18)

# #input
# enty_of_append = Entry(window,border=4,justify='center',font=("Helvetica",20))
# enty_of_append.place(relx=0.04,rely=0.36,width=639,height=48)
# #botao de adicionar
# button_of_butom = Button(window,image=img_bt,border=3, command=uuu)
# button_of_butom.place(relx=0.40,rely=0.78,width=141,height=70)

# scrollbar = Scrollbar(window)
# scrollbar.place(relx=0.91, rely=0.55, relheight=0.18)

# listi_box = Listbox(window, selectmode=SINGLE, width=30, yscrollcommand=scrollbar.set)
# listi_box.place(relx=0.08, rely=0.55, relwidth=0.83, relheight=0.18)
# scrollbar.config(command=listi_box.yview)
# for valor, item in enumerate(lista, start=0):
#     listi_box.insert(END, f'{valor}- {item}')
# window.mainloop()







b = ''
def listando():
    with open("alek.json","r") as file:
        data = json.load(file)
    a = etry_all.get()
    write = ''
    if a == 'PUSSY':
        return a
    if not a.isdigit():
        global lista
        data["lista_caraio"].append(a)
        with open("alek.json","w") as file:
            json.dump(data,file)
        return True
    elif a == 'PUSSY':
        return a
    else:
        write = 'Isso é um numero'
        return write


def removendo():
    with open("alek.json","r") as file:
        data = json.load(file)
    a = etry_all.get()
    l = len(data["lista_caraio"]) -1
    if int(a) >l:
        return False        
    else:
        data["lista_caraio"].pop(int(a))
        with open("alek.json","w") as file:
            json.dump(data,file)
        return True
    
def hora():

    a= etry_all.get()
    if not a.isdigit():
        return 'Nao é um numero'
    else:
        global b
        b = int(a)
        data["hours"] = b
        with open("alek.json","w") as file:
            json.dump(data,file)
        return True

def rem():
    with open("alek.json","r") as file:
        data = json.load(file)
    a = removendo()
    lb_error.config(text='')
    if a == True:
        list_box_goals.delete(0,END)
        for item, valor in enumerate(data["lista_caraio"],start=0):
            list_box_goals.insert(END,f'{item} - {valor}')
    else:
        lb_error.config(text=f'O numero não tem na lista..')

def hour():
    with open("alek.json","r") as file:
        data = json.load(file)
    a = hora()

    if a == True:
        lb_time_alarme.config(text='')
        lb_time_alarme.config(text=data["hours"])
    else:
        lb_error.config(text=a)
        

def resp():
    with open("alek.json","r") as file:
        data = json.load(file)
    a = listando()
    lb_error.config(text='')
    if a == True:
        list_box_goals.delete(0,END)
        for item, valor in enumerate(data["lista_caraio"],start=0):
            list_box_goals.insert(END,f'{item} - {valor}')
    elif a == 'PUSSY':
        bg.config(image=lp)
    else:
        lb_error.config(text=a)



CAMINHO_DA_IMAGEM = 'img'

principal = Tk()
 #configuração da janela
principal.geometry('800x800')
principal.title(f'Super Foco')
principal.resizable(False,False)

lp = PhotoImage(master=principal,file='img_1\\arumentos ou lambida7.png')
img_bg = PhotoImage(master=principal,file=f'{CAMINHO_DA_IMAGEM}\\pagina_1.png')
img_button_add = PhotoImage(file=f'{CAMINHO_DA_IMAGEM}\\adicionar_lista.png')
img_button_remove = PhotoImage(file=f'{CAMINHO_DA_IMAGEM}\\remover_lista.png')
img_button_time = PhotoImage(file=f'{CAMINHO_DA_IMAGEM}\\alterar_horario.png')
img_button_alarm = PhotoImage(file=f'{CAMINHO_DA_IMAGEM}\\alterar_data.png')

#background
bg= Label(principal,image=img_bg)
bg.pack()

#label hora e data 
lb_time_alarme = Label(principal)
lb_date = Label(principal)
lb_time_alarme.place(relx=0.25,rely=0.13,width=100,height=50)
lb_date.place(relx=0.76,rely=0.13,width=100,height=50)


# lb_date.config(text=data["timer"])
# lb_time_alarme.config(text=data["hours"])
#botao adicionar
bt_add = Button(principal,border=3,image=img_button_add,command=resp)#, command=add)
bt_add.place(relx=0.10,rely=0.33,width=100,height=50)

#botao remover
bt_remove = Button(principal,border=3,image=img_button_remove,command= rem)#,command=remove2)
bt_remove.place(relx=0.27,rely=0.33,width=100,height=50)

#botao alterar hora do alarme
bt_time = Button(principal,border=3,image=img_button_time,command=hour)#, command=change_hour)
bt_time.place(relx=0.60,rely=0.33,width=100,height=50)

#botao alterar data do fim do alarme
bt_end_alarm = Button(principal,border=3,image=img_button_alarm)#,command=change_date)
bt_end_alarm.place(relx=0.77,rely=0.33,width=100,height=50)

#entry input
etry_all  = Entry(principal,justify='center')
etry_all.place(relx=0.03,rely=0.43,width=752,height=49)

#LABEL DE ERROS 
lb_error = Label(principal)
lb_error.place(relx=0.03,rely=0.50,width=752,height=19)
lb_error.config(text='')

#Barra de rolagem 
bar_scroll = Scrollbar(principal,)
bar_scroll.place(relx=0.949, rely=0.53,width=23,height=350)

# # list box com as metas da lista
list_box_goals = Listbox(principal,selectmode=SINGLE, yscrollcommand=bar_scroll.set,font=("Arial",18))
list_box_goals.place(relx=0.03,rely=0.53,width=732,height=350)
bar_scroll.config(command=list_box_goals.yview)
with open("alek.json","r") as file:
    data = json.load(file)
lista = data["lista_caraio"]
for item, valor in enumerate(lista,start=0):
    list_box_goals.insert(END,f'{item} - {valor}')
def loop():
    principal.mainloop()


loop()