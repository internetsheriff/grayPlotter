import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter import filedialog

# abre a imagem com uma caixa de dialogo 
Tk().withdraw()
imagename = filedialog.askopenfilename(title='Selecionar Imagem')
original_image = cv2.imread(imagename)

# redimensiona a imagem, mantendo a razão de aspecto
image = imutils.resize(original_image, width=300)

# gera uma imagem em grayscale para obter a intensidade dos pixels
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cria uma janela para mostrar a imagem
cv2.imshow('Imagem', image)

# variavel global para manter coordenadas
coordenadas = []


# plota os valores de intensidade da luz (grayscale) em uma linha escolhida
def plotLineGrayscale(event, x, y, flags, parameters):
	global coordenadas

	# grava coordenadas ao pressionar o botão esquerdo
	if event == cv2.EVENT_LBUTTONDOWN:
		coordenadas = [(x, y)]

	# grava coordenadas ao soltar o botão esquerdo, desenha a linha e plota a intensidade de luz
	elif event == cv2.EVENT_LBUTTONUP:
		coordenadas.append((x, y))

		# mostra linha selecionada na imagem
		cv2.line(image, coordenadas[0], coordenadas[1], (255,255,0), 2)
		cv2.imshow("Imagem", image)

		# gera um array de valores entre os dois pontos 
		linha = []
		pt_a = np.array(coordenadas[0])
		pt_b = np.array(coordenadas[1])
		for p in np.linspace(pt_a, pt_b, 30):
			pixel = grayscale[tuple(np.int32(p))[1], tuple(np.int32(p))[0]]
			linha.append(pixel)

		# plota o perfil de intensidade luminosa
		plt.title('Perfil de intensidade luminosa')
		plt.xlabel("Distância")
		plt.ylabel("Intensidade")
		plt.plot(linha)
		plt.get_current_fig_manager().set_window_title('Perfil de intensidade luminosa')
		plt.show()

cv2.setMouseCallback('Imagem', plotLineGrayscale)

# adiciona wait key
cv2.waitKey(0)
# fecha janelas
cv2.destroyAllWindows()