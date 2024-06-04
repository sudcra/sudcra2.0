from eval_insert import inserta_eval , crea_df_item_respuesta, hace_conexion , cierra_conexion
from ruta_archivo import obtener_ruta_archivo
from xlsx_a_df import convertir_a_df_tipo_0 , convertir_a_df_tipo_1
from agrega_registros import agregar_registros

ruta = obtener_ruta_archivo()
respuesta=inserta_eval(ruta)

if respuesta[2] == 'Registro insertado correctamente':
    cod_asig = respuesta[0]
    prueba = respuesta[1]
    nombre_hoja="medidas"
    df = convertir_a_df_tipo_0(ruta, nombre_hoja)

    agregar_registros(df,nombre_hoja,[])

    nombre_hoja="escala"
    df = convertir_a_df_tipo_0(ruta, nombre_hoja)

    agregar_registros(df,nombre_hoja,[])


    nombre_hoja="calificaciones"
    df = convertir_a_df_tipo_0(ruta, nombre_hoja)

    agregar_registros(df,nombre_hoja,[])

    nombre_hoja="item"
    df = convertir_a_df_tipo_0(ruta, nombre_hoja)
    dfi = df.iloc[:, :-4]
    agregar_registros(dfi,nombre_hoja,[])

    nombre_hoja="item_medida"
    dfim = convertir_a_df_tipo_0(ruta, nombre_hoja)

    agregar_registros(dfim,nombre_hoja,[])

    nombre_hoja="item_respuesta"
    dfire=crea_df_item_respuesta(df, cod_asig, prueba)
    #print(dfire)
    agregar_registros(dfire,nombre_hoja,[])
else:
    print("La tabla ya fue cargada con anterioridad.")