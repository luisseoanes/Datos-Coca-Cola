import pandas as pd
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objs as go 
import seaborn as sns

def VOLATILIDAD(TIEMPO, ADJCIERRE):
    try:
        # Calcular los retornos diarios
        daily_returns = ADJCIERRE.pct_change()
        # Calcular la volatilidad utilizando la desviación estándar de los retornos diarios
        volatility = daily_returns.rolling(100, min_periods=1).std() 
        # Graficar la volatilidad histórica
        plt.figure(figsize=(10, 5))
        plt.plot(TIEMPO, volatility, color='orange')
        plt.title('Volatilidad Histórica de Coca-Cola')
        plt.xlabel('Fecha')
        plt.ylabel('Volatilidad')
        plt.grid(True)
        plt.show()
    except ValueError as ve:
        print("ERROR DE VALOR", ve)
    except Exception as general:
        print("ERROR GENERAL", general)

def CierreAjustado(TIEMPO, ADJCIERRA):
    try:
        # Gráfica de líneas del precio de cierre ajustado (Adj Cierre)
        plt.figure(figsize=(10, 5))
        plt.plot(TIEMPO, ADJCIERRA, color='blue')
        plt.title('Evolución del Precio de Cierre Ajustado de Coca-Cola')
        plt.xlabel('Fecha')
        plt.ylabel('Precio de Cierre Ajustado')
        plt.grid(True)
        plt.show()
    except ValueError as ve:
        print("ERROR DE VALOR", ve)
    except Exception as general:
        print("ERROR GENERAL", general)

def Barras(TIEMPO, VOLUMEN, CIERRE):
    try:
        # Gráfica de barras del volumen de negociación con una línea superpuesta del precio de cierre
        plt.figure(figsize=(10, 5))
        plt.bar(TIEMPO, VOLUMEN, color='gray')
        plt.plot(TIEMPO, CIERRE, color='red', linewidth=2, linestyle='--', label='Precio de Cierre')
        plt.title('Volumen de Negociación y Precio de Cierre de Coca-Cola')
        plt.xlabel('Fecha')
        plt.ylabel('Volumen / Precio de Cierre')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError as ve:
        print("ERROR DE VALOR", ve)
    except Exception as general:
        print("ERROR GENERAL", general)

def CAJASBIGOTES(TIEMPO, ADJCIERRE):
    try:

        # Organizamos el tiempo en meses y no en dias
        data['Mes'] = TIEMPO.dt.to_period('M')
        # Graficamos las cajas y bigotes con el comando "Boxplot" que es la traduccion, y con las variables
        plt.figure(figsize=(12, 6))
        sns.boxplot(x=data['Mes'], y=ADJCIERRE, data=data)
        plt.title('Distribución del Precio de Cierre Ajustado por Mes')
        plt.xlabel('Mes')
        plt.ylabel('Precio de Cierre Ajustado')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

    except ValueError as ve:
        print("ERROR DE VALOR", ve)
    except Exception as general:
        print("ERROR GENERAL", general)

def GRAFVELAS(TIEMPO, APERTURA, ALTAS, BAJAS, CIERRE, VOLUMEN):
    try:

        # Graficamos las velas japonesas de las graficas (Las subidas y bajadas)
        trace = go.Candlestick(x=TIEMPO,
                            open=APERTURA,
                            high=ALTAS,
                            low=BAJAS,
                            close=CIERRE,
                            name='Coca-Cola')
        
        # Graficamos el volumen para poder relacionar como afecta a las velas japonesas
        volume = go.Bar(x=TIEMPO,
                        y=VOLUMEN,
                        yaxis='y2',
                        marker=dict(color='gray'),
                        name='Volumen')
        
        # Graficamos la informacion RELEVANTE, como titulos, ejes y aja
        layout = go.Layout(title='Gráfico de Velas con Volumen de Coca-Cola',
                        yaxis=dict(title='Precio'),
                        yaxis2=dict(title='Volumen', overlaying='y', side='right'),
                        xaxis=dict(title='Fecha'))

        fig = go.Figure(data=[trace, volume], layout=layout)
        fig.show()
    except ValueError as ve:
        print("ERROR DE VALOR", ve)
    except Exception as general:
        print("ERROR GENERAL", general)

def COMPARACIONES(TIEMPO, ADJCIERRE):
    try:
        # Calculando promedios móviles de 20, 50 y 200 días
        data['MA20'] = ADJCIERRE.rolling(window=20).mean()
        data['MA50'] = ADJCIERRE.rolling(window=50).mean()
        data['MA200'] = ADJCIERRE.rolling(window=200).mean()

        # Gráfica de líneas comparativa del precio de cierre y el promedio móvil
        plt.figure(figsize=(10, 5))
        plt.plot(TIEMPO, ADJCIERRE, label='Precio de Cierre', color='blue')
        plt.plot(TIEMPO, data['MA20'], label='MA20', linestyle='--', color='orange')
        plt.plot(TIEMPO, data['MA50'], label='MA50', linestyle='--', color='green')
        plt.plot(TIEMPO, data['MA200'], label='MA200', linestyle='--', color='red')
        plt.title('Comparación del Precio de Cierre con Promedios Móviles de Coca-Cola')
        plt.xlabel('Fecha')
        plt.ylabel('Precio')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError as ve:
        print("ERROR DE VALOR", ve)
    except Exception as general:
        print("ERROR GENERAL", general)

def DISPERSION(ADJCIERRE, VOLUMEN):
    try:
            
        # Gráfica de dispersión del retorno diario vs. volumen
        data['Daily Return'] = ADJCIERRE.pct_change()
        plt.figure(figsize=(10, 5))
        plt.scatter(data['Daily Return'], VOLUMEN, color='purple')
        plt.title('Retorno Diario vs. Volumen de Coca-Cola')
        plt.xlabel('Retorno Diario')
        plt.ylabel('Volumen')
        plt.grid(True)
        plt.show()
    except ValueError as ve:
        print("ERROR DE VALOR", ve)
    except Exception as general:
        print("ERROR GENERAL", general)

def Manda(opcion):
    # Las opciones que se llaman de la interfaz, las hacemos llamar a las graficas
    if opcion == 1:
        VOLATILIDAD(TIEMPO, data['Adj Cierre'])
    elif opcion == 2:
        CierreAjustado(TIEMPO, ADJCIERRA)
    elif opcion == 3:
        Barras(TIEMPO, VOLUMEN, CIERRE)
    elif opcion == 4:
        CAJASBIGOTES(data["Tiempo"], ADJCIERRA)
    elif opcion == 5:
        GRAFVELAS(TIEMPO, APERTURA, ALTAS, BAJAS, CIERRE, VOLUMEN)
    elif opcion == 6:
        COMPARACIONES(TIEMPO,data['Adj Cierre'])
    elif opcion == 7:
        DISPERSION(data['Adj Cierre'], VOLUMEN)

try: 
    # Creamos listas, para luego reposarle los datos
    TIEMPO = []
    APERTURA = []
    ALTAS = []
    BAJAS = []
    CIERRE = []
    ADJCIERRA = []
    VOLUMEN = []

    with open("WorldEconomic.csv") as Datos:
        # Limpieza y separacion de datos, con el .split y el .strip
        Datos.readline()
        for i in Datos:
            DatosSeparados = i.strip().split(",")
            # Agregamos, linea a linea, los datos a las listas
            TIEMPO.append(DatosSeparados[0])
            APERTURA.append(float(DatosSeparados[1]))
            ALTAS.append(float(DatosSeparados[2]))
            BAJAS.append(float(DatosSeparados[3]))
            CIERRE.append(float(DatosSeparados[4]))
            ADJCIERRA.append(float(DatosSeparados[5]))
            VOLUMEN.append(int(DatosSeparados[6]))
    # Pasamos El tiempo, a una forma leible para el computador
    TIEMPO = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in TIEMPO]
    # Creamos un DATAFRAME en PD, o lo similar una matriz
    data = pd.DataFrame({
        'Adj Cierre': ADJCIERRA, 
        'Cierre': CIERRE,
        'Bajas': BAJAS,
        'Altas': ALTAS,
        'Tiempo': TIEMPO
        })
    
except ValueError as ve:
    print("ERROR DE VALOR", ve)
except TypeError as te:
    print("ERROR DE TIPADO", te)
except Exception as general:
    print("ERROR GENERAL", general)