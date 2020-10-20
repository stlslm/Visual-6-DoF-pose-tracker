import DoDecahedronUtils  as dodecapen
import numpy as np
from numpy import linalg as LA
import cv2
import cv2.aruco as aruco
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

import transforms3d as tf3d
import time

from scipy.optimize import minimize, leastsq,least_squares
from scipy import linalg

def main():

    data = dodecapen.txt_data()
    params = dodecapen.parameters()

    cap = cv2.VideoCapture('Calibration_files/pen_tip_calib.avi')
    j = 0
    ret = 1
    use_custom = False
    num_calib_frames = 24
    while(ret and j < num_calib_frames):
        
        ret,frame = cap.read()
        if frame is None:
            time.sleep(0.1)
            print("No image")
            continue

        if (use_custom):
            pass
            # detect markers

            # estimate pen pose
        else:
            frame_gray_draw,pose_without_opt, pose_APE,pose_DPR,visib_flag = dodecapen.find_pose(frame,params,data)

        visib_flag = 1
        if visib_flag == 1:
            print("frame number ", j)
            # cv2.imshow('frame_gray_draw',frame_gray_draw)
            cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q') & ret:    
                print ("stopped")
                break
            j+=1    

        

if __name__ == '__main__' :
    main()

