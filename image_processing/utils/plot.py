# Importa a biblioteca matplotlib.pyplot, que é usada para criar visualizações estáticas, animadas e interativas em Python.
import matplotlib.pyplot as plt

def plot_image(image):
    # Cria uma nova figura e um conjunto de eixos para o plot. O figsize define as dimensões da figura (largura=12 polegadas, altura=4 polegadas).
    plt.figure(figsize=(12, 4))
    # Exibe a imagem nos eixos. 'cmap='gray'' especifica o mapa de cores para exibir imagens em escala de cinza.
    plt.imshow(image, cmap='gray')
    # Desativa os eixos x e y para uma visualização mais limpa da imagem.
    plt.axis('off')
    # Mostra a figura na tela.
    plt.show()

def plot_result(*args):
    # Calcula o número de imagens passadas como argumento para a função.
    number_images = len(args)
    # Cria uma figura e um conjunto de subplots. Aqui, nrows=1 (uma linha) e ncols=number_images (número de colunas igual ao número de imagens).
    # figsize define o tamanho total da figura.
    fig, axis = plt.subplots(nrows=1, ncols = number_images, figsize=(12, 4))
    # Gera uma lista de nomes para as imagens, como 'Image 1', 'Image 2', etc.
    names_lst = ['Image {}'.format(i) for i in range(1, number_images)]
    # Adiciona o nome 'Result' ao final da lista de nomes, presumindo que a última imagem seja o resultado.
    names_lst.append('Result')
    # Itera sobre os eixos, nomes e imagens, emparelhando-os.
    for ax, name, image in zip(axis, names_lst, args):
        # Define o título de cada subplot como o nome correspondente.
        ax.set_title(name)
        # Exibe a imagem no subplot atual, usando o mapa de cores 'gray'.
        ax.imshow(image, cmap='gray')
        # Desativa os eixos x e y para o subplot atual.
        ax.axis('off')
    # Ajusta automaticamente os parâmetros do subplot para que os subplots se encaixem perfeitamente na área da figura.
    fig.tight_layout()
    # Mostra a figura com todos os subplots.
    plt.show()

def plot_histogram(image):
    # Cria uma figura e um conjunto de 3 subplots em uma linha (um para cada canal de cor).
    # sharex=True e sharey=True garantem que os eixos x e y sejam compartilhados entre os subplots.
    fig, axis = plt.subplots(nrows=1, ncols = 3, figsize=(12, 4), sharex=True, sharey=True)
    # Define uma lista de cores para os histogramas (vermelho, verde, azul).
    color_lst = ['red', 'green', 'blue']
    # Itera com o índice e os pares de eixo/cor.
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        # Define o título de cada subplot como o nome da cor (ex: 'Red Histogram').
        ax.set_title('{} histogram'.format(color.title()))
        # Plota o histograma para o canal de cor correspondente.
        # image[:, :, index].ravel() achata o array do canal de cor em 1D.
        # bins=256 define 256 'caixas' para o histograma (tipicamente para valores de pixel de 0 a 255).
        # color define a cor das barras e alpha define a transparência.
        ax.hist(image[:, :, index].ravel(), bins = 256, color = color, alpha = 0.8)
    # Ajusta automaticamente os parâmetros do subplot para que os subplots se encaixem perfeitamente na área da figura.
    fig.tight_layout()
    # Mostra a figura com todos os histogramas.
    plt.show()