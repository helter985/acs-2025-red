
# 📋 Test Plan - Lista de Precios

## 👥 Integrantes
- Enzo Mastrangelo  
- Santiago Navarro  
- Máximo Sat  
- Joaquín Piastrellini  

**Materia:** Aseguramiento de la Calidad de Software

---

## ✅ Document Approval

| Nombre                | Rol         | Fecha       | Aprobación |
|----------------------|-------------|-------------|------------|
| Máximo Rajbal Sat    | QA Lead     | 15/06/2025  | ✔ / ✘      |
| Enzo Mastrangelo      | Dev         | 15/06/2025  | ✔ / ✘      |
| Santiago Navarro     | Dev         | 15/06/2025  | ✔ / ✘      |
| Joaquín Piastrellini | Dev Lead    | 15/06/2025  | ✔ / ✘      |
| John Doe             | Cliente     | 15/06/2025  | ✔ / ✘      |

---

## 1. 📘 Introducción

### 1.1 Propósito
El propósito de este documento es definir el plan de pruebas para el sistema de consulta de precios desarrollado para una distribuidora de artículos de limpieza.

### 1.2 Alcance

**In Scope:**
- Funcionalidad: Validar que la app cargue precios, nombre, código e imagen de cada producto.
- Usabilidad: Pruebas en condiciones reales.
- Compatibilidad: Android y iOS con conexión permanente.
- UI: Claridad visual de la información.

**Out of Scope:**
- Seguridad.
- Performance.
- Hardware.
- Gestión de stock.
- Historial de listas.

### 1.3 Definiciones

| Término    | Definición                                                                 |
|------------|----------------------------------------------------------------------------|
| QA Lead    | Responsable de coordinar las pruebas.                                      |
| Dev Lead   | Responsable técnico del sistema.                                           |
| Dev        | Desarrollador.                                                             |
| Cliente    | Representante del negocio.                                                 |
| Vendedor   | Usuario final que consulta precios.                                        |
| Admin      | Carga listas semanalmente desde casa central.                              |

---

## 2. 📌 Requerimientos

### 2.1 Descripción de Roles

| Rol      | Descripción                                                                 |
|----------|------------------------------------------------------------------------------|
| Vendedor | Consulta precios desde celular (Android/iOS).                               |
| Admin    | Sube listas de precios semanalmente.                                         |
| Cliente  | Patrocinador del proyecto, valida entregables.                              |

### 2.2 Funcionalidades por Rol

**🧍 Vendedor**
- Buscar productos por nombre o código (barras o interno).
- Ver precio actual del producto.
- Visualizar imagen del producto.
- Verificar que la lista sea la más reciente.

**🧑‍💼 Admin**
- Subir listas de precios desde Excel.
- Mantener la versión vigente semanalmente.
- Cargar imágenes de productos.
- Verificar que cada producto tenga nombre, código, precio e imagen.

---