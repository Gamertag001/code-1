import customtkinter

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("Calculadora Simple")
app.geometry("500x450")

def calcular(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operacion == "sumar":
            resultado = num1 + num2
        elif operacion == "restar":
            resultado = num1 - num2
        elif operacion == "multiplicar":
            resultado = num1 * num2
        elif operacion == "dividir":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado_label.configure(text="Error: División por cero")
                return
        resultado_label.configure(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.configure(text="Error: Ingresa números válidos")

entry1 = customtkinter.CTkEntry(app, placeholder_text="Número 1")
entry1.pack(pady=10)

entry2 = customtkinter.CTkEntry(app, placeholder_text="Número 2")
entry2.pack(pady=10)

frame = customtkinter.CTkFrame(app)
frame.pack(pady=10)

btn_suma = customtkinter.CTkButton(frame, text="Sumar", command=lambda: calcular("sumar"))
btn_suma.grid(row=0, column=0, padx=5)

btn_resta = customtkinter.CTkButton(frame, text="Restar", command=lambda: calcular("restar"))
btn_resta.grid(row=0, column=1, padx=5)

btn_multi = customtkinter.CTkButton(frame, text="Multiplicar", command=lambda: calcular("multiplicar"))
btn_multi.grid(row=0, column=2, padx=5)

btn_div = customtkinter.CTkButton(frame, text="Dividir", command=lambda: calcular("dividir"))
btn_div.grid(row=0, column=3, padx=5)

resultado_label = customtkinter.CTkLabel(app, text="Resultado: ", font=("Arial", 18))
resultado_label.pack(pady=20)

app.mainloop()

