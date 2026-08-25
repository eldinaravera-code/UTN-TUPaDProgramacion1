#ejercicio 1 
#pedir el nombre del cliente
nombre = input("cliente:")
while nombre =="" or not nombre.isalpha():
    print("Error: el nombre no puede estar vacío y debe contener solo letras.")
    nombre = input("cliente:")
#pedir la cantidad de productos
cantidad_productos = input("cantidad de productos:")
while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("Error: la cantidad de productos debe ser un número entero positivo.")
    cantidad_productos = input("cantidad de productos:")
cantidad = int(cantidad_productos)
#variables para acumular el total y el descuento
total_sin_descuento = 0
total_con_descuento = 0
#pedir datos de cada producto
for i in range(cantidad):
    precio = input(f"precio del producto {i+1}:")
    while not precio.isdigit():
        print("error: el precio debe ser un numero entero.")
        precio = input(f"precio del producto {i+1}:")
    precio = int(precio)
    descuento = input("descuento (s/n):")
    while descuento.lower() != "s" and descuento.lower() != "n":
        print("error: debe ingresar 's' para sí o 'n' para no.")
        descuento = input("descuento (s/n):")
    #acumular el precio original
    total_sin_descuento += precio
    #aplicar el descuento si corresponde 
    if descuento.lower() =="s":
        precio_con_descuento = precio * 0.9  # aplicar un 10% de descuento
    else:
        precio_con_descuento = precio
    #acumular el precio final 
    total_con_descuento += precio_con_descuento
#calcular ahorro 
ahorro =total_sin_descuento -total_con_descuento
#calcular promedio
promedio = float (total_con_descuento) / cantidad
#mostrar resultados 
print()
print("resumen de la compra")
print(f"cliente: {nombre}")
print(f"total sin descuento: ${total_sin_descuento}")
print(f"total con descuento: ${total_con_descuento:.2f}")
print(f"ahorro: ${ahorro:.2f}")
print(f"promedio por producto: ${promedio:.2f}")


#ejercicio 2 

#credenciales correctas
usuario_correcto = "alumno"
clave_correcta = "python123"

#cantidad de intentos 
intentos = 0
accesos = False

#login
while intentos < 3: 
    usuario = input(f"intento {intentos + 1}/3 - usuario:")
    clave = input("clave:")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("acceso concedido")
        accesos = True
        break
    else:
        print("usuario o clave incorrectos")
        intentos += 1
# si no pudo ingresar despues de 3 intentos 

if not accesos:
    print("cuenta bloqueada")
else: #volver al menu
    opcion = ""
    while opcion != "4":
        print()
        print("1) estado")
        print("2) cambiar de clave")
        print("3) mensaje")
        print("4) salir")
        opcion = input("opcion: ")

#validar que sea un numero 
while not opcion.isdigit():
    print("error:ingrese un numero valido.")
    opcion = input("opcion: ")
#convertir a numreo entero 
opcion =int(opcion)
#validar que este entre 1 y 4 
while opcion <1 or opcion >4:
    print("error: fuera de rango. ingrese un numero entre 1 y 4.")
    opcion =input("opcion: ")
    while not opcion.isdigit():
        print("error: ingrese un numero valido.")
        opcion = input("opcion: ")
    opcion = int (opcion)
#opcion 1 
if opcion == 1:
    print("estado: inscripto")
#opcion 2 
elif opcion == 2:
    nueva_clave = input("ingrese nueva clave:")
    while len(nueva_clave) < 6:
        print("error: la clave debe tener al menos 6 caracteres.")
        nueva_clave = input("ingrese nueva clave:")
    confirmacion = input("confirme nueva clave:")
    while nueva_clave != confirmacion:
        print("error: las claves no coinciden.")
        confirmacion = input("confirme nueva clave:")
    clave_correcta = nueva_clave
    print("clave cambiada con exito")
#opcion 3 
elif  opcion == 3:
    print("segui avanzando!")
#opcion 4 
elif opcion == 4:
    print("sesion finalizada.")

# no se porque no me ejecuta las opciones ya probe de varias maneras y no me funciona, me podrias ayudar a corregirlo ? gracias 





#ejercicio 3

# AGENDA DE TURNOS

# TURNOS DEL DIA LUNES
lunes_t1 = ""
lunes_t2 = ""
lunes_t3 = ""
lunes_t4 = ""

# TURNOS DEL DIA MARTES
martes_t1 = ""
martes_t2 = ""
martes_t3 = ""


# NOMBRE DEL OPERADOR
operador = input("Nombre del operador: ")

while operador == "" or not operador.isalpha():
    print("Error: el nombre del operador no puede estar vacio y debe contener solo letras.")
    operador = input("Ingrese el nombre del operador: ")

print(f"Bienvenido {operador}!")


# MENU PRINCIPAL
opcion = ""

while opcion != 5:

    print()
    print("========== MENU PRINCIPAL ==========")
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Seleccionar una opcion: ")

    # VALIDAR QUE SEA UN NUMERO
    while not opcion.isdigit():
        print("Error: ingrese un numero valido del 1 al 5.")
        opcion = input("Seleccionar una opcion: ")

    # PASAR DE TEXTO A NUMERO
    opcion = int(opcion)

    # VALIDAR QUE ESTE ENTRE 1 Y 5
    while opcion < 1 or opcion > 5:

        print("Error: ingrese un numero del 1 al 5.")

        opcion = input("Seleccionar una opcion: ")

        while not opcion.isdigit():
            print("Error: ingrese un numero valido del 1 al 5.")
            opcion = input("Seleccionar una opcion: ")

        opcion = int(opcion)


    # OPCION 1 RESERVAR TURNO

    if opcion == 1:

        # PEDIR DIA
        dia = input("Ingrese el dia para reservar (lunes/martes): ")

        while dia.lower() != "lunes" and dia.lower() != "martes":
            print("Error: ingrese un dia valido (lunes/martes).")
            dia = input("Ingrese el dia para reservar (lunes/martes): ")


        # PEDIR NOMBRE DEL PACIENTE
        paciente = input("Ingrese el nombre del paciente: ")

        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre del paciente no puede estar vacio y debe contener solo letras.")
            paciente = input("Ingrese el nombre del paciente: ")


        # VERIFICAR SI EL PACIENTE YA TIENE UN TURNO
        if (paciente.lower() == lunes_t1.lower() or
            paciente.lower() == lunes_t2.lower() or
            paciente.lower() == lunes_t3.lower() or
            paciente.lower() == lunes_t4.lower() or
            paciente.lower() == martes_t1.lower() or
            paciente.lower() == martes_t2.lower() or
            paciente.lower() == martes_t3.lower()):

            print("Error: el paciente ya tiene un turno reservado.")


        # RESERVAR LUNES
        elif dia.lower() == "lunes":

            if lunes_t1 == "":
                lunes_t1 = paciente
                print("Turno reservado correctamente.")

            elif lunes_t2 == "":
                lunes_t2 = paciente
                print("Turno reservado correctamente.")

            elif lunes_t3 == "":
                lunes_t3 = paciente
                print("Turno reservado correctamente.")

            elif lunes_t4 == "":
                lunes_t4 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el dia lunes.")


        # RESERVAR MARTES
        else:

            if martes_t1 == "":
                martes_t1 = paciente
                print("Turno reservado correctamente.")

            elif martes_t2 == "":
                martes_t2 = paciente
                print("Turno reservado correctamente.")

            elif martes_t3 == "":
                martes_t3 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el dia martes.")


    # OPCION 2: CANCELAR TURNO

    elif opcion == 2:

        # PEDIR DIA
        dia = input("Ingrese el dia del turno a cancelar (lunes/martes): ")

        while dia.lower() != "lunes" and dia.lower() != "martes":
            print("Error: ingrese un dia valido (lunes/martes).")
            dia = input("Ingrese el dia del turno a cancelar (lunes/martes): ")


        # PEDIR PACIENTE
        paciente = input("Ingrese el nombre del paciente: ")

        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre del paciente no puede estar vacio y debe contener solo letras.")
            paciente = input("Ingrese el nombre del paciente: ")


        # CANCELAR TURNO DEL LUNES
        if dia.lower() == "lunes":

            if paciente.lower() == lunes_t1.lower() and lunes_t1 != "":
                lunes_t1 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == lunes_t2.lower() and lunes_t2 != "":
                lunes_t2 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == lunes_t3.lower() and lunes_t3 != "":
                lunes_t3 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == lunes_t4.lower() and lunes_t4 != "":
                lunes_t4 = ""
                print("Turno cancelado correctamente.")

            else:
                print("Error: el paciente no tiene un turno reservado para el dia lunes.")


        # CANCELAR TURNO DEL MARTES
        else:

            if paciente.lower() == martes_t1.lower() and martes_t1 != "":
                martes_t1 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == martes_t2.lower() and martes_t2 != "":
                martes_t2 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == martes_t3.lower() and martes_t3 != "":
                martes_t3 = ""
                print("Turno cancelado correctamente.")

            else:
                print("Error: el paciente no tiene un turno reservado para el dia martes.")


    # OPCION 3: VER AGENDA DEL DIA

    elif opcion == 3:

        dia = input("Ingrese el dia para ver la agenda (lunes/martes): ")

        while dia.lower() != "lunes" and dia.lower() != "martes":
            print("Error: ingrese un dia valido (lunes/martes).")
            dia = input("Ingrese el dia para ver la agenda (lunes/martes): ")


        # AGENDA DEL LUNES
        if dia.lower() == "lunes":

            print()
            print("AGENDA DEL DIA LUNES")

            print(f"Turno 1: {lunes_t1 if lunes_t1 else 'disponible'}")
            print(f"Turno 2: {lunes_t2 if lunes_t2 else 'disponible'}")
            print(f"Turno 3: {lunes_t3 if lunes_t3 else 'disponible'}")
            print(f"Turno 4: {lunes_t4 if lunes_t4 else 'disponible'}")


        # AGENDA DEL MARTES
        else:

            print()
            print("AGENDA DEL DIA MARTES")

            print(f"Turno 1: {martes_t1 if martes_t1 else 'disponible'}")
            print(f"Turno 2: {martes_t2 if martes_t2 else 'disponible'}")
            print(f"Turno 3: {martes_t3 if martes_t3 else 'disponible'}")


    # OPCION 4: VER RESUMEN GENERAL

    elif opcion == 4:

        # CONTAR TURNOS OCUPADOS DEL LUNES
        turnos_ocupados_lunes = 0

        if lunes_t1 != "":
            turnos_ocupados_lunes += 1

        if lunes_t2 != "":
            turnos_ocupados_lunes += 1

        if lunes_t3 != "":
            turnos_ocupados_lunes += 1

        if lunes_t4 != "":
            turnos_ocupados_lunes += 1


        # CONTAR TURNOS OCUPADOS DEL MARTES
        turnos_ocupados_martes = 0

        if martes_t1 != "":
            turnos_ocupados_martes += 1

        if martes_t2 != "":
            turnos_ocupados_martes += 1

        if martes_t3 != "":
            turnos_ocupados_martes += 1


        # MOSTRAR RESUMEN
        print()
        print("RESUMEN GENERAL DE TURNOS")

        print("Lunes")
        print("Ocupados:", turnos_ocupados_lunes)
        print("Disponibles:", 4 - turnos_ocupados_lunes)

        print()

        print("Martes")
        print("Ocupados:", turnos_ocupados_martes)
        print("Disponibles:", 3 - turnos_ocupados_martes)


        # COMPARAR LOS DOS DIAS
        if turnos_ocupados_lunes > turnos_ocupados_martes:

            print("El dia lunes tiene mas turnos ocupados.")

        elif turnos_ocupados_martes > turnos_ocupados_lunes:

            print("El dia martes tiene mas turnos ocupados.")

        else:

            print("Ambos dias tienen la misma cantidad de turnos ocupados.")


    # OPCION 5: CERRAR SISTEMA

    elif opcion == 5:

        print()
        print("Sistema cerrado.")


print("Fin del programa.")

#ejercicio 4 

# ESCAPE ROOM: LA BOVEDA

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# Variable para controlar las veces seguidas que se fuerza
forzar_seguidas = 0


# PEDIR NOMBRE DEL AGENTE
nombre = input("Ingrese el nombre del agente: ")
#uso isalpha para que detecte que lo qeu se ingreso sean letras 

while not nombre.isalpha():
    print("Error. El nombre debe contener solamente letras.")
    nombre = input("Ingrese el nombre del agente: ")


print()
print("       ESCAPE ROOM: LA BOVEDA")
print("Agente:", nombre)


# JUEGO PRINCIPAL
#el juego continua solo si se dan todas las condiciones 
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # BLOQUEO POR ALARMA
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print()
        print("       SISTEMA BLOQUEADO")
        print("===================================")
        print("La alarma se activo y queda poco tiempo.")
        print("DERROTA.")
        break

    print()
    print("-----------------------------------")
    print("ESTADO ACTUAL")
    print("Energia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Codigo parcial:", codigo_parcial)
    print("-----------------------------------")

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Elija una opcion: ")

    # Validar que sea un numero
    while not opcion.isdigit():
        print("Error. Debe ingresar un numero.")
        opcion = input("Elija una opcion: ")

    opcion = int(opcion)

    # Validar que sea 1, 2 o 3
    while opcion < 1 or opcion > 3:
        print("Error. La opcion debe ser 1, 2 o 3.")

        opcion = input("Elija una opcion: ")

        while not opcion.isdigit():
            print("Error. Debe ingresar un numero del 1 al 3 .")
            opcion = input("Elija una opcion: ")

        opcion = int(opcion)


    # FORZAR CERRADURA

    if opcion == 1:

        forzar_seguidas = forzar_seguidas + 1

        # Costo normal
        energia = energia - 20
        tiempo = tiempo - 2

        # REGLA ANTI-SPAM
        if forzar_seguidas == 3:

            alarma = True

            print()
            print("La cerradura se trabo.")
            print("ALARMA ACTIVADA.")
            print("No se abrio la cerradura.")

        else:

            # Si hay riesgo de alarma
            if energia <= 40:

                numero = input(
                    "Hay riesgo de alarma. Elija un numero del 1 al 3: "
                )

                while not numero.isdigit():
                    print("Error. Debe ingresar un numero.")
                    numero = input(
                        "Hay riesgo de alarma. Elija un numero del 1 al 3: "
                    )

                numero = int(numero)

                while numero < 1 or numero > 3:

                    print("Error. El numero debe estar entre 1 y 3.")

                    numero = input(
                        "Hay riesgo de alarma. Elija un numero del 1 al 3: "
                    )

                    while not numero.isdigit():
                        print("Error. Debe ingresar un numero.")
                        numero = input(
                            "Hay riesgo de alarma. Elija un numero del 1 al 3: "
                        )

                    numero = int(numero)

                if numero == 3:

                    alarma = True

                    print()
                    print("Elegiste el numero 3.")
                    print("ALARMA ACTIVADA.")
                    print("No se abrio la cerradura.")

                else:

                    if not alarma:
                        cerraduras_abiertas = cerraduras_abiertas + 1
                        print("Cerradura abierta.")

            else:

                if not alarma:
                    cerraduras_abiertas = cerraduras_abiertas + 1
                    print("Cerradura abierta.")


    
    # HACKEAR PANEL

    elif opcion == 2:

        # Cortamos la racha de forzar
        forzar_seguidas = 0

        energia = energia - 10
        tiempo = tiempo - 3

        print()
        print("Iniciando hackeo...")

        # FOR de 4 pasos
        for paso in range(4):

            print("Paso", paso + 1, "de 4")

            letra = input("Ingrese una letra: ")

            while not letra.isalpha():
                print("Error. Debe ingresar una letra.")
                letra = input("Ingrese una letra: ")

            codigo_parcial = codigo_parcial + letra

            print("Codigo parcial:", codigo_parcial)

        # Si hay 8 caracteres o mas,
        # se abre una cerradura
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas = cerraduras_abiertas + 1

            print()
            print("Hackeo exitoso.")
            print("Se abrio una cerradura.")


    #DESCANSAR

    else:

        # Cortamos la racha de forzar
        forzar_seguidas = 0

        energia = energia + 15

        # Maximo 100 de energia
        if energia > 100:
            energia = 100

        tiempo = tiempo - 1

        # Si la alarma esta activa,
        # descansar cuesta 10 de energia extra
        if alarma:
            energia = energia - 10

        print()
        print("Descansaste.")
        print("Energia:", energia)


# CONDICIONES FINALES


print()
print("===================================")
print("           FIN DEL JUEGO")
print("===================================")

if cerraduras_abiertas == 3:

    print("VICTORIA.")
    print("Abriste las 3 cerraduras.")

elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:

    print("DERROTA.")
    print("El sistema se bloqueo por la alarma.")

elif energia <= 0 or tiempo <= 0:

    print("DERROTA.")
    print("Te quedaste sin energia o sin tiempo.")




# EJERCICIO 5 - LA ARENA DEL GLADIADOR

# NOMBRE DEL GLADIADOR
#solo puede contener letras

while True:
    nombre = input("Nombre del Gladiador: ")

    if nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras.")


#VARIABLES INICIALES

vida_jugador = 100
vida_enemigo = 100
pociones = 3
daño_ataque = 15
daño_enemigo = 12
turno_gladiador = True


print()
print("= INICIO DEL COMBATE =")

# CICLO DE COMBATE
#el juego se repite mientras ambos jugadores tengan mas de 0puntos de vida 
while vida_jugador > 0 and vida_enemigo > 0:

    print()
    print("--------------------------------")
    print(f"{nombre} (HP: {vida_jugador})")
    print(f"Enemigo (HP: {vida_enemigo})")
    print(f"Pociones: {pociones}")
    print("--------------------------------")

    print("Elige una acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # VALIDACIÓN DE LA OPCIÓN
    
    while True:
        opcion = input("Opción: ")
#para verificar que sea numero lo ingresado 
        if opcion.isdigit():
            opcion = int(opcion)

            if opcion == 1 or opcion == 2 or opcion == 3:
                break
            else: #si no ingresa un numero entre 1 a 3 le pido que ingrese numero valido 
                print("Error: Ingrese 1, 2 o 3.")

        else:
            print("Error: Ingrese un número válido.")


    # ATAQUE PESADO
    
    if opcion == 1:
#si la vida del enemigo es menor a 20, se realiza un golpe critico y se multiplica el daño *1.5
        if vida_enemigo < 20:
            daño = daño_ataque * 1.5
            print(f"¡Golpe crítico! Daño: {daño}")
        else:
            daño = daño_ataque

        vida_enemigo = vida_enemigo - daño

        print(f"¡Atacaste al enemigo por {daño} puntos de daño!")


    # RÁFAGA VELOZ
#el bucle debe repetirse 3 veces usando range 
    elif opcion == 2:

        print("¡Inicias una ráfaga de golpes!")

        for i in range(3):
#por cada golpe restamos 5 puntos de vida 
            vida_enemigo = vida_enemigo - 5

            print("> Golpe conectado por 5 de daño")
#para evitar que siga restando al llegar a 0 pongo un break si llego a 0 puntos cortamos el juego 
            if vida_enemigo <= 0:
                break


    # CURAR
#las pociones suman 30 puntos 
    elif opcion == 3:

        if pociones > 0:

            vida_jugador = vida_jugador + 30
            pociones = pociones - 1

            print("Recuperaste 30 puntos de vida.")

        else:

            print("¡No quedan pociones!")


    # TURNO DEL ENEMIGO

    if vida_enemigo > 0:

        vida_jugador = vida_jugador - daño_enemigo

        print()
        print(
            f"¡El enemigo te atacó por "
            f"{daño_enemigo} puntos de daño!"
        )

# FIN DEL JUEGO
#termina cuando alguno de los dos llega a 0 puntos 
print()
print("=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")

elif vida_jugador <= 0:
    print("DERROTA. Has caído en combate.")
