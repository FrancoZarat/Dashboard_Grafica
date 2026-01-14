import streamlit as st
import pandas as pd
import plotly.express as px
#"Importar" el csv ya creado
df = pd.read_csv("datos_imprenta.csv")
lista_productos=df["Producto"].unique()
opcion_producto = st.multiselect("Selecciona los productos a revisar",lista_productos,default=lista_productos)
df_filtrado=df[df["Producto"].isin(opcion_producto)]
st.header("Estadisticas generales")
total_pedidos = len(df_filtrado)
total_ventas = df_filtrado["Precio_Venta"].sum()
margen_promedio = df_filtrado["Margen"].mean()
c1,c2,c3 = st.columns(3)
with c1:
    c1.metric("Pedidos Totales",total_pedidos)
with c2:
    c2.metric("Total Vendido", f"${total_ventas:,.0f}")
with c3:
    c3.metric("Margen Promedio",f"${margen_promedio:,.0f}")
st.title("Datos de venta")
with st.expander("Visualizacion de datos crudos"):#Oculta el df para que no moleste tanto
    st.dataframe(df_filtrado#Tambien puede usarse la notacion df[filaInicio:filaFinal]
    ,hide_index=True)
opciones_numericas=["Margen","Precio_Venta","Costo_Produccion"]
opciones_categoria=["Producto","Cliente","Estado"]

#Organizacion de los selectores
col1,col2,col3 = st.columns(3)
with col1:
    eje_x=st.selectbox("Primer filtro",
(opciones_numericas),index=None,placeholder="Selecciona uno...")
with col2:
    eje_y=st.selectbox("Segundo filtro",
(opciones_numericas),index=None,placeholder="Selecciona uno...")
with col3:
    columna_color=st.selectbox("Selecciona una categoria",(opciones_categoria))

st.write(f"Elegiste {eje_x} vs {eje_y}")

#Solucion al error que genera el no tener una opcion preestablecida 
if eje_x and eje_y:
        
    fig = px.scatter(
        df_filtrado,
        x = eje_x,
        y = eje_y,
        color=columna_color
    )
    st.plotly_chart(fig)
else:
    st.write("Para ver el grafico selecciona primero los filtros.")

