# Análisis de Rentabilidad para Flota de Transporte Propia

## 1. Objetivo del Proyecto

El objetivo principal de este proyecto es analizar la viabilidad y rentabilidad de reemplazar los servicios de transporte externos por una flota de vehículos propia para el abastecimiento y distribución. Se analizarán los datos de costos de transporte de los últimos tres meses para responder a las siguientes preguntas clave.

### Preguntas a Responder:

1.  **Rentabilidad:** ¿Es económicamente viable internalizar las operaciones de transporte en comparación con los costos actuales?
2.  **Rutas Óptimas:** ¿Cuáles son las rutas más frecuentes y/o costosas que podrían ser candidatas para ser operadas con flota propia?
3.  **Frecuencia:** ¿Con qué periodicidad se deberían realizar estas rutas para satisfacer la demanda actual?
4.  **Necesidades de Flota:** ¿Qué tipo de camiones (capacidad, refrigeración, etc.) y qué cantidad de ellos serían necesarios para cubrir estas rutas de manera eficiente?

## 2. Metodología

El proyecto se desarrollará siguiendo un enfoque de análisis de datos, modelado de costos y simulación.

1.  **Recopilación y Limpieza de Datos:**
    *   Consolidar los registros de cobros de las empresas de transporte de los últimos 3 meses.
    *   Realizar una limpieza de datos para estandarizar nombres de destinos, corregir errores y manejar datos faltantes.

2.  **Análisis Exploratorio de Datos (EDA):**
    *   Utilizando Jupyter Notebooks, se explorarán los datos para identificar patrones, tendencias y anomalías.
    *   Se analizará la distribución de viajes por destino, los costos por ruta, la frecuencia de los despachos y el peso/volumen de la carga.
    *   Se crearán visualizaciones (mapas, gráficos de barras, etc.) para entender mejor la operación actual.

3.  **Modelado de Costos y Simulación:**
    *   **Costeo Flota Externa:** Calcular el costo total y promedio por ruta con el modelo actual.
    *   **Costeo Flota Propia:** Estimar los costos fijos y variables de una operación interna. Esto incluye:
        *   *Costos de Capital (CAPEX):* Compra o leasing de camiones.
        *   *Costos de Operación (OPEX):* Salarios de conductores, combustible, mantenimiento, seguros, peajes y permisos.
    *   **Simulación de Rutas:** Agrupar puntos de entrega cercanos para diseñar rutas optimizadas. Se simulará la operación con diferentes configuraciones de flota para encontrar el punto de equilibrio y estimar el ahorro potencial.

4.  **Análisis de Sensibilidad:**
    *   Evaluar cómo variarían los resultados ante cambios en variables clave como el precio del combustible, los costos de mantenimiento o los salarios.

## 3. Herramientas y Entregables

*   **Lenguaje de Programación:** Python 3.x
*   **Librerías Principales:**
    *   `pandas` para la manipulación y análisis de datos.
    *   `numpy` para operaciones numéricas.
    *   `matplotlib` y `seaborn` para la visualización de datos estática.
    *   `plotly` o `folium` para visualizaciones interactivas, especialmente mapas.
    *   `scikit-learn` para algoritmos de clustering (ej. agrupar destinos).
*   **Entorno de Desarrollo:** Jupyter Notebooks será la herramienta principal para el análisis y la experimentación.

### Entregables

1.  **Notebook de Análisis (`Analisis_Transporte.ipynb`):** Un Jupyter Notebook detallado con todo el proceso de limpieza, análisis, modelado y conclusiones.
2.  **Informe de Resultados:** Un documento o presentación (posiblemente un dashboard en Power BI o similar) que resuma los hallazgos de forma ejecutiva, mostrando las conclusiones sobre la rentabilidad, las rutas propuestas y las recomendaciones de flota.
3.  **Datos Procesados:** Archivos CSV o Excel generados durante el análisis que puedan ser utilizados para la presentación de resultados.
