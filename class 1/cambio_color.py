import customtkinter as ct    

app = ct.CTk()
app.title("Contador de clics")
app.geometry("500x450")

def cambio(event=None):
	color = combo.get()
	app.configure(bg=color)


color = ["red", "green","blue","yellow","lightblue","lightgreen"]
combo = ct.CTkComboBox(app, values=color, state="readonly")
combo.set(color[0])
combo.pack(pady=20)

combo.bind("<<ComboboxSelected>>" , cambio)

app.mainloop