# Bibliotecas.
import tkinter as tk
import customtkinter as ctk

# Constantes.
COR_FUNDO = '#EBEBEB'
FONTE = ('Arial', 18)
TAM_BUTTON = 100

# Definir configurações.
ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def operacao(operador):
    try:
        numero1 = int(number1.get())
        numero2 = int(number2.get())

        if operador == '+':
            resultado = numero1 + numero2
        elif operador == '-':
            resultado = numero1 - numero2
        elif operador == '*':
            resultado = numero1 * numero2
        elif operador == '/':
            resultado = '{:.2f}'.format(numero1 / numero2)
        elif operador == '//':
            resultado = numero1 // numero2
        elif operador == '**':
            resultado = numero1 ** numero2
        elif operador == '%':
            resultado = numero1 % numero2
        else:
            resultado = 'Operador inválido'
    except ValueError:
        resultado = 'Erro: Números inválidos'
    
    text_var.set(f"{resultado}")


# Criar app e suas propriedades.
app = ctk.CTk()  # create CTk window like you do with the Tk window
width_screen = app.winfo_screenwidth()     # largura da tela.
height_screen = app.winfo_screenheight()   # altura da tela.

# Colocar no centro da tela.
width_janela = 400                        # largura da janela.
height_janela = 500                       # altura da janela.
app.geometry("{}x{}+{}+{}".format(width_janela, height_janela, int(width_screen/2) - int(width_janela/2), int(height_screen/2) - int(height_janela/2)))
app.title('Calculadora')
app.resizable(False, False)

frame_vazio = ctk.CTkFrame(app, fg_color=COR_FUNDO, width=25, height=25)
frame_vazio.grid(row=0, column=0)

text_number1_label = ctk.CTkLabel(app, text='Número 1:')
text_number1_label.grid(row=1, column=1)

text_number2_label = ctk.CTkLabel(app, text='Número 2:')
text_number2_label.grid(row=1, column=3)

number1 = ctk.CTkEntry(app, width=TAM_BUTTON)
number1.grid(row=2, column=1)

number2 = ctk.CTkEntry(app, width=TAM_BUTTON)
number2.grid(row=2, column=3)

frame_vazio = ctk.CTkFrame(app, fg_color=COR_FUNDO, width=25, height=25)
frame_vazio.grid(row=3, column=0)

text_operacao_label = ctk.CTkLabel(app, text='Operações:')
text_operacao_label.grid(row=4, column=1, columnspan=3)

button_adicao = ctk.CTkButton(app, text='+', width=TAM_BUTTON, height=50, font=FONTE, command=lambda: operacao('+'))
button_adicao.grid(row=5, column=1, padx=5, pady= 5)

button_subtracao = ctk.CTkButton(app, text='-', width=TAM_BUTTON, height=50, font=FONTE, command=lambda: operacao('-'))
button_subtracao.grid(row=5, column=2, padx=5, pady= 5)

button_multiplicacao = ctk.CTkButton(app, text='*', width=TAM_BUTTON, height=50, font=FONTE, command=lambda: operacao('*'))
button_multiplicacao.grid(row=5, column=3, padx=5, pady= 5)

button_divisao = ctk.CTkButton(app, text='/', width=TAM_BUTTON, height=50, font=FONTE, command=lambda: operacao('/'))
button_divisao.grid(row=6, column=1, padx=5, pady= 5)

button_divisao_inteira = ctk.CTkButton(app, text='//', width=TAM_BUTTON, height=50, font=FONTE, command=lambda: operacao('//'))
button_divisao_inteira.grid(row=6, column=2, padx=5, pady= 5)

button_potencia = ctk.CTkButton(app, text='**', width=TAM_BUTTON, height=50, font=FONTE, command=lambda: operacao('**'))
button_potencia.grid(row=6, column=3, padx=5, pady= 5)

button_resto = ctk.CTkButton(app, text='%', width=TAM_BUTTON*3 + (4*5), height=50, font=FONTE, command=lambda: operacao('%'))
button_resto.grid(row=7, column=1, columnspan=3, padx=5, pady= 5)

frame_vazio = ctk.CTkFrame(app, fg_color=COR_FUNDO, width=25, height=25)
frame_vazio.grid(row=8, column=0)

text_resultado_label = ctk.CTkLabel(app, text='Resultado:')
text_resultado_label.grid(row=9, column=1, columnspan=3)

text_var = tk.StringVar(value="")
resultado_label = ctk.CTkLabel(app, fg_color='#Bfc4c5', width=TAM_BUTTON*3 + (4*5), height=65, textvariable=text_var)
resultado_label.grid(row=10, column=1, columnspan=3)

app.mainloop()
