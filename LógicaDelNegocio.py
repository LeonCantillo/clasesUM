from datetime import date

class Paciente:

    def __init__(self, nombreCompleto:str, peso:float, estatura:float, añoNacimiento:int, mesNacimiento:int, díaNacimiento:int, sexo:str):
                 
        self.nombreCompleto = nombreCompleto
        self.peso = peso
        self.estatura = estatura
        self.añoNacimiento = añoNacimiento
        self.mesNacimiento = mesNacimiento
        self.díaNacimiento = díaNacimiento
        self.sexo = sexo
        self.VerificarValoresAtributos()
    
    def CalcularEdadActualEnAños(self):
        self.VerificarValoresAtributos()
        fechaDeHoy = date.today()
        edad = None
        restar = 0
        diferenciaDeAños = fechaDeHoy.year - self.añoNacimiento
        diferenciaDeMeses = fechaDeHoy.month - self.mesNacimiento
        diferenciaDeDías = fechaDeHoy.day - self.díaNacimiento
        if diferenciaDeMeses < 0 or (diferenciaDeMeses == 0 and diferenciaDeDías < 0):
            restar = 1
        edad = diferenciaDeAños - restar
        return edad
    
    def CalcularEdadActualEnMeses(self):
        self.VerificarValoresAtributos()
        fechaDeHoy = date.today()
        restarAños = 0
        diferenciaDeAños = fechaDeHoy.year - self.añoNacimiento
        diferenciaDeMeses = fechaDeHoy.month - self.mesNacimiento
        diferenciaDeDías = fechaDeHoy.day - self.díaNacimiento
        if diferenciaDeMeses < 0 or (diferenciaDeMeses == 0 and diferenciaDeDías < 0):
            restarAños = 1
        añosCompletos = diferenciaDeAños - restarAños
        mesesParaSumar = 0
        if restarAños == 0:
            restarMeses = 0
            if diferenciaDeMeses > 0 and diferenciaDeDías < 0:
                restarMeses = 1
            mesesParaSumar = diferenciaDeMeses -restarMeses
        else:
            restarMeses = 0
            if diferenciaDeMeses < 0 and diferenciaDeDías < 0:
                restarMeses = 1
            mesesParaSumar = 12 + diferenciaDeMeses - restarMeses
        edadEnMeses = añosCompletos * 12 + mesesParaSumar
        return edadEnMeses

    def DeterminarMayoríaDeEdad(self):
        categoríaEdad = None
        edad = self.CalcularEdadActualEnAños()
        if edad is not None:
            if edad >= 18:
                categoríaEdad = "mayor de edad"
            else:
                categoríaEdad = "menor de edad"
        return categoríaEdad

    def CalcularÍndiceMasaCorporal(self):
        self.VerificarValoresAtributos()
        índiceMasaCorporal = self.peso / (self.estatura ** 2)
        return índiceMasaCorporal

    def DeterminarCategoríaDePeso(self):
        índiceMasaCorporal = self.CalcularÍndiceMasaCorporal()
        categoríaDePeso = None
        if índiceMasaCorporal >= 30:
            categoríaDePeso = "obesidad"
        elif índiceMasaCorporal >= 25:
            categoríaDePeso = "sobrepeso"
        elif índiceMasaCorporal >= 18.5:
            categoríaDePeso = "peso normal"
        else:
            categoríaDePeso = "peso bajo"
        return categoríaDePeso
    
    def DeterminarEtapaDeLaVida(self):
        etapaVida = None
        edad = self.CalcularEdadActualEnAños()
        if edad <= 5:
            etapaVida = "primera infancia"
        elif edad <= 11:
            etapaVida = "infancia"
        elif edad <= 18:
            etapaVida = "adolescencia"
        elif edad <= 26:
            etapaVida = "juventud"
        elif edad <= 59:
            etapaVida = "adultez"
        else:
            etapaVida = "vejez"
        return etapaVida
    
    def EstimarEstaturaPrimerosMeses(self, mesProyección:int):
        estaturaEstimada = None
        edadActualEnMeses = self.CalcularEdadActualEnMeses()
        if edadActualEnMeses < 24 and edadActualEnMeses < mesProyección <= 24:
            if 0.45 <= self.estatura <= 0.55:
                factorSexo = None
                estaturaCalculada = None
                estaturaTrabajar = self.estatura
                if self.sexo == 'f':
                    factorSexo = 1.0
                else:
                    factorSexo = 1.115
                for mes in range(edadActualEnMeses, mesProyección, 1):
                    estaturaCalculada = estaturaTrabajar + (estaturaTrabajar / (mes + 1) ** 2)
                    estaturaTrabajar = estaturaCalculada
                estaturaEstimada = round((estaturaCalculada * factorSexo), 2)
        return estaturaEstimada

    def VerificarValoresAtributos(self):
        pesoMínimo = 1
        pesoMáximo = 500
        estaturaMínima = 0.25
        estaturaMáxima = 2.8
        añoMínimo = 1900
        añoMáximo = date.today().year
        mesMínimo = 1
        mesMáximo = 12
        díaMínimo = 1
        díaMáximo = None
        if self.peso < pesoMínimo or self.peso > pesoMáximo:
            raise ValueError("peso por fuera del rango válido establecido")
        if self.estatura < estaturaMínima or self.estatura > estaturaMáxima:
            raise ValueError("estatura por fuera del rango válido")
        if self.añoNacimiento <= añoMínimo or self.añoNacimiento > añoMáximo:
            raise ValueError("año de nacimiento por fuera del rango válido")
        if self.mesNacimiento < mesMínimo or self.mesNacimiento > mesMáximo:
            raise ValueError("mes de nacimiento por fuera del rango válido")
        if self.mesNacimiento == 2:
            if self.añoNacimiento % 4 == 0 and (self.añoNacimiento % 100 != 0 or self.añoNacimiento % 400 == 0):
                díaMáximo = 29
            else:
                díaMáximo = 28
        elif self.mesNacimiento in (4, 6, 9, 11):
            díaMáximo = 30
        else:
            díaMáximo = 31
        if self.díaNacimiento < díaMínimo or self.díaNacimiento > díaMáximo:
            raise ValueError("día de nacimiento por fuera del rango válido")
        if self.sexo not in ("f", "m"):
            raise ValueError("sexo no válido, debe ser la letra f o la letra m")    