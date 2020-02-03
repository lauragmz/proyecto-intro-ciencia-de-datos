# Definición de la función cargar_datos que permite:
# 1. Leer un archivo csv, separado por punto y coma
# 2. Guardarlo en un objeto de tipo dataframe (df)
# 3. Imprimir el número de observaciones y variables

import pandas as pd
def cargar_datos(archivo_csv):
    datos_df = pd.read_csv(archivo_csv, sep = ';')
    print('Número de observaciones: ',datos_df.shape[0])
    print('Número de variables: ',datos_df.shape[1])
    return datos_df

