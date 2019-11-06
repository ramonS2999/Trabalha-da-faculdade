import sqlite3, matplotlib
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox

matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        genero VARCHAR(9) NOT NULL,
        user  VARCHAR(8) NOT NULL,
        pass  VARCHAR(8) NOT NULL,
        nota_1 DECIMAL(4,2),
        nota_2 DECIMAL(4,2),
        media DECIMAL(4,2),
        vezes_f_teste INTEGER,
        cidade TEXT

);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS professor (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        genero VARCHAR(9) NOT NULL,
        user  VARCHAR(8) NOT NULL,
        pass  VARCHAR(8) NOT NULL,
        cidade TEXT
);
""")

conn.commit()
conn.close()


#=======================================================================================================================
#MOSTAR OS RESULTADOS PARA O ALUNO
#=======================================================================================================================
def apresentar_respostas_certas(respostas, respostas_certas, aluno, nota):
    apresentar_respostas = Toplevel(root)
    apresentar_respostas.title("RESULTADO")
    apresentar_respostas.configure(background="#00BFFF")
    apresentar_respostas.geometry("1300x450")
    apresentar_respostas.maxsize(1300, 450)

    frame1 = Frame(apresentar_respostas, width=10, height=10, bd=4, bg="BlueViolet", relief="raise")
    frame1.grid(row=3, column=4, rowspan=2, sticky=W)

    frame2 = Frame(apresentar_respostas, width=10, height=10, bd=4, bg="BlueViolet", relief="raise")
    frame2.grid(row=6, column=4, rowspan=2, sticky=W)


    lb1 = Label(apresentar_respostas, text="Pagina de verificação do resultado do questionario", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 56, "bold"))
    lb1.grid(row=0, column=0, columnspan=10, sticky=W)

    lbl03 = Label(apresentar_respostas, text=300 * "_", bg="DeepSkyBlue")
    lbl03.grid(row=1, column=0, columnspan=10)


    lb = Label(apresentar_respostas, text="Matricula", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb.grid(row=2, column=0, sticky=W)
    lb0 = Label(apresentar_respostas, text=str(aluno[0]), fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb0.grid(row=2, column=1, sticky=W)


    lb2 = Label(apresentar_respostas, text="Aluno" , fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb2.grid(row=3, column=0, sticky=W)
    lb02 = Label(apresentar_respostas, text=str(aluno[1]), fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb02.grid(row=3, column=1, sticky=W)


    lb3 = Label(apresentar_respostas, text="Cidade", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb3.grid(row=4, column=0, sticky=W)
    lb03 = Label(apresentar_respostas, text=str(aluno[9]), fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb03.grid(row=4, column=1, sticky=W)


    lb4 = Label(apresentar_respostas, text="Tentativa", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb4.grid(row=5, column=0, sticky=W)
    lb04 = Label(apresentar_respostas, text=str(aluno[8]), fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb04.grid(row=5, column=1, sticky=W)

    lb6 = Label(apresentar_respostas, text="Nota da Avalição:", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb6.grid(row=6, column=0, sticky=W)
    lb06 = Label(apresentar_respostas, text=str(nota), fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb06.grid(row=6, column=1, sticky=W)

    lb7 = Label(apresentar_respostas, text="Resposta do Aluno", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb7.grid(row=3, column=3, sticky=W)

    lb9 = Label(apresentar_respostas, text="Gabarito", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
    lb9.grid(row=6, column=3, sticky=W)

    for i in range(0, 10):
        lb8 = Label(frame1, text=respostas_certas[i]+" ", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 18, "bold"))
        lb8.grid(row=0, column=i + 3)

    for i in range(0, len(respostas)):
        lb8 = Label(frame1, text=respostas[i]+" ", fg="Black", bg="BlueViolet", font=("Agency FB", 18, "bold"))
        lb8.grid(row=1, column=i + 3)

    for i in range(0, 10):
        lb08 = Label(frame2, text=respostas_certas[i]+" ", fg="Black", bg="BlueViolet", font=("Agency FB", 18, "bold"))
        lb08.grid(row=0, column=i + 3, sticky=W)

    for i in range(10, len(respostas_certas)):
        lb008 = Label(frame2, text=respostas_certas[i]+" ", fg="Black", bg="BlueViolet", font=("Agency FB", 18, "bold"))
        lb008.grid(row=1, column=(i + 3) - 10, sticky=W)

    bt10 = Button(apresentar_respostas, text="VOLTAR", bg="Yellow", fg="MediumBlue", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: area_aluno(aluno, apresentar_respostas))
    bt10.grid(row=8, column=3)
#=======================================================================================================================


#=======================================================================================================================
#VERIFICA AS RESPOETAR CERTAS
#=======================================================================================================================
def verifica_respostas(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, aluno, questionario):
    print("Respostas")
    msg = f'1º: {q1.get()}\n2º: {q2.get()}\n3º: {q3.get()}\n4º: {q4.get()}\n5º: {q5.get()}\n6º: {q6.get()}\n7º: {q7.get()}\n8º: {q8.get()}\n9º: {q9.get()}\n10º: {q10.get()}'
    print(msg)

    respostas_aluno = []
    respostas_certas = ['1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º', '10º', 'd', 'a', 'c', 'e', 'b', 'c', 'e', 'c', 'e', 'a']
    nota = 0

    def letras(letra):
        if letra == 1:
            return 'a'
        elif letra == 2:
            return 'b'
        elif letra == 3:
            return 'c'
        elif letra == 4:
            return 'd'
        elif letra == 5:
            return 'e'
        else:
            return '-'

    if q1.get() == 4:
        respostas_aluno.append("d")
        nota += 1
    else:
        respostas_aluno.append(letras(q1.get()))
    if q2.get() == 1:
        respostas_aluno.append("a")
        nota += 1
    else:
        respostas_aluno.append(letras(q2.get()))
    if q3.get() == 3:
        respostas_aluno.append("c")
        nota += 1
    else:
        respostas_aluno.append(letras(q3.get()))
    if q4.get() == 5:
        respostas_aluno.append("e")
        nota += 1
    else:
        respostas_aluno.append(letras(q4.get()))
    if q5.get() == 2:
        respostas_aluno.append("b")
        nota += 1
    else:
        respostas_aluno.append(letras(q5.get()))
    if q6.get() == 3:
        respostas_aluno.append("c")
        nota += 1
    else:
        respostas_aluno.append(letras(q6.get()))
    if q7.get() == 5:
        respostas_aluno.append("e")
        nota += 1
    else:
        respostas_aluno.append(letras(q7.get()))
    if q8.get() == 3:
        respostas_aluno.append("c")
        nota += 1
    else:
        respostas_aluno.append(letras(q8.get()))
    if q9.get() == 5:
        respostas_aluno.append("e")
        nota += 1
    else:
        respostas_aluno.append(letras(q9.get()))
    if q10.get() == 1:
        respostas_aluno.append("a")
        nota += 1
    else:
        respostas_aluno.append(letras(q2.get()))

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    vezes = aluno[8] + 1

    print(nota)
    print(vezes)
    print(aluno[0])
    print(aluno[5])
    print(aluno[6])
    print(aluno[7])

    if vezes == 1:
        media = nota
        cursor.execute("""
                UPDATE aluno
                SET nota_1 = ?, media = ?,  vezes_f_teste = ?
                WHERE id = ?
                """, (nota, media, vezes, aluno[0]))
    elif vezes == 2:
        media = (aluno[7] + nota) / vezes
        cursor.execute("""
                UPDATE aluno
                SET nota_2 = ?, media = ?, vezes_f_teste = ?
                WHERE id = ?
                """, (nota, media, vezes, aluno[0]))

    cursor.execute("select * from aluno")

    for row in cursor.fetchall():
        print(row[0], row[3], row[4])
        if aluno[0] == row[0]:
            aluno = row
    conn.commit()
    conn.close()

    questionario.destroy()
    apresentar_respostas_certas(respostas_aluno, respostas_certas, aluno, nota)
    print(respostas_aluno)
#=======================================================================================================================


#=======================================================================================================================
#ALTENTICANDO O LOGIN DO ALUNO
#=======================================================================================================================
def aluno_login_def(nome_login, senha_login, aluno_login):
    use = nome_login.get()
    pas = senha_login.get()

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("select * from aluno")

    for row in cursor.fetchall():
        print(row[0], row[3], row[4])
        if use == row[3] and pas == row[4]:
            aluno = row
            conn.commit()
            conn.close()
            area_aluno(aluno, aluno_login)
            return 0

    conn.commit()
    conn.close()

    Label(aluno_login, text="USER OU PASS, INVALIDO!", fg="black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
#=======================================================================================================================


#=======================================================================================================================
#ALGORITIMO DE LOGIN DO PROFESSOR
#=======================================================================================================================
def professor_login_def(nome_login, senha_login, professor_login):
    use = nome_login.get()
    pas = senha_login.get()

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("select * from professor")

    for row in cursor.fetchall():
        print(row[0], row[3], row[4])
        if use == row[3] and pas == row[4]:
            professor = row
            conn.commit()
            conn.close()
            area_professor(professor, professor_login)
            return 0

    conn.commit()
    conn.close()

    Label(professor_login, text="USER OU PASS, INVALIDO!", fg="black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
#=======================================================================================================================



#=======================================================================================================================
#ALGORITIMO DE CADASTRO DO ALUNO
#=======================================================================================================================
def cadastra_aluno_def(nome, user, pas, cidade, sexo):
    nome_1 = nome.get().upper()
    user_1 = user.get()
    pas_1 = pas.get()
    sexo_1 = sexo.get().upper()
    nota_1 = 0.0
    nota_2 = 0.0
    media = 0.0
    vezes_f_teste = 0
    cidade_1 = cidade.get().upper()

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("select * from aluno")

    verifica_senha = True
    for row in cursor.fetchall():
        print(type(str(pas_1)), ' -> ', sexo_1)
        print(type(row[2]), ' -> ', row[2])
        print(type(row[4]), ' -> ', row[4])

        if str(pas_1) == row[4] or pas_1 == '' or pas_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='USE OUTRA SENHA')
            break

        if str(user_1) == row[3] or user_1 == '' or user_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='USEUARIO INVALIDO')
            break

        if (sexo_1 == 'FEMININO' or sexo_1 == 'MASCULINO') == False:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='DEFINA GENERO')
            break

        if nome_1 == '' or nome_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='NOME INVALIUDO')
            break

        if cidade_1 == '' or cidade_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='CIDADE INVALIDA')
            break

        else:
            verifica_senha = True

    if verifica_senha:
        cursor.execute("""
            INSERT INTO aluno (nome, genero, user, pass, nota_1, nota_2, media, vezes_f_teste, cidade)
            VALUES (?,?,?,?,?,?,?,?,?)
            """, (nome_1, sexo_1, user_1, pas_1, nota_1, nota_2, media, vezes_f_teste, cidade_1))

        messagebox.showerror(title='SUCESSO', message='ALUNO CADASTRADO COM SUCESSO')

        conn.commit()
        conn.close()
        return 0

    conn.commit()
    conn.close()
#=======================================================================================================================


#=======================================================================================================================
#ALGORITIMO DE CADASTRO DO PROFESSOR
#=======================================================================================================================
def cadastra_professro_def(nome, user, pas, cidade, sexo):
    nome_1 = nome.get().upper()
    user_1 = user.get()
    pas_1 = pas.get()
    sexo_1 = sexo.get().upper()
    cidade_1 = cidade.get().upper()

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("select * from professor")

    verifica_senha = True
    for row in cursor.fetchall():
        print(type(str(pas_1)), ' -> ', pas_1)
        print(type(row[3]), ' -> ', row[3])
        print(type(row[4]), ' -> ', row[4])
        print(row)

        if str(pas_1) == row[4] or pas_1 == '' or pas_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='USE OUTRA SENHA')
            break

        if str(user_1) == row[3] or user_1 == '' or user_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='USEUARIO INVALIDO')
            break

        if (sexo_1 == 'FEMININO' or sexo_1 == 'MASCULINO') == False:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='DEFINA GENERO')
            break

        if nome_1 == '' or nome_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='NOME INVALIUDO')
            break

        if cidade_1 == '' or cidade_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='CIDADE INVALIDA')
            break

        else:
            verifica_senha = True

    if verifica_senha:
        cursor.execute("""
            INSERT INTO professor (nome, genero, user, pass, cidade)
            VALUES (?,?,?,?,?)
            """, (nome_1, sexo_1, user_1, pas_1, cidade_1))
        messagebox.showerror(title='SUCESSO', message='PROFESSOR CADASTRADO COM SUCESSO')

        conn.commit()
        conn.close()
        return 0

    conn.commit()
    conn.close()
#=======================================================================================================================



#=======================================================================================================================
#MOSTRA ANALISE ESTATISTICA DA TURMA
#=======================================================================================================================
def mostra_dados_estatisticos_turma(professor_aria):
    area_estatistica = Toplevel(professor_aria)
    area_estatistica.geometry("650x500+200+90")
    area_estatistica.configure(background="DeepSkyBlue")
    area_estatistica.title("ANALISE ESTATISTICA DA TURMA")

    # ===================================================================================================================
    # FRAMES QUE ESTÃO SENDO USADOS
    frame1 = Frame(area_estatistica, width=400, height=200, bd=4, bg="GreenYellow", relief="raise")
    frame1.grid(row=0, column=0, rowspan=2)
    #===================================================================================================================

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    #cursor.execute("select * from aluno")
    cursor.execute("SELECT ID FROM aluno WHERE ID IS NULL")
    print(cursor)

    cont = 0
    lista_media = []
    lista_nome = []
    for row in cursor.fetchall():
        aluno = row
        cont += 1
        lista_media.append(aluno[7])
        lista_nome.append(aluno[0])

    # GRAFICO
    figure = Figure(figsize=(cont, cont), dpi=50)
    plt = figure.add_subplot(1, 1, 1)

    y_axis = lista_media
    x_axis = lista_nome
    width_n = 0.4
    bar_color = 'Red'


    plt.bar(x_axis, y_axis, label='MEDIA', width=width_n, color=bar_color)
    plt.legend()

    '''
    x = lista_nome
    y = lista_media
    plot.plot(x, y, color="Blue", marker="x", linestyle="--")
    '''

    canvas = FigureCanvasTkAgg(figure, frame1)
    canvas.get_tk_widget().grid(row=0, column=0)

    conn.commit()
    conn.close()

    area_estatistica.mainloop()
#=======================================================================================================================



#=======================================================================================================================
#MOSTRA OS DADOS ESTATISCOS DO ALUNO
#=======================================================================================================================
def mostra_dados_aluno_professor(aluno, professor_aria):
    aria_professor_aluno = Toplevel(professor_aria)
    aria_professor_aluno.geometry("650x500+200+90")
    #aria_professor_aluno.maxsize(450, 400)
    aria_professor_aluno.configure(background="DeepSkyBlue")
    aria_professor_aluno.title("ÁREA DO ALUNO")

    #===================================================================================================================
    #LABEL PRINCIPAL
    lbl0 = Label(aria_professor_aluno, text="Dados do Aluno", bg="#00BFFF", font="lucida 40 bold", justify=LEFT, padx=14)
    lbl0.grid(row=0, column=0, columnspan=3)

    #===================================================================================================================
    #FRAMES QUE ESTÃO SENDO USADOS
    frame1 = Frame(aria_professor_aluno, width=400, height=200, bd=4, bg="GreenYellow", relief="raise")
    frame1.grid(row=2, column=0, rowspan=2)

    frame2 = Frame(aria_professor_aluno, width=300, height=300, bd=4, bg="GreenYellow", relief="raise")
    frame2.grid(row=2, column=1)

    #===================================================================================================================
    #LABELS QUE EXPLICAM OS DADOS
    lbl1 = Label(frame1, text="Matricula", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1.grid(row=0, column=0, sticky=W)
    lbl1_1 = Label(frame1, text=aluno[0], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1_1.grid(row=0, column=1, sticky=W)

    lbl2 = Label(frame1, text="Nome", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2.grid(row=2, column=0, sticky=W)
    lbl2_1 = Label(frame1, text=aluno[1], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2_1.grid(row=2, column=1, sticky=W)

    lbl3 = Label(frame1, text="1º Nota", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3.grid(row=4, column=0, sticky=W)
    lbl3_1 = Label(frame1, text=aluno[5], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3_1.grid(row=4, column=1, sticky=W)

    lbl4 = Label(frame1, text="2º Nota", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl4.grid(row=6, column=0, sticky=W)
    lbl4_1 = Label(frame1, text=aluno[6], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl4_1.grid(row=6, column=1, sticky=W)

    lbl5 = Label(frame1, text="Media", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl5.grid(row=8, column=0, sticky=W)
    lbl5_1 = Label(frame1, text=aluno[7], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl5_1.grid(row=8, column=1, sticky=W)

    lbl6 = Label(frame1, text="Cidade", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl6.grid(row=10, column=0, sticky=W)
    lbl6_1 = Label(frame1, text=aluno[9], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl6_1.grid(row=10, column=1, sticky=W)

    lbl7 = Label(frame1, text="Genero", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl7.grid(row=12, column=0, sticky=W)
    lbl7_1 = Label(frame1, text=aluno[2], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl7_1.grid(row=12, column=1, sticky=W)

    lbl8 = Label(frame1, text="Feito o testes", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl8.grid(row=14, column=0, sticky=W)
    lbl8_1 = Label(frame1, text=str(aluno[8])+' vezes', bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl8_1.grid(row=14, column=1, sticky=W)

    if float(aluno[7]) < 7 and float(aluno[8]) > 1:
        lbl9 = Label(frame1, text="REPROVADO", bg="Red", font="lucida 14 bold", justify=LEFT, padx=14)
        lbl9.grid(row=16, column=0, sticky=W)

    elif float(aluno[7]) >= 7 and int(aluno[8]) > 1:
        lbl9 = Label(frame1, text="APROVADO", fg='Yellow', bg="Red", font="lucida 14 bold", justify=LEFT, padx=14)
        lbl9.grid(row=16, column=0, sticky=W)

    # ===================================================================================================================
    # GRAFICO 1
    figure = Figure(figsize=(6, 3), dpi=70)
    plot = figure.add_subplot(1, 1, 1)

    plot.plot(10, 10, color="red", marker="o", linestyle="")

    x = ['1°', '2°', 'MEDIA']
    y = [aluno[5], aluno[6], aluno[7]]
    plot.plot(x, y, color="blue", marker="x", linestyle="--")

    canvas = FigureCanvasTkAgg(figure, frame2)
    canvas.get_tk_widget().grid(row=0, column=0)

    # GRAFICO 2
    figure = Figure(figsize=(6, 3), dpi=70)
    plt = figure.add_subplot(1, 1, 1)

    y_axis = [aluno[5]]
    y_axis2 = [aluno[6]]
    y_axis3 = [aluno[7]]

    x_axis = [aluno[5]]
    x_axis2 = [aluno[6]]
    x_axis3 = [aluno[7]]

    width_n = 0.4

    plt.bar(x_axis, y_axis, label='1° NOTA', width=width_n, color="Red")
    plt.legend()

    plt.bar(x_axis2, y_axis2, label='2° NOTA', width=width_n, color="Yellow")
    plt.legend()

    plt.bar(x_axis3, y_axis3, label='MEDIA', width=width_n, color="Blue")
    plt.legend()

    canvas = FigureCanvasTkAgg(figure, frame2)
    canvas.get_tk_widget().grid(row=1, column=0)

    #===================================================================================================================
    #LINHAS
    lbl02 = Label(aria_professor_aluno, text=500 * "_", fg='Black', bg="DeepSkyBlue", font="20")
    lbl02.grid(row=1, column=0, columnspan=25)

    lbl03 = Label(aria_professor_aluno, text=500 * "_", fg='Black', bg="DeepSkyBlue", font="20")
    lbl03.grid(row=4, column=0, columnspan=25)

    i = 1
    while(i < 19):
        lbl04 = Label(frame1, text=100 * "_", bg="GreenYellow")
        lbl04.grid(row=i, column=0, columnspan=10)
        i += 2
#=======================================================================================================================



#=======================================================================================================================
#VERIFICA SE A MATRICULA DIGITADA TEM NO BANCO DE DADOS
#=======================================================================================================================
def pequisa_aluno(pesquisa, professor_aria):
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("select * from aluno")

    for row in cursor.fetchall():
        if row[0] == pesquisa.get():
            aluno = row
            mostra_dados_aluno_professor(aluno, professor_aria)
            conn.commit()
            conn.close()
            return 0


    messagebox.showerror(title='ERROR', message='ALUNO NÃO CADASTRADO')

    conn.commit()
    conn.close()
#=======================================================================================================================



#=======================================================================================================================
#JANELA DO PROFESSOR. É CHAMADA QUANDO O PROFESSOR LOGA!
#=======================================================================================================================
def area_professor(professor, janela):
    professor_aria = Toplevel(root)
    professor_aria.geometry("700x400+200+90")
    professor_aria.configure(background="DeepSkyBlue")
    professor_aria.maxsize(700, 400)
    professor_aria.title("ÁREA DO PROFESSOR")

    sair_janela(janela)

    pesquisa = IntVar()

    lbl0 = Label(professor_aria, text="Área do Professor", bg="DeepSkyBlue", font="lucida 40 bold", justify=LEFT, padx=14)
    lbl0.grid(row=0, column=0, columnspan=2)
    lbl01 = Label(professor_aria, text=200*"_", bg="DeepSkyBlue")
    lbl01.grid(row=1, column=0, columnspan=10)
    lbl02 = Label(professor_aria, text=200*"_", bg="DeepSkyBlue")
    lbl02.grid(row=6, column=0, columnspan=10)
    lbl03 = Label(professor_aria, text=200*"_", bg="DeepSkyBlue")
    lbl03.grid(row=4, column=0, columnspan=10)

    frame1 = Frame(professor_aria, width=400, height=200, bd=4, bg="GreenYellow", relief="raise")
    frame1.grid(row=5, column=0)

    frame2 = Frame(professor_aria, width=300, height=650, bd=4, bg="Lime", relief="raise")
    frame2.grid(row=7, column=0)


    lbl1 = Label(frame1, text="ID: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1.grid(row=0, column=0)
    lbl1_1 = Label(frame1, text=professor[0], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1_1.grid(row=0, column=1)

    lbl2 = Label(frame1, text="Nome: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2.grid(row=1, column=0)
    lbl2_1 = Label(frame1, text=professor[1], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2_1.grid(row=1, column=1)

    lbl3 = Label(frame1, text="Cidade: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3.grid(row=2, column=0)
    lbl3_1 = Label(frame1, text=professor[5], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3_1.grid(row=2, column=1)

    lbl5 = Label(professor_aria, text="Pesquisa Aluno Pela Matricula", bg="DeepSkyBlue", font="lucida 16 bold", justify=LEFT, padx=14)
    lbl5.grid(row=2, column=0, sticky=E)
    entry_pesquisa = Entry(professor_aria, textvariable=pesquisa)
    entry_pesquisa.grid(row=2, column=1, sticky=W)
    bt0 = Button(professor_aria, text="Pesquisar", bg="Crimson", fg="White", font=("Agency FB", 14, "bold"), command=lambda: pequisa_aluno(pesquisa, professor_aria))
    bt0.grid(row=2, column=2, sticky=W)

    lbl6 = Label(professor_aria, text="Análise Estatística da Turma", bg="DeepSkyBlue", font="lucida 16 bold", justify=LEFT, padx=14)
    lbl6.grid(row=3, column=0, sticky=E)
    bt02 = Button(professor_aria, text="  Analise  ", bg="Crimson", fg="White", font=("Agency FB", 14, "bold"), command=lambda: mostra_dados_estatisticos_turma(professor_aria))
    bt02.grid(row=3, column=2, sticky=W)

    bt1 = Button(frame2, text="Cadastar Professor", bg="GreenYellow", fg="Black", font=("Agency FB", 14, "bold"), command=cadastra_professro)
    bt1.grid(row=0, column=0)

    bt2 = Button(frame2, text="Cadastrar Aluno", bg="GreenYellow", fg="Black", font=("Agency FB", 14, "bold"),command=cadastra_aluno)
    bt2.grid(row=0, column=1)

    bt3 = Button(frame2, text="SAIR", bg="GreenYellow", fg="Black", font=("Agency FB", 14, "bold"), command=lambda: sair_janela(professor_aria))
    bt3.grid(row=0, column=2)
#=======================================================================================================================



#=======================================================================================================================
#JANELA DO ALUNO. É CHAMADA QUANDO O ALUNO LOGA!
#=======================================================================================================================
def area_aluno(aluno, janela):
    aluno_aria = Toplevel(root)
    aluno_aria.geometry("670x400+200+90")
    aluno_aria.maxsize(670, 400)
    aluno_aria.configure(background="#00BFFF")
    aluno_aria.title("ÁREA DO ALUNO")

    sair_janela(janela)

    #===================================================================================================================
    #LABELS
    lbl0 = Label(aluno_aria, text="Área do Aluno", bg="#00BFFF", font="lucida 40 bold", justify=LEFT, padx=14)
    lbl0.grid(row=0, column=0, columnspan=3)

    lbl02 = Label(aluno_aria, text=200 * "_", bg="DeepSkyBlue")
    lbl02.grid(row=1, column=0, columnspan=7)

    lbl03 = Label(aluno_aria, text=200 * "_", bg="DeepSkyBlue")
    lbl03.grid(row=3, column=0, columnspan=7)

    #===================================================================================================================
    #FRAMES
    frame1 = Frame(aluno_aria, width=400, height=200, bd=4, bg="#00BFFF", relief="raise")
    frame1.grid(row=2, column=1)

    frame2 = Frame(aluno_aria, width=300, height=650, bd=4, bg="GreenYellow", relief="raise")
    frame2.grid(row=4, column=1)

    #===================================================================================================================
    #BUTÕES
    bt1 = Button(frame1, text="QUESTIONARIO", bg="#00FF00", font="lucida 14 bold", command=lambda: verifica_tentativas(aluno, aluno_aria))
    bt1.grid(row=0, column=0)

    bt3 = Button(frame1, text="NOTAS", bg="#A020F0", font="lucida 14 bold", command=lambda: mostar_noats_aluno(aluno, frame2))
    bt3.grid(row=0, column=1)

    #===================================================================================================================
    #LABELS
    lbl1 = Label(frame2, text="Matricula: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1.grid(row=0, column=0)
    lbl1_1 = Label(frame2, text=aluno[0], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1_1.grid(row=0, column=1)

    lbl2 = Label(frame2, text="Nome: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2.grid(row=1, column=0)
    lbl2_1 = Label(frame2, text=aluno[1], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2_1.grid(row=1, column=1)

    lbl3 = Label(frame2, text="Cidade: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3.grid(row=2, column=0)
    lbl3_1 = Label(frame2, text=aluno[9], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3_1.grid(row=2, column=1)
#=======================================================================================================================


#=======================================================================================================================
#MOSTRA AS NOTAS DO ALUNO
#=======================================================================================================================
def mostar_noats_aluno(aluno, frame2):
    lbl1 = Label(frame2, text="1º Nota: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1.grid(row=3, column=0)
    lbl1_1 = Label(frame2, text=aluno[5], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1_1.grid(row=3, column=1)

    lbl2 = Label(frame2, text="2º Nota: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2.grid(row=4, column=0)
    lbl2_1 = Label(frame2, text=aluno[6], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2_1.grid(row=4, column=1)

    lbl3 = Label(frame2, text="Media: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3.grid(row=5, column=0)
    lbl3_1 = Label(frame2, text=aluno[7], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3_1.grid(row=5, column=1)

    lbl4 = Label(frame2, text="Qt. vezes: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl4.grid(row=6, column=0)
    lbl4_1 = Label(frame2, text=aluno[8], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl4_1.grid(row=6, column=1)
#=======================================================================================================================



#=======================================================================================================================
#VERIFICA AS TENTATIVAS DO ALUNO EM RELAÇÃO AO TESTE
#=======================================================================================================================
def verifica_tentativas(aluno, aluno_aria):
    if aluno[8] < 2:
        questionario_aluno(aluno, aluno_aria)
    else:
        messagebox.showerror(title='ERROR', message='VOCÊ JÁ FEZ O TESTE 2 VEZES!\nNÃO PODE FAZER MAIS!')
#=======================================================================================================================



#=======================================================================================================================
#JANELA DO QUESTINOARIO DO ALUNO
#=======================================================================================================================
def questionario_aluno(aluno, aluno_aria):
    questionario = Toplevel(root)
    questionario.geometry("1050x615+200+80")
    questionario.configure(background="#00BFFF")
    questionario.attributes('-alpha', 0.9)
    questionario.maxsize(1050, 625)
    questionario.title("QUESTIONARIO")

    sair_janela(aluno_aria)


    Tops = Frame(questionario, bg='Lime', width=500, height=650, bd=4, relief="raise")
    Tops.grid(row=0, column=0, columnspan=3)


    frame1 = Frame(questionario, bg='SlateBlue', width=900, height=650, bd=4)
    frame1.grid(row=1, column=0, columnspan=3, sticky=W)

    frame2 = Frame(questionario, bg='SlateBlue', width=900, height=650, bd=4)
    frame2.grid(row=2, column=0, columnspan=3, sticky=W)
    frame3 = Frame(questionario, bg='Lime', width=900, height=650, bd=8, relief="raise")
    frame3.grid(row=3, column=0, sticky=W)
    frame4 = Frame(questionario, width=500, height=180, bd=4)
    frame4.grid(row=3, column=2,  columnspan=4, sticky=W)
    frame5 = Frame(questionario, bg='SlateBlue', width=500, height=500, bd=4)
    frame5.grid(row=3, column=1)

    q1 = IntVar()
    q2 = IntVar()
    q3 = IntVar()
    q4 = IntVar()
    q5 = IntVar()
    q6 = IntVar()
    q7 = IntVar()
    q8 = IntVar()
    q9 = IntVar()
    q10 = IntVar()


    Label(Tops, font=("arial", 30, "bold"), bg='Yellow', text="SISTEMA DE TESTE", bd=4, width=30).grid(row=1, column=0)

    Label(frame1, text="1ª) Quanto é 2 + 2?", fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=0, sticky=W)
    Radiobutton(frame1, text="A)  5", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q1, value=1).grid(row=1, column=0, sticky=W)
    Radiobutton(frame1, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q1, value=2).grid(row=2, column=0, sticky=W)
    Radiobutton(frame1, text="C)  7", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q1, value=3).grid(row=3, column=0, sticky=W)
    Radiobutton(frame1, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q1, value=4).grid(row=4, column=0, sticky=W)
    Radiobutton(frame1, text="E)  1", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q1, value=5).grid(row=5, column=0, sticky=W)

    Label(frame1, text="2ª) Quanto é 2 + 3?", fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=1, sticky=W)
    Radiobutton(frame1, text="A)  5", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q2, value=1).grid(row=1, column=1, sticky=W)
    Radiobutton(frame1, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q2, value=2).grid(row=2, column=1, sticky=W)
    Radiobutton(frame1, text="C)  7", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q2, value=3).grid(row=3, column=1, sticky=W)
    Radiobutton(frame1, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q2, value=4).grid(row=4, column=1, sticky=W)
    Radiobutton(frame1, text="E)  1", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q2, value=5).grid(row=5, column=1, sticky=W)

    Label(frame1, text="3ª) Quanto é 2 + 5?", fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=2, sticky=W)
    Radiobutton(frame1, text="A)  5", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q3, value=1).grid(row=1, column=2, sticky=W)
    Radiobutton(frame1, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q3, value=2).grid(row=2, column=2, sticky=W)
    Radiobutton(frame1, text="C)  7", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q3, value=3).grid(row=3, column=2, sticky=W)
    Radiobutton(frame1, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q3, value=4).grid(row=4, column=2, sticky=W)
    Radiobutton(frame1, text="E)  1", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q3, value=5).grid(row=5, column=2, sticky=W)

    Label(frame1, text="4ª) Quanto é 2 - 1?", fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=3, sticky=W)
    Radiobutton(frame1, text="A)  5", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q4, value=1).grid(row=1, column=3, sticky=W)
    Radiobutton(frame1, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q4, value=2).grid(row=2, column=3, sticky=W)
    Radiobutton(frame1, text="C)  7", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q4, value=3).grid(row=3, column=3, sticky=W)
    Radiobutton(frame1, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q4, value=4).grid(row=4, column=3, sticky=W)
    Radiobutton(frame1, text="E)  1", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q4, value=5).grid(row=5, column=3, sticky=W)

    Label(frame1, text="5ª) Quanto é 2 + 1?  ", fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=4, sticky=W)
    Radiobutton(frame1, text="A)  5", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q5, value=1).grid(row=1, column=4, sticky=W)
    Radiobutton(frame1, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q5, value=2).grid(row=2, column=4, sticky=W)
    Radiobutton(frame1, text="C)  7", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q5, value=3).grid(row=3, column=4, sticky=W)
    Radiobutton(frame1, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q5, value=4).grid(row=4, column=4, sticky=W)
    Radiobutton(frame1, text="E)  1", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q5, value=5).grid(row=5, column=4, sticky=W)

    Label(frame2, text="6ª) Quanto é 2 - 2?", fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=0, sticky=W)
    Radiobutton(frame2, text="A)  5", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q6, value=1).grid(row=1, column=0, sticky=W)
    Radiobutton(frame2, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q6, value=2).grid(row=2, column=0, sticky=W)
    Radiobutton(frame2, text="C)  0", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q6, value=3).grid(row=3, column=0, sticky=W)
    Radiobutton(frame2, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q6, value=4).grid(row=4, column=0, sticky=W)
    Radiobutton(frame2, text="E)  1", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q6, value=5).grid(row=5, column=0, sticky=W)

    Label(frame2, text="7ª) Quanto é 4 + 2?", fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=1, sticky=W)
    Radiobutton(frame2, text="A)  5", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q7, value=1).grid(row=1, column=1, sticky=W)
    Radiobutton(frame2, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q7, value=2).grid(row=2, column=1, sticky=W)
    Radiobutton(frame2, text="C)  7", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q7, value=3).grid(row=3, column=1, sticky=W)
    Radiobutton(frame2, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q7, value=4).grid(row=4, column=1, sticky=W)
    Radiobutton(frame2, text="E)  6", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q7, value=5).grid(row=5, column=1, sticky=W)

    Label(frame2, text="8ª) Quanto é 4 + 3?", fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=2, sticky=W)
    Radiobutton(frame2, text="A)  5", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q8, value=1).grid(row=1, column=2, sticky=W)
    Radiobutton(frame2, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q8, value=2).grid(row=2, column=2, sticky=W)
    Radiobutton(frame2, text="C)  7", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q8, value=3).grid(row=3, column=2, sticky=W)
    Radiobutton(frame2, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q8, value=4).grid(row=4, column=2, sticky=W)
    Radiobutton(frame2, text="E)  1", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q8, value=5).grid(row=5, column=2, sticky=W)

    Label(frame2, text="9ª) Quanto é 4 + 4?", fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=3, sticky=W)
    Radiobutton(frame2, text="A)  5", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q9, value=1).grid(row=1, column=3, sticky=W)
    Radiobutton(frame2, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q9, value=2).grid(row=2, column=3, sticky=W)
    Radiobutton(frame2, text="C)  7", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q9, value=3).grid(row=3, column=3, sticky=W)
    Radiobutton(frame2, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q9, value=4).grid(row=4, column=3, sticky=W)
    Radiobutton(frame2, text="E)  8", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q9, value=5).grid(row=5, column=3, sticky=W)

    Label(frame2, text="10ª) Quanto é 3 + 3?",fg='White', bg='SlateBlue', font="lucida 14 bold", justify=LEFT, padx=14).grid(row=0, column=4, sticky=W)
    Radiobutton(frame2, text="A)  6", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q10, value=1).grid(row=1, column=4, sticky=W)
    Radiobutton(frame2, text="B)  3", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q10, value=2).grid(row=2, column=4, sticky=W)
    Radiobutton(frame2, text="C)  7", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q10, value=3).grid(row=3, column=4, sticky=W)
    Radiobutton(frame2, text="D)  4", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q10, value=4).grid(row=4, column=4, sticky=W)
    Radiobutton(frame2, text="E)  1", fg='Black', bg='SlateBlue', font="lucida 10 bold", padx=14, variable=q10, value=5).grid(row=5, column=4, sticky=W)
    

    bt1 = Button(frame3, text="FINALIZAR", bg="Yellow", fg="#0000CD", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: verifica_respostas(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, aluno, questionario))
    bt1.pack()

    Label(frame3,text=" ", fg='Lime', bg='Lime').pack()

    bt1 = Button(frame3, text="VOLTAR", bg="Yellow", fg="#0000CD", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: area_aluno(aluno, questionario))
    bt1.pack()


    lbl1 = Label(frame4, text="Matricula: ", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl1.grid(row=0, column=0, sticky=W)
    lbl1_1 = Label(frame4, text=str(aluno[0]), bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl1_1.grid(row=0, column=1, columnspan=2, sticky=W)


    lbl2 = Label(frame4, text="Nome: ", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl2.grid(row=1, column=0, sticky=W)
    lbl2_1 = Label(frame4, text=str(aluno[1]), bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl2_1.grid(row=1, column=1, columnspan=2, sticky=W)


    lbl3 = Label(frame4, text="Cidade: ", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl3.grid(row=2, column=0, sticky=W)
    lbl3_1 = Label(frame4, text=str(aluno[9]), bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl3_1.grid(row=2, column=1, columnspan=2, sticky=W)


    lbl4 = Label(frame4, text=str(aluno[8]+1)+"º", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl4.grid(row=3, column=0, sticky=W)
    lbl4_1 = Label(frame4, text="Tentativa ", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl4_1.grid(row=3, column=1, columnspan=2, sticky=W)


    photo = PhotoImage(file="logo_fatepi.png")
    label = Label(frame5, image=photo)
    label.grid()

    questionario.mainloop()
#=======================================================================================================================

def sair():
    root.destroy()

def sair_janela(janela):
    janela.destroy()


#=======================================================================================================================
#TELA QUE O PROFESSOR COLOCARÁ USUÁRIO E SENHA!
#=======================================================================================================================
def login_professor():
    professor_login = Toplevel(root)
    professor_login.title("LOGIN PROFESSOR")
    professor_login.configure(background="DeepSkyBlue")
    professor_login.geometry("240x310+1000+370")
    professor_login.maxsize(240, 310)

    lb1 = Label(professor_login, text="Por favor insira seus dados abaixo", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 16, "bold"))
    lb1.pack()
    Label(professor_login, text="", bg="DeepSkyBlue").pack()

    nome_login = StringVar()
    senha_login = StringVar()

    frame1 = Frame(professor_login, width=900, height=650, bg="DeepSkyBlue", bd=8, relief="raise")
    frame1.pack()

    lb2 = Label(frame1, text="User ", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 13, "bold"))
    lb2.pack()

    nome_entry = Entry(frame1, textvariable=nome_login)
    nome_entry.pack()

    lb4 = Label(frame1, text="Pass ", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 13, "bold"))
    lb4.pack()

    senha_entry = Entry(frame1, show="☻", textvariable=senha_login)
    senha_entry.pack()

    lb5 = Label(frame1, text="", bg="DeepSkyBlue")
    lb5.pack()

    frame2 = Frame(frame1, width=5, height=5, bg="DeepSkyBlue", bd=4, relief="raise")
    frame2.pack()

    bt1 = Button(frame2, text="Login", bg="Yellow", fg="Black", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: professor_login_def(nome_login, senha_login, professor_login))
    bt1.pack()

    lb6 = Label(frame1, text="", bg="DeepSkyBlue")
    lb6.pack()
#=======================================================================================================================


#=======================================================================================================================
#TELA QUE O ALUNO COLOCARÁ USUÁRIO E SENHA!
#=======================================================================================================================
def login_aluno():
    aluno_login = Toplevel(root)
    aluno_login.title("LOGIN ALUNO")
    aluno_login.configure(background="DeepSkyBlue")
    aluno_login.geometry("240x310+1000+20")
    aluno_login.maxsize(240, 310)

    lb1 = Label(aluno_login, text="Por favor insira seus dados abaixo", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 16, "bold"))
    lb1.pack()
    Label(aluno_login, text="", bg="DeepSkyBlue").pack()

    frame1 = Frame(aluno_login, width=900, height=650, bg="DeepSkyBlue", bd=8, relief="raise")
    frame1.pack()

    nome_login = StringVar()
    senha_login = StringVar()

    lb2 = Label(frame1, text="User ", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 13, "bold"))
    lb2.pack()

    nome_entry = Entry(frame1, textvariable=nome_login)
    nome_entry.pack()

    lb4 = Label(frame1, text="Pass ", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 13, "bold"))
    lb4.pack()

    senha_entry = Entry(frame1, show="☻", textvariable=senha_login)
    senha_entry.pack()

    lb5 = Label(frame1, text="", bg="DeepSkyBlue")
    lb5.pack()

    frame2 = Frame(frame1, width=5, height=5, bg="DeepSkyBlue", bd=4, relief="raise")
    frame2.pack()

    bt1 = Button(frame2, text="Login", bg="Yellow", fg="Black", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: aluno_login_def(nome_login, senha_login, aluno_login))
    bt1.pack()

    lb6 = Label(frame1, text="", bg="DeepSkyBlue")
    lb6.pack()
#=======================================================================================================================


#=======================================================================================================================
#TELA DE CADASTRO DO PROFESSOR
#=======================================================================================================================
def cadastra_professro():
    professro_cadastra = Toplevel(root)
    professro_cadastra.title("CADASTRAR PROFESSOR")
    professro_cadastra.configure(background="#00BFFF")
    professro_cadastra.geometry("300x550+660+80")
    professro_cadastra.maxsize(300, 550)


    Label(professro_cadastra, text="", bg="#00BFEF").pack()
    frame1 = Frame(professro_cadastra, width=900, height=650, bg="#00BFFF", bd=8, relief="raise")
    frame1.pack()

    nome = StringVar()
    user = StringVar()
    pas = StringVar()
    sexo = StringVar()
    cidade = StringVar()

    Label(frame1, text="Por favor insira seus dados abaixo", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    Label(frame1, text="", bg="#00BFFF").pack()

    Label(frame1, text="Nome completo ", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    nome_entry = Entry(frame1, textvariable=nome)
    nome_entry.pack()

    Label(frame1, text="Cidade ", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    cidade_entry = Entry(frame1, textvariable=cidade)
    cidade_entry.pack()

    sexo1 = Radiobutton(frame1, text='Feminino', bg="#00BFFF", variable=sexo, value='FEMININO', font=("Agency FB", 13, "bold"))
    sexo1.pack()
    sexo2 = Radiobutton(frame1, text='Masculino', bg="#00BFFF", variable=sexo, value='MASCULINO', font=("Agency FB", 13, "bold"))
    sexo2.pack()

    Label(frame1, text="", bg="#00BFFF").pack()

    Label(frame1, text="User ", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    use_entry = Entry(frame1, textvariable=user)
    use_entry.pack()

    Label(frame1, text="Pass ", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    senha_entry = Entry(frame1, show="☺", textvariable=pas)
    senha_entry.pack()

    Label(frame1, text="", bg="#00BFFF").pack()
    bt1 = Button(frame1, text="OK", bg="#FFFF00", fg="Black", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: cadastra_professro_def(nome, user, pas, cidade, sexo))
    bt1.pack()

    Label(frame1, text="", bg="#00BFFF").pack()

    professro_cadastra.mainloop()
#=======================================================================================================================


#=======================================================================================================================
#TELA DE CADASTRO DO ALUNO
#=======================================================================================================================
def cadastra_aluno():
    aluno_cadastra = Toplevel(root)
    aluno_cadastra.title("CADASTRAR ALUNO")
    aluno_cadastra.configure(background="#00BFEF")
    aluno_cadastra.geometry("300x550+350+80")
    aluno_cadastra.maxsize(350, 550)

    Label(aluno_cadastra, text="", bg="#00BFEF").pack()
    frame1 = Frame(aluno_cadastra, width=900, height=650, bg="#00BFFF", bd=8, relief="raise")
    frame1.pack()

    nome = StringVar()
    user = StringVar()
    pas = StringVar()
    sexo = StringVar()
    cidade = StringVar()


    Label(frame1, text="Por favor insira seus dados abaixo", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    Label(frame1, text="", bg="#00BFFF").pack()

    Label(frame1, text="Nome completo ", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    nome_entry_completo = Entry(frame1, textvariable=nome)
    nome_entry_completo.pack()

    Label(frame1, text="Cidade ", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    nome_entry_cidade = Entry(frame1, textvariable=cidade)
    nome_entry_cidade.pack()

    sexo1 = Radiobutton(frame1, text='Feminino', bg="#00BFFF", variable=sexo, value='Feminino', font=("Agency FB", 13, "bold"))
    sexo1.pack()
    sexo2 = Radiobutton(frame1, text='Masculino', bg="#00BFFF", variable=sexo, value='Masculino', font=("Agency FB", 13, "bold"))
    sexo2.pack()

    Label(frame1, text="", bg="#00BFFF").pack()

    Label(frame1, text="User ", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    nome_entry_login = Entry(frame1, textvariable=user)
    nome_entry_login.pack()

    Label(frame1, text="Pass ", fg="Black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
    senha_entry_login = Entry(frame1, show="☺", textvariable=pas)
    senha_entry_login.pack()

    Label(frame1, text=" ", bg="#00BFFF").pack()
    bt1 = Button(frame1, text="OK", bg="#FFFF00", fg="Black", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: cadastra_aluno_def(nome, user, pas, cidade, sexo))
    bt1.pack()
    Label(frame1, text="", bg="#00BFFF").pack()

    aluno_cadastra.mainloop()
#=======================================================================================================================



#=======================================================================================================================
#JANELA PRINCIPAL: ONDE O CODIGO CHAMA AS FUNÇÕES
#=======================================================================================================================
def main():
    global root
    root = Tk()
    root.geometry("300x100+50+200")
    root.maxsize(300, 190)
    root.title("MENU")
    root.attributes('-alpha', 0.9)
    root.configure(background="DarkRed")

    menu = Menu(root)
    root.config(menu=menu)
    sub_menu1 = Menu(menu)
    sub_menu2 = Menu(menu)
    sub_menu3 = Menu(menu)

    photo = PhotoImage(file="logo_fatepi.png")
    label = Label(root, image=photo)
    label.pack()

    menu.add_cascade(label="LOGIN", menu=sub_menu1)
    sub_menu1.add_command(label="Aluno", command=login_aluno)
    sub_menu1.add_separator()
    sub_menu1.add_command(label="Professor", command=login_professor)

    menu.add_cascade(label="CADASTRO", menu=sub_menu2)
    sub_menu2.add_command(label="Aluno", command=cadastra_aluno)
    sub_menu2.add_separator()
    sub_menu2.add_command(label="Professor", command=cadastra_professro)

    menu.add_cascade(label="SAIR", menu=sub_menu3)
    sub_menu3.add_command(label="Sair", command=sair)

    root.mainloop()
#=======================================================================================================================

#CHAMADA DO PROGRAMA
main()
