import streamlit as st

# Define the main function for the Streamlit app
def main():
    st.title("Calculator App")

    # Sidebar for navigation
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

# Function to display Resumen del Activo
def display_resumen_del_activo():
    st.header("Resumen del Activo")

    # Define dictionaries for municipios and barrios
    precios_medios_municipios = {
        "Madrid": 5000,  # Ejemplo
        "Valencia": 3000,  # Ejemplo
        "Barcelona": 4500,  # Ejemplo
        "Sevilla": 2800  # Ejemplo
    }

    barrios_madrid = {
        "Salamanca": 7000,  # Ejemplo
        "Chamberí": 6500,  # Ejemplo
        "Centro": 6000,  # Ejemplo
        "Retiro": 6400,  # Ejemplo
        # Agrega más barrios y precios según sea necesario
    }

    # Selección de municipio
    municipio = st.selectbox("Municipio", list(precios_medios_municipios.keys()))

    # Selección de barrio si el municipio es Madrid
    barrio = None
    if municipio == "Madrid":
        barrio = st.selectbox("Barrio en Madrid", list(barrios_madrid.keys()))
        precio_m2 = barrios_madrid[barrio]
    else:
        precio_m2 = precios_medios_municipios[municipio]

    # Inputs de dirección y otros datos generales
    direccion = st.text_input("Dirección")
    ref_cat = st.text_input("Ref Cat")
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

    # Display collected data
    st.subheader("Resumen del Activo Data")
    st.write(f"Dirección: {direccion}")
    st.write(f"Ref Cat: {ref_cat}")
    st.write(f"Municipio: {municipio}")
    if barrio:
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
    st.write(f"Precio por m2: €{precio_m2}")

# Function to display Tipo de Reforma
def display_tipo_de_reforma():
    st.header("Tipo de Reforma")

    tipo_reforma = st.selectbox("Tipo de Reforma", ["Humilde", "Normal", "Premium"])
    nivel_reforma = st.selectbox("Nivel de Reforma", ["Full", "Parcial", "Sin Reforma"])
    pluses_calidad = st.text_input("Pluses de Calidad (Letra)")
    calidades_banos = st.radio("Calidades Baños", ["Yes", "No"])
    calidades_cocina = st.radio("Calidades Cocina", ["Yes", "No"])
    calidades_otros = st.radio("Calidades Otros", ["Yes", "No"])
    tipo_venta = st.selectbox("Tipo de Venta", ["Reformado", "Pase"])

    # Display collected data
    st.subheader("Tipo de Reforma Data")
    st.write(f"Tipo de Reforma: {tipo_reforma}")
    st.write(f"Nivel de Reforma: {nivel_reforma}")
    st.write(f"Pluses de Calidad: {pluses_calidad}")
    st.write(f"Calidades Baños: {calidades_banos}")
    st.write(f"Calidades Cocina: {calidades_cocina}")
    st.write(f"Calidades Otros: {calidades_otros}")
    st.write(f"Tipo de Venta: {tipo_venta}")

# Function to display Resumen Activo Calculations
def display_resumen_activo():
    st.header("Resumen Activo")
    
    # Inputs para Aire Acondicionado
    aire_split = st.number_input("Aire acondicionado (split)", min_value=0)
    aire_conductos = st.number_input("Aire acondicionado (conductos)", min_value=0)
    total_aire = aire_split * 1800 + aire_conductos * 3500

    # Inputs para ACS + Calefacción
    tipo_calefaccion = st.text_input("Tipo de calefacción")
    calefaccion_num = st.number_input("Número de sistemas de calefacción", min_value=0)
    acs = st.number_input("ACS", min_value=0)
    total_acs_calefaccion = calefaccion_num * 1800 + acs * 3000

    # Inputs para Terraza
    accion = st.number_input("Acción (Terraza)", min_value=0)
    total_terraza = accion * 60

    # Inputs para Carpitnaria Exterior
    ventana_s = st.number_input("Ventana S", min_value=0)
    ventana_m = st.number_input("Ventana M", min_value=0)
    ventana_l = st.number_input("Ventana L", min_value=0)
    ventana_xl = st.number_input("Ventana XL", min_value=0)
    ventana_paso = st.number_input("Ventana de Paso", min_value=0)
    cerramientos = st.number_input("Cerramientos", min_value=0)
    total_carpitnaria = (ventana_s * 600 + ventana_m * 750 + ventana_l * 1000 +
                         ventana_xl * 1800 + ventana_paso * 2500 + cerramientos * 3000)

    # Inputs para Armarios
    armario_s = st.number_input("Armario S", min_value=0)
    armario_m = st.number_input("Armario M", min_value=0)
    armario_l = st.number_input("Armario L", min_value=0)
    empotrados = st.number_input("Empotrados", min_value=0)
    total_armarios = (armario_s * 1000 + armario_m * 1500 + armario_l * 2000 + empotrados * 2500)

    # Inputs para Baños
    baños_s = st.number_input("Baños S", min_value=0)
    baños_m = st.number_input("Baños M", min_value=0)
    baños_l = st.number_input("Baños L", min_value=0)
    total_baños = baños_s * 6000 + baños_m * 8000 + baños_l * 10000

    # Inputs para Habitaciones
    hab_menor_10 = st.number_input("Habitaciones <10m2", min_value=0)
    hab_mayor_10 = st.number_input("Habitaciones >10m2", min_value=0)
    hab_salon = st.number_input("Salón", min_value=0)
    cocina_salon = st.number_input("Cocina / Salón", min_value=0)
    total_habitaciones = (hab_menor_10 * 4000 + hab_mayor_10 * 6000 +
                          hab_salon * 8000 + cocina_salon * 12000)

    # Inputs para Demolición / Limpieza
    demolicion = st.number_input("Demolición", min_value=0)
    limpieza = st.number_input("Limpieza", min_value=0)
    total_demolicion_limpieza = demolicion * 2000 + limpieza * 1000

    # Display totals
    st.subheader("Resumen Activo Totals")
    st.write(f"Total Aire Acondicionado: €{total_aire}")
    st.write(f"Total ACS + Calefacción: €{total_acs_calefaccion}")
    st.write(f"Total Terraza: €{total_terraza}")
    st.write(f"Total Carpitnaria Exterior: €{total_carpitnaria}")
    st.write(f"Total Armarios: €{total_armarios}")
    st.write(f"Total Baños: €{total_baños}")
    st.write(f"Total Habitaciones: €{total_habitaciones}")
    st.write(f"Total Demolición / Limpieza: €{total_demolicion_limpieza}")

# Function to display P&L de la Operación
def display_pl_operacion():
    st.header("P&L de la Operación")

    # Precios medios por metro cuadrado en diferentes municipios
    precios_medios_municipios = {
        "Madrid": 5000,  # Ejemplo
        "Valencia": 3000,  # Ejemplo
        "Barcelona": 4500,  # Ejemplo
        "Sevilla": 2800  # Ejemplo
        # Agrega más municipios y precios según sea necesario
    }

    # Selección de municipio
    municipio = st.selectbox("Municipio", list(precios_medios_municipios.keys()))

    # Precio medio en función del municipio seleccionado
    precio_m2 = st.number_input("Precio por m2", min_value=0.0, value=precios_medios_municipios[municipio])

    # Inputs for calculations
    coste_total = st.number_input("Coste Total", min_value=0.0)
    sqm_venta = st.number_input("m2 para Venta", min_value=0.0)
    sqm_venta_madrid = st.number_input("m2 para Venta en Madrid", min_value=0.0)
    precio_m2_venta_madrid = st.number_input("Precio por m2 en Madrid", min_value=0.0)
    gastos_impuestos = st.number_input("Gastos e Impuestos", min_value=0.0)
    otros_gastos = st.number_input("Otros Gastos", min_value=0.0)
    honorarios_agencia = st.number_input("Honorarios de Agencia", min_value=0.0)

    # Total Ingresos and Total Gastos calculations
    total_ingresos = precio_m2 * sqm_venta
    total_gastos = coste_total + gastos_impuestos + otros_gastos + honorarios_agencia

    # Resultado de la operación
    resultado_operacion = total_ingresos - total_gastos

    # Display P&L details
    st.subheader("Detalles de P&L")
    st.write(f"Municipio: {municipio}")
    st.write(f"Precio por m2: €{precio_m2}")
    st.write(f"Coste Total: €{coste_total}")
    st.write(f"m2 para Venta: {sqm_venta}")
    st.write(f"Gastos e Impuestos: €{gastos_impuestos}")
    st.write(f"Otros Gastos: €{otros_gastos}")
    st.write(f"Honorarios de Agencia: €{honorarios_agencia}")
    st.write(f"Total Ingresos: €{total_ingresos}")
    st.write(f"Total Gastos: €{total_gastos}")
    st.write(f"Resultado de la Operación: €{resultado_operacion}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
