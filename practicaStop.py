import cv2
import easyocr

# Cargar la imagen

def recorrerPixeles(imagen):
    ancho, alto, canales = imagen.shape
    print("Dimensiones de la imagen: ", alto, ancho)

    for x in range(0, alto):
        for y in range(0, ancho):

            #Esta en bgr en lugar de rgb
            blue, green, red = imagen[y,x][0], imagen[y,x][1], imagen[y,x][2]
            isRedOk = (100 < red and red < 175 ) 
            isGreenOk = (green < 30)
            isBlueOk = (25 < blue and blue < 55)

            isTheRightColor = isRedOk and isGreenOk and isBlueOk

            if (not isTheRightColor):
                imagen[y,x] = [0,0,0]

def reconocerTexto():
    print('Reconocer texto')

     

def mostrarImagen(imagen):

    imagenOriginal = cv2.imread(image_path)
    recorrerPixeles(imagen)

    cv2.imshow('Imagen por parametro', imagen)
    cv2.imshow('Imagen por original', imagenOriginal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':

    image_path = 'stop.jpg'
    imagen = cv2.imread(image_path)

    mostrarImagen(imagen)

    reconocerTexto(imagen)


    