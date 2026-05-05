import pandas as pd
import json

print("🚀 Iniciando Prueba de Estrés del Pipeline ETL...")

# Definí el nombre de tu archivo nuevo acá:
archivo_entrada = '2resultados-inti.csv'

# 1. EXTRACCIÓN
# Agregamos skiprows=1 para saltar la trampa de 'sep=' que inyecta el sistema legacy
try:
    df = pd.read_csv(archivo_entrada, encoding='latin1', sep=';', on_bad_lines='skip', skiprows=1)
    print(f"📊 Registros iniciales extraídos exitosamente: {len(df)}")
except FileNotFoundError:
    print(f"❌ Error: No se encontró el archivo '{archivo_entrada}'.")
    exit()

# 2. TRANSFORMACIÓN
# A) Borrar basura
df = df.dropna(axis=1, how='all')

# B) Normalizar Claves
df.columns = df.columns.str.lower()
# Solo renombramos las columnas si existen en este nuevo export
columnas_a_renombrar = {
    'título': 'titulo',
    'año': 'anio',
    'autor institucional': 'autor_institucional',
    'reunión': 'reunion',
    'código doc': 'codigo_doc'
}
df.rename(columns={k: v for k, v in columnas_a_renombrar.items() if k in df.columns}, inplace=True)

# C) Rellenar agujeros
df = df.fillna("")

# D) Estructurar campos repetibles
if 'descriptores' in df.columns:
    df['descriptores'] = df['descriptores'].apply(
        lambda x: [termino.strip() for termino in str(x).split(';') if termino.strip()]
    )

# 3. CARGA
nombre_salida = 'catalogo_masivo.json'
registros_dict = df.to_dict(orient='records')

with open(nombre_salida, 'w', encoding='utf-8') as archivo:
    json.dump(registros_dict, archivo, ensure_ascii=False, indent=4)

print(f"✅ ¡Éxito total! Base procesada.")
print(f"📁 Se guardaron {len(registros_dict)} registros impecables en '{nombre_salida}'")