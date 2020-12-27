from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x420")
ventana.resizable(0, 0)
ventana.iconbitmap("img/icons8_calculator.ico")
ventana.config(bg="#0D293E")

# ------------------------------------------------------------------------- Caja resultado
numero = StringVar()
caja_resultado = Entry(ventana, bg="Black", fg="Green", font="Dubai 15 bold", insertbackground="Green", width=34)
caja_resultado.config(textvariable=numero)
caja_resultado.place(x=11, y=10)


# ------------------------------------------------------------------------- Caja resultado

# ------------------------------------------------------------------------- Funciones de los botones


def numero_pulsado(n):
    numero.set(numero.get() + n)


def resultado():
    try:
        result = eval(numero.get())
        caja_resultado.delete(0, END)
        caja_resultado.insert(0, result)
    except:
        caja_resultado.delete(0, END)
        caja_resultado.insert(0, "ERROR")


def limpiar():
    caja_resultado.delete(0, END)


# ------------------------------------------------------------------------- Funciones de los botones

# ------------------------------------------------------------------------- Botones
# Primera linea
Button(ventana, text="7", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("7")).place(x=7, y=70)
Button(ventana, text="8", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("8")).place(x=107, y=70)
Button(ventana, text="9", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("9")).place(x=207, y=70)
Button(ventana, text="/", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("/")).place(x=307, y=70)
# Segunda linea
Button(ventana, text="4", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("4")).place(x=7, y=140)
Button(ventana, text="5", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("5")).place(x=107, y=140)
Button(ventana, text="6", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("6")).place(x=207, y=140)
Button(ventana, text="x", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("*")).place(x=307, y=140)
# Tercera fila
Button(ventana, text="1", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("1")).place(x=7, y=210)
Button(ventana, text="2", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("2")).place(x=107, y=210)
Button(ventana, text="3", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("3")).place(x=207, y=210)
Button(ventana, text="-", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("-")).place(x=307, y=210)
# Cuarta fila
Button(ventana, text="0", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("0")).place(x=7, y=280)
Button(ventana, text=",", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado(",")).place(x=107, y=280)
Button(ventana, text="=", bg="Black", fg="Green", font="Dubai 15", width=7, height=1, command=resultado).place(x=207,
                                                                                                               y=280)
Button(ventana, text="+", bg="Black", fg="Green", font="Dubai 15", width=7, height=1,
       command=lambda: numero_pulsado("+")).place(x=307, y=280)

Button(ventana, text="Limpiar", bg="Black", fg="Green", font="Dubai 15",
       width=34, height=1, command=limpiar).place(x=7, y=350)
# ------------------------------------------------------------------------- Botones
ventana.mainloop()
