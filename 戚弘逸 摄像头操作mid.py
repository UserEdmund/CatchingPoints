"""
This is a game based on mediapipe and gesture recognition

There will be 5 points on the screen and you will have to "catch" the points on the screen

Place your hand over the blue points on the screen so that the blue point you want to capture is in the yellow box and close all your fingers to form a fist

The points will disappear as you "catch" them and if the points all disappears the game will exit and you win!!!

"""




import cv2
import mediapipe as mp
import numpy as np
import random

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
points2catch = np.zeros((0, 2), dtype=np.int32) #initialize the positions of the points to be catched

numpoint = 5 #number of points

for i in range(0,numpoint):
    points2catch = np.append(points2catch, [[random.randint(50, 280), random.randint(50, 340)]], axis=0) #set point randomly
    print(points2catch[i])

print(points2catch)

while cap.isOpened():
    result, image = cap.read()
    #print(image.shape)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    
    
    for i in range(0, int(points2catch.size/2)):
        cv2.circle(image,points2catch[i],5,(0,245,255),-1) #draw points to catch

    h, w, c = image.shape
    lst_lms = np.zeros((0, 2), dtype=np.int32)  # Initialize as empty 2D array

    # 将所有手势坐标点，加到一个列表当中 [(x1,y1),(x2,y2),....]总计21个
    if results.multi_hand_landmarks:
        for single_hand_marks in results.multi_hand_landmarks:
            for id, lm in enumerate(single_hand_marks.landmark):
                x, y = int(w * lm.x), int(h * lm.y)
                cv2.circle(image, (x, y), 2, (255, 1, 0), -1)
                lst_lms = np.append(lst_lms, [[x, y]], axis=0)  # Append [x, y] as a row

        hull_index = [0, 1, 2, 3, 6, 10, 14, 18, 17]  # 取出来目标的9个点，
        if len(lst_lms) > 0:  # Check if lst_lms is not empty
            hull = cv2.convexHull(lst_lms[hull_index])  # 将九个点连成一个闭环

            cv2.polylines(image, [hull], True, (222, 222, 0), 2)  # 画出来这个闭环

            up_finger = []  # 这是闭环外的列表

            for i in [4, 8, 12, 16, 20]:  # 轮训这五个指尖点，看看哪些指尖点是在上面的闭环外
                point = (int(lst_lms[i][0]), int(lst_lms[i][1]))
                dist = cv2.pointPolygonTest(hull, point, True)  # 计算点到轮廓的距离，小于0说明在轮廓外面。
                print(dist)
                if dist < 0:
                    up_finger.append(i)
            print(up_finger)

            for i in range(numpoint):
                if i < points2catch.shape[0]:
                    pint = (int(points2catch[i][0]), int(points2catch[i][1]))
                    print(pint)
                    dist = cv2.pointPolygonTest(hull, pint, True)
                    if dist >= 0 and len(up_finger) < 2:
                        points2catch = np.delete(points2catch, i, 0)
                        numpoint -= 1



            """if len(up_finger) == 1 and up_finger[0] == 8:  # 如果在闭环外面的点只有一个，且这个手是8号点
                gesture = 'one'
            elif len(up_finger) == 2 and up_finger[0] == 8 and up_finger[1] == 12:
                gesture = "two"
            elif len(up_finger) == 1 and up_finger[0] == 12:
                gesture = "middle finger"
            else:
                gesture = 'None'
            if gesture:
                cv2.putText(image, gesture, (30,30), cv2.FONT_HERSHEY_COMPLEX, 1, (222,21,122), 1)
            """

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow("camera", image)  # 显示该图像

    if cv2.waitKey(20) & 0xFF == ord(' '):
        break
    if points2catch.size == 0:
        break


hands.close()
cv2.destroyAllWindows()
cap.release()
