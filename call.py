import requests
import pandas as pd
from datetime import datetime

#Funcion para realizar la llamada, para obtener los datos.

def callMedianteJson(horas):
    horas=int(horas/3) #Lo dividimos en 3 epocas o periodos (24, 48, y 72)

    #Obtenemos los datos almacenandolo en un json.
    json= r = requests.get(url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?lat=35&lon=139&appid=b6907d289e10d714a6e88b30761fae22")
    datos = json.json() 

    #Normalizamos los datos de json, ya que empieza por la palabra "list"
    dataframe = pd.io.json.json_normalize(datos['list'])

    fechahoy = datetime.now() #Seleccionamos como referencia la fecha de hoy

    #Actualizamos el indice, con la fecha de hoy, el numero de periodos que son las horas, y la frecuencia, por horas.
    indice = pd.date_range(fechahoy, periods=horas, freq='H')

    #Seleccionamos las columnas que vamos a mostrar del DataFrame
    salida= pd.DataFrame(index=indice, columns=['Temperatura',"Temperatura Min","Temperatura Max",'Humedad'])

    #Mostramos la temperatura, la humedad, y tambien como dato opcional la temperatura max y min
    salida['Temperatura']=dataframe['main.temp'].head(horas).values
    salida['Temperatura Min']=dataframe['main.temp_min'].head(horas).values
    salida['Temperatura Max']=dataframe['main.temp_max'].head(horas).values
    salida['Humedad']=dataframe['main.humidity'].head(horas).values    

    return salida