from collections import deque 
## SISTEMA DE GESTION DE BIBLIOTECA

book = [] ## VARIABLE DE TIPO LISTA
book.append("")
user = []  ## VARIABLE DE TIPO COLA
user.append("")

                                                                ##BOTON DE VOLVER AL MENU ANTERIOR
##PRIMERA PANTALLA
name = input("Crea por favor tu usuario : ")  ## Funcion disponible
name =input("")

def Create_User(): 
    global user
    
    if user:
        name.append(user) 
        print(f"Tu usuario es: {user} agregado correctamente {user}") ## Funcion disponible
         ##SEGUNDA PANTALLA
    else:
        print("El nombre no puede estar vacio")





##TERCERA PANTALLA

while True:
    print("Por favor presionar varias veces enter para  que conozca las categorias en libros que tenemos para usted: ")

    ##MENU DE OPCIONES 
    input("1.Ingenieria ")  ##Funcion disponible
    input("2.Medicina ")    ##Funcion disponible
    input("3.Historia ")    ##Funcion disponible
    input("4.Psicologia ")  ##Funcion disponible
    input("5.Sexologia ")   ##Funcion disponible
    input("6.Ocio ")        ##Funcion disponible
    input("7.Literatura")   ##Funcion disponible
    input("8.¿Deseas ver los libros escogidos? ") ##Funcion disponible
    input("9.¿Deseas eliminar el usuario? ")      ##Funcion disponible
    input("10. Realizar busqueda de libros en general por fecha, autor, año de publicacion") ##Funcion aun no disponible


    
    option = input("Elige por favor entre el (1-7) para escoger las categorias en libros que tenemos para usted: ")
    print("**Aviso importante escribe solo el primer nombre del libro, enfrente del titulo, o obra, que desees tomar ")
    
    match option:

        case "1":
         

            print("Por favor de nuevo presionar varias veces enter: ")
            book_inginier = [      
            
            input("1. Clean code: "),
            input("2. Clean architecture: "),
            input("3. User stories appilled: "),
            input("4. BDD in action: "),
            input("5. Los secretos del software:"),
            input("6. Estructuras de datos y algoritmos: "),

            ]

            book.extend([books for books in  book_inginier if books.strip()])

            input(" Presiona enter para volver al menu anterior... ")
            continue
        case "2":

            print("Por favor de nuevo presionar varias veces enter: ")

            book_medicine = [     
            input("1. Tratado de fisiologia medica "),
            input("2. Harrison y cotran. Patalogia estructural y funcional"),
            input("3. Robbins y cotran. Patologia estructural y funcional"),
            input("4. Atlas de antomia humana"),
            input("5. El emperador de todos los males: una biografía del cáncer"),
            input("6. Esto va a doler: diarios secretos de un médico junior"),
            input(" Volver al menu anterior enter... ")
            ]
            book.extend([books for books in  book_medicine if books.strip()])
            input(" Presiona enter para volver al menu anterior... {option}")
            continue
        case "3":
            print("Por favor de nuevo presionar varias veces enter: "),
            book_history = [      
            
            input("1. Sapiens: De animales a dioses: "),
            input("2. Armas, gérmenes y acero Breve historia de todo el mundo durante los últimos 13.000 años: "),
            input("3. La historia del mundo contada para escépticos: "),
            input("4. Una breve historia de casi todo: "),
            input("5. Los pilares de la Tierra: "),
            input("6. SPQR: Una historia de la antigua Roma: "),
            input("6. SPQR: Una historia de la antigua Roma: "),
            input(" Volver al menu anterior enter... "),
             ]
            book.extend([books for books in  book_history if books.strip()])
      
            continue
        case "4":
            print("Por favor de nuevo presionar varias veces enter: ")
            input("1. Pensar rápido, pensar despacio")
            input("2. Inteligencia emocional")
            input("3. El hombre en busca de sentido" )
            input("4. Mujeres que corren con los lobos")
            input("5. El arte de amar")
            input("6. Tus zonas erróneas" )
            input(" Volver al menu anterior enter... ")

            book.extend("1. Pensar rápido, pensar despacio","2. Inteligencia emocional","4. Mujeres que corren con los lobos","5. El arte de amar","6. Tus zonas erróneas")
            continue
        case "5":
            print("Por favor de nuevo presionar varias veces enter: ")
            input("1. Tus zonas erróneas" )
            input("2. Mitos del sexo")
            input("3. La función del orgasmo")
            input("4. Mujeres orgásmicas")
            input("5. Sexperimentando")
            input("6. El hombre multiorgásmico")
            
            book.extend("1. Tus zonas erróneas","2. Mitos del sexo","3. La función del orgasmo","4. Mujeres orgásmicas","5. Sexperimentando","6. El hombre multiorgásmico")
            continue
        case "6":
            input("1.El camino del artista" )
            input("2.Destroza este diario")
            input("3.Guía de la escalada en bloque: 50 movimientos clave, 10 combinaciones técnicas" )
            input("4.101 destinos del mundo sorprendentes")
            input("5.Momentos de quietud con Dios: 365 Inspiraciones Diarias. Meyer, Joyce")
            input("6.Páramos para colorear")
            input(" Volver al menu anterior enter... ")
            book.extend("1.El camino del artista","2.Destroza este diario","3.Guía de la escalada en bloque: 50 movimientos clave, 10 combinaciones técnicas","4.101 destinos del mundo sorprendentes","5.Momentos de quietud con Dios: 365 Inspiraciones Diarias. Meyer, Joyce","6.Páramos para colorear")
            continue
        case "7":
            print("Por favor de nuevo presionar varias veces enter: ")
            input("1.Cien años de soledad")
            input("2.Don Quijote de la Mancha")
            input("3.Orgullo y prejuicio")
            input("4.Crimen y castigo" )
            input("5.La Odisea")
            input("5.El amor en los tiempos del cólera")
            input(" Volver al menu anterior enter... ")
            book.extend("1.Cien años de soledad","2.Don Quijote de la Mancha","3.Orgullo y prejuicio","4.Crimen y castigo","5.La Odisea","5.El amor en los tiempos del cólera","5.La Odisea","5.El amor en los tiempos del cólera")
            continue

        
        
        
        case "8":
            ## QUINTA PANTALLA
            print("Ten en cuenta que el prestamo esta vigente por los siguientes 15 dias")
            print("Estos son los libros que tomaste en alquiler: ") 
            for i, books in enumerate(book, 1):
                print(f"{i}. {books}")
            list = int(input("ingrese el numero del libro que deseas eliminar: ")) - 1
           
            if 0 <= list < len(book):
                 erased = book.pop(list)
       
            for i, erased in enumerate(book, 1):
                print("Se elemino satisfactoriamente: ")
                print(f"{i}. {erased}")
            else : 
                print("Ingresa un numero por favor")


            
        case "9":
            ##QUINTA PANTALLA
           def unstack_element():
               global user
               if  user: 
                print("La pila esta vacia")
                return None
               else:     
                    unstack_element = user.pop()
                    print(f"eliminado{unstack_element}".eleminado)               
                                
               unstack_element()                 
                
           
        




