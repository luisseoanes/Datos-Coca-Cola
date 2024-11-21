import TrabajoFinal as tf
import RegresionLineal as rl

def menu():
    # Escribimos el menu en una funcion para que sea mas facil y manejable llamarla
    print("Selecciona la función que deseas ejecutar:")
    print("1. Volatilidad")
    print("2. Cierre Ajustado")
    print("3. Gráfico de Barras")
    print("4. Cajas y Bigotes")
    print("5. Gráfico de Velas")
    print("6. Comparaciones")
    print("7. Dispersion")
    print("8. REGRESION LINEAL")
    print("9. Salir")

try:
    while True:
        #Llamos el menu y luego mandamos un input para que el usuario digite lo que desea imprimir 
        menu()
        opcion = int(input("Ingresa el número de la función que deseas ejecutar o '9' para salir: "))
        # De la opcion 1 a la 7 son las GRAFICAS , la 8 llama otro programa de REGRESION LINEAL y la 9 acaba el programa
        
        if opcion >= 1 and opcion <= 7:
            tf.Manda(opcion)
        elif opcion == 8:
            print("Los calculos de la regresion lineal son:")
            rl.OPCION()
        elif opcion == 9:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 9.")
        
except ValueError as ve:
    print("ERROR DE VALOR", ve)
except TypeError as te:
    print("ERROR DE TIPADO", te)
except Exception as general:
    print("ERROR GENERAL", general)
finally:
    print("Hasta el siguiente semestre")