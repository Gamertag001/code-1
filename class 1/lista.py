import customtkinter as ct

ct.set_appearance_mode("dark")
app = ct.CTk()
app.title("añadir tarea")
app.geometry("500x450")

def añadir_tarea():
    tarea = entry.get().strip()
    if tarea:
        listbox.insert(ct.END, tarea)
        entry.delete(0, ct.END)

def remover():
    seleccion = listbox.curselection()
    if seleccion:
        listbox.delete(seleccion[0])

entry = ct.CTkEntry(app)
entry.pack(padx=10, pady=5)


boton = ct.CTkButton(app, text="remover", command=añadir_tarea)
boton.pack(pady=20)

boton = ct.CTkButton(app, text="remover", command=remover)
boton.pack(pady=20)

import tkinter as tk

frame = ct.CTkFrame(app)
frame.pack(padx=10, pady=5, fill=ct.BOTH, expand=True)

listbox = tk.Listbox(frame)
listbox.pack(fill=tk.BOTH, expand=True)


app.mainloop()