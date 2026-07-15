import validaciones3decimas as vld
def main():
    coleccion_de_temperaturas = []
    while True:
        vld.menu()
        opcion = vld.escoger()
        if opcion == 1:
            vld.agregar_temperatura(coleccion_de_temperaturas)
        elif opcion == 2:
            print("\n --- BUSCAR TEMPERATURA ---")
            dia = input("Ingrese el día de la semana a buscar: ")
            pos = vld.buscar_temp(coleccion_de_temperaturas, dia)
            if pos != -1:
                registro = coleccion_de_temperaturas[pos]
                estado_critico = "SÍ" if registro["critico"] else "NO"
                print(f"\n¡Registro encontrado!")
                print(f"Día: {registro['dia_de_la_semana'].capitalize()} (Mes: {registro['dia_del_mes']}) "
                    f"| Temp: {registro['temperatura']}°C | Crítico: {estado_critico}")
            else:
                print("Ese día no está registrado.")
        elif opcion == 3:
            vld.eliminar_temp(coleccion_de_temperaturas)
        elif opcion == 4:
            vld.actualiza_estado(coleccion_de_temperaturas)
        elif opcion == 5:
            vld.mostrar_temp(coleccion_de_temperaturas)
        elif opcion == 6:
            print("\n¡Gracias por usar el sistema! Saliendo del programa...")
            break
        else:
            print("\nOpción inválida. Por favor, selecciona un número del 1 al 6.")
if __name__=="__main__":
    main() 