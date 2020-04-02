import pandas as pd
from datetime import datetime
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
import numpy as np
from sklearn.externals import joblib


def predecirModelo(n):

    #Cargamos los modelos, tanto de temperatura, como de humedad
    mtemperatura= joblib.load('./modelo/temperatura.pkl')
    mhumedad= joblib.load('./modelo/humedad.pkl')
    
    #Predecimos, la temperatura y la humedad, con predit, pasandole el número de periodos (En este caso serán la horas)
    # y la variable return_conf_int a True.
    predTemperatura, confint = mtemperatura.predict(n_periods=n, return_conf_int=True)
    predHumedad, confint = mhumedad.predict(n_periods=n, return_conf_int=True)
    
    # Seleccionamos la fecha de hoy, y ponemos que la frecuencia sea por horas, y el numero de periodos sea el marcado.
    fechahoy = datetime.now()
    indice = pd.date_range(fechahoy, periods=n, freq='H')

    # Del DataFrame, sacamos las columnas temperatura y humedad
    salida= pd.DataFrame(index=indice, columns=['Temperatura','Humedad'])

    #Asignamos a temperatura y a humedad la preccion realizada.
    temperatura=np.array(predTemperatura)
    humedad=np.array(predHumedad)
    
    salida['Temperatura']=temperatura
    salida['Humedad']=humedad

    return salida


if __name__ == '__main__':
    salida = predecirModelo(24)
    print(salida)