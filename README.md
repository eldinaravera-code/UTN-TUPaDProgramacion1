# UTN-TUPaDProgramacion1

1repositorio programacion 1







\#ejercicio 1 

\#pedir el nombre del cliente

nombre = input("cliente:")

while nombre =="" or not nombre.isalpha():

&#x20;   print("Error: el nombre no puede estar vacío y debe contener solo letras.")

&#x20;   nombre = input("cliente:")

\#pedir la cantidad de productos

cantidad\_productos = input("cantidad de productos:")

while not cantidad\_productos.isdigit() or int(cantidad\_productos) <= 0:

&#x20;   print("Error: la cantidad de productos debe ser un número entero positivo.")

&#x20;   cantidad\_productos = input("cantidad de productos:")

cantidad = int(cantidad\_productos)

\#variables para acumular el total y el descuento

total\_sin\_descuento = 0

total\_con\_descuento = 0

\#pedir datos de cada producto

for i in range(cantidad):

&#x20;   precio = input(f"precio del producto {i+1}:")

&#x20;   while not precio.isdigit():

&#x20;       print("error: el precio debe ser un numero entero.")

&#x20;       precio = input(f"precio del producto {i+1}:")

&#x20;   precio = int(precio)

&#x20;   descuento = input("descuento (s/n):")

&#x20;   while descuento.lower() != "s" and descuento.lower() != "n":

&#x20;       print("error: debe ingresar 's' para sí o 'n' para no.")

&#x20;       descuento = input("descuento (s/n):")

&#x20;   #acumular el precio original

&#x20;   total\_sin\_descuento += precio

&#x20;   #aplicar el descuento si corresponde 

&#x20;   if descuento.lower() =="s":

&#x20;       precio\_con\_descuento = precio \* 0.9  # aplicar un 10% de descuento

&#x20;   else:

&#x20;       precio\_con\_descuento = precio

&#x20;   #acumular el precio final 

&#x20;   total\_con\_descuento += precio\_con\_descuento

\#calcular ahorro 

ahorro =total\_sin\_descuento -total\_con\_descuento

\#calcular promedio

promedio = float (total\_con\_descuento) / cantidad

\#mostrar resultados 

print()

print("resumen de la compra")

print(f"cliente: {nombre}")

print(f"total sin descuento: ${total\_sin\_descuento}")

print(f"total con descuento: ${total\_con\_descuento:.2f}")

print(f"ahorro: ${ahorro:.2f}")

print(f"promedio por producto: ${promedio:.2f}")





\#ejercicio 2 



\#credenciales correctas

usuario\_correcto = "alumno"

clave\_correcta = "python123"



\#cantidad de intentos 

intentos = 0

accesos = False



\#login

while intentos < 3: 

&#x20;   usuario = input(f"intento {intentos + 1}/3 - usuario:")

&#x20;   clave = input("clave:")

&#x20;   if usuario == usuario\_correcto and clave == clave\_correcta:

&#x20;       print("acceso concedido")

&#x20;       accesos = True

&#x20;       break

&#x20;   else:

&#x20;       print("usuario o clave incorrectos")

&#x20;       intentos += 1

\# si no pudo ingresar despues de 3 intentos 



if not accesos:

&#x20;   print("cuenta bloqueada")

else: #volver al menu

&#x20;   opcion = ""

&#x20;   while opcion != "4":

&#x20;       print()

&#x20;       print("1) estado")

&#x20;       print("2) cambiar de clave")

&#x20;       print("3) mensaje")

&#x20;       print("4) salir")

&#x20;       opcion = input("opcion: ")



\#validar que sea un numero 

while not opcion.isdigit():

&#x20;   print("error:ingrese un numero valido.")

&#x20;   opcion = input("opcion: ")

\#convertir a numreo entero 

opcion =int(opcion)

\#validar que este entre 1 y 4 

while opcion <1 or opcion >4:

&#x20;   print("error: fuera de rango. ingrese un numero entre 1 y 4.")

&#x20;   opcion =input("opcion: ")

&#x20;   while not opcion.isdigit():

&#x20;       print("error: ingrese un numero valido.")

&#x20;       opcion = input("opcion: ")

&#x20;   opcion = int (opcion)

\#opcion 1 

if opcion == 1:

&#x20;   print("estado: inscripto")

\#opcion 2 

elif opcion == 2:

&#x20;   nueva\_clave = input("ingrese nueva clave:")

&#x20;   while len(nueva\_clave) < 6:

&#x20;       print("error: la clave debe tener al menos 6 caracteres.")

&#x20;       nueva\_clave = input("ingrese nueva clave:")

&#x20;   confirmacion = input("confirme nueva clave:")

&#x20;   while nueva\_clave != confirmacion:

&#x20;       print("error: las claves no coinciden.")

&#x20;       confirmacion = input("confirme nueva clave:")

&#x20;   clave\_correcta = nueva\_clave

&#x20;   print("clave cambiada con exito")

\#opcion 3 

elif  opcion == 3:

&#x20;   print("segui avanzando!")

\#opcion 4 

elif opcion == 4:

&#x20;   print("sesion finalizada.")



\# no se porque no me ejecuta las opciones ya probe de varias maneras y no me funciona, me podrias ayudar a corregirlo ? gracias 











\#ejercicio 3



\# AGENDA DE TURNOS



\# TURNOS DEL DIA LUNES

lunes\_t1 = ""

lunes\_t2 = ""

lunes\_t3 = ""

lunes\_t4 = ""



\# TURNOS DEL DIA MARTES

martes\_t1 = ""

martes\_t2 = ""

martes\_t3 = ""





\# NOMBRE DEL OPERADOR

operador = input("Nombre del operador: ")



while operador == "" or not operador.isalpha():

&#x20;   print("Error: el nombre del operador no puede estar vacio y debe contener solo letras.")

&#x20;   operador = input("Ingrese el nombre del operador: ")



print(f"Bienvenido {operador}!")





\# MENU PRINCIPAL

opcion = ""



while opcion != 5:



&#x20;   print()

&#x20;   print("========== MENU PRINCIPAL ==========")

&#x20;   print("1) Reservar turno")

&#x20;   print("2) Cancelar turno")

&#x20;   print("3) Ver agenda del dia")

&#x20;   print("4) Ver resumen general")

&#x20;   print("5) Cerrar sistema")



&#x20;   opcion = input("Seleccionar una opcion: ")



&#x20;   # VALIDAR QUE SEA UN NUMERO

&#x20;   while not opcion.isdigit():

&#x20;       print("Error: ingrese un numero valido del 1 al 5.")

&#x20;       opcion = input("Seleccionar una opcion: ")



&#x20;   # PASAR DE TEXTO A NUMERO

&#x20;   opcion = int(opcion)



&#x20;   # VALIDAR QUE ESTE ENTRE 1 Y 5

&#x20;   while opcion < 1 or opcion > 5:



&#x20;       print("Error: ingrese un numero del 1 al 5.")



&#x20;       opcion = input("Seleccionar una opcion: ")



&#x20;       while not opcion.isdigit():

&#x20;           print("Error: ingrese un numero valido del 1 al 5.")

&#x20;           opcion = input("Seleccionar una opcion: ")



&#x20;       opcion = int(opcion)





&#x20;   # OPCION 1 RESERVAR TURNO



&#x20;   if opcion == 1:



&#x20;       # PEDIR DIA

&#x20;       dia = input("Ingrese el dia para reservar (lunes/martes): ")



&#x20;       while dia.lower() != "lunes" and dia.lower() != "martes":

&#x20;           print("Error: ingrese un dia valido (lunes/martes).")

&#x20;           dia = input("Ingrese el dia para reservar (lunes/martes): ")





&#x20;       # PEDIR NOMBRE DEL PACIENTE

&#x20;       paciente = input("Ingrese el nombre del paciente: ")



&#x20;       while paciente == "" or not paciente.isalpha():

&#x20;           print("Error: el nombre del paciente no puede estar vacio y debe contener solo letras.")

&#x20;           paciente = input("Ingrese el nombre del paciente: ")





&#x20;       # VERIFICAR SI EL PACIENTE YA TIENE UN TURNO

&#x20;       if (paciente.lower() == lunes\_t1.lower() or

&#x20;           paciente.lower() == lunes\_t2.lower() or

&#x20;           paciente.lower() == lunes\_t3.lower() or

&#x20;           paciente.lower() == lunes\_t4.lower() or

&#x20;           paciente.lower() == martes\_t1.lower() or

&#x20;           paciente.lower() == martes\_t2.lower() or

&#x20;           paciente.lower() == martes\_t3.lower()):



&#x20;           print("Error: el paciente ya tiene un turno reservado.")





&#x20;       # RESERVAR LUNES

&#x20;       elif dia.lower() == "lunes":



&#x20;           if lunes\_t1 == "":

&#x20;               lunes\_t1 = paciente

&#x20;               print("Turno reservado correctamente.")



&#x20;           elif lunes\_t2 == "":

&#x20;               lunes\_t2 = paciente

&#x20;               print("Turno reservado correctamente.")



&#x20;           elif lunes\_t3 == "":

&#x20;               lunes\_t3 = paciente

&#x20;               print("Turno reservado correctamente.")



&#x20;           elif lunes\_t4 == "":

&#x20;               lunes\_t4 = paciente

&#x20;               print("Turno reservado correctamente.")



&#x20;           else:

&#x20;               print("No hay turnos disponibles para el dia lunes.")





&#x20;       # RESERVAR MARTES

&#x20;       else:



&#x20;           if martes\_t1 == "":

&#x20;               martes\_t1 = paciente

&#x20;               print("Turno reservado correctamente.")



&#x20;           elif martes\_t2 == "":

&#x20;               martes\_t2 = paciente

&#x20;               print("Turno reservado correctamente.")



&#x20;           elif martes\_t3 == "":

&#x20;               martes\_t3 = paciente

&#x20;               print("Turno reservado correctamente.")



&#x20;           else:

&#x20;               print("No hay turnos disponibles para el dia martes.")





&#x20;   # OPCION 2: CANCELAR TURNO



&#x20;   elif opcion == 2:



&#x20;       # PEDIR DIA

&#x20;       dia = input("Ingrese el dia del turno a cancelar (lunes/martes): ")



&#x20;       while dia.lower() != "lunes" and dia.lower() != "martes":

&#x20;           print("Error: ingrese un dia valido (lunes/martes).")

&#x20;           dia = input("Ingrese el dia del turno a cancelar (lunes/martes): ")





&#x20;       # PEDIR PACIENTE

&#x20;       paciente = input("Ingrese el nombre del paciente: ")



&#x20;       while paciente == "" or not paciente.isalpha():

&#x20;           print("Error: el nombre del paciente no puede estar vacio y debe contener solo letras.")

&#x20;           paciente = input("Ingrese el nombre del paciente: ")





&#x20;       # CANCELAR TURNO DEL LUNES

&#x20;       if dia.lower() == "lunes":



&#x20;           if paciente.lower() == lunes\_t1.lower() and lunes\_t1 != "":

&#x20;               lunes\_t1 = ""

&#x20;               print("Turno cancelado correctamente.")



&#x20;           elif paciente.lower() == lunes\_t2.lower() and lunes\_t2 != "":

&#x20;               lunes\_t2 = ""

&#x20;               print("Turno cancelado correctamente.")



&#x20;           elif paciente.lower() == lunes\_t3.lower() and lunes\_t3 != "":

&#x20;               lunes\_t3 = ""

&#x20;               print("Turno cancelado correctamente.")



&#x20;           elif paciente.lower() == lunes\_t4.lower() and lunes\_t4 != "":

&#x20;               lunes\_t4 = ""

&#x20;               print("Turno cancelado correctamente.")



&#x20;           else:

&#x20;               print("Error: el paciente no tiene un turno reservado para el dia lunes.")





&#x20;       # CANCELAR TURNO DEL MARTES

&#x20;       else:



&#x20;           if paciente.lower() == martes\_t1.lower() and martes\_t1 != "":

&#x20;               martes\_t1 = ""

&#x20;               print("Turno cancelado correctamente.")



&#x20;           elif paciente.lower() == martes\_t2.lower() and martes\_t2 != "":

&#x20;               martes\_t2 = ""

&#x20;               print("Turno cancelado correctamente.")



&#x20;           elif paciente.lower() == martes\_t3.lower() and martes\_t3 != "":

&#x20;               martes\_t3 = ""

&#x20;               print("Turno cancelado correctamente.")



&#x20;           else:

&#x20;               print("Error: el paciente no tiene un turno reservado para el dia martes.")





&#x20;   # OPCION 3: VER AGENDA DEL DIA



&#x20;   elif opcion == 3:



&#x20;       dia = input("Ingrese el dia para ver la agenda (lunes/martes): ")



&#x20;       while dia.lower() != "lunes" and dia.lower() != "martes":

&#x20;           print("Error: ingrese un dia valido (lunes/martes).")

&#x20;           dia = input("Ingrese el dia para ver la agenda (lunes/martes): ")





&#x20;       # AGENDA DEL LUNES

&#x20;       if dia.lower() == "lunes":



&#x20;           print()

&#x20;           print("AGENDA DEL DIA LUNES")



&#x20;           print(f"Turno 1: {lunes\_t1 if lunes\_t1 else 'disponible'}")

&#x20;           print(f"Turno 2: {lunes\_t2 if lunes\_t2 else 'disponible'}")

&#x20;           print(f"Turno 3: {lunes\_t3 if lunes\_t3 else 'disponible'}")

&#x20;           print(f"Turno 4: {lunes\_t4 if lunes\_t4 else 'disponible'}")





&#x20;       # AGENDA DEL MARTES

&#x20;       else:



&#x20;           print()

&#x20;           print("AGENDA DEL DIA MARTES")



&#x20;           print(f"Turno 1: {martes\_t1 if martes\_t1 else 'disponible'}")

&#x20;           print(f"Turno 2: {martes\_t2 if martes\_t2 else 'disponible'}")

&#x20;           print(f"Turno 3: {martes\_t3 if martes\_t3 else 'disponible'}")





&#x20;   # OPCION 4: VER RESUMEN GENERAL



&#x20;   elif opcion == 4:



&#x20;       # CONTAR TURNOS OCUPADOS DEL LUNES

&#x20;       turnos\_ocupados\_lunes = 0



&#x20;       if lunes\_t1 != "":

&#x20;           turnos\_ocupados\_lunes += 1



&#x20;       if lunes\_t2 != "":

&#x20;           turnos\_ocupados\_lunes += 1



&#x20;       if lunes\_t3 != "":

&#x20;           turnos\_ocupados\_lunes += 1



&#x20;       if lunes\_t4 != "":

&#x20;           turnos\_ocupados\_lunes += 1





&#x20;       # CONTAR TURNOS OCUPADOS DEL MARTES

&#x20;       turnos\_ocupados\_martes = 0



&#x20;       if martes\_t1 != "":

&#x20;           turnos\_ocupados\_martes += 1



&#x20;       if martes\_t2 != "":

&#x20;           turnos\_ocupados\_martes += 1



&#x20;       if martes\_t3 != "":

&#x20;           turnos\_ocupados\_martes += 1





&#x20;       # MOSTRAR RESUMEN

&#x20;       print()

&#x20;       print("RESUMEN GENERAL DE TURNOS")



&#x20;       print("Lunes")

&#x20;       print("Ocupados:", turnos\_ocupados\_lunes)

&#x20;       print("Disponibles:", 4 - turnos\_ocupados\_lunes)



&#x20;       print()



&#x20;       print("Martes")

&#x20;       print("Ocupados:", turnos\_ocupados\_martes)

&#x20;       print("Disponibles:", 3 - turnos\_ocupados\_martes)





&#x20;       # COMPARAR LOS DOS DIAS

&#x20;       if turnos\_ocupados\_lunes > turnos\_ocupados\_martes:



&#x20;           print("El dia lunes tiene mas turnos ocupados.")



&#x20;       elif turnos\_ocupados\_martes > turnos\_ocupados\_lunes:



&#x20;           print("El dia martes tiene mas turnos ocupados.")



&#x20;       else:



&#x20;           print("Ambos dias tienen la misma cantidad de turnos ocupados.")





&#x20;   # OPCION 5: CERRAR SISTEMA



&#x20;   elif opcion == 5:



&#x20;       print()

&#x20;       print("Sistema cerrado.")





print("Fin del programa.")



\#ejercicio 4 



\# ESCAPE ROOM: LA BOVEDA



\# Variables iniciales

energia = 100

tiempo = 12

cerraduras\_abiertas = 0

alarma = False

codigo\_parcial = ""



\# Variable para controlar las veces seguidas que se fuerza

forzar\_seguidas = 0





\# PEDIR NOMBRE DEL AGENTE

nombre = input("Ingrese el nombre del agente: ")

\#uso isalpha para que detecte que lo qeu se ingreso sean letras 



while not nombre.isalpha():

&#x20;   print("Error. El nombre debe contener solamente letras.")

&#x20;   nombre = input("Ingrese el nombre del agente: ")





print()

print("       ESCAPE ROOM: LA BOVEDA")

print("Agente:", nombre)





\# JUEGO PRINCIPAL

\#el juego continua solo si se dan todas las condiciones 

while energia > 0 and tiempo > 0 and cerraduras\_abiertas < 3:



&#x20;   # BLOQUEO POR ALARMA

&#x20;   if alarma and tiempo <= 3 and cerraduras\_abiertas < 3:

&#x20;       print()

&#x20;       print("       SISTEMA BLOQUEADO")

&#x20;       print("===================================")

&#x20;       print("La alarma se activo y queda poco tiempo.")

&#x20;       print("DERROTA.")

&#x20;       break



&#x20;   print()

&#x20;   print("-----------------------------------")

&#x20;   print("ESTADO ACTUAL")

&#x20;   print("Energia:", energia)

&#x20;   print("Tiempo:", tiempo)

&#x20;   print("Cerraduras abiertas:", cerraduras\_abiertas)

&#x20;   print("Codigo parcial:", codigo\_parcial)

&#x20;   print("-----------------------------------")



&#x20;   print("1. Forzar cerradura")

&#x20;   print("2. Hackear panel")

&#x20;   print("3. Descansar")



&#x20;   opcion = input("Elija una opcion: ")



&#x20;   # Validar que sea un numero

&#x20;   while not opcion.isdigit():

&#x20;       print("Error. Debe ingresar un numero.")

&#x20;       opcion = input("Elija una opcion: ")



&#x20;   opcion = int(opcion)



&#x20;   # Validar que sea 1, 2 o 3

&#x20;   while opcion < 1 or opcion > 3:

&#x20;       print("Error. La opcion debe ser 1, 2 o 3.")



&#x20;       opcion = input("Elija una opcion: ")



&#x20;       while not opcion.isdigit():

&#x20;           print("Error. Debe ingresar un numero del 1 al 3 .")

&#x20;           opcion = input("Elija una opcion: ")



&#x20;       opcion = int(opcion)





&#x20;   # FORZAR CERRADURA



&#x20;   if opcion == 1:



&#x20;       forzar\_seguidas = forzar\_seguidas + 1



&#x20;       # Costo normal

&#x20;       energia = energia - 20

&#x20;       tiempo = tiempo - 2



&#x20;       # REGLA ANTI-SPAM

&#x20;       if forzar\_seguidas == 3:



&#x20;           alarma = True



&#x20;           print()

&#x20;           print("La cerradura se trabo.")

&#x20;           print("ALARMA ACTIVADA.")

&#x20;           print("No se abrio la cerradura.")



&#x20;       else:



&#x20;           # Si hay riesgo de alarma

&#x20;           if energia <= 40:



&#x20;               numero = input(

&#x20;                   "Hay riesgo de alarma. Elija un numero del 1 al 3: "

&#x20;               )



&#x20;               while not numero.isdigit():

&#x20;                   print("Error. Debe ingresar un numero.")

&#x20;                   numero = input(

&#x20;                       "Hay riesgo de alarma. Elija un numero del 1 al 3: "

&#x20;                   )



&#x20;               numero = int(numero)



&#x20;               while numero < 1 or numero > 3:



&#x20;                   print("Error. El numero debe estar entre 1 y 3.")



&#x20;                   numero = input(

&#x20;                       "Hay riesgo de alarma. Elija un numero del 1 al 3: "

&#x20;                   )



&#x20;                   while not numero.isdigit():

&#x20;                       print("Error. Debe ingresar un numero.")

&#x20;                       numero = input(

&#x20;                           "Hay riesgo de alarma. Elija un numero del 1 al 3: "

&#x20;                       )



&#x20;                   numero = int(numero)



&#x20;               if numero == 3:



&#x20;                   alarma = True



&#x20;                   print()

&#x20;                   print("Elegiste el numero 3.")

&#x20;                   print("ALARMA ACTIVADA.")

&#x20;                   print("No se abrio la cerradura.")



&#x20;               else:



&#x20;                   if not alarma:

&#x20;                       cerraduras\_abiertas = cerraduras\_abiertas + 1

&#x20;                       print("Cerradura abierta.")



&#x20;           else:



&#x20;               if not alarma:

&#x20;                   cerraduras\_abiertas = cerraduras\_abiertas + 1

&#x20;                   print("Cerradura abierta.")





&#x20;   

&#x20;   # HACKEAR PANEL



&#x20;   elif opcion == 2:



&#x20;       # Cortamos la racha de forzar

&#x20;       forzar\_seguidas = 0



&#x20;       energia = energia - 10

&#x20;       tiempo = tiempo - 3



&#x20;       print()

&#x20;       print("Iniciando hackeo...")



&#x20;       # FOR de 4 pasos

&#x20;       for paso in range(4):



&#x20;           print("Paso", paso + 1, "de 4")



&#x20;           letra = input("Ingrese una letra: ")



&#x20;           while not letra.isalpha():

&#x20;               print("Error. Debe ingresar una letra.")

&#x20;               letra = input("Ingrese una letra: ")



&#x20;           codigo\_parcial = codigo\_parcial + letra



&#x20;           print("Codigo parcial:", codigo\_parcial)



&#x20;       # Si hay 8 caracteres o mas,

&#x20;       # se abre una cerradura

&#x20;       if len(codigo\_parcial) >= 8 and cerraduras\_abiertas < 3:



&#x20;           cerraduras\_abiertas = cerraduras\_abiertas + 1



&#x20;           print()

&#x20;           print("Hackeo exitoso.")

&#x20;           print("Se abrio una cerradura.")





&#x20;   #DESCANSAR



&#x20;   else:



&#x20;       # Cortamos la racha de forzar

&#x20;       forzar\_seguidas = 0



&#x20;       energia = energia + 15



&#x20;       # Maximo 100 de energia

&#x20;       if energia > 100:

&#x20;           energia = 100



&#x20;       tiempo = tiempo - 1



&#x20;       # Si la alarma esta activa,

&#x20;       # descansar cuesta 10 de energia extra

&#x20;       if alarma:

&#x20;           energia = energia - 10



&#x20;       print()

&#x20;       print("Descansaste.")

&#x20;       print("Energia:", energia)





\# CONDICIONES FINALES





print()

print("===================================")

print("           FIN DEL JUEGO")

print("===================================")



if cerraduras\_abiertas == 3:



&#x20;   print("VICTORIA.")

&#x20;   print("Abriste las 3 cerraduras.")



elif alarma and tiempo <= 3 and cerraduras\_abiertas < 3:



&#x20;   print("DERROTA.")

&#x20;   print("El sistema se bloqueo por la alarma.")



elif energia <= 0 or tiempo <= 0:



&#x20;   print("DERROTA.")

&#x20;   print("Te quedaste sin energia o sin tiempo.")









\# EJERCICIO 5 - LA ARENA DEL GLADIADOR



\# NOMBRE DEL GLADIADOR

\#solo puede contener letras



while True:

&#x20;   nombre = input("Nombre del Gladiador: ")



&#x20;   if nombre.isalpha():

&#x20;       break

&#x20;   else:

&#x20;       print("Error: Solo se permiten letras.")





\#VARIABLES INICIALES



vida\_jugador = 100

vida\_enemigo = 100

pociones = 3

daño\_ataque = 15

daño\_enemigo = 12

turno\_gladiador = True





print()

print("= INICIO DEL COMBATE =")



\# CICLO DE COMBATE

\#el juego se repite mientras ambos jugadores tengan mas de 0puntos de vida 

while vida\_jugador > 0 and vida\_enemigo > 0:



&#x20;   print()

&#x20;   print("--------------------------------")

&#x20;   print(f"{nombre} (HP: {vida\_jugador})")

&#x20;   print(f"Enemigo (HP: {vida\_enemigo})")

&#x20;   print(f"Pociones: {pociones}")

&#x20;   print("--------------------------------")



&#x20;   print("Elige una acción:")

&#x20;   print("1. Ataque Pesado")

&#x20;   print("2. Ráfaga Veloz")

&#x20;   print("3. Curar")



&#x20;   # VALIDACIÓN DE LA OPCIÓN

&#x20;   

&#x20;   while True:

&#x20;       opcion = input("Opción: ")

\#para verificar que sea numero lo ingresado 

&#x20;       if opcion.isdigit():

&#x20;           opcion = int(opcion)



&#x20;           if opcion == 1 or opcion == 2 or opcion == 3:

&#x20;               break

&#x20;           else: #si no ingresa un numero entre 1 a 3 le pido que ingrese numero valido 

&#x20;               print("Error: Ingrese 1, 2 o 3.")



&#x20;       else:

&#x20;           print("Error: Ingrese un número válido.")





&#x20;   # ATAQUE PESADO

&#x20;   

&#x20;   if opcion == 1:

\#si la vida del enemigo es menor a 20, se realiza un golpe critico y se multiplica el daño \*1.5

&#x20;       if vida\_enemigo < 20:

&#x20;           daño = daño\_ataque \* 1.5

&#x20;           print(f"¡Golpe crítico! Daño: {daño}")

&#x20;       else:

&#x20;           daño = daño\_ataque



&#x20;       vida\_enemigo = vida\_enemigo - daño



&#x20;       print(f"¡Atacaste al enemigo por {daño} puntos de daño!")





&#x20;   # RÁFAGA VELOZ

\#el bucle debe repetirse 3 veces usando range 

&#x20;   elif opcion == 2:



&#x20;       print("¡Inicias una ráfaga de golpes!")



&#x20;       for i in range(3):

\#por cada golpe restamos 5 puntos de vida 

&#x20;           vida\_enemigo = vida\_enemigo - 5



&#x20;           print("> Golpe conectado por 5 de daño")

\#para evitar que siga restando al llegar a 0 pongo un break si llego a 0 puntos cortamos el juego 

&#x20;           if vida\_enemigo <= 0:

&#x20;               break





&#x20;   # CURAR

\#las pociones suman 30 puntos 

&#x20;   elif opcion == 3:



&#x20;       if pociones > 0:



&#x20;           vida\_jugador = vida\_jugador + 30

&#x20;           pociones = pociones - 1



&#x20;           print("Recuperaste 30 puntos de vida.")



&#x20;       else:



&#x20;           print("¡No quedan pociones!")





&#x20;   # TURNO DEL ENEMIGO



&#x20;   if vida\_enemigo > 0:



&#x20;       vida\_jugador = vida\_jugador - daño\_enemigo



&#x20;       print()

&#x20;       print(

&#x20;           f"¡El enemigo te atacó por "

&#x20;           f"{daño\_enemigo} puntos de daño!"

&#x20;       )



\# FIN DEL JUEGO

\#termina cuando alguno de los dos llega a 0 puntos 

print()

print("=== FIN DEL COMBATE ===")



if vida\_jugador > 0:

&#x20;   print(f"¡VICTORIA! {nombre} ha ganado la batalla.")



elif vida\_jugador <= 0:

&#x20;   print("DERROTA. Has caído en combate.")



