import pandas as pd

# 1. Carga del archivo
# Usamos 'latin1' o 'utf-8-sig' por si el export del sistema legacy tiene caracteres especiales (ñ, tildes)
try:
    nombre_archivo = 'resultados-inti.csv'
    df = pd.read_csv(nombre_archivo, encoding='latin1', sep=';', on_bad_lines='skip')
    
    print(f"✅ Archivo '{nombre_archivo}' cargado con éxito.\n")
    
    # 2. Inspección Estructural (El "Mapa del Tesoro")
    print("--- ESTRUCTURA DE LAS COLUMNAS ---")
    print(df.info()) # Muestra nombres de columnas y tipos de datos (objeto, int, float)
    
    print("\n--- VISTA PREVIA (Primeros 5 registros) ---")
    print(df.head())
    
    # 3. Diagnóstico de Datos Faltantes
    print("\n--- VALORES NULOS POR COLUMNA ---")
    print(df.isnull().sum())
    
    # 4. Conteo de registros
    print(f"\nTotal de registros encontrados: {len(df)}")

except FileNotFoundError:
    print("❌ Error: No encontré el archivo 'resultados-inti.csv'. Asegurate de que esté en la misma carpeta que este script.")
except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")