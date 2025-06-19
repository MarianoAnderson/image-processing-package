# Importa a biblioteca NumPy, fundamental para operações numéricas e manipulação de arrays
import numpy as np
# Importa a função rgb2gray do módulo color da biblioteca scikit-image, usada para converter imagens RGB para escala de cinza
from skimage.color import rgb2gray
# Importa a função match_histograms do módulo exposure da biblioteca scikit-image, utilizada para fazer a correspondência de histogramas entre imagens
from skimage.exposure import match_histograms
# Importa a função structural_similarity do módulo metrics da biblioteca scikit-image, usada para calcular a similaridade estrutural entre duas imagens
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    # Verifica se as duas imagens têm a mesma forma (dimensões)
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."
    # Converte a primeira imagem de RGB para escala de cinza
    gray_image1 = rgb2gray(image1)
    # Converte a segunda imagem de RGB para escala de cinza
    gray_image2 = rgb2gray(image2)
    # Calcula a similaridade estrutural entre as duas imagens em escala de cinza e retorna o score e a imagem de diferença
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    # Imprime o score de similaridade das imagens
    print("Similarity of the images:", score)
    # Normaliza a imagem de diferença para que seus valores fiquem entre 0 e 1
    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))
    # Retorna a imagem de diferença normalizada
    return normalized_difference_image

def transfer_histogram(image1, image2):
    # Realiza a correspondência de histograma da image1 para a image2, preservando os múltiplos canais de cor
    matched_image = match_histograms(image1, image2, multichannel=True)
    # Retorna a imagem com o histograma correspondido
    return matched_image