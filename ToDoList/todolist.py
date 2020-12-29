from tkinter import *
from tkinter import messagebox
import sqlite3

ventana_todo = Tk()
ventana_todo.title("ToDo List")
centrar_ventana = 1080 - 700
ventana_todo.geometry(f"700x700+{centrar_ventana}+50")
ventana_todo.resizable(0, 0)
ventana_todo.iconbitmap("img/icons8_checklist_1.ico")
ventana_todo.config(bg="#FF4C54")


# ----------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------- Base de Datos

def agregar_datos_base_de_datos(registro):
    database = sqlite3.connect("dblist.db")
    cursor = database.cursor()

    cursor.execute("INSERT INTO Tareas VALUES(?,?)", registro)

    database.commit()

    database.close()


def consulta_titulos():
    database = sqlite3.connect("dblist.db")
    cursor = database.cursor()

    cursor.execute("SELECT Titulo FROM Tareas")

    indice = 0
    for titulo in cursor:
        listbox.insert(indice, titulo[0])

    database.close()


def consulta_comentario(titulo_seleccionado, indice_seleccionado):
    database = sqlite3.connect("dblist.db")
    cursor = database.cursor()

    cursor.execute("SELECT Titulo, Comentario FROM Tareas")

    for titulo, comentario in cursor:
        if titulo == titulo_seleccionado:
            caja_texto["state"] = NORMAL
            caja_texto.delete(1.0, END)
            caja_texto.insert(1.0, comentario)
            caja_texto["state"] = DISABLED
            listbox.selection_clear(indice_seleccionado)
            database.close()
            break


def consulta_actualizar_titulo(actualizar):
    database = sqlite3.connect("dblist.db")
    cursor = database.cursor()

    cursor.execute("UPDATE Tareas SET Titulo = (?) WHERE Titulo = (?)", actualizar)

    database.commit()

    database.close()

def consulta_eliminar_tarea(tarea):
    try:
        database = sqlite3.connect("dblist.db")
        cursor = database.cursor()

        cursor.execute("DELETE FROM Tareas WHERE Titulo = (?)", (tarea,))

        database.commit()

        database.close()
    except Exception as e:
        print(e)

# ---------------------------------------------------------------------------------------------------- Base de Datos

# ---------------------------------------------------------------------------------------------------- Funciones

def agregar_tarea():
    titulo = caja_titulo.get()
    comentario = caja_comentario.get(1.0, END)

    if titulo == "" and len(comentario) == 1:
        messagebox.showerror("Error", "Los campos no pueden estar vacios")
    else:
        if titulo == "":
            messagebox.showerror("Error", "El campo titulo no puede estar vacio")
        else:
            if len(comentario) == 1:
                messagebox.showerror("Error", "El campo comentario no puede estar vacio")
            else:
                registro = (titulo, comentario)
                agregar_datos_base_de_datos(registro)
                listbox.delete(0, END) # PUEDE CAUSAR UNA EXPCION EN EL CASO DE QUE NO EXISTAN TITULOS
                consulta_titulos()
                messagebox.showinfo("Exito", "Tarea agregada con exito")

    caja_titulo.delete(0, END)
    caja_comentario.delete(1.0, END)


def mostrar_tarea():
    item_seleccionado, indice_seleccionado = listbox.get(ANCHOR), listbox.curselection()

    if not item_seleccionado or not indice_seleccionado:
        messagebox.showerror("Error", "Por favor seleccione un item")
    else:
        consulta_comentario(item_seleccionado, indice_seleccionado)


def actualizar_tarea():
    if not listbox.get(ANCHOR):
        messagebox.showerror("Error", "Por favor selecciona un item que desees actualizar")
    else:
        ventana_actualizar = Toplevel()
        ventana_actualizar.title("Ventana  Actualizar")
        ventana_actualizar.geometry(f"450x120+{centrar_ventana + 120}+150")
        ventana_actualizar.resizable(0, 0)
        ventana_actualizar.iconbitmap("img/icons8_update.ico")
        ventana_actualizar.config(bg="#FF4C54")

        Label(ventana_actualizar, text="Nuevo Titulo", font="Bree 20 bold", bg="#FF4C54", fg="#117EE8").pack()
        caja_titulo_nuevo = Entry(ventana_actualizar, font="Bree 15 bold", bg="#FFFFFF", fg="#117EE8")
        caja_titulo_nuevo.pack(fill="x")

        def update():
            if caja_titulo_nuevo.get() == "":
                messagebox.showerror("Error", "Por favor rellene el campo nuevo titulo")
            else:
                item_seleccionado, titulo_nuevo = listbox.get(ANCHOR), caja_titulo_nuevo.get()
                actualizar = (titulo_nuevo, item_seleccionado)
                consulta_actualizar_titulo(actualizar)

                listbox.delete(0, END)

                consulta_titulos()

                ventana_actualizar.destroy()

                messagebox.showinfo("Actualizado", "El titulo de la tarea se actualizo con exito")

        Button(ventana_actualizar, text="Actualizar Titulo", font="Bree 15 bold", bg="#FFFFFF", fg="#117EE8",
               command=update).pack(fill="x", pady=10)


def eliminar_tarea():
    item_seleccionado = listbox.get(ANCHOR)
    if not listbox.get(ANCHOR):
        messagebox.showerror("Error", "Por favor selecciona el item que deseas borrar")
    else:
        consulta_eliminar_tarea(item_seleccionado)
        listbox.delete(0,END)
        consulta_titulos()


# ---------------------------------------------------------------------------------------------------- Funciones

# ---------------------------------------------------------------------------------------------------- Interfaz

Label(ventana_todo, text="Titulo", font="Bree 20 bold", bg="#FF4C54", fg="#117EE8").place(x=100, y=20)
caja_titulo = Entry(ventana_todo, width=20, font="Bree 15 bold", bg="#FFFFFF", fg="#117EE8")
caja_titulo.place(x=30, y=65)

Label(ventana_todo, text="Comentario", font="Bree 20 bold", bg="#FF4C54", fg="#117EE8").place(x=390, y=20)
caja_comentario = Text(ventana_todo, width=48, height="10", font="Bree 11 bold", bg="#FFFFFF", fg="#117EE8")
caja_comentario.place(x=280, y=60)

frame_listbox = Frame(ventana_todo, width=230, height=250)
barra = Scrollbar(frame_listbox, orient=VERTICAL)
listbox = Listbox(frame_listbox, yscrollcommand=barra.set, font="Bree 11 bold", bg="#FFFFFF", fg="#117EE8")

barra.config(command=listbox.yview)
listbox.config(width=25, height=17)

frame_listbox.place(x=30, y=350)
barra.pack(side=RIGHT, fill=Y)
listbox.pack()

caja_texto = Text(ventana_todo, width=47, height=18, state=DISABLED, font="Bree 11 bold", bg="#FFFFFF", fg="#117EE8")
caja_texto.place(x=290, y=350)
# ---------------------------------------------------------------------------------------------------- Interfaz


# ---------------------------------------------------------------------------------------------------- Botones

Button(ventana_todo, text="Agregar Tarea", font="Bree 15 bold", bg="#FFFFFF", fg="#117EE8",
       command=agregar_tarea).place(x=63, y=130)

Button(ventana_todo, text="Mostrar tarea", font="Bree 15 bold", bg="#FFFFFF", fg="#117EE8",
       command=mostrar_tarea).place(x=63, y=270)

Button(ventana_todo, text="Actualizar Tarea", font="Bree 15 bold", bg="#FFFFFF", fg="#117EE8",
       command=actualizar_tarea).place(x=263, y=270)

Button(ventana_todo, text="Eliminar tarea", font="Bree 15 bold", bg="#FFFFFF", fg="#117EE8",
       command=eliminar_tarea).place(x=493, y=270)

# ---------------------------------------------------------------------------------------------------- Botones
consulta_titulos()
ventana_todo.mainloop()
