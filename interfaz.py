import tkinter as tk
from tkinter import ttk, messagebox

from Arrays import (
    mostrar_strongman,
    agregar_strongman,
    eliminar_strongman,
    mostrar_suplementos,
    buscar_pre_workout,
)


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Strongman")
        self.root.geometry("550x420")
        self.root.resizable(False, False)

        self.titulo = ttk.Label(root, text="Lista de Strongman", font=("Arial", 14, "bold"))
        self.titulo.pack(pady=(15, 5))

        frame_entrada = ttk.Frame(root)
        frame_entrada.pack(fill="x", padx=20, pady=5)

        ttk.Label(frame_entrada, text="Nuevo nombre:").pack(side="left")

        self.txt_nombre = ttk.Entry(frame_entrada, width=30)
        self.txt_nombre.pack(side="left", padx=(10, 10))

        self.btn_agregar = ttk.Button(frame_entrada, text="Agregar", command=self.agregar_nombre)
        self.btn_agregar.pack(side="left")

        self.lista_strongman = tk.Listbox(root, width=40, height=10)
        self.lista_strongman.pack(padx=20, pady=10)

        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=5)

        self.btn_eliminar = ttk.Button(frame_botones, text="Eliminar seleccionado", command=self.eliminar_nombre)
        self.btn_eliminar.pack(side="left", padx=10)

        self.btn_mostrar = ttk.Button(frame_botones, text="Mostrar suplementos", command=self.mostrar_suplementos)
        self.btn_mostrar.pack(side="left", padx=10)

        self.texto_suplementos = tk.Text(root, width=45, height=8, state="disabled")
        self.texto_suplementos.pack(padx=20, pady=10)

        self.lbl_info = ttk.Label(root, text="")
        self.lbl_info.pack(pady=(0, 10))

        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_strongman.delete(0, tk.END)
        for nombre in mostrar_strongman():
            self.lista_strongman.insert(tk.END, nombre)

    def agregar_nombre(self):
        nombre = self.txt_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Escribe un nombre antes de agregar.")
            return

        agregar_strongman(nombre)
        self.txt_nombre.delete(0, tk.END)
        self.actualizar_lista()
        messagebox.showinfo("Correcto", f"Se agregó: {nombre}")

    def eliminar_nombre(self):
        seleccion = self.lista_strongman.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un nombre para eliminar.")
            return

        nombre = self.lista_strongman.get(seleccion[0])
        eliminar_strongman(nombre)
        self.actualizar_lista()
        messagebox.showinfo("Correcto", f"Se eliminó: {nombre}")

    def mostrar_suplementos(self):
        suplementos = mostrar_suplementos()
        texto = ""
        for i, grupo in enumerate(suplementos, start=1):
            texto += f"Grupo {i}: {', '.join(grupo)}\n"

        self.texto_suplementos.config(state="normal")
        self.texto_suplementos.delete("1.0", tk.END)
        self.texto_suplementos.insert(tk.END, texto)
        self.texto_suplementos.config(state="disabled")

        ubicacion = buscar_pre_workout()
        if ubicacion is not None:
            fila, columna = ubicacion
            self.lbl_info.config(text=f"'Pre-Workout' está en la fila {fila + 1}, columna {columna + 1}.")
        else:
            self.lbl_info.config(text="No se encontró 'Pre-Workout'.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
