import tkinter as tk
from tkinter import filedialog

def obtener_ruta_archivo():
    ruta_seleccionada = filedialog.askopenfilename(
        initialdir="/",  # Directorio inicial (puedes cambiarlo)
        title="Seleccionar archivo",
        filetypes=(("Archivos", "*.*"), ("Todos los archivos", "*.*"))
    )
    return ruta_seleccionada

# Crear una ventana simple
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Llamar a la función para obtener la ruta del archivo
#m = obtener_ruta_archivo()
#print (m)