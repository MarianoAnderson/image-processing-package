# Importa as funções imread (para ler imagens) e imsave (para salvar imagens) do módulo io da biblioteca scikit-image
from skimage.io import imread, imsave

def read_image(path, is_gray = False):
    # Lê a imagem do caminho especificado. O parâmetro 'as_gray' determina se a imagem será lida em escala de cinza.
    image = imread(path, as_gray = is_gray)
    # Retorna a imagem lida
    return image

def save_image(image, path):
    # Salva a imagem no caminho especificado
    imsave(path, image)