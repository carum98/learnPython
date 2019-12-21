cadena = "Carlos Umaña Acevedo"

print(cadena[-1])

print(cadena[3])

print(cadena[:3])

print(cadena.capitalize())

alumnos = 2500
academia = "Fidelistas"

cadena = "La Universidad {} tiene {} alumnos".format(academia, alumnos)
print(cadena)

cadena = "La Universidad {a} tiene {b} alumnos".format(a=academia, b=alumnos)
print(cadena)

cadena = f"La Universidad {academia} tiene {alumnos} alumnos"
print(cadena)

print("Ingrese su nombre")
nombre = input()
print(f"Su nombre es {nombre}")

nombre = input("Ingrese su nombre")
print(f"Su nombre es {nombre}")