from datetime import date

class paciente:
    
    def __init__(self, nombreCompleto , peso, estatura, anioNacimiento, mesNacimiento, diaNacimiento):
        self.nombreCompleto = nombreCompleto
        self.peso = peso
        self.estatura = estatura
        self.anioNacimiento = anioNacimiento
        self.mesNacimiento = mesNacimiento
        self.diaNacimiento = diaNacimiento

    def ValidarPeso (self):
        pesoValidado  = False
        # El peso mínimo de un bebé es de 2.5kg y 594.8kg es el record guinness del mayor peso
        # -5% de 2.5 = 2.375; +5% de 594.8 = 654.54.
        if (2.37 <= self.peso <= 624):
            pesoValidado = True
        return pesoValidado
    
    def ValidarEstatura (self):
        estaturaValidada = False
        # La estatura mínima de un bebe es de 35cm y el record guinness de la persona más alta es de 2.43m
        # 35cm = 0.35m
        # -5% de 0.35 = 0.3325
        # +5% de 2.43 = 2.5515
        if (0.33 <= self.estatura <= 2.55):
            estaturaValidada = True
        return estaturaValidada
    
    def ValidarFecha (self):
        fechaDeHoy = date.today()
        # Se le asigna dicho valor por la persona que mas ha vivido en la historia 115 años
        # +5% de 115 = 120
        limiteEdad = fechaDeHoy.year - 120
        rangoDias = False
        anioBisiesto = False
        fechaValidada = False  # RETORNA

        if (self.anioNacimiento % 4 == 0 and ( self.anioNacimiento % 100 != 0 or self.anioNacimiento % 400 == 0)):
            anioBisiesto = True
        
        if ((
        # Validando meses con 31 días
        (self.mesNacimiento == 1
        or self.mesNacimiento == 3
        or self.mesNacimiento == 5
        or self.mesNacimiento == 7
        or self.mesNacimiento == 8
        or self.mesNacimiento == 10
        or self.mesNacimiento == 12)
        and (0 < self.diaNacimiento <= 31))

        # Validando meses con 30 días 
        or ((self.mesNacimiento == 4
        or self.mesNacimiento == 6
        or self.mesNacimiento == 9
        or self.mesNacimiento == 11)
        and (0 < self.diaNacimiento <= 30))

        # FEBRERO =========================
        # Año bisiesto
        or (((self.mesNacimiento == 2)
        and (anioBisiesto == True))
        and (0 < self.diaNacimiento <= 29))
        # Año no bisiesto
        or ((self.mesNacimiento == 2))
        and (anioBisiesto == False)
        and (0 < self.diaNacimiento <= 28)):
            rangoDias = True
        
        if (( (rangoDias == True) and (0 < self.mesNacimiento <= 12) and (limiteEdad <= self.anioNacimiento <= fechaDeHoy.year))):
            fechaValidada = True
        return fechaValidada
        
        

    def CalcularEdad (self):
        fechaDeHoy = date.today()
        rangoDias = self.ValidarFecha()
        edad = None # RETORNA
        restar = 0
        
        if (rangoDias == True):
            diferenciaDeAnios =  fechaDeHoy.year - self.anioNacimiento
            diferenciaDeMeses = fechaDeHoy.month - self.mesNacimiento
            diferenciaDeDias = fechaDeHoy.day - self.diaNacimiento
            if diferenciaDeMeses < 0 or (diferenciaDeMeses==0 and diferenciaDeDias < 0):
                restar=1
            edad = diferenciaDeAnios - restar
        return edad
        
    def DeterminarCategoriaEdad (self):
        categoriaEdad = None
        edad = self.CalcularEdad()
        if edad == None:
            categoriaEdad = None
        elif edad >=18:
            categoriaEdad = "mayor de edad"
        else:
            categoriaEdad = "menor de edad"
        return categoriaEdad
    
    def IndiceMasaCorporal (self):
        imc  = None
        limitePeso = self.ValidarPeso()
        if (limitePeso == True):
            imc = round(self.peso / (self.estatura **2),2)
        return imc
    
    def NivelDePesoPaciente (self):
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