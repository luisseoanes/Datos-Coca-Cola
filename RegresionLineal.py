import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def ENTRENAMIENTO(NUMDIAS, ADJCIERRE):
    # Dividir los datos en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
    X_train, X_test, y_train, y_test = train_test_split(NUMDIAS, ADJCIERRE, test_size=0.2, random_state=50)
    return X_train, X_test, y_train, y_test

def CREARENTRENAR(EntrenamientoX, EntrenamientoY):
    # Crear y entrenar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(EntrenamientoX, EntrenamientoY)
    return model

def PREDICCIONES(model, EntrenamientoX, PruebaX):
    # Predecir los precios de cierre ajustados para los datos de entrenamiento y prueba
    PredEntrenamientoY = model.predict(EntrenamientoX)
    PredPruebaY = model.predict(PruebaX)
    return PredEntrenamientoY, PredPruebaY

def CALCULOS(EntrenamientoY, PredEntrenamientoY, PruebaY, PredPruebaY):
    # Calcular el error cuadrático medio y el coeficiente de determinación (R^2)
    ECUADRATICOENTRE = round(mean_squared_error(EntrenamientoY, PredEntrenamientoY),3)
    ECUADRATICOPRUEBA = round(mean_squared_error(PruebaY, PredPruebaY),3)
    COEDETEENTRE = round(r2_score(EntrenamientoY, PredEntrenamientoY),3)
    COEDETERPRUEBA = round(r2_score(PruebaY, PredPruebaY),3)
    return ECUADRATICOPRUEBA, ECUADRATICOENTRE, COEDETERPRUEBA, COEDETEENTRE

def IMPRIMIR(EntrenamientoX, EntrenamientoY, PruebaX, PruebaY, PredEntrenamientoY):
    # Graficar los datos de entrenamiento y prueba junto con la regresión lineal
    plt.figure(figsize=(10, 6))
    plt.scatter(EntrenamientoX, EntrenamientoY, color='blue', label='Datos de Entrenamiento')
    plt.scatter(PruebaX, PruebaY, color='red', label='Datos de Prueba')
    plt.plot(EntrenamientoX, PredEntrenamientoY, color='green', linewidth=2, label='Regresión Lineal')
    plt.title('Regresión Lineal para Predecir el Precio de Cierre Ajustado de Coca-Cola')
    plt.xlabel('Día')
    plt.ylabel('Precio de Cierre Ajustado')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def OPCION():
    ErrorCprueba, ErrorCentre, CoeficienteDprueba, CoeficienteDentre = CALCULOS(EntrenamientoY,PredEntrenamientoY, PruebaY, PredPruebaY)
    print(f'Error cuadrático medio (Entrenamiento): {ErrorCentre}')
    print(f'Error cuadrático medio (Prueba): {ErrorCprueba}')
    print(f'Coeficiente de determinación (R^2) (Entrenamiento): {CoeficienteDentre}')
    print(f'Coeficiente de determinación (R^2) (Prueba): {CoeficienteDprueba}')
    IMPRIMIR(EntrenamientoX, EntrenamientoY, PruebaX, PruebaY, PredEntrenamientoY)


# Creamos listas, para luego reposarle los datos
ADJCIERRA = []

with open("WorldEconomic.csv") as Datos:
    # Limpieza y separacion de datos, con el .split y el .strip
    Datos.readline()
    for i in Datos:
        DatosSeparados = i.strip().split(",")
        # Agregamos, linea a linea, los datos a las listas
        ADJCIERRA.append(float(DatosSeparados[5]))

data = pd.DataFrame({
    'Adj Cierre': ADJCIERRA, 
    })

# Crear una característica para representar el día actual
data['Day'] = np.arange(len(data))
# Reformamos, para que sea una matriz bidimensional
X = data['Day'].values.reshape(-1, 1)

EntrenamientoX, PruebaX, EntrenamientoY, PruebaY = ENTRENAMIENTO(X, ADJCIERRA)
modelo = CREARENTRENAR(EntrenamientoX, EntrenamientoY)
PredEntrenamientoY, PredPruebaY = PREDICCIONES(modelo, EntrenamientoX, PruebaX)
