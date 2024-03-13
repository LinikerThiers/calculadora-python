from tkinter import *


#cores
cor_preta = "#3b3b3b"
cor_branca = "#feffff"
cor_cinza_escuro = "#7a7878"
cor_cinza = "#ECEFF1"
cor_laranja = "#FFAB40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor_preta)

#partes da calculadora
frame_display = Frame(janela, width=235, height=50, bg=cor_preta)
frame_display.grid(row=0, column=0)

frame_botoes = Frame(janela, width=235, height=268, bg=cor_preta)
frame_botoes.grid(row=1, column=0)

# funcionalidade da calculadora
valor_string = StringVar()
todos_valores = ''


def entrada_valores(valor):
    global todos_valores

    todos_valores = todos_valores + str(valor)
    valor_string.set(todos_valores)


def resultado():
    try:
        global todos_valores
        if '///' in todos_valores:
            valor_string.set('Equação Inválida.')
        
        if '**' in todos_valores:
            valor_string.set('Equação Inválida.')

        if '*-+' in todos_valores:
            valor_string.set('Equação Inválida.')

        if '*+-' in todos_valores:

            valor_string.set('Equação Inválida.')

        else:
            resultado = eval(todos_valores)
            todos_valores = str(resultado)
            valor_string.set(resultado)
    except SyntaxError:
        valor_string.set('Equação Inválida')
    except ZeroDivisionError:
        valor_string.set('Equação Inválida')

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_string.set('')
    

#Label
app_label = Label(frame_display, textvariable=valor_string, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, bg=cor_preta, fg=cor_branca, font=("Ivy 17 bold"))
app_label.place(x=0, y=0)

#Botoes
button_C = Button(frame_botoes, command=limpar_tela, text="C", width=11, height=2, bg=cor_cinza_escuro, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_C.place(x=0, y=0)
button_modulo = Button(frame_botoes, command=lambda: entrada_valores('%'), text="M", width=5, height=2, bg=cor_cinza_escuro, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_modulo.place(x=120, y=0)
button_barr = Button(frame_botoes, command=lambda: entrada_valores('/'), text="/", width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_barr.place(x=180, y=0)

button_7 = Button(frame_botoes, command=lambda: entrada_valores('7'), text="7", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_7.place(x=0, y=52)
button_8 = Button(frame_botoes, command=lambda: entrada_valores('8'), text="8", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_8.place(x=60, y=52)
button_9 = Button(frame_botoes, command=lambda: entrada_valores('9'), text="9", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_9.place(x=120, y=52)
button_multi = Button(frame_botoes, command=lambda: entrada_valores('*'), text="x", width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_multi.place(x=180, y=52)

button_4 = Button(frame_botoes, command=lambda: entrada_valores('4'), text="4", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_4.place(x=0, y=104)
button_5 = Button(frame_botoes, command=lambda: entrada_valores('5'), text="5", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_5.place(x=60, y=104)
button_6 = Button(frame_botoes, command=lambda: entrada_valores('6'), text="6", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_6.place(x=120, y=104)
button_subtr = Button(frame_botoes, command=lambda: entrada_valores('-'), text="-", width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_subtr.place(x=180, y=104)

button_1 = Button(frame_botoes, command=lambda: entrada_valores('1'), text="1", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_1.place(x=0, y=156)
button_2 = Button(frame_botoes, command=lambda: entrada_valores('2'), text="2", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_2.place(x=60, y=156)
button_3 = Button(frame_botoes, command=lambda: entrada_valores('3'), text="3", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=120, y=156)
button_adic = Button(frame_botoes, command=lambda: entrada_valores('+'), text="+", width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_adic.place(x=180, y=156)

button_0 = Button(frame_botoes, command=lambda: entrada_valores('0'), text="0", width=11, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_0.place(x=0, y=208)
button_ponto = Button(frame_botoes, command=lambda: entrada_valores('.'), text=".", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_ponto.place(x=120, y=208)
button_igual = Button(frame_botoes, command=resultado, text="=", width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_igual.place(x=180, y=208)



janela.mainloop()