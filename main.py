from rembg import remove
from PIL import Image
import sys

def remove_background(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img_no_bg = remove(img)
            img_no_bg.save(output_path, "PNG")
            print(f"Imagem salva sem fundo em: {output_path}")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python remove_bg.py <input_image> <output_image>")
    else:
        input_image = sys.argv[1]
        output_image = sys.argv[2]
        remove_background(input_image, output_image)
