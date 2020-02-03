# Definición de la función tranformar_minusculas que recibe como argumento un dataframe, convierte a minúsculas la información contenida en cada una de las columnas y devuelve el dataframe con esta modificación.

def transformar_minusculas(df,columnas):
    return df.apply(lambda x: x.astype(str).str.lower() if x.name in columnas else x)


# Definición de la función eliminar_signos que recibe como argumento un dataframe con información en minúsculas y aplica las siguientes transformaciones:
# 1. Eliminación de acentos
# 2. Reemplazo de espacios por guiones bajo
# 3. Eliminación de comas, puntos, punto y coma, signos de mas
# 4. Transformación de los "nan" a "NaN"
# y devuelve un dataframe con todas estas modificaciones.


def eliminar_signos(df,columnas):
    return df.apply(lambda x: x.astype(str).str.replace('á','a').
                    str.replace('é','e').
                    str.replace('í','i').
                    str.replace('ó','o').
                    str.replace('ú','u').
                    str.replace(' ','_').
                    str.replace(',','').
                    str.replace('.','').
                    str.replace(';','').
                    str.replace('+','').
                    str.replace('nan','NaN') if x.name in columnas else x)



# Definición de la función estandarizar_datos que recibe como argumento un dataframe, utiliza las dos funciones anteriores para estandarizar (convertir a minúsculas, reemplazar espacios por guiones bajo y eliminar ciertos caracteres) la información de dicho dataframe y deveuelve un nuevo dataframe en formato estandar.

def estandarizar_datos(df):
    df_minusculas = transformar_minusculas(df,df.columns)
    df_estandar = eliminar_signos(df_minusculas,df_minusculas.columns)
    return df_estandar


# Definición de la función eliminar_variables que recibe como argumento una dataframe y una lista con el nombre de las columnas a eliminar; y devuelve el dataframe con las columnas reducidas

def eliminar_variables(df,lista_columnas):
    df_reducido =df.drop(lista_columnas, axis =1)
    return df_reducido


# Definición de la función convertir_variable que recibe como argumento un dataframe, la columna que quiere transfomarse y el tipo de variable al que desea transformarse; y devuelve un nuevo dataframe con las variables ya transformadas

def convertir_variable(df,columna,tipo_variable):
    df_convertido = df.astype({columna:tipo_variable})
    return df_convertido