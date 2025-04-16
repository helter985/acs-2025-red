INTEGRANTES: Enzo Mastrangelo, Santiago Navarro, Máximo Sat, Joaquin Piastrellini
MATERIA: Aseguramiento de la Calidad de Software

# TEST PLAN - LISTA DE PRECIOS

## Document Approval

+------------------------+----------------+------------+------------+
| Nombre                 | Rol            | Fecha      | Aprobación |
+------------------------+----------------+------------+------------+
| Máximo Rajbal Sat      | QA Lead        | 15/06/2025 | ✔ / ✘     |
| Enzo Mastrangelo       | Dev            | 15/06/2025 | ✔ / ✘     |
| Santiago Navarro       | Dev            | 15/06/2025 | ✔ / ✘     |
| Joaquín Piastrellini   | Dev Lead       | 15/06/2025 | ✔ / ✘     |
| John Doe               | Cliente        | 15/06/2025 | ✔ / ✘     |
+------------------------+----------------+------------+------------+

---

## 1. Introduction

### 1.1 Purpose
El propósito de este documento es definir el plan de pruebas para el sistema de consulta de precios desarrollado para una distribuidora de artículos de limpieza.

Este sistema permitirá a los vendedores (entre 40 y 50 personas) consultar rápidamente y sin errores el precio actualizado de los productos en su celular.

### 1.2 Scope

**In Scope:**
- Funcionalidad: Validar que la aplicación y las listas carguen correctamente.
- Usabilidad: Pruebas reales de uso.
- Compatibilidad: Funciona en Android/iOS.
- UI: Pruebas visuales y claridad.

**Out of Scope:**
- Seguridad
- Performance
- Hardware
- Gestión de stock
- Historial de listas

### 1.3 Definitions

+--------------+--------------------------------------------------------------------+
| Término      | Definición                                                         |
+--------------+--------------------------------------------------------------------+
| QA Lead      | Responsable de planificación y ejecución de pruebas               |
| Dev Lead     | Responsable técnico                                                |
| Dev          | Responsable del desarrollo                                         |
| Cliente      | Valida que se cumplan los requisitos                              |
| Vendedor     | Usuario final que consulta precios                                 |
| Admin        | Carga listas semanalmente                                          |
+--------------+--------------------------------------------------------------------+

---

## 2. Requerimientos

### 2.1 Descripción de Roles

**Vendedor:** Usuario que consulta precios desde el celular.  
**Admin:** Carga listas desde casa central.  
**Cliente:** Valida entregables y requisitos.

### 2.2 Features por Rol

**Vendedor:**
- Consultar productos por nombre o código.
- Ver precio actual.
- Ver imagen (si está).
- Confirmar versión más reciente.

**Admin:**
- Subir listas de precios en Excel.
- Actualizar semanalmente.
- Cargar imágenes.
- Verificar nombre, código, precio e imagen.

---

### 2.3 User Stories

**Historia 1 - Buscar producto por nombre o código**  
Como vendedor quiero buscar productos por nombre/código para ver información del producto.  
*Criterios:* búsqueda parcial/total, mostrar mensaje si no existe.

**Historia 2 - Ver precio actualizado**  
Como vendedor quiero ver precio actualizado para dar información correcta.  
*Criterios:* mostrar precio de la última lista.

**Historia 3 - Ver imagen del producto**  
Como vendedor quiero ver la imagen para confirmar visualmente.  
*Criterios:* mostrar imagen o ícono si no hay.

**Historia 4 - Confirmar última versión**  
Como vendedor quiero saber si la lista es la última.  
*Criterios:* mostrar fecha de última carga.

**Historia 5 - Subir listas desde Excel**  
Como admin quiero subir listas para mantener el sistema actualizado.  
*Criterios:* aceptar .xls/.xlsx, error si mal formateado.

**Historia 6 - Mantener versión vigente**  
Como admin quiero actualizar semanalmente la lista.  
*Criterios:* reemplazar lista sin errores.

**Historia 7 - Cargar imágenes manualmente**  
Como admin quiero subir imágenes para mejorar experiencia visual.  
*Criterios:* aceptar .png/.jpg, asociar a producto.

**Historia 8 - Verificar información completa**  
Como admin quiero validar que todos los productos tengan info básica.  
*Criterios:* alertar si falta algún campo antes de guardar.

---

### 2.4 Test Cases

+--------+---------------------------+------------------------------------------+
| TC ID  | Historia                  | Resumen                                  |
+--------+---------------------------+------------------------------------------+
| TC-01  | Historia 1                | Buscar producto por nombre               |
| TC-02  | Historia 1                | Buscar producto por código de barras     |
| TC-03  | Historia 2                | Ver precio actualizado                   |
| TC-04  | Historia 3                | Ver imagen del producto                  |
| TC-05  | Historia 4                | Verificar versión de lista               |
| TC-06  | Historia 5                | Subir Excel con productos                |
| TC-07  | Historia 5                | Subir Excel inválido                     |
| TC-08  | Historia 6                | Reemplazar lista anterior                |
| TC-09  | Historia 7                | Subir imagen de producto                 |
| TC-10  | Historia 8                | Verificar campos requeridos              |
+--------+---------------------------+------------------------------------------+
