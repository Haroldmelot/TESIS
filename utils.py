# import csv  ## importo bibloteca de python para trabajar con archivos CSV
# import pandas as pd
# def read_csv_file(file_path)  ## funcion para leer datos de CSV y devolverlos como  lista
#     data_list = [] ## crear una lista vacia llamada data_list
#     try:  ## "funcion para menjar excepciones en caso de algun error en el codigo"
#         with open(file_path, 'r', newline='') as csvfile: ##abrir archivo CSV en modo lectura (r)
#             csv_reader = csv.reader(csvfile)   ## funccion para leer el contenido del archivo CSV linea por linea
#             for row in csv_reader:  ## recorre cada fila y columna del archivo en CSV
#                 data_list.append(row) ## almacenar todo los datos a una lista
#         return data_list     ## funcion que retorna el resultado
#     except FileNotFoundError:   ## si el archivo especificado no se encuntra se muestra mensaje
#         print(f"The file '{file_path}' was not found.")
#         return []
#     except Exception as e:
#         print(f"There was an error while reading the CSV file: {e}")
#         return []

# # Ruta del archivo CSV que deseas leer
# csv_file_path = "ruta/al/archivo.csv"  # Reemplaza esto con la ruta de tu archivo CSV

# # Leer el archivo CSV
# data = read_csv_file(csv_file_path)

# # Mostrar los datos recuperados
# if data:
#     for row in data:
#         print(row)
# else:
#     print("No data found or there was an issue reading the CSV file.")


# def get_data(nombre_archivo_input, nombre_hoja_input):
#     df = pd.read_excel(nombre_archivo_input, sheet_name=nombre_hoja_input)
#     return df


# def store_data(df, nombre_archivo_output, nombre_hoja_output):
#     df.to_excel(nombre_archivo_output, index=False,
#                 sheet_name=nombre_hoja_output)

# from utils import get_data, store_data

# df = get_data("Prueba.xlsx", "Hoja2")
# x = 1+1
# df.loc[0, 'Edad'] = x
# # Aqui procesas el df
# store_data(df, "Prueba Output 2.xlsx", "Principal 2")
# print(df.head())

# df = get_data("Prueba.xlsx", "Hoja2")
# store_data(df, "Prueba Output 2.xlsx", "Principal 2")
