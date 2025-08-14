
# ejer 1

print("bienvenido mi loc")

num = int(input("numeros a ingresar: "))

positivos = 0
negativos = 0
ceros = 0

for i in range(num):
	num = int(input(f"ingrese el numero {i+1}: "))
	if num > 0:
		positivos += 1
	elif num < 0:
		negativos += 1

	else:
		ceros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")


# ejer 2

compras = []
while True:
    producto = input("Producto (o 'fin'): ")
    if producto == "fin":
        break
    compras.append(producto)

print("\nLista de compras:")
for p in compras:
    print(p)


# ejer 3

print("\n1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
op = input("Opción: ")
x = float(input("Num1: "))
y = float(input("Num2: "))

if op == "1":
    print(x + y)
elif op == "2":
    print(x - y)
elif op == "3":
    print(x * y)
elif op == "4":
    if y != 0:
        print(x / y)
    else:
        print("No se puede dividir entre 0")

# ejer 4
n = int(input("\nNúmero: "))
tabla = []
for i in range(1, 11):
    tabla.append(n * i)

for t in tabla:
    print(t) 
    
	




