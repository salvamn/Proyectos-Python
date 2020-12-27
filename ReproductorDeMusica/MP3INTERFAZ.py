from tkinter import Tk, Label, Frame, Scrollbar, VERTICAL, Listbox, SOLID, RIGHT, Y, ANCHOR, Button, DISABLED
from tkinter import messagebox
from PIL import Image, ImageTk
# ----------------------
from ReproductorDeMusica import MP3

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

lista_canciones, directorio = MP3.filtrar_y_listar_musica()

indice = 0
for insertar_cancion in lista_canciones:
    listbox.insert(indice, insertar_cancion)
    indice += 1

# ------------------------------------------------------------------------- Frame, Listbox y Barra

# ------------------------------------------------------------------------- Funciones
# thd = []


"""def destruir_ventana():
    if mixer.get_init():
        mixer.music.stop()
        # thd[0].join()
    print("------------------------------------------------------------------------------")
    ventana_mp3.destroy()"""


def reproducir_cancion():
    if not listbox.get(ANCHOR):
        messagebox.showinfo("Informacion", "Por favor selecciona una cancion")
    else:
        seleccion_de_cancion = listbox.get(ANCHOR)
        MP3.reproducir(seleccion_de_cancion)


def reproducir_la_cola():
    # proceso = threading.Thread(target=MP3.cola_de_musica)
    # thd.append(proceso)
    # proceso.start()
    pass


# ------------------------------------------------------------------------- Funciones

# -------------------------------------------------------------------------- Botones
Button(ventana_mp3, text="Reproducir", font="Dubai 13", fg="#F04526", bg="#2B2B2B", command=reproducir_cancion).place(
    x=10, y=350)
Button(ventana_mp3, text="Pausa", font="Dubai 13", fg="#F04526", bg="#2B2B2B", width=9, command=MP3.pausar).place(x=110,
                                                                                                                  y=350)
Button(ventana_mp3, text="Sacar Pausa", font="Dubai 13", fg="#F04526", bg="#2B2B2B", width=10,
       command=MP3.despausar).place(x=210, y=350)
Button(ventana_mp3, text="Detener Musica", font="Dubai 13", fg="#F04526", bg="#2B2B2B", command=MP3.parar_musica).place(
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

# ventana_mp3.protocol("WM_DELETE_WINDOW", destruir_ventana)

ventana_mp3.mainloop()
