import re
from pathlib import Path
import argparse
import shutil
import os
import pandas as pd
from dateutil import parser


DATA_PATH = Path("Machine_Learning/Calendarizacion de Transportes/Consolidado de Transporte.txt")
OUT_PATH = DATA_PATH.with_name(DATA_PATH.stem + "_normalized_preview.csv")


def try_parse_date(x):
    if x is None:
        return pd.NaT
    s = str(x).strip()
    if s == "":
        return pd.NaT

    # Common numeric pattern dd-mm-yyyy or d-m-yyyy
    if re.match(r"^\d{1,2}-\d{1,2}-\d{4}$", s):
        return pd.to_datetime(s, dayfirst=True, format="%d-%m-%Y", errors="coerce")

    # If uses slashes, convert to dashes and try
    if re.match(r"^\d{1,2}/\d{1,2}/\d{4}$", s):
        return pd.to_datetime(s.replace("/","-"), dayfirst=True, errors="coerce")

    # If looks like Excel serial (integer-ish and in plausible range)
    if re.match(r"^\d+$", s):
        try:
            n = int(s)
            if 2000 <= n <= 50000:  # plausible Excel serials (e.g., 44000+)
                return pd.to_datetime(n, unit='D', origin='1899-12-30', errors='coerce')
        except Exception:
            pass

    # Translate Spanish month names to English (helps dateutil parse)
    s_low = s.lower()
    months_map = {
        'enero':'January','febrero':'February','marzo':'March','abril':'April',
        'mayo':'May','junio':'June','julio':'July','agosto':'August',
        'septiembre':'September','setiembre':'September','octubre':'October',
        'noviembre':'November','diciembre':'December'
    }
    for sp, en in months_map.items():
        if sp in s_low:
            # replace case-insensitively
            s = re.sub(sp, en, s, flags=re.IGNORECASE)
            break

    # Last resort: dateutil parser with dayfirst
    try:
        dt = parser.parse(s, dayfirst=True, fuzzy=True)
        return pd.to_datetime(dt)
    except Exception:
        return pd.NaT


def main():
    parser_arg = argparse.ArgumentParser(description='Normaliza Fecha Expedicion. Use --apply para sobrescribir el archivo original y borrar el preview.')
    parser_arg.add_argument('--apply', action='store_true', help='Sobrescribe el archivo original con la columna normalizada y borra el CSV preview')
    args = parser_arg.parse_args()

    print(f"Leyendo: {DATA_PATH}")
    # Archivo contiene caracteres acentuados; usar latin-1 / cp1252 para evitar UnicodeDecodeError
    df = pd.read_csv(DATA_PATH, sep='\t', dtype=str, engine='python', keep_default_na=False, encoding='latin-1')

    col_candidates = [c for c in df.columns if 'Fecha' in c or 'Exped' in c]
    if not col_candidates:
        print("No encontré columna con 'Fecha' o 'Exped' en el header. Columnas disponíbles:")
        print(list(df.columns))
        return

    fecha_col = col_candidates[0]
    print(f"Usando columna: {fecha_col}\n")

    unique_vals = pd.Series(df[fecha_col].astype(str).unique())
    print(f"Total filas: {len(df)}")
    print(f"Valores únicos en {fecha_col}: {len(unique_vals)} (muestro hasta 30):\n")
    print(unique_vals.head(30).to_list())

    parsed = df[fecha_col].apply(try_parse_date)
    parsed_count = parsed.notna().sum()
    print(f"\nFechas parseadas correctamente: {parsed_count} / {len(df)}")

    # Mostrar ejemplos fallidos
    failed_idx = parsed[parsed.isna()].index[:20]
    if len(failed_idx):
        print("\nEjemplos no parseados (hasta 20):")
        for i in failed_idx:
            print(f"- fila {i+1}: '{df.loc[i, fecha_col]}'")
    else:
        print("\nNo hay valores fallidos de parseo.")

    # Añadir columna normalizada y guardar muestra
    df['Fecha_Expedicion_normalizada'] = parsed.dt.strftime('%Y-%m-%d')
    # Keep original rows order; save a preview to OUT_PATH
    preview = df.copy()
    preview.to_csv(OUT_PATH, index=False)
    print(f"\nArchivo de salida guardado en: {OUT_PATH} (completa con columna 'Fecha_Expedicion_normalizada')")

    if args.apply:
        # Crear backup antes de sobrescribir
        backup_path = DATA_PATH.with_name(DATA_PATH.stem + "_backup" + DATA_PATH.suffix)
        print(f"Creando backup en: {backup_path}")
        shutil.copy2(DATA_PATH, backup_path)

        # Reemplazar la columna original con la normalizada (vacíos donde no se pudo parsear)
        df[fecha_col] = df['Fecha_Expedicion_normalizada'].fillna('')

        # Eliminar columna auxiliar si existe
        if 'Fecha_Expedicion_normalizada' in df.columns:
            df = df.drop(columns=['Fecha_Expedicion_normalizada'])

        # Guardar con mismo formato (tab) y encoding
        df.to_csv(DATA_PATH, sep='\t', index=False, encoding='latin-1')
        print(f"Archivo original sobrescrito: {DATA_PATH}")

        # Borrar el archivo preview si existe
        try:
            if OUT_PATH.exists():
                os.remove(OUT_PATH)
                print(f"Archivo preview eliminado: {OUT_PATH}")
        except Exception as e:
            print(f"No pude borrar el preview: {e}")


if __name__ == '__main__':
    main()
