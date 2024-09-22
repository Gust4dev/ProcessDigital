import cv2
import numpy as np
import os

def analyze_image(image_path):
    # Carrega a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        raise ValueError(f"Erro ao carregar a imagem {image_path}")
    
    # Usar detecção de bordas (Canny) para destacar regiões de interesse
    edges = cv2.Canny(image, 100, 200)
    
    # Encontrar contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Criar uma imagem em branco para desenhar os contornos
    contour_image = np.zeros_like(image)
    cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 1)
    
    # Salvar a imagem com contornos
    output_image_path = os.path.join("output_images", "contours_image.png")
    cv2.imwrite(output_image_path, contour_image)
    
    print(f"Análise de imagem concluída. Imagem salva em {output_image_path}")

if __name__ == "__main__":
    input_image = os.path.join("output_images", "preprocessed_image.png")
    analyze_image(input_image)
