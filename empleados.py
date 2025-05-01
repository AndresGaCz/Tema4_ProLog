# Importación de librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:
        # Parte 1: Análisis de productividad con numpy
        productividad_semanal = np.array([75, 80, 90, 85, 70])
        print("Productividad semanal:", productividad_semanal)
        
        print("\nEstadísticas de productividad:")
        print("Promedio de productividad:", np.mean(productividad_semanal))
        print("Productividad máxima:", np.max(productividad_semanal))
        print("Productividad mínima:", np.min(productividad_semanal))
        print("Desviación estándar:", np.std(productividad_semanal))
        
        # Parte 2: Análisis de empleados con pandas
        print("\nLeyendo archivo de empleados...")
        try:
            # Intentar con diferentes codificaciones comunes
            encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
            
            for encoding in encodings:
                try:
                    # Lectura del archivo CSV
                    empleados = pd.read_csv("empleados.csv", encoding=encoding)
                    print(f"\nArchivo leído correctamente con encoding: {encoding}")
                    break
                except UnicodeDecodeError:
                    continue
            else:
                print("\nError: No se pudo leer el archivo con ninguno de los encodings probados")
                return
            
            print("\nPrimeras 5 filas de datos:\n", empleados.head())
            
            # Verificación de columnas necesarias
            columnas_requeridas = {'Nombre', 'Departamento', 'Salario'}
            if not columnas_requeridas.issubset(empleados.columns):
                print("\nError: El archivo CSV no contiene las columnas requeridas.")
                print("Columnas encontradas:", empleados.columns.tolist())
                return
            
            # Filtrado de empleados de Ventas
            empleados_ventas = empleados[empleados['Departamento'].str.contains('Ventas')]
            print("\nEmpleados del departamento de Ventas:")
            print(empleados_ventas[['Nombre', 'Departamento']].to_string(index=False))
            
            # Cálculo del bono (10% del salario)
            empleados['Bono'] = empleados['Salario'] * 0.10
            print("\nDataFrame con columna de Bono agregada:")
            print(empleados.head())
            
            # Visualización de datos con matplotlib
            plt.figure(figsize=(14, 7))
            barras = plt.bar(empleados['Nombre'], 
                           empleados['Salario'], 
                           color='skyblue')
            
            plt.title('Salarios de Empleados', fontsize=16)
            plt.xlabel('Nombre del Empleado', fontsize=12)
            plt.ylabel('Salario ($)', fontsize=12)
            plt.xticks(rotation=90, ha='right', fontsize=8)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            
            # Añadir valores encima de las barras
            for barra in barras:
                height = barra.get_height()
                plt.text(barra.get_x() + barra.get_width()/2., height,
                        f'{int(height)}',
                        ha='center', va='bottom', fontsize=8)
            
            plt.tight_layout()
            plt.show()
            
        except FileNotFoundError:
            print("\nError: No se encontró el archivo 'empleados.csv'")
            print("Asegúrate de que:")
            print("1. El archivo existe en la misma carpeta que este script")
            print("2. El nombre del archivo es exactamente 'empleados.csv'")
            print("3. La extensión del archivo es .csv y no .xlsx u otro formato")
        except Exception as e:
            print(f"\nError inesperado al procesar el archivo CSV: {str(e)}")
            
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")

if __name__ == "__main__":
    main()