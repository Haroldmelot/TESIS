# from Leer_imprimir_datos import get_data, store_data
import pandas as pd


def get_data(nombre_archivo_input, nombre_hoja_input):
    df = pd.read_excel(nombre_archivo_input, sheet_name=nombre_hoja_input)
    return df


def store_data(df, nombre_archivo_output, nombre_hoja_output):
    df.to_excel(nombre_archivo_output, index=False,
                sheet_name=nombre_hoja_output)


df2 = get_data("Prueba.xlsx", "Hoja2")

# x = 1+1
# df.loc[0, 'Edad'] = x


# Aqui procesas el df
store_data(df2, "Prueba Output 2.xlsx", "Principal 2")
print(df2.head())
