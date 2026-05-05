# data-normalizer-etl
Data Normalizer Pipeline: Legacy to JSON 🔄
📌 Descripción del Proyecto
Script ETL (Extract, Transform, Load) desarrollado en Python para automatizar la migración, auditoría y limpieza de registros bibliográficos exportados desde un sistema legacy a un formato estructurado moderno (JSON).

Este proyecto demuestra la aplicación de principios de Arquitectura de Información mediante código, transformando datos estáticos en estructuras dinámicas listas para la Web Semántica, bases de datos de grafos o sistemas RAG.

🚧 El Desafío
Las exportaciones masivas de sistemas legacy suelen presentar inconsistencias críticas que rompen las bases de datos modernas:

Conflictos de codificación (ANSI/Latin-1 vs UTF-8).

Inyección de metadatos anómalos en cabeceras (sep=;).

Campos repetibles colapsados en cadenas de texto plano.

Columnas fantasma sin datos estructurados.

🏗️ Metodología y Estructura del Repositorio
El pipeline está dividido en dos fases lógicas:

1. Análisis Exploratorio (01_diagnostico.py)
Script de auditoría inicial que mapea la base cruda. Detecta tipos de datos, contabiliza valores nulos y expone problemas de delimitadores antes de realizar cualquier transformación, evitando la corrupción de datos.

2. Pipeline de Normalización (02_normalizador.py)
El motor principal que ejecuta las transformaciones de curaduría:

Limpieza Estructural: Purga de variables 100% nulas.

Normalización de Keys: Conversión de etiquetas a estándar snake_case garantizando interoperabilidad.

Jerarquización Semántica: División de descriptores planos en listas iterables reales.

Exportación de Alta Precisión: Uso de la librería nativa de JSON para evitar el escapado innecesario de caracteres en URLs y directorios.

💻 Tecnologías Utilizadas
Lenguaje: Python 3.x

Librerías: Pandas (Manipulación de DataFrames), JSON (Estructuración final)

🚀 Cómo ejecutarlo localmente
1. Clonar el repositorio.

2. Instalar dependencias requeridas:
pip install pandas

3. Ejecutar el diagnóstico de la base cruda:
python 01_diagnostico.py

4. Correr la normalización final:
python 02_normalizador.py
