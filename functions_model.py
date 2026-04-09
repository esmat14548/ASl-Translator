def save_sign(sign_name, num_of_shots):
    import json
    import cv2
    import mediapipe as mp
    import math
    capt = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands # type: ignore
    hands = mp_hands.Hands(False, 2, 1)
    draw = mp.solutions.drawing_utils # type: ignore
    coordinates = []
    rounded_parameters = []
    n = 0
    while n < num_of_shots:
        success, img = capt.read()
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    coordinates.append([id, cx, cy])
                draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
                cv2.imshow("image", img)
                cv2.waitKey(1)
                cv2.waitKey(200)
                parameters = [
                    coordinates[0][2] - coordinates[4][2],
                    coordinates[0][2] - coordinates[8][2],
                    coordinates[0][2] - coordinates[12][2],
                    coordinates[0][2] - coordinates[16][2],
                    coordinates[0][2] - coordinates[20][2],
                    coordinates[6][1] - coordinates[15][1],
                    coordinates[19][1] - coordinates[12][1],
                    coordinates[15][2] - coordinates[8][2],
                    coordinates[17][1] - coordinates[1][1],
                    coordinates[17][2] - coordinates[1][2],
                    coordinates[4][1] - coordinates[20][1],
                    coordinates[4][2] - coordinates[20][2],
                    coordinates[15][1] - coordinates[7][1],
                    coordinates[13][2] - coordinates[8][2],
                    coordinates[16][1] - coordinates[3][1],
                    coordinates[17][1] - coordinates[5][1],
                    coordinates[19][1] - coordinates[7][1],
                    coordinates[1][1] - coordinates[0][1],
                    coordinates[5][1] - coordinates[0][1],
                    coordinates[17][1] - coordinates[0][1]
                ]
                mag = math.sqrt((parameters[8] ** 2) + (parameters[9] ** 2))
                for parameter in parameters:
                    rounded_parameters.append(int(abs(round(parameter/mag, 3)) * 1000))
                rounded_parameters.append(sign_name)
                print(rounded_parameters)
                dump_parameters = json.dumps(rounded_parameters)
                open_parameters_file = open("parameters_file.json", "a")
                open_parameters_file.write(dump_parameters)
                open_parameters_file.write(",\n")
                open_parameters_file.close()
                coordinates.append(sign_name)
                dump_coordinates = json.dumps(coordinates)
                open_coordinates_file = open("coordinates_file.json", "a")
                open_coordinates_file.write(dump_coordinates)
                open_coordinates_file.write(",\n")
                open_coordinates_file.close()
                rounded_parameters = []
                coordinates = []
            n = n + 1


def check(parameters, coordinates, p_range):
    import os
    import math
    import json
    t = 0
    s = 0
    rounded_parameters = []
    live_parameters = [
        coordinates[0][2] - coordinates[4][2],
        coordinates[0][2] - coordinates[8][2],
        coordinates[0][2] - coordinates[12][2],
        coordinates[0][2] - coordinates[16][2],
        coordinates[0][2] - coordinates[20][2],
        coordinates[6][1] - coordinates[15][1],
        coordinates[19][1] - coordinates[12][1],
        coordinates[15][2] - coordinates[8][2],
        coordinates[17][1] - coordinates[1][1],
        coordinates[17][2] - coordinates[1][2],
        coordinates[4][1] - coordinates[20][1],
        coordinates[4][2] - coordinates[20][2],
        coordinates[15][1] - coordinates[7][1],
        coordinates[13][2] - coordinates[8][2],
        coordinates[16][1] - coordinates[3][1],
        coordinates[17][1] - coordinates[5][1],
        coordinates[19][1] - coordinates[7][1],
        coordinates[1][1] - coordinates[0][1],
        coordinates[5][1] - coordinates[0][1],
        coordinates[17][1] - coordinates[0][1]
    ]
    mag = math.sqrt((live_parameters[8] * live_parameters[8]) + (live_parameters[9] * live_parameters[9]))
    for parameter in live_parameters:
        rounded_parameters.append(abs(round(parameter/mag, 3) * 1000))
    while t < len(rounded_parameters) and s < len(parameters):
        point = parameters[s][t]
        if point + p_range >= rounded_parameters[t] >= point - p_range:
            t = t + 1
        else:
            t = 0
            s = s + 1
    with open("previous_sign_name.json", "r") as f:
        data = json.load(f)
    name = data["name"]
    if t == len(rounded_parameters) and parameters[s][len(rounded_parameters)] != name:
        name = {"name": parameters[s][len(rounded_parameters)]}
        with open("previous_sign_name.json", "w") as ff:
            json.dump(name, ff, indent=4)
        sign = name['name']
        print(sign, end="\n\n")
        os.system(f"sounds\{sign}.mp3") # type: ignore

def binary_check(parameters, coordinates, p_range):
    import os
    import math
    import json
    t = 0
    s = 0
    rounded_parameters = []
    live_parameters = [
        coordinates[0][2] - coordinates[4][2],
        coordinates[0][2] - coordinates[8][2],
        coordinates[0][2] - coordinates[12][2],
        coordinates[0][2] - coordinates[16][2],
        coordinates[0][2] - coordinates[20][2],
        coordinates[6][1] - coordinates[15][1],
        coordinates[19][1] - coordinates[12][1],
        coordinates[15][2] - coordinates[8][2],
        coordinates[17][1] - coordinates[1][1],
        coordinates[17][2] - coordinates[1][2],
        coordinates[4][1] - coordinates[20][1],
        coordinates[4][2] - coordinates[20][2],
        coordinates[15][1] - coordinates[7][1],
        coordinates[13][2] - coordinates[8][2],
        coordinates[16][1] - coordinates[3][1],
        coordinates[17][1] - coordinates[5][1],
        coordinates[19][1] - coordinates[7][1],
        coordinates[1][1] - coordinates[0][1],
        coordinates[5][1] - coordinates[0][1],
        coordinates[17][1] - coordinates[0][1]
    ]
    mag = math.sqrt((live_parameters[8] * live_parameters[8]) + (live_parameters[9] * live_parameters[9]))
    for parameter in live_parameters:
        rounded_parameters.append(abs(round(parameter/mag, 3) * 1000))
    while t < len(rounded_parameters) and s < len(parameters):
        point = parameters[s][t]
        if point + p_range >= rounded_parameters[t] >= point - p_range:
            t = t + 1
        else:
            t = 0
            s = s + 1
    
    with open("previous_sign_name.json", "r") as f:
        data = json.load(f)
    name = data["name"]
    if t == len(rounded_parameters) and parameters[s][len(rounded_parameters)] != name:
        name = {"name": parameters[s][len(rounded_parameters)]}
        with open("previous_sign_name.json", "w") as ff:
            json.dump(name, ff, indent=4)
        sign = name['name']
        print(sign, end="\n\n")
        os.system(f"sounds\{sign}.mp3") # type: ignore