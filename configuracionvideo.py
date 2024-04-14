import cv2


# Clase que crea una captura de video mediante opencv
class Configuracionvideo:
    def __init__(self):
        self.camara = 0

    # Se le pregunta al usuario por consola la camara a utilizar
    def video(self):
        print("Inicializando Video")
        camara = int(input("Ingrese la cámara:\n"
                           "0 - Portátil\n"
                           "1 - Webcam\n"
                           ))
        self.camara = camara
        cap = cv2.VideoCapture(camara)
        while True:
            ret, frame = cap.read()
            cv2.imshow("VIDEO CAPTURA", frame)
            t = cv2.waitKey(1)
            # ESC para salir
            if t == 27:
                break
        cap.release()
        cv2.destroyAllWindows()


v = Configuracionvideo()
v.video()
