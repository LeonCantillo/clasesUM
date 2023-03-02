from LógicaDelNegocio import Paciente

print("caso 1")
Martina = Paciente("Martina De Luque",6,0.55,2022,4,28,"f")
print("Paciente con nombre", Martina.nombreCompleto)
print("Su edad es", Martina.CalcularEdadActualEnAños(), "años")
print("Esta edad corresponde a una persona", Martina.DeterminarMayoríaDeEdad())
print("En esta edad una persona se ecuentra viviendo su", Martina.DeterminarEtapaDeLaVida())
print("Su índice de masa corporal (IMC) es", round(Martina.CalcularÍndiceMasaCorporal(),2))
print("Con este IMC se consiera que tiene", Martina.DeterminarCategoríaDePeso())
print("Su edad en meses es:", Martina.CalcularEdadActualEnMeses())
mesParaEstimarEstatura = 7
print("Su estatura actual es:", Martina.estatura)
print("La estatura estimada al mes", mesParaEstimarEstatura, "es:", Martina.EstimarEstaturaPrimerosMeses(mesParaEstimarEstatura))

print("caso 2")
Antonio = Paciente("Antonio Zambrano",11.3,0.87,2020,12,28,"m")
print("Paciente con nombre", Antonio.nombreCompleto)
print("Su edad es", Antonio.CalcularEdadActualEnAños(), "años")
print("Esta edad corresponde a una persona", Antonio.DeterminarMayoríaDeEdad())
print("En esta edad una persona se ecuentra viviendo su", Antonio.DeterminarEtapaDeLaVida())
print("Su índice de masa corporal (IMC) es", round(Antonio.CalcularÍndiceMasaCorporal(),2))
print("Con este IMC se consiera que tiene", Antonio.DeterminarCategoríaDePeso())
print("Su edad en meses es:", Antonio.CalcularEdadActualEnMeses())
mesParaEstimarEstatura = 7
print("Su estatura actual es:", Antonio.estatura)
print("La estatura estimada al mes", mesParaEstimarEstatura, "es:", Antonio.EstimarEstaturaPrimerosMeses(mesParaEstimarEstatura))