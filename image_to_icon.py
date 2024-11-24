from PIL import Image
import sys
import os

def convert_to_ico(input_image, output_icon, sizes=[16, 32, 48, 64, 128, 256]):
    try:
        # Abre la imagen de entrada
        img = Image.open(input_image)

        # Convierte la imagen a modo RGBA si no está en un formato compatible
        if img.mode != "RGBA":
            img = img.convert("RGBA")

        # Guarda la imagen como archivo .ico con los tamaños especificados
        img.save(output_icon, format="ICO", sizes=[(size, size) for size in sizes])
        print(f"Icono creado exitosamente: {output_icon}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python convert_to_ico.py <imagen_entrada> <icono_salida>")
    else:
        input_image = sys.argv[1]
        output_icon = sys.argv[2]

        # Verifica que el archivo de entrada exista
        if not os.path.exists(input_image):
            print(f"Error: La imagen de entrada '{input_image}' no existe.")
        else:
            convert_to_ico(input_image, output_icon)
