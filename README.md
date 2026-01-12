Dashboard Analítico de Producción Gráfica

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)
![Status](https://img.shields.io/badge/Status-En_Desarrollo-green.svg)

> Un dashboard interactivo para visualizar KPIs, márgenes de ganancia y cuellos de botella en una imprenta simulada.

![Vista Previa del Dashboard](ruta_de_tu_imagen.png)
//Falta la captura del proyecto

## Contexto
Trabajando en la industria gráfica noté la falta de herramientas visuales para analizar la rentabilidad real lo que me llevó a crear esta pequeña herramienta.

Este proyecto simula un entorno de producción (Tarjetas, Lonas, Vinilos) para responder preguntas clave:
* ¿Qué productos tienen el mayor margen de ganancia?
* ¿Qué clientes generan más volumen de trabajo vs. rentabilidad?
* ¿Cómo evoluciona la producción mes a mes?

## Tecnologías Utilizadas
* **Python:** Lógica principal y manipulación de datos.
* **Pandas:** ETL (Extracción, Transformación y Carga) y filtrado de datos.
* **Streamlit:** Framework para la creación de la web app interactiva.
* **Plotly Express:** Visualización de datos interactiva (Scatter plots dinámicos).
* **Numpy:** Generación de escenarios y datos aleatorios para la simulación.

## Características Principales
1.  **Generador de Datos Sintéticos:** Un script (`generador_datos.py`) que crea un escenario realista de 1000 pedidos con fechas, costos variables y estados.
2.  **Filtros Globales:** Capacidad de segmentar toda la información por "Estado" (Entregado, Cancelado, En Proceso).
3.  **Análisis Multidimensional:** El usuario puede elegir dinámicamente qué variables cruzar en los ejes X e Y (ej: *Costo* vs *Venta* o *Margen* vs *Tiempo*).
4.  **Drill-Down:** Tabla de datos crudos ocultable para inspección detallada.

## Instalación y Uso Local

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/FrancoZarat/Proyecto-de-datos.git](https://github.com/FrancoZarat/Proyecto-de-datos.git)
    cd Proyecto-de-datos
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install pandas plotly streamlit
    ```

3.  **Ejecutar la aplicación:**
    ```bash
    streamlit run app.py
    ```

## Estructura del Proyecto
* `app.py`: El corazón del dashboard. Contiene la interfaz y la lógica de visualización.
* `generador_datos.py`: Script auxiliar para crear el dataset `datos_imprenta.csv`.
* `datos_imprenta.csv`: Dataset estático utilizado para la demo.

## Próximos Pasos
* [ ] Implementar conexión a una base de datos SQL real.
* [ ] Agregar predicción de ventas futuras usando Regresión Lineal (Scikit-learn).
* [ ] Deployar la aplicación en Streamlit Cloud.

---
**Desarrollado por Franco Zárate**
*Estudiante de Licenciatura en Informática @ UNAHUR*
