from PIL import Image
import sys
import os

def convert_to_ico(input_image, output_icon, sizes=[16, 32, 48, 64, 128, 256]):
    try:
        img = Image.open(input_image)
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        img.save(output_icon, format="ICO", sizes=[(size, size) for size in sizes])
        print(f"Icono creado exitosamente: {output_icon}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python convert_to_ico.py <imagen_entrada> <icono_salida>")
    else:
        input_image, output_icon = sys.argv[1], sys.argv[2]
        if not os.path.exists(input_image):
            print(f"Error: La imagen de entrada '{input_image}' no existe.")
        else:
            convert_to_ico(input_image, output_icon)
