# Importación de librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:
        # Creación de arreglos con numpy
        ventas_semana = np.array([150, 200, 170, 220, 300, 250, 190])
        print("Ventas por semana:", ventas_semana)
        
        # Operaciones con arreglos
        print("\nEstadísticas de ventas:")
        print("Promedio de ventas:", np.mean(ventas_semana))
        print("Ventas máxima:", np.max(ventas_semana))
        print("Ventas mínima:", np.min(ventas_semana))
        print("Desviación estándar:", np.std(ventas_semana))
        
        # Lectura de archivos CSV con pandas
        print("\nLeyendo archivo de ventas...")
        try:
            # Usar ruta relativa (el archivo debe estar en la misma carpeta que el script)
            datos_ventas = pd.read_csv("ventas.csv", encoding='utf-8')
            
            print("\nPrimeras 5 filas de datos:\n", datos_ventas.head())
            
            # Verificar columnas necesarias
            columnas_requeridas = {'Producto', 'Unidades Vendidas'}
            if not columnas_requeridas.issubset(datos_ventas.columns):
                print("\nError: El archivo CSV no contiene las columnas requeridas.")
                print("Columnas encontradas:", datos_ventas.columns.tolist())
                return
            
            # Visualización de datos con matplotlib
            plt.figure(figsize=(10, 6))
            plt.bar(datos_ventas['Producto'], 
                   datos_ventas['Unidades Vendidas'], 
                   color='skyblue')
            
            plt.title('Unidades Vendidas por Producto', fontsize=14)
            plt.xlabel('Producto', fontsize=12)
            plt.ylabel('Unidades Vendidas', fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            
            # Añadir valores encima de las barras
            for i, valor in enumerate(datos_ventas['Unidades Vendidas']):
                plt.text(i, valor + 0.5, str(valor), ha='center', va='bottom')
            
            plt.tight_layout()
            plt.show()
            
        except FileNotFoundError:
            print("\nError: No se encontró el archivo 'ventas.csv'")
            print("Asegúrate de que el archivo esté en la misma carpeta que este script.")
        except UnicodeDecodeError:
            print("\nError: Problema al leer el archivo. Intenta con encoding='latin-1'")
        except Exception as e:
            print(f"\nError inesperado al procesar el archivo CSV: {str(e)}")
            
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")

if __name__ == "__main__":
    main()