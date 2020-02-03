# Definición de la función limpiar_columna que realiza las siguientes transformaciones al nombre de una columna:
# 1. Convertir a minúsculas
# 2. Reemplazar espacios por guiones bajo
# 3. Eliminar puntos
# 4. Eliminar acentos
# 5. Eliminar comas

def limpiar_columna(nombre_columna):
    return nombre_columna.lower()\
           .replace(' ','_')\
           .replace('.','')\
           .replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')\
           .replace(',','')


# Definición de la función limpiar_encabezado que aplica la función anterior para "limpiar" los nombres de todas las columnas que conforman al dataframe y devuelve un arreglo con los nombres limpios de las columnas

def limpiar_encabezado (df):
    columnas_limpias = []
    for i in range(0,len(df.columns)):
        nombre_columna_limpia = limpiar_columna(df.columns[i])
        columnas_limpias.append(nombre_columna_limpia)  
    return columnas_limpias


# Definición de la función reemplazar_columnas que reemplaza los nombres originales de las de una dataframe, por los nombres en formato limpio o estandar y devuelve el dataframe con los nombres de columnas en formato estandar

def reemplazar_columnas(df,columnas_limpias):
    for i in range(0,len(df.columns)):
        df.rename(columns =  {df.columns[i]: columnas_limpias[i]}, inplace = True)
    return df


# Definición de la función estandarizar_columnas que utiliza las funciones anteriores para estandarizar (tranformar a minúsculas, eliminar acentos, reemplazar espacios y eliminar ciertos caracteres) los nombres de las columnas de un dataframe y devolver un dataframe con los nombres de columna ya transformados

def estandarizar_columnas(df):
    columnas_limpias = limpiar_encabezado(df)
    df_columnas_limpias = reemplazar_columnas(df,columnas_limpias)
    
    return df_columnas_limpias