import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def split_rgb(image_name):
    # Caminho da imagem de entrada
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, '../../input_images', f'{image_name}.png')

    # Carrega a imagem
    img = cv2.imread(input_path)

    # Verifica se a imagem foi carregada corretamente
    if img is None:
        print(f"Erro: Imagem {image_name} não encontrada no caminho {input_path}.")
        return

    # Separação dos canais
    blue, green, red = cv2.split(img)

    # Caminho para salvar as imagens processadas
    output_path = os.path.join(current_dir, '../../output_images/')
    os.makedirs(output_path, exist_ok=True)

    # Salvando cada canal separadamente
    cv2.imwrite(os.path.join(output_path, f'{image_name}_red.png'), red)
    cv2.imwrite(os.path.join(output_path, f'{image_name}_green.png'), green)
    cv2.imwrite(os.path.join(output_path, f'{image_name}_blue.png'), blue)

    # Exibe os canais separados
    plt.figure(figsize=(10, 7))

    plt.subplot(1, 3, 1)
    plt.imshow(red, cmap="gray")
    plt.title('Canal Vermelho')

    plt.subplot(1, 3, 2)
    plt.imshow(green, cmap="gray")
    plt.title('Canal Verde')

    plt.subplot(1, 3, 3)
    plt.imshow(blue, cmap="gray")
    plt.title('Canal Azul')

    plt.show()

if __name__ == "__main__":
    # Lista das imagens para processamento
    image_names = ["img1", "img2", "img3"]
    
    # Processa cada imagem
    for image_name in image_names:
        split_rgb(image_name)
