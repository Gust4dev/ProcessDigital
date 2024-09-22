import cv2
import os

def preprocess_image(image_path, output_path):
    # Carrega a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        raise ValueError(f"Erro ao carregar a imagem {image_path}")
    
    # Aplicar equalização de histograma para melhorar o contraste
    processed_image = cv2.equalizeHist(image)
    
    # Salvar a imagem pré-processada
    cv2.imwrite(output_path, processed_image)
    
    print(f"Imagem pré-processada salva em {output_path}")

if __name__ == "__main__":
    input_image = os.path.join("input_images", "sua_imagem.png")
    output_image = os.path.join("output_images", "preprocessed_image.png")
    
    preprocess_image(input_image, output_image)
