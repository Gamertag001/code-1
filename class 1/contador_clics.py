import customtkinter

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("Contador de clics")
app.geometry("500x450")

contador = 0

def aumentar_contador():
    global contador
    contador += 1
    etiqueta.configure(text=f"Clics: {contador}")

def reset_comand():
    global contador
    contador = 0
    etiqueta.configure(text=f"Clics: {contador}")

etiqueta = customtkinter.CTkLabel(app, text="Clics: 0", font=("Arial", 20))
etiqueta.pack(pady=20)

boton = customtkinter.CTkButton(app, text="Clic aquí", command=aumentar_contador)
boton.pack(pady=20)

boton = customtkinter.CTkButton(app, text="reset aqui", command=reset_comand)
boton.pack(pady=10)

app.mainloop()