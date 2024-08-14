import streamlit as st

def main():
    st.title("Calculator App")

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Resumen del Activo", "Tipo de Reforma", "Resumen Activo", "P&L de la Operación"])

    if selection == "Resumen del Activo":
        display_resumen_del_activo()
    elif selection == "Tipo de Reforma":
        display_tipo_de_reforma()
    elif selection == "Resumen Activo":
        display_resumen_activo()
    elif selection == "P&L de la Operación":
        display_pl_operacion()

def display_resumen_del_activo():
    st.header("Resumen del Activo")
    
    direccion = st.text_input("Dirección")
    ref_cat = st.text_input("Ref Cat")
    barrio = st.text_input("Barrio")
    sqm_construido = st.number_input("sqm Construido medido", min_value=0)
    sqm_util = st.number_input("sqm Útil medido", min_value=0)
    sqm_catastro = st.number_input("Sqm Catastro", min_value=0)
    ea_habitaciones = st.number_input("EA Habitaciones", min_value=0)
    ea_banos = st.number_input("EA Baños", min_value=0)
    distribucion_actual = ea_habitaciones + ea_banos
    er_habitaciones = st.number_input("ER Habitaciones", min_value=0)
    er_banos = st.number_input("ER Baños", min_value=0)
    distribucion_futura = er_habitaciones + er_banos
    ascensor = st.selectbox("Ascensor", [0, 1, "na"])
    garaje_trastero = st.selectbox("Garaje / trastero", [0, 1, "na"])
    aacc = st.selectbox("AACC", [0, 1, "na"])
    orientacion = st.selectbox("Orientación", ["na", "N", "S", "E", "W"])
    terraza_balcon = st.selectbox("Terraza / Balcon", [0, 1, "na"])
    jardin = st.selectbox("Jardín", [0, 1, "na"])
    tipo_patio = st.selectbox("Tipo de patio", ["na", "pequeño", "medio", "grande"])
    portero_fisico = st.selectbox("Portero físico", [0, 1, "na"])
    planta = st.selectbox("Planta", ["Bajo", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

    st.subheader("Resumen del Activo Data")
    st.write(f"Dirección: {direccion}")
    st.write(f"Ref Cat: {ref_cat}")
    st.write(f"Barrio: {barrio}")
    st.write(f"sqm Construido medido: {sqm_construido}")
    st.write(f"sqm Útil medido: {sqm_util}")
    st.write(f"Sqm Catastro: {sqm_catastro}")
    st.write(f"EA Habitaciones: {ea_habitaciones}")
    st.write(f"EA Baños: {ea_banos}")
    st.write(f"Distribución Actual: {distribucion_actual}")
    st.write(f"ER Habitaciones: {er_habitaciones}")
    st.write(f"ER Baños: {er_banos}")
    st.write(f"Distribución Futura: {distribucion_futura}")
    st.write(f"Ascensor: {ascensor}")
    st.write(f"Garaje / Trastero: {garaje_trastero}")
    st.write(f"AACC: {aacc}")
    st.write(f"Orientación: {orientacion}")
    st.write(f"Terraza / Balcon: {terraza_balcon}")
    st.write(f"Jardín: {jardin}")
    st.write(f"Tipo de Patio: {tipo_patio}")
    st.write(f"Portero Físico: {portero_fisico}")
    st.write(f"Planta: {planta}")

def display_tipo_de_reforma():
    st.header("Tipo de Reforma")

    tipo_reforma = st.selectbox("Tipo de Reforma", ["Humilde", "Normal", "Premium"])
    nivel_reforma = st.selectbox("Nivel de Reforma", ["Full", "Parcial", "Sin Reforma"])
    pluses_calidad = st.text_input("Pluses de Calidad (Letra)")
    calidades_banos = st.radio("Calidades Baños", ["Yes", "No"])
    calidades_cocina = st.radio("Calidades Cocina", ["Yes", "No"])
    calidades_otros = st.radio("Calidades Otros", ["Yes", "No"])
    tipo_venta = st.selectbox("Tipo de Venta", ["Reformado", "Pase"])

    st.subheader("Tipo de Reforma Data")
    st.write(f"Tipo de Reforma: {tipo_reforma}")
    st.write(f"Nivel de Reforma: {nivel_reforma}")
    st.write(f"Pluses de Calidad: {pluses_calidad}")
    st.write(f"Calidades Baños: {calidades_banos}")
    st.write(f"Calidades Cocina: {calidades_cocina}")
    st.write(f"Calidades Otros: {calidades_otros}")
    st.write(f"Tipo de Venta: {tipo_venta}")

def display_resumen_activo():
    st.header("Resumen Activo")
    
    aire_split = st.number_input("Aire acondicionado (split)", min_value=0)
    aire_conductos = st.number_input("Aire acondicionado (conductos)", min_value=0)
    total_aire = aire_split * 1800 + aire_conductos * 3500

    tipo_calefaccion = st.text_input("Tipo de calefacción")
    calefaccion_num = st.number_input("Número de sistemas de calefacción", min_value=0)
    acs = st.number_input("ACS", min_value=0)
    total_acs_calefaccion = calefaccion_num * 1800 + acs * 3000

    accion = st.number_input("Acción (Terraza)", min_value=0)
    total_terraza = accion * 60

    ventana_s = st.number_input("Ventana S", min_value=0)
    ventana_m = st.number_input("Ventana M", min_value=0)
    ventana_l = st.number_input("Ventana L", min_value=0)
    ventana_xl = st.number_input("Ventana XL", min_value=0)
    ventana_paso = st.number_input("Ventana de Paso", min_value=0)
    cerramientos = st.number_input("Cerramientos", min_value=0)
    total_carpitnaria = (ventana_s * 600 + ventana_m * 750 + ventana_l * 1000 +
                         ventana_xl * 1800 + ventana_paso * 2500 + cerramientos * 3000)

    armario_s = st.number_input("Armario S", min_value=0)
    armario_m = st.number_input("Armario M", min_value=0)
    armario_l = st.number_input("Armario L", min_value=0)
    empotrados = st.number_input("Empotrados", min_value=0)
    total_armarios = (armario_s * 1300 + armario_m * 1600 + armario_l * 1900 + empotrados * 2100)

    baño_s = st.number_input("Baño S", min_value=0)
    baño_m = st.number_input("Baño M", min_value=0)
    baño_l = st.number_input("Baño L", min_value=0)
    total_baños = baño_s * 3000 + baño_m * 3500 + baño_l * 3800

    habitacion_s = st.number_input("Habitacion S", min_value=0)
    habitacion_m = st.number_input("Habitacion M", min_value=0)
    habitacion_l = st.number_input("Habitacion L", min_value=0)
    total_habitaciones = habitacion_s * 2800 + habitacion_m * 3100 + habitacion_l * 4900

    facil = st.number_input("Facil", min_value=0)
    compleja = st.number_input("Compleja", min_value=0)
    limpieza = st.number_input("Limpieza", min_value=0)
    total_demolicion_limpieza = facil * 20 + compleja * 28 + limpieza * 6

    cocina_s = st.number_input("Cocina S", min_value=0)
    cocina_m = st.number_input("Cocina M", min_value=0)
    cocina_l = st.number_input("Cocina L", min_value=0)
    total_cocina = cocina_s * 5000 + cocina_m * 7000 + cocina_l * 12000

    tabiqueria = st.number_input("Tabiqueria", min_value=0)
    falsos_techos = st.number_input("Falsos techos", min_value=0)
    cambio_suelos = st.number_input("Cambio de suelos", min_value=0)
    lijado_suelos = st.number_input("Lijado y adecuación suelos", min_value=0)
    pintura_alisado = st.number_input("Pintura + Alisado", min_value=0)
    pintura_solo = st.number_input("Pintura solo", min_value=0)
    puerta_paso = st.number_input("Puerta Paso", min_value=0)
    puerta_acceso = st.number_input("Puerta Acceso", min_value=0)
    iluminacion = st.number_input("Iluminción y electricidad", min_value=0)
    contenedores = st.number_input("Contenedores", min_value=0)
    total_albanileria = (tabiqueria * 30 + falsos_techos * 28 + cambio_suelos * 38 +
                         lijado_suelos * 24 + pintura_alisado * 33 + pintura_solo * 23 +
                         puerta_paso * 1100 + puerta_acceso * 1500 + iluminacion * 40 + 
                         contenedores * 1000)

    total_gasto = (total_aire + total_acs_calefaccion + total_terraza + total_carpitnaria +
                  total_armarios + total_baños + total_habitaciones + total_demolicion_limpieza +
                  total_cocina + total_albanileria)

    iva = total_gasto * 0.21
    total_con_iva = total_gasto + iva

    sqm_construido = st.number_input("sqm Construido medido", min_value=1)
    costo_por_sqm = total_con_iva / sqm_construido

    st.write(f"Total Gasto (sin IVA): {total_gasto} €")
    st.write(f"IVA (21%): {iva} €")
    st.write(f"Total Gasto (con IVA): {total_con_iva} €")
    st.write(f"Costo por sqm Construido Medido: {costo_por_sqm} €/sqm")

def display_pl_operacion():
    st.header("P&L de la Operación")
    
    # Diccionario de precios por metro cuadrado por municipio
    precios_medios_municipios = {
        "Madrid Capital": 5353,
        "Fuenlabrada": 2110,
        "Alcalá de Henares": 2225,
        "Parla": 1767,
        "Móstoles": 2263,
        "Getafe": 2577,
        "Torrejón de Ardoz": 2178,
        "Valdemoro": 2190,
        "Leganés": 2469,
        "Alcorcón": 2457,
        "Las Rozas de Madrid": 3681,
        "Pinto": 2352,
        "Aranjuez": 1883,
        "Collado Villalba": 2176,
        "Pozuelo de Alarcón": 4680,
        "San Sebastián de los Reyes": 3037,
        "Boadilla del Monte": 3886,
        "Villaviciosa de Odón": 3349,
        "Majadahonda": 3996,
        "Coslada": 2598
    }

    # Diccionario de precios por metro cuadrado por barrio en Madrid Capital
    precio_m2_barrio = {
        "Arganzuela": 4957,
        "Barajas": 3727,
        "Carabanchel": 2730,
        "Centro": 6223,
        "Chamartín": 6389,
        "Chamberí": 6848,
        "Ciudad Lineal": 4020,
        "Fuencarral": 3475,
        "Hortaleza": 4667,
        "Latina": 3037,
        "Moncloa": 4957,
        "Moratalaz": 3527,
        "Puente de Vallecas": 2038,
        "Retiro": 6286,
        "Salamanca": 7690,
        "San Blas": 2963,
        "Tetúan": 4970,
        "Usera": 3036,
        "Vicálvaro": 2786,
        "Villa de Vallecas": 2747,
        "Villaverde": 2333
    }

    # Selección del municipio
    municipio = st.selectbox("Municipio", list(precios_medios_municipios.keys()))
    
    if municipio == "Madrid Capital":
        barrio = st.selectbox("Barrio", list(precio_m2_barrio.keys()))
        precio_m2 = precio_m2_barrio[barrio]
    else:
        precio_m2 = precios_medios_municipios[municipio]

    sqm_construido = st.number_input("sqm Construido medido", min_value=0)
    factor_incremento = st.number_input("Factor de Incremento (%)", min_value=0, max_value=100, value=0)
    
    # Cálculo del precio de venta estimado
    precio_venta_estimado = sqm_construido * precio_m2 * (1 + factor_incremento / 100)

    # Inputs adicionales
    margen_anualizado = st.number_input("Margen Anualizado (%)", min_value=0.0, max_value=100.0, value=10.0)
    dob_objetivo = st.number_input("DoB Objetivo", min_value=0.0, max_value=100.0, value=20.0)
    margen_esperado = st.number_input("Margen Esperado (%)", min_value=0.0, max_value=100.0, value=20.0)
    
    # Cálculo del máximo de inversión permitida
    max_inversion_permitida = precio_venta_estimado * (1 - margen_esperado / 100)

    # Display de resultados
    st.write(f"Precio de Venta Estimado: {precio_venta_estimado:.2f} €")
    st.write(f"Margen Anualizado: {margen_anualizado:.2f}%")
    st.write(f"DoB Objetivo: {dob_objetivo:.2f}%")
    st.write(f"Margen Esperado: {margen_esperado:.2f}%")
    st.write(f"Máximo de Inversión Permitida: {max_inversion_permitida:.2f} €")

# Run the app
if __name__ == "__main__":
    main()
