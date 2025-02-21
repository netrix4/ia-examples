import cv2
import easyocr
import matplotlib.pyplot as plt


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

def reconocerTexto(imagen):
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    lector = easyocr.Reader(["es", "en"])

    # Leer texto de la imagen
    resultado = lector.readtext(imagen_rgb)

    # Mostrar resultados
    print("Texto extraído de la imagen:")
    for bbox, texto, prob in resultado:
        print(f"{texto} (Confianza: {prob:.2f})")

        # Dibujar el cuadro delimitador en la imagen
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = bbox
        cv2.rectangle(imagen_rgb, (int(x0), int(y0)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(
            imagen_rgb,
            texto,
            (int(x0), int(y0) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2,
        )
    plt.imshow(imagen_rgb)
    plt.axis("off")
    plt.show()


def mostrarImagen(imagen):

    imagenOriginal = cv2.imread(image_path)
    recorrerPixeles(imagen)

    cv2.imshow('Imagen por parametro', imagen)
    cv2.imshow('Imagen por original', imagenOriginal)

def mostrarImagenMatPlot(imagen):
    
    imagenOriginal = cv2.imread(image_path)
    imagenOriginal_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    recorrerPixeles(imagen)

    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    plt.imshow(imagen_rgb)
    plt.axis("off")
    plt.show()

    plt.imshow(imagenOriginal_rgb)
    plt.axis("off")
    plt.show()

if __name__ == '__main__':

    image_path = 'assets/stop.jpg'
    imagen = cv2.imread(image_path)

    # mostrarImagen(imagen)

    reconocerTexto(imagen)
    mostrarImagenMatPlot(imagen)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    