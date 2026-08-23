import streamlit as st
import pandas as pd
import numpy as np

# Importar las librerías provistas
import libreria_funciones_proyecto1 as lib_func
import libreria_clases_proyecto1 as lib_class

# =========================================================
# CONFIGURACIÓN DE LA PÁGINA Y ESTILOS EJECUTIVOS (ROSA / BURDEOS)
# =========================================================
st.set_page_config(
    page_title="Proyecto 1 - Python Fundamentals",
    page_icon="📊",
    layout="wide"
)

# Estilos CSS personalizados con los ajustes solicitados
st.markdown("""
    <style>
    /* Importar tipografías Google Fonts (Quicksand y Prata) */
    @import url('https://fonts.googleapis.com/css2?family=Prata&family=Quicksand:wght@400;500;600;700&display=swap');
    
    /* Tipografía general Sans Serif (Quicksand) */
    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }
    
    /* Fondo general de la aplicación: Rosa pastel */
    .stApp {
        background-color: #FFF0F3;
    }
    
    /* Estilo para los contenedores generales */
    div.stMarkdown, div.stForm {
        border-radius: 8px;
    }
    
    /* Personalización de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #FFE5EC;
        border-right: 1px solid #FFC5D3;
    }
    
    /* Títulos principales con tipografía Prata y color Rosa Oscuro (#C11C84) */
    h1, h2, h3 {
        font-family: 'Prata', serif;
        color: #C11C84 !important;
        font-weight: 700;
    }
    
    /* Textos y etiquetas generales */
    p, span, label {
        color: #4A1525;
        font-weight: 500;
    }
    
    /* Personalización correcta del cuadro de Información General (st.info) */
    [data-testid="stAlert"] {
        background-color: #FFB5C0 !important;
        border: 1px solid #FF5C52 !important;
    }
    
    [data-testid="stAlert"] [data-testid="stMarkdownContainer"], 
    [data-testid="stAlert"] p, 
    [data-testid="stAlert"] span, 
    [data-testid="stAlert"] strong, 
    [data-testid="stAlert"] li {
        color: #550000 !important;
    }
    
    /* Tarjetas de métricas personalizadas con acento Burdeos */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #FFC5D3;
        padding: 15px;
        border-radius: 10px;
    }
    
    [data-testid="stMetricLabel"] {
        color: #E83256 !important; 
        font-weight: 600;
    }
    
    [data-testid="stMetricValue"] {
        color: #C11C84 !important;
        font-weight: 700;
    }
    
    .stButton>button, div.stFormSubmitButton>button {
        background-color: #d971b2;
        color: #FFB5C0 !important;
        border-radius: 8px;
        border: none;
        font-weight: 700;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover, div.stFormSubmitButton>button:hover {
        background-color: #660033;
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# MENÚ DE NAVEGACIÓN LATERAL
# =========================================================
st.sidebar.image("DMC Logo.png", width=80)

st.sidebar.title("Menú de Navegación")
menu = st.sidebar.selectbox(
    "Seleccione una sección:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# =========================================================
# 1. HOME
# =========================================================
if menu == "Home":
    st.title("📊 Especialización en Python for Analytics")
    st.subheader("Módulo 1 - Python Fundamentals | Proyecto Aplicado")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 💡 Descripción del Proyecto
        Esta aplicación interactiva integra los conceptos fundamentales aprendidos durante el módulo, que
        incluye variables, estructuras de datos, control de flujo, funciones y programación.
        
        El sistema permite simular operaciones prácticas organizadas en módulos interactivos, diseñado bajo 
        un enfoque analítico para la gestión eficiente de procesos operativos y de costos.
        """)
        
        st.markdown("""
        ### 🛠️ Tecnologías y Librerías
        * **Python:** Lenguaje principal de procesamiento.
        * **Streamlit:** Interfaz web interactiva en la nube.
        * **NumPy & Pandas:** Estructuración y cálculo analítico de arreglos.
        * **GitHub:** Control de versiones y despliegue en la nube (`Streamlit Cloud`).
        """)
        
    with col2:
        st.info("""
        **Información General:**
        * **Estudiante:** Liz Esthefanny Marquez Panuera
        * **Módulo:** Python Fundamentals
        * **Año:** 2026
        """)

# =========================================================
# 2. EJERCICIO 1 - Flujo de caja con listas
# =========================================================
elif menu == "Ejercicio 1":
    st.title("💰 Ejercicio 1: Flujo de Caja con Listas")
    st.markdown("""
    Gestión dinámica de movimientos financieros mediante estructuras de listas y condicionales en Python.
    """)
    
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    with st.form("form_flujo"):
        col1, col2, col3 = st.columns(3)
        with col1:
            concepto = st.text_input("Concepto del movimiento", placeholder="Ej. Insumos médicos, Servicios")
        with col2:
            tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
        with col3:
            valor = st.number_input("Valor (S/.)", min_value=0.0, step=10.0)
            
        submitted = st.form_submit_button("Agregar Movimiento")
        if submitted:
            if concepto.strip() != "":
                st.session_state.movimientos.append({
                    "Concepto": concepto,
                    "Tipo": tipo,
                    "Valor": valor
                })
                st.success(f"Movimiento '{concepto}' agregado correctamente.")
            else:
                st.error("Por favor, ingrese un concepto válido.")

    if st.session_state.movimientos:
        df_mov = pd.DataFrame(st.session_state.movimientos)
        
        total_ingresos = df_mov[df_mov["Tipo"] == "Ingreso"]["Valor"].sum()
        total_gastos = df_mov[df_mov["Tipo"] == "Gasto"]["Valor"].sum()
        saldo_final = total_ingresos - total_gastos

        # Formatear valores en la tabla con el prefijo S/.
        df_mov_display = df_mov.copy()
        df_mov_display["Valor"] = df_mov_display["Valor"].apply(lambda x: f"S/. {x:,.2f}")

        st.markdown("### 📋 Historial de Movimientos")
        st.dataframe(df_mov_display, use_container_width=True)

        # Métricas actualizadas con S/. en lugar de $
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Total Ingresos", f"S/. {total_ingresos:,.2f}")
        col_m2.metric("Total Gastos", f"S/. {total_gastos:,.2f}")
        col_m3.metric("Saldo Final", f"S/. {saldo_final:,.2f}")

        if saldo_final >= 0:
            st.success("✅ El flujo de caja está **a favor**.")
        else:
            st.error("⚠️ El flujo de caja está **en contra**.")
            
        if st.button("Limpiar Registros"):
            st.session_state.movimientos = []
            st.rerun()

# =========================================================
# 3. EJERCICIO 2 - Registro con NumPy, DataFrame, Agregar y Actualizar
# =========================================================
elif menu == "Ejercicio 2":
    st.title("📦 Ejercicio 2: Registro con NumPy y DataFrame")
    st.markdown("""
    Optimización de operaciones aritméticas usando arreglos de **NumPy** convertidos a DataFrames de Pandas, permitiendo agregar y actualizar registros.
    """)

    if "datos_numpy" not in st.session_state:
        st.session_state.datos_numpy = {
            "productos": [],
            "categorias": [],
            "precios": [],
            "cantidades": []
        }

    tab_agregar_np, tab_actualizar_np = st.tabs(["Agregar Registro", "Actualizar Registro"])

    with tab_agregar_np:
        with st.form("form_numpy"):
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                prod = st.text_input("Nombre del producto/servicio")
            with c2:
                cat = st.selectbox("Categoría", ["Farmacia", "Laboratorio", "Cirugía", "Administrativo"])
            with c3:
                precio = st.number_input("Precio unitario (S/.)", min_value=0.0, step=1.0)
            with c4:
                cantidad = st.number_input("Cantidad", min_value=1, step=1)
                
            btn_np = st.form_submit_button("Registrar en Array")
            if btn_np:
                if prod.strip():
                    st.session_state.datos_numpy["productos"].append(prod)
                    st.session_state.datos_numpy["categorias"].append(cat)
                    st.session_state.datos_numpy["precios"].append(precio)
                    st.session_state.datos_numpy["cantidades"].append(cantidad)
                    st.success("Registro añadido con éxito.")
                else:
                    st.error("El nombre del producto no puede estar vacío.")

    with tab_actualizar_np:
        if st.session_state.datos_numpy["productos"]:
            with st.form("form_update_numpy"):
                prod_a_editar = st.selectbox("Seleccione producto a actualizar", st.session_state.datos_numpy["productos"])
                idx_actual = st.session_state.datos_numpy["productos"].index(prod_a_editar)
                
                nuevo_precio = st.number_input("Nuevo Precio Unitario (S/.)", min_value=0.0, value=float(st.session_state.datos_numpy["precios"][idx_actual]), step=1.0)
                nueva_cantidad = st.number_input("Nueva Cantidad", min_value=1, value=int(st.session_state.datos_numpy["cantidades"][idx_actual]), step=1)
                
                btn_upd_np = st.form_submit_button("Actualizar Datos")
                if btn_upd_np:
                    st.session_state.datos_numpy["precios"][idx_actual] = nuevo_precio
                    st.session_state.datos_numpy["cantidades"][idx_actual] = nueva_cantidad
                    st.success(f"¡El producto '{prod_a_editar}' fue actualizado correctamente!")
        else:
            st.info("No hay registros disponibles para actualizar.")

    if st.session_state.datos_numpy["productos"]:
        arr_precios = np.array(st.session_state.datos_numpy["precios"])
        arr_cantidades = np.array(st.session_state.datos_numpy["cantidades"])
        arr_totales = arr_precios * arr_cantidades

        df_registros = pd.DataFrame({
            "Producto/Servicio": st.session_state.datos_numpy["productos"],
            "Categoría": st.session_state.datos_numpy["categorias"],
            "Precio Unitario": arr_precios,
            "Cantidad": arr_cantidades,
            "Total Calculado": arr_totales
        })

        # Mostrar dataframe con formato estricto en Soles (S/.)
        df_reg_display = df_registros.copy()
        df_reg_display["Precio Unitario"] = df_reg_display["Precio Unitario"].apply(lambda x: f"S/. {x:,.2f}")
        df_reg_display["Total Calculado"] = df_reg_display["Total Calculado"].apply(lambda x: f"S/. {x:,.2f}")

        st.markdown("### 📊 Tabla Consolidada")
        st.dataframe(df_reg_display, use_container_width=True)
        
        if st.button("Reiniciar Registros"):
            st.session_state.datos_numpy = {"productos": [], "categorias": [], "precios": [], "cantidades": []}
            st.rerun()

# =========================================================
# 4. EJERCICIO 3 - Funciones externas y resultados limpios
# =========================================================
elif menu == "Ejercicio 3":
    st.title("⚙️ Ejercicio 3: Funciones desde Librería Externa")
    st.markdown("""
    Ejecución de funciones modulares con visualización limpia de resultados ejecutivos.
    """)

    if "historico_func" not in st.session_state:
        st.session_state.historico_func = []

    funcion_seleccionada = st.selectbox(
        "Seleccione la función a ejecutar:",
        ["calcular_costo_unitario_total", "calcular_punto_equilibrio", "calcular_imc"]
    )

    st.markdown("---")
    
    if funcion_seleccionada == "calcular_costo_unitario_total":
        st.subheader("Parámetros: Costo Unitario Total")
        mat = st.number_input("Costo de Materiales ($)", min_value=0.0, value=1500.0)
        mo = st.number_input("Costo de Mano de Obra ($)", min_value=0.0, value=3000.0)
        ci = st.number_input("Costos Indirectos ($)", min_value=0.0, value=500.0)
        unidades = st.number_input("Unidades Producidas", min_value=1, value=100)

        if st.button("Ejecutar Función"):
            try:
                res = lib_func.calcular_costo_unitario_total(mat, mo, ci, unidades)
                st.success("¡Cálculo ejecutado exitosamente!")
                
                col_r1, col_r2 = st.columns(2)
                col_r1.metric("Costo Total", f"${res.get('costo_total', 0):,.2f}")
                col_r2.metric("Costo Unitario", f"${res.get('costo_unitario', 0):,.2f}")
                
                st.session_state.historico_func.append({
                    "Función": funcion_seleccionada,
                    "Resultado Principal": f"Costo Unitario: ${res.get('costo_unitario', 0):,.2f}"
                })
            except Exception as e:
                st.error(f"Error en el cálculo: {e}")

    elif funcion_seleccionada == "calcular_punto_equilibrio":
        st.subheader("Parámetros: Punto de Equilibrio")
        cf = st.number_input("Costos Fijos ($)", min_value=0.0, value=5000.0)
        pu = st.number_input("Precio Unitario ($)", min_value=0.0, value=100.0)
        cv = st.number_input("Costo Variable Unitario ($)", min_value=0.0, value=40.0)

        if st.button("Ejecutar Función"):
            try:
                res = lib_func.calcular_punto_equilibrio(cf, pu, cv)
                st.success("¡Cálculo ejecutado exitosamente!")
                
                col_r1, col_r2, col_r3 = st.columns(3)
                col_r1.metric("Margen Contribución", f"S/.{res.get('margen_contribucion_unitario', 0):,.2f}")
                col_r2.metric("Punto Equilibrio (Unid.)", f"{res.get('punto_equilibrio_unidades', 0):,.2f}")
                col_r3.metric("Punto Equilibrio (Ventas)", f"S/.{res.get('punto_equilibrio_ventas', 0):,.2f}")
                
                st.session_state.historico_func.append({
                    "Función": funcion_seleccionada,
                    "Resultado Principal": f"Punto de Equilibrio en Unidades: {res.get('punto_equilibrio_unidades', 0):,.2f}"
                })
            except Exception as e:
                st.error(f"Error en el cálculo: {e}")

    elif funcion_seleccionada == "calcular_imc":
        st.subheader("Parámetros: Índice de Masa Corporal")
        peso = st.number_input("Peso (kg)", min_value=1.0, value=70.0)
        altura = st.number_input("Altura (m)", min_value=0.5, value=1.75)

        if st.button("Ejecutar Función"):
            try:
                res = lib_func.calcular_imc(peso, altura)
                st.success("¡Cálculo ejecutado exitosamente!")
                
                col_r1, col_r2 = st.columns(2)
                col_r1.metric("IMC Calculado", f"{res.get('imc', 0):,.2f}")
                col_r2.metric("Clasificación", f"{res.get('clasificacion', '')}")
                
                st.session_state.historico_func.append({
                    "Función": funcion_seleccionada,
                    "Resultado Principal": f"IMC: {res.get('imc', 0):,.2f} ({res.get('clasificacion', '')})"
                })
            except Exception as e:
                st.error(f"Error en el cálculo: {e}")

    if st.session_state.historico_func:
        st.markdown("### 📈 Histórico de Ejecuciones")
        st.dataframe(pd.DataFrame(st.session_state.historico_func), use_container_width=True)

# =========================================================
# 5. EJERCICIO 4 - Clases con CRUD
# =========================================================
elif menu == "Ejercicio 4":
    st.title("🏢 Ejercicio 4: Clases con CRUD (POO)")
    st.markdown("""
    Gestión completa de inventarios orientada a objetos importada desde `libreria_clases_proyecto1.py`.
    """)

    if "inventario_objetos" not in st.session_state:
        st.session_state.inventario_objetos = []

    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])

    with tab_crear:
        st.subheader("Crear Nuevo Registro")
        with st.form("form_crear_prod"):
            nombre_p = st.text_input("Nombre del Producto")
            costo_p = st.number_input("Costo Unitario ($)", min_value=0.01, value=10.0)
            precio_p = st.number_input("Precio Unitario ($)", min_value=0.01, value=25.0)
            stock_a = st.number_input("Stock Actual", min_value=0, value=50)
            stock_m = st.number_input("Stock Mínimo", min_value=0, value=10)
            
            btn_crear = st.form_submit_button("Instanciar Objeto")
            if btn_crear:
                if nombre_p.strip():
                    nuevo_prod = lib_class.InventarioProducto(
                        nombre=nombre_p,
                        costo_unitario=costo_p,
                        precio_unitario=precio_p,
                        stock_actual=stock_a,
                        stock_minimo=stock_m
                    )
                    st.session_state.inventario_objetos.append(nuevo_prod)
                    st.success(f"Objeto '{nombre_p}' incorporado exitosamente.")
                else:
                    st.error("El nombre del producto es obligatorio.")

    with tab_leer:
        st.subheader("Visualización del Inventario")
        if st.session_state.inventario_objetos:
            resumenes = [obj.resumen() for obj in st.session_state.inventario_objetos]
            df_inv = pd.DataFrame(resumenes)
            st.dataframe(df_inv, use_container_width=True)
        else:
            st.info("No hay registros creados todavía.")

    with tab_actualizar:
        st.subheader("Actualizar Stock")
        if st.session_state.inventario_objetos:
            nombres = [obj.nombre for obj in st.session_state.inventario_objetos]
            prod_seleccionado = st.selectbox("Seleccione producto", nombres, key="upd_select")
            nuevo_stock = st.number_input("Nuevo Stock Actual", min_value=0, value=20, key="upd_stock_val")
            
            if st.button("Actualizar Stock"):
                for obj in st.session_state.inventario_objetos:
                    if obj.nombre == prod_seleccionado:
                        obj.stock_actual = int(nuevo_stock)
                        st.success(f"Stock actualizado correctamente.")
                st.rerun()
        else:
            st.info("No hay productos disponibles.")

    with tab_eliminar:
        st.subheader("Eliminar Registro")
        if st.session_state.inventario_objetos:
            nombres_del = [obj.nombre for obj in st.session_state.inventario_objetos]
            prod_a_borrar = st.selectbox("Seleccione producto a eliminar", nombres_del, key="del_select")
            
            if st.button("Eliminar"):
                st.session_state.inventario_objetos = [
                    obj for obj in st.session_state.inventario_objetos if obj.nombre != prod_a_borrar
                ]
                st.success(f"Registro eliminado correctamente.")
                st.rerun()
        else:
            st.info("No hay productos disponibles.")
