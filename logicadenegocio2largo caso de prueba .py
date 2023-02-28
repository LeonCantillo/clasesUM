from logicadenegocio2largo import paciente
Martina = paciente("Martina De Luque", 70, 1.70, 1984, 2, 29)

if (Martina.IndiceMasaCorporal() == None):
    print("El peso ingresado no es valido")
elif (Martina.CalcularEdad() == None):
    print("La fecha de nacimiento no está en un rango válido")
elif (Martina.ValidarEstatura() == False):
    print("La estatura introdcida está fuera del rango aceptado")
else:
    print (f"La paciente {Martina.nombreCompleto} tiene {Martina.CalcularEdad()} por lo que es {Martina.DeterminarCategoriaEdad()}.")
    print (f"Su indice de mas corporal es de {Martina.IndiceMasaCorporal()}.")
    print (f"El nivel de peso de la paciente es '{Martina.NivelDePesoPaciente()}'")