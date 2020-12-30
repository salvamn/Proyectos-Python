from tkinter import *
from tkinter import messagebox
import sqlite3


# --------------------------- Imports

# --------------------------------------------------------------------------------------------------------- Base de Datos

def consulta_agregar(contacto):
    try:
        database = sqlite3.connect("contactosdb.db")
        cursor = database.cursor()

        cursor.execute("INSERT INTO Contactos VALUES(?,?,?,?,?)", contacto)

        database.commit()

        database.close()
    except Exception as e:
        print(e)


def consulta_nombres():
    database = sqlite3.connect("contactosdb.db")
    cursor = database.cursor()

    cursor.execute("SELECT Nombre FROM Contactos")

    indice = 0
    for nombre in cursor:
        listbox.insert(indice, nombre)
        indice += 1

    database.close()


def consulta_mostrar_contacto(contacto):
    database = sqlite3.connect("contactosdb.db")
    cursor = database.cursor()

    cursor.execute("SELECT * FROM Contactos WHERE Nombre = (?)", (contacto,))

    return cursor, database


def consulta_eliminar_contacto(contacto):
    database = sqlite3.connect("contactosdb.db")
    cursor = database.cursor()

    cursor.execute("DELETE FROM Contactos WHERE Nombre = (?)", contacto)

    database.commit()

    database.close()


# --------------------------------------------------------------------------------------------------------- Base de Datos


# --------------------------------------------------------------------------------------------------------- Funciones

def agregar_contacto():
    nombre_persona = caja_nombre.get()
    apellido_persona = caja_apellido.get()
    correo_persona = caja_mail.get()
    numero_persona = caja_telefono.get()
    direccion_persona = caja_direccion.get()

    if nombre_persona == "" and apellido_persona == "" and numero_persona == "":
        messagebox.showerror("Error",
                             "Por favor rellene los siguientes campos obligatorios:\nnombre, apellido y telefono")
    else:
        if nombre_persona == "":
            messagebox.showerror("Error", "Por favor rellene el campo nombre")
        else:
            if apellido_persona == "":
                messagebox.showerror("Error", "Por favor rellene el campo apellido")
            else:
                if numero_persona == "":
                    messagebox.showerror("Error", "Por favor rellene el campo telefono")
                else:
                    contacto = (numero_persona, nombre_persona, apellido_persona, correo_persona, direccion_persona)

                    consulta_agregar(contacto)

                    listbox.delete(0, END)
                    consulta_nombres()

                    caja_nombre.delete(0, END)
                    caja_apellido.delete(0, END)
                    caja_mail.delete(0, END)
                    caja_telefono.delete(0, END)
                    caja_direccion.delete(0, END)

                    messagebox.showinfo("Agregar", "El contacto se agrego con exito")


def mostrar_contacto():
    item_seleccionado = listbox.get(ANCHOR)

    if not listbox.get(ANCHOR):
        messagebox.showerror("Error", "Por favor selecciona un item")
    else:
        ventana_mostrar = Toplevel()
        ventana_mostrar.geometry("510x80")
        ventana_mostrar.resizable(0, 0)
        ventana_mostrar.config(bg="#010101")

        Label(ventana_mostrar, text="Nombre", bg="#010101", fg="#FFFFFF", font="Roboto 13 bold").grid(row=0, column=0)
        caja_nombre_mostrar = Entry(ventana_mostrar, bg="#DC3545", fg="#FFFFFF", font="Roboto 13 bold")
        caja_nombre_mostrar.grid(row=0, column=1)

        Label(ventana_mostrar, text="Apellido", bg="#010101", fg="#FFFFFF", font="Roboto 13 bold").grid(row=0, column=2)
        caja_apellido_mostrar = Entry(ventana_mostrar, bg="#DC3545", fg="#FFFFFF", font="Roboto 13 bold")
        caja_apellido_mostrar.grid(row=0, column=3)

        Label(ventana_mostrar, text="Mail", bg="#010101", fg="#FFFFFF", font="Roboto 13 bold").grid(row=1, column=0)
        caja_mail_mostrar = Entry(ventana_mostrar, bg="#DC3545", fg="#FFFFFF", font="Roboto 13 bold")
        caja_mail_mostrar.grid(row=1, column=1)

        Label(ventana_mostrar, text="Telefono", bg="#010101", fg="#FFFFFF", font="Roboto 13 bold").grid(row=1, column=2)
        caja_telefono_mostrar = Entry(ventana_mostrar, bg="#DC3545", fg="#FFFFFF", font="Roboto 13 bold")
        caja_telefono_mostrar.grid(row=1, column=3)

        Label(ventana_mostrar, text="Direccion", bg="#010101", fg="#FFFFFF", font="Roboto 13 bold").grid(row=2,
                                                                                                         column=0)
        caja_direccion_mostrar = Entry(ventana_mostrar, bg="#DC3545", fg="#FFFFFF", font="Roboto 13 bold")
        caja_direccion_mostrar.grid(row=2, column=1)

        contacto, database = consulta_mostrar_contacto(item_seleccionado[0])

        for tel, nom, ape, mai, dire in contacto:
            caja_nombre_mostrar.insert(0, nom)
            caja_apellido_mostrar.insert(0, ape)
            caja_mail_mostrar.insert(0, mai)
            caja_telefono_mostrar.insert(0, tel)
            caja_direccion_mostrar.insert(0, dire)
            break

        database.close()


def editar_contacto(): # Me da flojera
    pass


def eliminar_contacto():
    item_seleccionado = listbox.get(ANCHOR)

    if not listbox.get(ANCHOR):
        messagebox.showerror("Error", "Por favor selecciona un item a borrar")
    else:
        consulta_eliminar_contacto(item_seleccionado)
        listbox.delete(0, END)
        consulta_nombres()
        messagebox.showinfo("Borrado", "El contacto fue eliminado con exito")


# --------------------------------------------------------------------------------------------------------- Funciones


ventana_agenda = Tk()
# --------------------------------------------------------------------------------------------------------- Interfaz
ventana_agenda.title("Agenda de Contactos")
centrar_ventana = 1080 - 700
ventana_agenda.geometry(f"610x480+{centrar_ventana}+100")
ventana_agenda.resizable(0, 0)
ventana_agenda.config(bg="#010101")
ventana_agenda.iconbitmap("img/icons8_search_contacts_1.ico")

Label(ventana_agenda, text="Agenda de Contactos", bg="#010101", fg="#FFFFFF", font="Roboto 20 bold").place(relx=0.2,
                                                                                                           y=20)

Label(ventana_agenda, text="Primer Nombre", bg="#010101", fg="#FFFFFF", font="Roboto 15 bold").place(x=20, y=70)
caja_nombre = Entry(ventana_agenda, bg="#DC3545", fg="#FFFFFF", font="Roboto 15 bold")
caja_nombre.place(x=20, y=110)

Label(ventana_agenda, text="Primer Apellido", bg="#010101", fg="#FFFFFF", font="Roboto 15 bold").place(x=20, y=150)
caja_apellido = Entry(ventana_agenda, bg="#DC3545", fg="#FFFFFF", font="Roboto 15 bold")
caja_apellido.place(x=20, y=190)

Label(ventana_agenda, text="Correo Electronico", bg="#010101", fg="#FFFFFF", font="Roboto 15 bold").place(x=20, y=230)
caja_mail = Entry(ventana_agenda, bg="#DC3545", fg="#FFFFFF", font="Roboto 15 bold")
caja_mail.place(x=20, y=270)

Label(ventana_agenda, text="Numero de Telefono", bg="#010101", fg="#FFFFFF", font="Roboto 15 bold").place(x=20, y=310)
caja_telefono = Entry(ventana_agenda, bg="#DC3545", fg="#FFFFFF", font="Roboto 15 bold")
caja_telefono.place(x=20, y=350)

Label(ventana_agenda, text="Direccion", bg="#010101", fg="#FFFFFF", font="Roboto 15 bold").place(x=20, y=390)
caja_direccion = Entry(ventana_agenda, bg="#DC3545", fg="#FFFFFF", font="Roboto 15 bold")
caja_direccion.place(x=20, y=430)

frame_listbox = Frame(ventana_agenda, width=400, height=300)
barra = Scrollbar(frame_listbox, orient=VERTICAL)
listbox = Listbox(frame_listbox, yscrollcommand=barra.set)

barra.config(command=listbox.yview)
listbox.config(width=26, height=13, bg="#DC3545", fg="#FFFFFF", font="Roboto 14")

frame_listbox.place(x=280, y=80)
barra.pack(side=RIGHT, fill=Y)
listbox.pack()

# --------------------------------------------------------------------------------------------------------- Interfaz

# ----------------------------------------------------------------------------------------- Botones

Button(ventana_agenda, text="Agregar Contacto", bg="#DC3545", fg="#FFFFFF", font="Roboto 11 bold", width=16,
       command=agregar_contacto).place(x=280, y=390)
Button(ventana_agenda, text="Mostrar Contacto", bg="#DC3545", fg="#FFFFFF", font="Roboto 11 bold", width=15,
       command=mostrar_contacto).place(x=440, y=390)
Button(ventana_agenda, text="Editar Contacto", bg="#DC3545", fg="#FFFFFF", font="Roboto 11 bold", width=16,
       command=editar_contacto).place(x=280,
                                      y=430)
Button(ventana_agenda, text="Eliminar Contacto", bg="#DC3545", fg="#FFFFFF", font="Roboto 11 bold", width=15,
       command=eliminar_contacto).place(
    x=440, y=430)
# ----------------------------------------------------------------------------------------- Botones

consulta_nombres()
ventana_agenda.mainloop()
