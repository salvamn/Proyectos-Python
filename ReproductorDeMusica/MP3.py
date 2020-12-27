from tkinter import messagebox
from pygame import mixer
from getpass import getuser
import os


def filtrar_y_listar_musica():
    """
    Esta funcion nos permite obtener el nombre de usuario de la maquina y cuando se obtiene se le pasa a la variable
    directorio, la variable directorio se le pasa a una funcion listdir del modulo os y con un for iteraremos esta lista
    entregandonos cada nombre de carpeta de dicho directorio, estas carpetas seran evaluadas con un condicional if
    esta evaluacion compara si el nombre de la carpeta es igual a "Music" si esto devulve true actualizamos el direc-
    torio y rompemos el bucle.

    lo siguiente que haremos es crear una variable que en donde le asignaremos las extension de las canciones en mi
    caso .mp3

    ahora con compresion de listas crearemos una variable cancion, crearemos un for y le pasamos la variable cancion,
    este for recorrera la variable directorio con la ruta hacia la carpeta musica, con un if que evalua si
    cancion.lower() (En el caso de que este la extension en mayusculas).endwith(extension) si devuelve true esta
    cancion se guarda en la lista, y asi tendremos todas las canciones en una lista.
    :return:
    """

    nombre_usuario = getuser()
    directorio = rf"C:\Users\{nombre_usuario}"

    for carpeta in os.listdir(directorio):
        if carpeta == "Music":
            directorio = rf"C:\Users\{nombre_usuario}\{carpeta}"
            break

    extension_cancion = ".mp3"

    canciones = [cancion for cancion in os.listdir(directorio) if cancion.lower().endswith(extension_cancion)]

    return canciones, directorio


def reproducir(cancion):
    musica, directorio = filtrar_y_listar_musica()

    mixer.init()
    mixer.music.load(f"{directorio}\\{cancion}")
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


# ---------------------------------------------------------------------------------------------- REVISAR(NO FUNCIONA)
"""def cola_de_musica():
    musica, directorio = filtrar_y_listar_musica()

    contador = 1
    mixer.init()
    mixer.music.load(f"{directorio}\\{musica[contador]}")
    mixer.music.set_volume(0.7)
    mixer.music.play()

    while True:
        if not mixer.music.get_busy():
            print("Entro en if")
            contador += 1
            mixer.init()
            mixer.music.queue(f"{directorio}\\{musica[contador]}")
            mixer.music.set_volume(0.7)
            mixer.music.play()
    else:
        if pausar:
            pausar()
        else:
            print("Entro en else")
            contador += 1
    print(contador)
    print("Sali del While")
"""
