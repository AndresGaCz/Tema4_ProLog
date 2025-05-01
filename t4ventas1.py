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
            
            # Agregar columna de Ventas Totales (Unidades Vendidas * Precio Unitario)
            datos_ventas['Ventas Totales'] = datos_ventas['Unidades Vendidas'] * datos_ventas['Precio Unitario']
            
            print("\nDatos con columna de Ventas Totales agregada:")
            print(datos_ventas.head())
            
            # Verificar columnas necesarias
            columnas_requeridas = {'Producto', 'Unidades Vendidas'}
            if not columnas_requeridas.issubset(datos_ventas.columns):
                print("\nError: El archivo CSV no contiene las columnas requeridas.")
                print("Columnas encontradas:", datos_ventas.columns.tolist())
                return
            
            # Gráfico de barras con nuevos colores
            plt.figure(figsize=(10, 6))
            colores_barras = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Colores de la paleta 'tab10'
            barras = plt.bar(datos_ventas['Producto'], 
                           datos_ventas['Unidades Vendidas'], 
                           color=colores_barras)
            
            plt.title('Unidades Vendidas por Producto', fontsize=14)
            plt.xlabel('Producto', fontsize=12)
            plt.ylabel('Unidades Vendidas', fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            
            # Añadir valores encima de las barras
            for barra in barras:
                height = barra.get_height()
                plt.text(barra.get_x() + barra.get_width()/2., height,
                        f'{int(height)}',
                        ha='center', va='bottom')
            
            plt.tight_layout()
            plt.show()
            
            # Gráfico de pastel con proporción de unidades vendidas
            plt.figure(figsize=(8, 8))
            colores_pastel = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
            explode = (0.05, 0.05, 0.05, 0.05)  # Separar ligeramente las porciones
            
            plt.pie(datos_ventas['Unidades Vendidas'],
                   labels=datos_ventas['Producto'],
                   autopct='%1.1f%%',
                   startangle=90,
                   colors=colores_pastel,
                   explode=explode,
                   shadow=True,
                   textprops={'fontsize': 12})
            
            plt.title('Proporción de Unidades Vendidas por Producto', fontsize=14, pad=20)
            plt.axis('equal')  # Para que el pastel sea circular
            plt.tight_layout()
            plt.show()
            
            # Mostrar tabla con ventas totales
            print("\nResumen de Ventas Totales:")
            print(datos_ventas[['Producto', 'Unidades Vendidas', 'Precio Unitario', 'Ventas Totales']])
            
            # Calcular y mostrar el total general de ventas
            total_ventas = datos_ventas['Ventas Totales'].sum()
            print(f"\nTotal general de ventas: ${total_ventas:,.2f}")
            
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