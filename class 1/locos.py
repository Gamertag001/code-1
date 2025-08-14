import random 

nombres = []

while True:
    nombre = input("nombre (fin para terminar): ")
    if nombre.lower() == "fin":
        break
    nombres.append(nombres)
    
if nombres:
    ganador = random.choice(nombres)
    print(f"el desafortunado es: {ganador}")
    
else:
    print("no hay nombres")