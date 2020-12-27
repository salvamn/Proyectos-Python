from tkinter import Tk, Label, Frame, Scrollbar, VERTICAL, Listbox, SOLID, RIGHT, Y, ANCHOR, Button, DISABLED
from tkinter import messagebox
from PIL import Image, ImageTk
from pygame import mixer
from getpass import getuser
import os

ventana_mp3 = Tk()
ventana_mp3.title("BullaMusic")
ventana_mp3.iconbitmap("img/icons8_music.ico")
ventana_mp3.config(bg="#0D1117")
ventana_mp3.geometry("600x450")
ventana_mp3.resizable(0, 0)

Label(ventana_mp3, text="BullaMusic", bg="#0D1117", fg="#F04526", font="Dubai 30 bold").place(x=100, y=10)

# ------------------------------------------------------------------------- Frame, Listbox y Barra
frame_para_listbox = Frame(ventana_mp3, width=400, height=250, bg="#2B2B2B")
barra = Scrollbar(frame_para_listbox, orient=VERTICAL)
listbox = Listbox(frame_para_listbox, yscrollcommand=barra.set, bg="#2B2B2B", fg="#F04526")

listbox.config(width=79, height=10, font="Dubai 10", relief=SOLID, bd=3)
barra.config(command=listbox.yview)

frame_para_listbox.place(x=10, y=100)
barra.pack(side=RIGHT, fill=Y)
listbox.pack()


def filtrar_y_listar_musica():
    nombre_usuario = getuser()
    directorio = rf"C:\Users\{nombre_usuario}"

    for carpeta in os.listdir(directorio):
        if carpeta == "Music":
            directorio = rf"C:\Users\{nombre_usuario}\{carpeta}"
            break

    extension_cancion = ".mp3"

    canciones = [cancion for cancion in os.listdir(directorio) if cancion.lower().endswith(extension_cancion)]

    return canciones, directorio


lista_canciones, directorios = filtrar_y_listar_musica()

indice = 0
for insertar_cancion in lista_canciones:
    listbox.insert(indice, insertar_cancion)
    indice += 1

# ------------------------------------------------------------------------- Frame, Listbox y Barra

# ------------------------------------------------------------------------- Funciones

def destruir_ventana():
    if mixer.get_init():
        mixer.music.stop()
    print("------------------------------------------------------------------------------")
    ventana_mp3.destroy()


def reproducir(cancion):
    mixer.init()
    mixer.music.load(f"{directorios}\\{cancion}")
    mixer.music.set_volume(0.7)
    mixer.music.play()


def pausar():
    if mixer.get_init():
        if mixer.music.get_busy():
            mixer.music.pause()
    else:
        messagebox.showinfo("Informacion(pausar)", "No se esta reproduciendo nada")


def despausar():
    if mixer.get_init():
        mixer.music.unpause()
    else:
        messagebox.showinfo("Informacion(sacar pausa)", "No se esta reproduciendo nada")


def parar_musica():
    if mixer.get_init():
        mixer.music.stop()
        mixer.stop()
    else:
        messagebox.showinfo("Informacion(detener musica)", "No se esta reproduciendo nada")


def reproducir_cancion():
    if not listbox.get(ANCHOR):
        messagebox.showinfo("Informacion", "Por favor selecciona una cancion")
    else:
        seleccion_de_cancion = listbox.get(ANCHOR)
        reproducir(seleccion_de_cancion)


def reproducir_la_cola():
    pass


# ------------------------------------------------------------------------- Funciones

# -------------------------------------------------------------------------- Botones
Button(ventana_mp3, text="Reproducir", font="Dubai 13", fg="#F04526", bg="#2B2B2B", command=reproducir_cancion).place(
    x=10, y=350)
Button(ventana_mp3, text="Pausa", font="Dubai 13", fg="#F04526", bg="#2B2B2B", width=9, command=pausar).place(x=110,
                                                                                                              y=350)
Button(ventana_mp3, text="Sacar Pausa", font="Dubai 13", fg="#F04526", bg="#2B2B2B", width=10,
       command=despausar).place(x=210, y=350)
Button(ventana_mp3, text="Detener Musica", font="Dubai 13", fg="#F04526", bg="#2B2B2B", command=parar_musica).place(
    x=318, y=350)
Button(ventana_mp3, text="Reproducir Todo", font="Dubai 13", fg="#F04526", bg="#2B2B2B",
       state=DISABLED, command=reproducir_la_cola).place(x=450, y=350)

# -------------------------------------------------------------------------- Botones

# ----------------------------------------------------------------------------
Label(ventana_mp3, text="BullaMusic © Salvador Mellado", font="Dubai 10", fg="#F04526", bg="#0D1117").place(x=376,
                                                                                                            y=410)
imagen = Image.open("img/icons8_music_record_48px.png")
imagen = imagen.resize((70, 70), Image.ANTIALIAS)
imagen = ImageTk.PhotoImage(imagen)

Label(ventana_mp3, bg="#0D1117", image=imagen).place(x=310, y=10)

ventana_mp3.protocol("WM_DELETE_WINDOW", destruir_ventana)

ventana_mp3.mainloop()
