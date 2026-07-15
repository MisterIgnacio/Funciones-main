# 🌡️ Sistema de Registro y Control de Temperaturas

Un sistema interactivo en consola desarrollado en **Python** para gestionar y analizar temperaturas diarias a lo largo de un mes. El proyecto destaca por su **diseño modular**, separando las validaciones y operaciones lógicas del flujo de ejecución principal.

---

## 📂 Estructura del Proyecto

El código está organizado en dos archivos independientes que se comunican entre sí:

| Archivo | Propósito | Funciones Clave |
| :--- | :--- | :--- |
| **`validaciones3decimas.py`** | Motor lógico y validaciones del sistema. | `agregar_temperatura()`, `buscar_temp()`, `eliminar_temp()`, `actualiza_estado()`, `mostrar_temp()`, `validar_temp()`. |
| **`main.py`** | Punto de entrada y control del flujo. | `main()`, inicialización de la lista de datos, gestión del menú interactivo. |

> ⚠️ **Importante**: Ambos archivos deben estar guardados en la **misma carpeta** para que el sistema funcione correctamente.

---

## 🚀 Características y Flujo del Programa

El sistema ofrece un menú interactivo con las siguientes opciones:

1. **Agregar temperatura**: Permite ingresar un día (lunes a domingo), el número de día del mes (1-30) y la temperatura (-20°C a 100°C).
2. **Buscar temperatura**: Localiza de manera rápida cualquier registro por el nombre del día.
3. **Eliminar temperatura**: Remueve registros de la lista de forma segura.
4. **Actualizar estados críticos**: Analiza automáticamente las temperaturas registradas. Si la temperatura es **menor a 15.0°C**, el sistema marcará el día en estado **Crítico (SÍ)**.
5. **Mostrar temperaturas**: Imprime un reporte limpio y ordenado de todos los datos ingresados.
6. **Salir**: Cierra el programa de manera ordenada.

---

## 🛡️ Robustez y Prevención de Errores

El programa ha sido diseñado para ser **a prueba de fallas comunes**:

* **Entradas de menú seguras**: Si el usuario digita letras o caracteres especiales en el menú, el sistema lo maneja mediante un bloque `try-except` sin detener la ejecución.
* **Búsqueda inteligente**: Las búsquedas de texto ignoran espacios accidentales y no distinguen entre mayúsculas o minúsculas (por ejemplo, buscar `" lUnEs "` coincidirá con `"Lunes"`).
* **Validación de rangos**: No se permiten temperaturas fuera del rango de `-20.0` a `100.0`, ni días del mes fuera de `1` a `30`.

---

## 💻 Instrucciones de Ejecución

Para iniciar el sistema, abre tu terminal en el directorio del proyecto y ejecuta el archivo principal:

```bash
python main.py
