import customtkinter 

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("Contador de clics")
app.geometry("500x450")



import tkinter as tk

window = tk.Tk()
window.title("Lista de Tareas")
window.geometry("300x400")

def añadir_tarea():
    tarea = entry.get().strip()
    if tarea:
        listbox.insert(tk.END, tarea)
        entry.delete(0, tk.END)

def remover():
    seleccion = listbox.curselection()
    if seleccion:
        listbox.delete(seleccion[0])

entry = tk.Entry(window)
entry.pack(padx=10, pady=5)

bt_frame = tk.Frame(window)
bt_frame.pack(pady=5)

boton_agregar = tk.Button(bt_frame, text="Agregar", command=añadir_tarea)
boton_agregar.pack(side=tk.LEFT, padx=5)

boton_borrar = tk.Button(bt_frame, text="Eliminar", command=remover)
boton_borrar.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(window)
listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

window.mainloop()