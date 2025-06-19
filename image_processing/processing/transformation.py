# Importa a função resize do módulo transform da biblioteca scikit-image, usada para redimensionar imagens
from skimage.transform import resize

def resize_image(image, proportion):
    # Verifica se a proporção especificada está entre 0 e 1 (inclusive)
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1."
    # Calcula a nova altura da imagem arredondando o resultado para o número inteiro mais próximo
    height = round(image.shape[0] * proportion)
    # Calcula a nova largura da imagem arredondando o resultado para o número inteiro mais próximo
    width = round(image.shape[1] * proportion)
    # Redimensiona a imagem para a nova altura e largura, aplicando anti-aliasing para evitar serrilhamento
    image_resized = resize(image, (height, width), anti_aliasing=True)
    # Retorna a imagem redimensionada
    return image_resized