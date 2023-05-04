class Moto():

    def __init__(self, color, matricula, combistuble_litro, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, precio, capacidad_tanque): 

        self.color = color
        self.matricula = matricula
        self.combustible_litro = combistuble_litro
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.precio = precio
        self.capacidad_tanque = capacidad_tanque
        self.motor = False
        

    def encender(self):
        if self.motor:
            print('La moto',self.marca, self.modelo,'Ya estaba encendida')
        else:
            self.motor = True
            print('La moto',self.marca, self.modelo,'Se ha encendido')
        

    def apagar(self):
        if self.motor:
            self.motor = False 
            print('La moto',self.marca, self.modelo,'Se ha apagado')
        else:
            print('La moto',self.marca, self.modelo,'Ya estaba apagada')

    def checar_precio(self):
        print('La moto',self.modelo,self.marca,'Tiene un precio de',self.precio)

    def checar_gas(self):
        gas_faltante = self.capacidad_tanque - self.combustible_litro
        print('=====> Reporte del depósito de',self.marca, self.modelo,'de motocicleta» <=====.',
        '\nCombustible disponible:',self.combustible_litro,'Litros',
        '\nCapacidad de tanque:',self.capacidad_tanque, 'Litros',
        '\nLitros Faltantes a llenar:', gas_faltante,)

    def reposar(self):
        reposar = int(input('Cantidad de gas que debe de tener para reposar'))
        while True:
            if reposar > self.capacidad_tanque:
                print('Los litros no puede sobrepasar la cantidad maxima del tanque')
                reposar = int(input('Cantidad de gas que tiene que tener para reposar'))

            elif reposar < self.combustible_litro:
                print("La cantidad de gas que la",self.marca,self.modelo,'tiene es de:',self.combustible_litro)
                break
            else:
                print("La cantidad de gas que la",self.marca,self.modelo,'tiene es de:',self.combustible_litro)
                print('La Moto',self.marca,self.modelo,'debe reposar')
                break

    def menu(self):
        print('=======> Modelo de moto:',self.marca,self.modelo,'<=======')
        print('=======> Selecciona la opcion a elejir <=======')
        while True:
            print(  '\n Encender.',
                        '\n Apagar.',
                        '\n Cechar precio.',
                        '\n Checar gas.',
                        '\n Reposar.',
                        '\n Salir.')
            opcion = input('')
            if opcion.lower() == 'encender':
                self.encender()
            elif opcion.lower() == 'apagar':
                self.apagar()
            elif opcion.lower() == 'checar precio':
                self.checar_precio()
            elif opcion.lower() == 'checar gas':
                self.checar_gas()
            elif opcion.lower() == 'reposar':
                self.reposar()
            elif opcion.lower() == 'salir':
                break
            else:
                print('Valor invalido')

italika = Moto('Negro', 123, 1, 2, 'Italika', 'c300', 2023, '120k/h', '40,000 Pesos',10)
ninja =   Moto('Negro', 158, 10, 2, 'Yamaha', 'ninja', 2023, '250k/h', '110,000',15)

ninja.menu()