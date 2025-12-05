# Análisis de Rentabilidad para Flota de Transporte Propia
## Resumen de Hallazgos y Recomendaciones

---

## 1. RESUMEN EJECUTIVO

### Objetivo del Análisis
Evaluar la viabilidad económica de reemplazar los servicios de transporte externos por una flota de vehículos propia para abastecimiento y distribución, analizando datos de costos de transporte de septiembre a noviembre 2025.

### Conclusión Principal
**Es VIABLE implementar una flota propia** enfocada en rutas consolidadas desde Santiago, con un volumen de **~500 m³/semana** que justifica **10 despachos semanales** usando 2 rampas de carga de 50m³.

---

## 2. DATOS DEL ANÁLISIS

### Periodo Analizado
- **Meses:** Septiembre, Octubre, Noviembre 2025
- **Duración:** 3 meses (12 semanas)
- **Datos válidos:** 10,327 envíos

### Volumen de Operación
- **Total envíos:** 10,327 registros
- **Promedio mensual:** 3,442 envíos/mes
- **Promedio diario:** ~115 envíos/día
- **Costo total 3 meses:** $421,028,537 CLP
- **Costo promedio mensual:** $140,342,846 CLP
- **Costo promedio por envío:** $40,770 CLP

### Distribución por Origen
- **Santiago (consolidado):** 64% de los envíos
  - Incluye: Santiago, Lampa, Colina, Quilicura, Renca, Dartel Matta, CD Los Libertadores
- **Otros orígenes:** 36% de los envíos
  - Antofagasta, Concepción, Puerto Montt, etc.

---

## 3. HALLAZGOS CRÍTICOS POR TRANSPORTISTA

### Tres Transportistas Operando

| Transportista | Envíos | % Total | Costo Total | Costo Promedio | $/kg |
|---------------|--------|---------|-------------|----------------|------|
| **PDQ** | 5,365 | 52% | $130.4M | $24,305 | $167 |
| **SAMEX** | 2,703 | 26% | $173.0M | $63,989 | $193 |
| **TVP** | 2,259 | 22% | $117.7M | $52,089 | $5,274* |

*Anomalía en TVP sugiere error de datos o modelo diferente de cobro

### Insights Clave

#### PDQ - Servicio Express/Premium
- **Característica:** Envíos más pequeños (promedio 160 kg vs 370-420 kg otros)
- **Modelo de cobro:** Por servicio/envío (correlación peso-costo: 0.494)
- **Perfil:** 62% envíos muy pequeños (<50kg)
- **Costo/kg:** $167 (competitivo para su tamaño)

#### SAMEX - Transporte Consolidado
- **Característica:** Envíos medianos-grandes (promedio 370 kg)
- **Modelo de cobro:** Por peso/volumen (correlación: 0.977)
- **Perfil:** Mayor consolidación, 42% envíos pequeños
- **Costo/kg:** $193

#### TVP - Transporte Consolidado
- **Característica:** Envíos grandes (promedio 422 kg)
- **Modelo de cobro:** Por peso/volumen (correlación: 0.977)
- **Perfil:** 30% envíos pequeños, mejor consolidación
- **Costo/kg:** Dato anómalo, requiere validación

### Implicación Estratégica
**Una flota propia debe competir con el modelo consolidado (SAMEX/TVP)**, NO con el servicio express (PDQ), ya que este último opera en un nicho diferente de alta urgencia.

---

## 4. ANÁLISIS DE RUTAS PRINCIPALES

### Top 15 Rutas Más Costosas (desde Santiago)

| Ruta | Costo Total | Envíos | Costo/Envío | Vol/Semana | % Ocupación |
|------|-------------|--------|-------------|------------|-------------|
| **Santiago → Antofagasta** | $45.5M | 608 | $74,896 | 87.2 m³ | 174% |
| **Santiago → Iquique** | $36.5M | 480 | $76,024 | 60.0 m³ | 120% |
| **Santiago → Puerto Montt** | $22.3M | 296 | $75,433 | 42.2 m³ | 84% |
| **Santiago → Temuco** | $21.9M | 394 | $55,463 | 35.6 m³ | 71% |
| **Santiago → Calama** | $20.9M | 418 | $49,958 | 37.6 m³ | 75% |
| **Santiago → Copiapo** | $19.8M | 395 | $50,179 | 41.1 m³ | 82% |
| **Santiago → Serena** | $18.9M | 402 | $46,977 | 48.7 m³ | 97% |
| **Santiago → Concepcion** | $17.4M | 475 | $36,573 | 34.4 m³ | 69% |
| **Santiago → Valdivia** | $15.8M | 304 | $51,972 | 24.0 m³ | 48% |
| **Santiago → Talca** | $15.7M | 421 | $37,364 | 37.2 m³ | 74% |
| **Santiago → Chillan** | $10.2M | 261 | $39,049 | 21.9 m³ | 44% |
| **Santiago → Los Angeles** | $6.1M | 243 | $25,168 | 11.8 m³ | 24% |
| **Santiago → Osorno** | - | 188 | - | 7.4 m³ | 15% |
| **Santiago → Rancagua** | $6.4M | 293 | $22,007 | 18.3 m³ | 37% |

### Principio de Pareto
- **17 rutas representan el 80% del costo total**
- **14 rutas representan el 80% de la frecuencia**
- Alta concentración permite optimización enfocada

---

## 5. CALENDARIO DE DESPACHOS OPTIMIZADO

### Estrategia de Despacho
- **Capacidad por rampa:** 50 m³
- **Rampas disponibles:** 2
- **Horario:** Lunes a Viernes (NO viernes noche)
- **Camiones grandes:** 10 despachos/semana
- **Camiones adicionales:** 2 locales (mediano + pequeño)

### Calendario Semanal

#### 🟢 LUNES
| Ruta | Tipo Camión | Volumen | Destinos | Notas |
|------|-------------|---------|----------|-------|
| Antofagasta + Calama | Grande (50m³) | 50 de 75m³ | Antofagasta, Calama | 25m³ excedente por courier |
| Rancagua | Mediano (18m³) | 18.3 m³ | Rancagua | Ruta local sur |
| Valparaíso | Pequeño (5m³) | 4.2 m³ | Valparaíso | Ruta local oeste |

**Uso de rampas grandes:** 1/2 (50%)

---

#### 🟢 MARTES
| Ruta | Tipo Camión | Volumen | Destinos | Notas |
|------|-------------|---------|----------|-------|
| Osorno + Puerto Montt | Grande (50m³) | 49.6 m³ | Osorno, Puerto Montt | 99% ocupación - ÓPTIMO |
| Talca + Chillán | Grande (50m³) | 50 de 59m³ | Talca, Chillán | 9m³ excedente por courier |

**Uso de rampas grandes:** 2/2 (100%)

---

#### 🟢 MIÉRCOLES
| Ruta | Tipo Camión | Volumen | Destinos | Notas |
|------|-------------|---------|----------|-------|
| Temuco + Valdivia | Grande (50m³) | 50 de 60m³ | Temuco, Valdivia | 10m³ excedente por courier |
| Los Angeles + Concepción | Grande (50m³) | 46.2 m³ | Los Angeles, Concepción | 92% ocupación |

**Uso de rampas grandes:** 2/2 (100%)

---

#### 🟢 JUEVES
| Ruta | Tipo Camión | Volumen | Destinos | Notas |
|------|-------------|---------|----------|-------|
| La Serena | Grande (50m³) | 48.7 m³ | La Serena | 97% ocupación |
| Copiapó | Grande (50m³) | 41.1 m³ | Copiapó | 82% ocupación |

**Uso de rampas grandes:** 2/2 (100%)

---

#### 🟢 VIERNES (Despachos Fin de Semana)
| Ruta | Tipo Camión | Volumen | Destinos | Notas |
|------|-------------|---------|----------|-------|
| Iquique | Grande (50m³) | 50 de 60m³ | Iquique | 🚚 Viaja FDS, entrega LUNES |
| Antofagasta Directo | Grande (50m³) | 50 de 87m³ | Antofagasta | 🚚 Viaja FDS, entrega LUNES |

**Uso de rampas grandes:** 2/2 (100%)

**Nota:** Resto de volumen Antofagasta va en ruta compartida del lunes

---

### Resumen de Operación Semanal

| Métrica | Valor |
|---------|-------|
| **Total despachos camiones grandes** | 10/semana |
| **Total despachos camiones locales** | 2/semana (lunes) |
| **Volumen transportado flota propia** | ~490 m³/semana |
| **Volumen total generado** | ~543 m³/semana |
| **Excedente por courier** | ~53 m³/semana (9.8%) |
| **Ocupación promedio camiones grandes** | ~98% |
| **Costo actual total/semana** | $24.0M CLP |
| **Costo actual mensual** | $96.0M CLP |
| **Costo actual anual** | $1,248M CLP |

---

## 6. ANÁLISIS DE CONSOLIDACIÓN DE RUTAS

### Rutas que NO se deben consolidar
Basado en análisis de volumen y geografía:

1. **La Serena ≠ Copiapó**
   - Razón: Ambas tienen >80% ocupación individual
   - Distancia: 335 km entre ellas
   - Tiempo adicional: 4-5 horas + descarga
   - Decisión: Despachos separados jueves

2. **Antofagasta ≠ Calama (siempre)**
   - Razón: Antofagasta sola ya necesita 1.7 camiones/semana
   - Decisión:
     - Viernes: Antofagasta directo (50m³)
     - Lunes: Antofagasta + Calama compartido (75m³ en 1 camión)

3. **Rancagua ≠ Valparaíso**
   - Razón: Direcciones opuestas desde Santiago
   - Rancagua: Sur (120 km)
   - Valparaíso: Oeste (120 km)
   - Decisión: Despachos separados mismo día (lunes) con camiones más pequeños

### Consolidaciones Exitosas

| Ruta Consolidada | Razón | Ocupación |
|------------------|-------|-----------|
| **Osorno + Puerto Montt** | Osorno está en la ruta hacia Puerto Montt | 99% ÓPTIMO |
| **Talca + Chillán** | Talca está de paso hacia Chillán | 118% (courier) |
| **Temuco + Valdivia** | Zona costa sur, geográficamente cercanas | 119% (courier) |
| **Los Angeles + Concepción** | Zona sur, ruta natural | 92% |
| **Antofagasta + Calama** | Norte, ruta compartida cuando conviene | 150% (lunes) |

---

## 7. ESTRATEGIA DE MANEJO DE EXCEDENTES

### Problema
Cuando una ruta consolidada genera >50m³, usar 2 camiones es ineficiente:
- Camión 1: 100% lleno
- Camión 2: <20% lleno (desperdicio)

### Solución Propuesta
**Regla de Oro:** Si volumen está entre 50-60m³:
1. Llenar 1 camión completo (50m³)
2. Enviar excedente (10m³) por courier/PDQ

### Excedentes por Ruta

| Ruta | Volumen Total | En Camión | Excedente | % Excedente |
|------|---------------|-----------|-----------|-------------|
| Antofagasta + Calama (lunes) | 75.0 m³ | 50 m³ | 25.0 m³ | 33% |
| Iquique | 60.0 m³ | 50 m³ | 10.0 m³ | 17% |
| Talca + Chillán | 59.1 m³ | 50 m³ | 9.1 m³ | 15% |
| Temuco + Valdivia | 59.6 m³ | 50 m³ | 9.6 m³ | 16% |
| **TOTAL** | **253.7 m³** | **200 m³** | **53.7 m³** | **21%** |

### Beneficio
- **Ahorro operacional:** No operar 4 camiones semivacíos
- **Flexibilidad:** Excedentes van por servicio express cuando necesario
- **Eficiencia:** Ocupación promedio sube de 60% a 98%

---

## 8. ANÁLISIS DE FRECUENCIA

### Despachos por Día de Semana (Datos Históricos)

| Día | Envíos Totales | Costo Total | % del Total |
|-----|----------------|-------------|-------------|
| **Lunes** | 2,008 | $904.7M | 21.5% |
| **Martes** | 2,237 | $1,031.6M | 24.5% |
| **Miércoles** | 2,036 | $1,190.3M | 28.3% |
| **Jueves** | 2,129 | $1,119.6M | 26.6% |
| **Viernes** | 1,702 | $742.8M | 17.6% |
| **Sábado** | 24 | $57.5M | 1.4% |
| **Domingo** | 0 | $0 | 0% |

### Insight
- **Mayor actividad:** Martes-Jueves
- **Sábado:** Actividad mínima (24 envíos en 3 meses)
- **Propuesta:** Usar viernes para despachos que viajan fin de semana (Iquique, Antofagasta)

---

## 9. NECESIDADES DE FLOTA

### Flota Semanal Estimada

#### Camiones Grandes (50m³ / ~16 toneladas)
- **Cantidad:** 10 despachos/semana
- **Uso:** Rutas principales de larga distancia
- **Ocupación promedio:** 98%
- **Kilometraje semanal estimado:**
  - Promedio por camión: ~1,000 km
  - Total flota: ~10,000 km/semana

#### Camiones Medianos (~18m³ / ~8 toneladas)
- **Cantidad:** 1 despacho/semana
- **Uso:** Rancagua (ruta local, 120 km)
- **Ocupación:** 100% (18.3 m³)

#### Camiones Pequeños (~5m³ / ~3.5 toneladas)
- **Cantidad:** 1 despacho/semana
- **Uso:** Valparaíso (ruta local, 120 km)
- **Ocupación:** 84% (4.2 m³)

### Estrategia de Propiedad

**Opción A - Flota 100% Propia:**
- 10 camiones grandes
- 1 camión mediano
- 1 camión pequeño

**Opción B - Modelo Mixto (RECOMENDADO):**
- **Propios:** 6-8 camiones grandes para rutas fijas (lun-jue)
- **Leasing/Outsourcing:** 2-4 camiones para picos de demanda (viernes)
- **Locales:** Outsourcing para Rancagua y Valparaíso (bajo volumen)

---

## 10. RECOMENDACIONES ESTRATÉGICAS

### 1. Implementación por Fases

#### Fase 1 - Piloto (Mes 1-3)
- **Rutas:** Top 5 más rentables
  - Antofagasta directo (viernes)
  - Iquique (viernes)
  - La Serena (jueves)
  - Osorno + Puerto Montt (martes)
  - Talca + Chillán (martes)
- **Flota:** 5 camiones grandes
- **Impacto:** ~40% del costo actual

#### Fase 2 - Expansión (Mes 4-6)
- **Agregar:**
  - Copiapó (jueves)
  - Antofagasta + Calama (lunes)
  - Temuco + Valdivia (miércoles)
- **Flota:** 8 camiones grandes
- **Impacto:** ~70% del costo actual

#### Fase 3 - Consolidación (Mes 7-12)
- **Agregar:**
  - Los Angeles + Concepción (miércoles)
  - Rutas locales (lunes)
- **Flota:** 10 camiones grandes + 2 locales
- **Impacto:** ~85% del costo actual

### 2. Optimizaciones Operacionales

#### A. Gestión de Excedentes
- Negociar tarifa preferencial con PDQ/courier para 53m³/semana
- Evaluar si algunos excedentes pueden consolidarse o reprogramarse

#### B. Carga de Retorno
- Investigar oportunidades de carga de retorno en rutas largas:
  - Antofagasta → Santiago (minería)
  - Puerto Montt → Santiago (productos regionales)
  - Iquique → Santiago (zona franca)

#### C. Optimización de Rutas
- Implementar software de ruteo dinámico
- Ajustar frecuencias según estacionalidad (datos de solo 3 meses)

### 3. Análisis de Riesgos

#### Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Variabilidad estacional | Alta | Medio | Modelo mixto propio + leasing |
| Falla mecánica | Media | Alto | Mantenimiento preventivo + camión backup |
| Aumento precio combustible | Alta | Alto | Cláusulas de ajuste en contratos |
| Pérdida de carga | Baja | Alto | Seguros + procedimientos de calidad |
| Cambio regulatorio | Baja | Medio | Monitoreo normativo continuo |

### 5. Métricas de Éxito (KPIs)

#### Operacionales
- **Ocupación de camiones:** >90%
- **Entregas a tiempo:** >95%
- **Kilómetros sin carga:** <10%
- **Disponibilidad de flota:** >90%

#### Financieros
- **Costo por km:** Benchmark vs actual
- **Costo por m³ transportado:** <$XXX
- **ROI:** Positivo en 18-24 meses
- **Ahorro vs outsourcing:** >25%

#### Calidad
- **Daños en tránsito:** <0.5%
- **Reclamos de clientes:** <2%
- **Devoluciones por error logístico:** <1%

---

## 11. PRÓXIMOS PASOS

### Análisis Pendientes

1. **Estimación de Costos de Flota Propia (CAPEX y OPEX)**
   - Costo de adquisición de camiones
   - Salarios de conductores
   - Combustible mensual
   - Mantenimiento
   - Seguros y permisos
   - Depreciación

2. **Análisis de Viabilidad Financiera**
   - Comparación costo actual vs flota propia
   - Punto de equilibrio
   - ROI esperado
   - Análisis de sensibilidad (precio combustible, volúmenes)

3. **Estudio de Estacionalidad**
   - Analizar más meses de datos (si disponible)
   - Identificar picos y valles de demanda
   - Ajustar tamaño de flota según estacionalidad

4. **Análisis de Carga de Retorno**
   - Investigar mercado de carga disponible
   - Potencial de ingresos adicionales
   - Impacto en rentabilidad

---

## 12. CONCLUSIONES

### Hallazgos Principales

1. **Volumen Concentrado:** El 80% del costo se concentra en solo 17 rutas desde Santiago
2. **Alta Frecuencia:** 10 rutas justifican despachos semanales con ocupación >80%
3. **Optimización Posible:** Calendario balanceado de 2 rampas/día, 5 días/semana
4. **Excedentes Manejables:** Solo 9.8% del volumen como excedente (courier)
5. **Operación Sostenible:** ~490 m³/semana en 10 despachos es un volumen estable

### Viabilidad

✅ **VIABLE desde perspectiva operacional:**
- Volumen suficiente y constante
- Rutas bien definidas
- Infraestructura disponible (2 rampas)
- Calendario optimizado

⏳ **PENDIENTE análisis financiero completo:**
- Costo CAPEX de flota
- Costo OPEX mensual
- Comparación ROI vs outsourcing actual
- Punto de equilibrio

### Recomendación Preliminar

**PROCEDER con análisis financiero detallado** para validar rentabilidad. Los fundamentos operacionales son sólidos y el volumen justifica la inversión, pero se requiere:

1. Cotización de camiones
2. Estimación precisa de costos operacionales
3. Análisis de financiamiento (compra vs leasing)
4. Proyección de flujo de caja a 5 años

---

## APÉNDICES

### A. Glosario

- **FTL (Full Truck Load):** Carga completa de camión
- **LTL (Less Than Truck Load):** Carga parcial
- **CAPEX:** Gastos de capital (inversión)
- **OPEX:** Gastos operacionales (recurrentes)
- **ROI:** Retorno de inversión
- **TMS:** Sistema de gestión de transporte
- **FDS:** Fin de semana

### B. Supuestos del Análisis

1. Capacidad de rampa: 50 m³ (estándar camión grande)
2. Datos representativos de operación normal (no estacionalidad extrema)
3. Infraestructura de 2 rampas disponible en Santiago
4. No se considera inversión en rampas adicionales
5. Costos de courier para excedentes similares a PDQ actual
6. Horario laboral: Lunes a Viernes (no nocturnos)

### C. Limitaciones del Análisis

1. **Datos limitados:** Solo 3 meses (Sep-Nov 2025)
2. **Estacionalidad desconocida:** No se puede inferir variabilidad anual
3. **Costos financieros:** No incluidos aún (CAPEX/OPEX pendiente)
4. **Carga de retorno:** No considerada (oportunidad de ingreso adicional)
5. **Contingencias:** No se modelaron eventos extraordinarios

---

**Documento generado:** Diciembre 2025
**Análisis de datos:** Septiembre - Noviembre 2025
**Próxima actualización:** Tras completar análisis financiero CAPEX/OPEX
