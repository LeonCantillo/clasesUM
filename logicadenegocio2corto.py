from datetime import date

class paciente:
    
    def __init__(self, nombreCompleto:str , peso:float, estatura:float, anioNacimiento:int, mesNacimiento:int, diaNacimiento:int, sexo:str):
        self.nombreCompleto = nombreCompleto
        self.peso = peso
        self.estatura = estatura
        self.anioNacimiento = anioNacimiento
        self.mesNacimiento = mesNacimiento
        self.diaNacimiento = diaNacimiento
        self.sexo = sexo
        self.VerificarValoresAtributos()

    def ValidarSexo(self):
        if self.sexo not in ("f", "m"):
            raise ValueError("sexo no válido, debe ser la letra f o la letra m")

    def ValidarPeso (self):
        # El peso mínimo de un bebé es de 2.5kg y 594.8kg es el record guinness del mayor peso
        # -5% de 2.5 = 2.375; +5% de 594.8 = 654.54.
        if not (2.37 <= self.peso <= 624):
            raise ValueError("Peso por fuera del rango válido establecido")
    
    def ValidarEstatura (self):
        # La estatura mínima de un bebe es de 35cm y el record guinness de la persona más alta es de 2.43m
        # 35cm = 0.35m
        # -5% de 0.35 = 0.3325
        # +5% de 2.43 = 2.5515
        if (0.33 <= self.estatura <= 2.55):
            raise ValueError("Estatura por fuera del rango válido")
    
    def ValidarFecha (self):
        fechaDeHoy = date.today()
        # Se le asigna dicho valor por la persona que mas ha vivido en la historia 115 años
        # +5% de 115 = 120
        limiteEdad = fechaDeHoy.year - 120

        def anioBisiesto(anio):
            return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

        diasPorMes = {
            1: 31,
            2: 29 if anioBisiesto(self.anioNacimiento) else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        diasEnMes = diasPorMes[self.mesNacimiento]
        
        if not (1 <= self.diaNacimiento <= diasEnMes):
            raise ValueError("Día de nacimiento por fuera del rango válido")
        elif not (1 <= self.mesNacimiento <= 12):
            raise ValueError("Mes de nacimiento por fuera del rango válido")
        elif not (limiteEdad <= self.anioNacimiento <= fechaDeHoy.year):
            raise ValueError("Año de nacimiento por fuera del rango válido")
        
        

    def CalcularEdadEnAniosyMeses (self):
        self.ValidarFecha()
        fechaDeHoy = date.today()
        edadFinal = {"edadEnAnios": "", "edadEnMeses": ""}
        edadEnAnios = None # RETORNA
        edadEnMeses = None # RETORNA
        restarAnios = 0
        diferenciaDeAnios = fechaDeHoy.year - self.anioNacimiento
        diferenciaDeMeses = fechaDeHoy.month - self.mesNacimiento
        diferenciaDeDias = fechaDeHoy.day - self.diaNacimiento
        if diferenciaDeMeses < 0 or (diferenciaDeMeses == 0 and diferenciaDeDias < 0):
            restarAnios = 1
        edadEnAnios = diferenciaDeAnios - restarAnios
        mesesParaSumar = 0
        if restarAnios == 0:
            restarMeses = 0
            if diferenciaDeMeses > 0 and diferenciaDeDias < 0:
                restarMeses = 1
            mesesParaSumar = diferenciaDeMeses - restarMeses
        else:
            restarMeses = 0
            if diferenciaDeMeses < 0 and diferenciaDeDias < 0:
                restarMeses = 1
            mesesParaSumar = 12 + diferenciaDeMeses - restarMeses
        edadEnMeses = edadEnAnios * 12 + mesesParaSumar
        edadFinal["edadEnAnios"] = edadEnAnios
        edadFinal["edadEnMeses"] = edadEnMeses
        return edadFinal
        
    def DeterminarCategoriaEdad (self):
        categoriaEdad = None
        edad = self.CalcularEdadEnAniosyMeses["edadEnAnios"]
        if edad is not None:
            if edad >= 18:
                categoriaEdad = "mayor de edad"
            else:
                categoriaEdad = "menor de edad"
        return categoriaEdad
    
    def IndiceMasaCorporal (self):
        self.ValidarPeso()
        return round(self.peso / (self.estatura **2),2)
    
    def NivelDePesoPaciente (self):
        self.ValidarPeso()
        nivelPeso = None
        imc = self.IndiceMasaCorporal()
        if imc >= 30 :
            nivelPeso = "Obesidad"
        elif imc >= 25:
            nivelPeso = "sobrepeso"
        elif imc >= 18:
            nivelPeso = "Peso normal"
        else: 
            nivelPeso = "Peso Bajo" 
        return nivelPeso
    
    def VerificarValoresAtributos(self):
        self.ValidarPeso()
        self.ValidarEstatura()
        self.ValidarFecha()
        self.sexo()