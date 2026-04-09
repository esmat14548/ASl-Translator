import functions_model
import cv2
import mediapipe as mp
import json
capt = cv2.VideoCapture(0)
mpHands = mp.solutions.hands # type: ignore
hands = mpHands.Hands(False)
draw = mp.solutions.drawing_utils # type: ignore
live_coordinates = []
x = 0
a = []
pp = []
parameters = []
open_parameters_file = open('parameters_file.json')
load_parameters = json.load(open_parameters_file)
for par in load_parameters["pars"]:
    parameters.append(par)
open_parameters_file.close()
while True:
    success, img = capt.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                live_coordinates.append([id, cx, cy])
            functions_model.check(parameters, live_coordinates, 200)
            live_coordinates.clear()
            draw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            cv2.imshow("image", img)
            cv2.waitKey(1)
