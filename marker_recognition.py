import cv2 as cv2
import cv2.aruco as aruco
import enum 

class ScalingMode(enum.Enum): 
    PERCENTAGE = 1
    FIX_SIZE = 2

## Constant parameters
ARUCO_PARAMETERS = aruco.DetectorParameters_create()
ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_4X4_100)


SCALING_PERCENT = 40
FIX_WIDTH = 1280
FIX_HEIGHT = 960

## ________________________________________________________________________

## Program
def marker_recognition(input_img, scalingMode):
    image = cv2.imread(input_img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # resize image
    if (scalingMode == ScalingMode.PERCENTAGE):    
        width = int(gray.shape[1] * SCALING_PERCENT / 100)
        height = int(gray.shape[0] * SCALING_PERCENT / 100)
    else:
        width = FIX_WIDTH
        height = FIX_HEIGHT

    dim = (width, height)
    resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

    # detect Aruco markers
    corners, ids, rejectedImgPoints = aruco.detectMarkers(resized, ARUCO_DICT, parameters=ARUCO_PARAMETERS)
    print('Ids: ', ids)
    print('Corners: ', corners)
    #print('imgPoints: ', rejectedImgPoints)

    # draw detected markers
    aruco.drawDetectedMarkers(resized, corners, ids)
    aruco.drawDetectedMarkers(resized, rejectedImgPoints, borderColor=(150, 150, 240))

    cv2.imwrite("result_pic.jpg", resized)
    cv2.imshow('result_img', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return ids, corners
