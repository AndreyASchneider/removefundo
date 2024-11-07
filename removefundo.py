import os
os.environ["NUMBA_DISABLE_JIT"] = "1"  # Desativa o JIT do numba

from rembg import remove
from PIL import Image
import io

# Abra a imagem e converta para bytes
with open("imgfundo.png", "rb") as input_file:
    img_data = input_file.read()

# Remove o fundo e converte para uma imagem PIL
output_data = remove(img_data)
output_img = Image.open(io.BytesIO(output_data))

# Salva a imagem de saída
output_img.save('img1.png')
