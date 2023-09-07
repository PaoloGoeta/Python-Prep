class Operaciones:

    def __init__ (self, lista_prueba):
        self.lista = lista_prueba

    def es_primo(self):
        for i in self.lista:
            if (self.__es_primo(i)):
                print('El número ', i, 'es primo')
            else:
                print('El número ', i, 'no es primo')



    def convertidor_temperatura(self, unidad_origen, unidad_destino):
        for i in self.lista:
            print(i,' grados', unidad_origen, self.__convertidor_temperatura (i,unidad_origen,unidad_destino),'grados ', unidad_destino)



    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', factorial)

#verificar primo    

    def __es_primo(self,a):
        primo = True
        for i in range(2, a):
            if a % i == 0:
                primo = False
            break
        return primo
    


#valor modal

    def repetido(lista):
        lista_unicos = []
        lista_repetidos = []
        if len(lista) == 0:
            return None
        for elemento in lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repetidos[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repetidos.append(1)
        repeticiones = lista_unicos[0]
        maximo = lista_repetidos[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repetidos[i] > maximo:
                repeticiones = lista_unicos[i]
                maximo = lista_repetidos[i]
        return repeticiones, maximo
    



#Conversión grados

    def __convertidor_temperatura(self,valor, unidad_origen, unidad_destino):
        if (unidad_origen == "C" and unidad_destino == "F"):
            return valor * 9/5 + 32
        elif (unidad_origen == "F" and unidad_destino == "C"):
            return (valor - 32) * 5/9
        elif (unidad_origen == "C" and unidad_destino == "K"):
            return valor + 273.15
        elif (unidad_origen == "K" and unidad_destino == "C"):
            return valor - 273.15
        elif (unidad_origen == "F" and unidad_destino == "K"):
            celsius = (valor - 32) * 5/9
            return celsius + 273.15
        elif (unidad_origen == "K" and unidad_destino == "F"):
            celsius = valor - 273.15
            return celsius * 9/5 + 32
        else:
            return valor 
        


#Factorial
            
    def factorial(self,numero):

        if(type(numero) != int):
            return 'El número tiene que ser un entero'
        elif(numero < 0):
            return 'El número tiene que ser pósitivo'
        else:
            for i in range(1,numero):        
                numero *= i

        return numero
    



