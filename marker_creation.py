import cv2
import cv2.aruco as aruco

def marker_creation(codeId):
    ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_4X4_100)
    RESULT_FILE_NAME = "marker%s.jpg" %codeId
    img = aruco.drawMarker(ARUCO_DICT, codeId, 700)
    cv2.imwrite(RESULT_FILE_NAME, img)
