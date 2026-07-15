def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar temperatura del día")
    print("2. Buscar termperatura")
    print("3. Eliminar temperatura del día")
    print("4. Actualizar estados")
    print("5. Mostrar todas las temperaturas")
    print("6. Salir")
    print("=====================================")
def escoger():
    try:
        opcion = int(input("Ingrese la opción que desea realizar (1-6): "))
        return opcion
    except ValueError:
        return -1
def validar_dia_semana(dia):
    return len(dia.strip()) > 0
def validar_numero_dia(numero_dia):
    try:
        numero_dia = int(numero_dia)
        return numero_dia >= 1 and numero_dia <= 30
    except ValueError:
        return False
def validar_temp(temp):
    try:
        temp = float(temp)
        return temp >= -20.0 and temp <= 100.0
    except ValueError:
        return False
def agregar_temperatura(lista_temp):
    print("\n --- AGREGAR TEMPERATURA ---")
    semana = input("Ingrese el día de la semana (lunes a domingo): ")
    if not validar_dia_semana(semana):
        print("Ingresa un día correcto")
        return  
    numero_dia = input("Ingrese número del mes (1-30): ")
    if not validar_numero_dia(numero_dia):
        print("Ingresa un número dentro del rango (1-30)")
        return
    tempe = input("Ingresa la temperatura (-20.0 - 100.0): ")
    if not validar_temp(tempe):
        print("Ingresa una temperatura dentro del rango")
        return
    agregar_temp ={
        "dia_de_la_semana":semana.strip(),
        "dia_del_mes":int(numero_dia),
        "temperatura":float(tempe),
        "critico":False
    }
    lista_temp.append(agregar_temp)
    print("Temperatura registrada satisfactoriamente")
def buscar_temp(lista_temp,buscar):
    for i in range(len(lista_temp)):
        if lista_temp[i]["dia_de_la_semana"].lower().strip() == buscar.strip().lower():
            return i
    return -1
def eliminar_temp(lista_temp):
    eliminar = input("Ingresa el día a eliminar: ")
    pos = buscar_temp(lista_temp,eliminar)
    if pos != -1:
        eliminado = lista_temp.pop(pos)
        print(f"El registro del día '{eliminado['dia_de_la_semana']}' ha sido eliminado con éxito")
    else:
        print(f"No se encontró ningún registro para el día {eliminar}")
def actualiza_estado(lista_temp):
    print("\n --- ACTUALIZAR ESTADOS CRITICOS ---")
    if len(lista_temp) == 0:
        print("No hay temperaturas registradas para actualizar.")
        return
    for registro in lista_temp:
        if registro["temperatura"] < 15.0:
            registro["critico"] = True
        else:
            registro["critico"] = False
    print("Estados de criticidad actualizados correctamente.")
def mostrar_temp(lista_temp):
    print("\n --- LISTADO GENERAL DE TEMPERATURAS ---")
    if len(lista_temp) == 0:
        print("La lista está vacía. No hay datos registrados.")
        return
        
    for registro in lista_temp:
        estado_critico = "SÍ" if registro["critico"] else "NO"
        print(f"Día: {registro['dia_de_la_semana'].capitalize()} (Mes: {registro['dia_del_mes']}) "
              f"| Temp: {registro['temperatura']}°C | Crítico: {estado_critico}")