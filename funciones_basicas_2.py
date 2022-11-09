#1
#Cuenta regresiva: crea una función que acepte un número como entrada. 
#Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

def countdown(num):
    lista = []       #creamos lista vacia para poner todos los numeros q recibamos
    for x in range(num, -1, -1): #(num: con el q comenzamos (5), -1 dnd queremos q pare, -1 como queremos q avance)
        lista.append(x)
        #lista += [x] tb se puede hacer asi
    return lista

lista_countdown = countdown(5)
print(lista_countdown)
        


#la misma funcion pero con while y con valor countdown 10
def countdownWhile(num):
    lista = []
    while num > -1:       #condicional
        lista.append(num) #append: agregar a la lista
        num -= 1
    return lista

lista_countdown = countdownWhile(10)
print(lista_countdown)      
#print(countdown(10)) tb se en puede poner solo el print (en vez de la linea 25 y 26)
print("---------")




#2
#Imprimir y devolver: crea una función que reciba una lista con dos números. 
#Imprime el primer valor y devuelve el segundo.
#Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

def imprimir_y_devolver(lista): #lista = [1, 2]
    print(lista[0])
    return lista[1]
    
imprimir_y_devolver([1, 2])
print("---------")




#3
#Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, 
#más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
def primero_mas_longitud(lista):
    sum = lista[0] + len(lista)
    return sum

total = primero_mas_longitud([1, 2, 3, 4, 5])
print(total)
print("---------")




#4
#Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva lista que contenga solo 
#los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego 
#devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
def valores_mayores_que_el_segundo(lista):
    nueva_lista = []
    if len(lista) < 2:
        return False
    else:
        for num in lista:
            if num > lista[1]:
                nueva_lista.append(num)

        print(len(nueva_lista))
        return nueva_lista

valores_mayores_que_el_segundo([5,2,3,2,1,4]) 


#otra forma de hacerlo (compañeras)
def valor_mayor_que_el_segundo(lista):
    lista_nueva = []
    if len(lista) <= 1:
        return False
    for i in range(len(lista)):
        if (lista[i] > lista[1] and i!= 1):
            lista_nueva.append(lista[i])
    print(len(lista_nueva))
    return lista_nueva

print(valor_mayor_que_el_segundo([5,2,3,2,1,4]))
print(valor_mayor_que_el_segundo([3]))
print("---------")





#5
#Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
#La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos 
#el valor dado.
#Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
def longitud_y_valor(longitud, valor):
    lista = []
    for x in range(longitud):
        lista.append(valor)
    
    return lista
print(longitud_y_valor(4, 7))


#otra forma de hacerlo
def length_and_value(length, value):
    lista = [value]*length
    return lista
result1 = length_and_value(6, 2)
print(result1)


