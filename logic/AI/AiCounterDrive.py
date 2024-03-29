from ultralytics import YOLO
import cv2
import cvzone
import math
from .sort import *
from pathlib import Path
from data.dataconnection import DataConnection

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class AiCountDrive:
    def __init__(self):
        self.running = False
        self.cap = cv2.VideoCapture(absPath('cars.mp4'))
        self.cap.set(3,1280)
        self.cap.set(4,720)

        self.model = YOLO('../yolo_weigths/yolov8l.pt')

        self.colours = [(255,56,56),(56,56,255),(56,255,56),(155,0,155)]

        self.classNames = ["persona", "bicycle", "auto", "moto", "aeroplane", "bus", "train", "camion", "boat",
            "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
            "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
            "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
            "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
            "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
            "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
            "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
            "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
            "teddy bear", "hair drier", "toothbrush"
            ]
        
        self.mask = cv2.imread(absPath("mask.png"))

        self.tracker_car = Sort(max_age=20, min_hits=3,iou_threshold=0.3)
        self.tracker_moto = Sort(max_age=20, min_hits=3,iou_threshold=0.3)
        self.tracker_bus = Sort(max_age=20, min_hits=3,iou_threshold=0.3)
        self.tracker_truck = Sort(max_age=20, min_hits=3,iou_threshold=0.3)

        self.limits = [200,347,673,347]

        self.car_count = []
        self.moto_count = []
        self.bus_count = []
        self.truck_count = []


        # Crear una instancia de DataConnection
        self.data_connection = DataConnection(absPath("../../data/AiCountDrive.db"))
        self.data_connection.check_database()
        self.data_connection.close_connection()

        # Asegurarse de que la base de datos y la tabla existen
        # self.data_connection.check_database()


    def connect_camera(self,connection):
        """
        Para conectar a una camara ip
        """
        self.cap = cv2.VideoCapture(connection)
        self.cap.set(3,1280)
        self.cap.set(4,720)


    def define_line(self,y1,y2,x):
        """Define la linea de conteo"""
        self.limits = [y1,x,y2,x]


    def stop_count(self):
        """ Detiene el conteo de vehiculos"""
        self.running = False


    def run_count(self):
        self.running = True
        while self.running:
            succes, self.img = self.cap.read() # captura un boleno y un frame
            img_region = cv2.bitwise_and(self.img,self.mask) # corto la region de la imagen

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            
            # imagen o grafico para volverlo mas chevere
            # img_graphics = cv2.imread("./graphics.png",cv2.IMREAD_UNCHANGED)
            # self.img = cvzone.overlayPNG(self.img,img_graphics,(0,0))
            
            results = self.model(img_region,stream=True)
            
            detections_car = np.empty((0,5))
            detections_moto = np.empty((0,5))
            detections_bus = np.empty((0,5))
            detections_truck = np.empty((0,5))
            
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1,y1,x2,y2=box.xyxy[0]
                    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
                    w, h = x2-x1,y2-y1
                    
                    #confidence
                    conf = math.ceil((box.conf[0]*100))/100
                    print(conf)
                    
                    # Class name
                    cls = int(box.cls[0])
                    currentClass = self.classNames[cls]
                    
                    match currentClass:
                        case "auto":
                            detections_car = self.select_class(detections_car,self.classNames[cls],conf,x1,x2,y1,y2,self.colours[0])
                        case "moto":
                            detections_moto = self.select_class(detections_moto,self.classNames[cls],conf,x1,x2,y1,y2,self.colours[1])
                        case "bus":
                            detections_bus =  self.select_class(detections_bus,self.classNames[cls],conf,x1,x2,y1,y2,self.colours[2])
                        case "camion":
                            detections_truck =  self.select_class(detections_truck,self.classNames[cls],conf,x1,x2,y1,y2,self.colours[3])
                        
                        
            results_tracker_car = self.tracker_car.update(detections_car)
            results_tracker_moto = self.tracker_moto.update(detections_moto)
            results_tracker_bus = self.tracker_bus.update(detections_bus)
            results_tracker_truck =  self.tracker_truck.update(detections_truck)
            cv2.line(self.img,(self.limits[0],self.limits[1]),(self.limits[2],self.limits[3]),(0,255,255),5)

            self.detection_count(results_tracker_car,self.car_count,self.colours[0],'auto')
            self.detection_count(results_tracker_moto,self.moto_count,self.colours[1],'moto')
            self.detection_count(results_tracker_bus,self.bus_count,self.colours[2],'bus')  
            self.detection_count(results_tracker_truck,self.truck_count,self.colours[3],'camion')  

            cv2.putText(self.img,str(len(self.car_count)),(255,100),cv2.FONT_HERSHEY_PLAIN,5,self.colours[0],8)
            cv2.putText(self.img,str(len(self.moto_count)),(455,100),cv2.FONT_HERSHEY_PLAIN,5,self.colours[1],8)
            cv2.putText(self.img,str(len(self.bus_count)),(655,100),cv2.FONT_HERSHEY_PLAIN,5,self.colours[2],8)
            cv2.putText(self.img,str(len(self.truck_count)),(855,100),cv2.FONT_HERSHEY_PLAIN,5,self.colours[3],8)
            
            cv2.imshow("Img", self.img)
            # cv2.imshow("ImgRegion", img_region)
            cv2.waitKey(1)


    def select_class(self,detections,class_name,conf,x1,x2,y1,y2,color=(0,0,0)):
        cvzone.putTextRect(self.img,f'{class_name}: {conf}',(max(0,x1),max(35,y1-10)),
                            scale=1,thickness=2,offset=3,colorR=color)
        current_array = np.array([x1,y1,x2,y2,conf])
        detections = np.vstack((detections,current_array))
        return detections


    def detection_count(self,results_tracker, count, color, object_type):
        """Esta funcion cuenta los objetos que pasan por la linea"""
        # mas tarde debo agregar un atributo type para añadirlos a la base de datos segun su tipo.
        for result in results_tracker:
            x1,y1,x2,y2,id = result
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            w, h = x2-x1,y2-y1
            cvzone.cornerRect(self.img,(x1,y1,w,h),l=10,rt=5, colorR=color, colorC=color)
            
            cx, cy = x1+w//2, y1+h//2
            cv2.circle(self.img,(cx,cy),5,color,cv2.FILLED)
            
            if self.limits[0] < cx < self.limits[2] and self.limits[1]-20 < cy < self.limits[1]+20:
                if count.count(id) == 0:
                    count.append(id)
                    cv2.line(self.img,(self.limits[0],self.limits[1]),(self.limits[2],self.limits[3]),(0,0,255),5)

                    # Para añadir a la base de datos
                    self.data_connection.open_connection()
                    self.data_connection.db.exec_(f"insert into vehicles (type) values('{object_type}')")
                    self.data_connection.db.commit()
                    self.data_connection.close_connection()

    def destroy_window(self):
        cv2.destroyAllWindows()



if __name__ == '__main__':
    pro =  AiCountDrive()
    pro.run_count()