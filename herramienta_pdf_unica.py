import PyPDF2
import os

# --- FUNCIONES DE MANIPULACIÓN (MODIFICADAS) ---

def extraer_una_pagina():
    """Extrae una página específica de un PDF."""
    print("\n--- [1] EXTRAER PÁGINA ÚNICA ---")
    
    # PEDIMOS LA RUTA COMPLETA O RELATIVA
    full_input_path = input("Ruta completa o relativa del PDF de origen (ej: C:\\docs\\archivo.pdf): ").strip()

    if not os.path.exists(full_input_path):
        print(f"❌ Error: Archivo '{full_input_path}' no encontrado.")
        return

    try:
        pg_number = input("¿Qué página te gustaría extraer?: ")
        page_index = int(pg_number) - 1 # PyPDF2 usa índice base 0
        
        with open(full_input_path, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            
            if 0 <= page_index < len(pdf_reader.pages):
                page_obj = pdf_reader.pages[page_index]
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(page_obj)
                
                output_file_name = input ("Nombrá el nuevo archivo PDF de salida (ej: resultado.pdf): ").strip()
                
                with open(output_file_name, 'wb') as pdf_output_file:
                    pdf_writer.write(pdf_output_file)
                
                print(f"\n✅ ¡Éxito! La página {pg_number} ha sido extraída a '{output_file_name}'.")
            else:
                print(f"❌ Error: La página {pg_number} está fuera del rango (El PDF tiene {len(pdf_reader.pages)} páginas).")

    except ValueError:
        print("❌ Error: Debes ingresar números enteros para las páginas.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

def extraer_rango_paginas():
    """Extrae un rango de páginas de un PDF."""
    print("\n--- [2] EXTRAER RANGO DE PÁGINAS ---")

    # PEDIMOS LA RUTA COMPLETA O RELATIVA
    full_input_path = input("Ruta completa o relativa del PDF de origen (ej: C:\\docs\\archivo.pdf): ").strip()

    if not os.path.exists(full_input_path):
        print(f"❌ Error: Archivo '{full_input_path}' no encontrado.")
        return
    
    try:
        start_page = int(input("¿Desde qué página (número inicial) te gustaría extraer?: "))
        end_page = int(input("¿Hasta qué página (número final) te gustaría extraer?: "))

        with open(full_input_path, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

            start_index = start_page - 1
            end_index = end_page

            if start_index < 0 or end_index > len(pdf_reader.pages) or start_index >= end_index:
                print(f"\n❌ Error: Rango de páginas inválido. El PDF tiene {len(pdf_reader.pages)} páginas.")
            else:
                pdf_writer = PyPDF2.PdfWriter()
                
                for page_num in range(start_index, end_index):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                output_file_name = input("\nNombrá el nuevo archivo PDF para el rango (ej: resultado.pdf): ").strip()
                
                with open(output_file_name, 'wb') as pdf_output_file:
                    pdf_writer.write(pdf_output_file)
                
                print(f"\n✅ ¡Éxito! Páginas {start_page} a {end_page} extraídas a '{output_file_name}'.")

    except ValueError:
        print("❌ Error: Debes ingresar números enteros para las páginas.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")


def fusionar_pdfs():
    """Fusiona múltiples archivos PDF en uno solo."""
    print("\n--- [3] FUSIONAR MÚLTIPLES PDFS ---")
    pdf_merger = PyPDF2.PdfMerger()
    input_files = []
    
    print("Ingresa la ruta completa de cada PDF a fusionar (ej: C:\\docs\\file.pdf). Escribe 'fin' cuando termines.")
    
    while True:
        full_path = input("Ruta completa de PDF a añadir: ").strip()
        
        if full_path.lower() in ('fin', 'listo', 'quit', ''):
            break
        
        # Validación de que la ruta exista
        if os.path.exists(full_path):
            input_files.append(full_path)
            print(f"✔️ '{full_path}' agregado.")
        else:
            print(f"❌ Error: '{full_path}' no encontrado. Verifica la ruta.")

    if len(input_files) < 2:
        print("⚠️ Se necesitan al menos dos archivos para fusionar. Cancelando.")
        return

    try:
        for pdf_path in input_files:
            pdf_merger.append(pdf_path)

        output_file_name = input("\nNombrá el nuevo archivo PDF combinado (ej: LibroCompleto.pdf): ").strip()
        
        with open(output_file_name, 'wb') as output_file:
            pdf_merger.write(output_file)
        
        print(f"\n✅ ¡Éxito! Archivos combinados en '{output_file_name}'.")

    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado durante la fusión: {e}")
    finally:
        pdf_merger.close()

# --- MENÚ PRINCIPAL (SIN CAMBIOS) ---

def menu_principal():
    """Muestra el menú y gestiona las opciones del usuario."""
    while True:
        print("\n====================================")
        print("    HERRAMIENTA PDF TODO-EN-UNO")
        print("====================================")
        print("Selecciona la tarea a realizar:")
        print("1: Extraer una página única de un PDF")
        print("2: Extraer un rango de páginas de un PDF")
        print("3: Fusionar múltiples PDFs")
        print("4: Salir de la aplicación")
        
        choice = input("\nIngresa el número de la opción deseada: ")
        
        if choice == '1':
            extraer_una_pagina()
        elif choice == '2':
            extraer_rango_paginas()
        elif choice == '3':
            fusionar_pdfs()
        elif choice == '4':
            print("\n¡Gracias por usar la herramienta! Adiós.")
            break
        else:
            print("\n⚠️ Opción no válida. Por favor, ingresa un número del 1 al 4.")

if __name__ == "__main__":
    menu_principal()