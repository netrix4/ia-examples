import cv2

# Cargar las imágenes
img1 = cv2.imread('fuego.jpg')
img2 = cv2.imread('stop.jpg')

# Mostrar las imágenes en dos ventanas separadas
cv2.imshow('Imagen 1', img1)
cv2.imshow('Imagen 2', img2)

# Esperar una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
