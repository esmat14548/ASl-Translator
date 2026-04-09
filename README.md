# Sign to See — English Sign Language Translator

A real-time assistive technology system that translates American sign language
into spoken words using a webcam, OpenCV, and Google Text-to-Speech.

Built as a STEM capstone project at Red Sea STEM School, Egypt — 2023/2024.

-------------------

## Project Overview

Egypt has approximately 7.5 million mute individuals. This project addresses
their social isolation by building a sign language recognition system that
captures hand signs via a laptop webcam, classifies them using a machine
learning model, converts the result to text, and outputs spoken audio through
the laptop speakers.

-------------------

## How It Works

1. The laptop webcam captures live hand gestures in real time
2. OpenCV detects 21 hand landmark coordinates using a trained ML model
3. Custom parameters are calculated from landmark distances to classify signs,
independent of hand orientation and distance from the camera
4. A magnification ratio formula (M = h'/h = q/p) normalises for depth,
reducing distance-based error from \~58% to \~2%
5. The classified sign is converted to text
6. gTTS (Google Text-to-Speech) converts the text to audio
7. Audio plays directly through the laptop speakers

-------------------

## Key Technical Challenges Solved

**Challenge 1 — Depth / Distance Normalisation**
OpenCV does not provide depth (3D) information. Instead of using an
ultrasonic sensor (which increases cost and power consumption), a
magnification ratio was calculated using the Pythagorean distance between
landmark points 1 and 17 — the most geometrically stable pair — reducing
the distance-based error from \~58% to \~2%.

**Challenge 2 — Similar Sign Differentiation**
Some Arabic signs differ only slightly in thumb coordinate position.
This was solved by increasing the number of random classification parameters
to 20, which improved differentiation between visually similar signs.

**Challenge 3 — Accuracy vs Speed Trade-off**
Accuracy was tested across 6 speed intervals (27–117 signs/minute).
Correlation coefficient: **r = −0.91584**
Regression equation: **ŷ = −11.06x + 110.55**
At a 75% acceptable accuracy threshold → maximum speed ≈ **75.1 signs/minute**

-------------------

## Requirements

**Hardware:**

* Any laptop with a built-in or external webcam

**Software \& Libraries:**

* Python 3.x
* OpenCV
* gTTS (Google Text-to-Speech)
* JSON

-------------------
## How to Run

1. Clone this repository:

```
   git clone https://github.com/YOUR-USERNAME/sign-to-see.git
   cd sign-to-see
   ```

2. Install dependencies:

```
   pip install -r requirements.txt
   ```

3. Train the model on your hand sign dataset:

```
   python trainingCode.py
   ```

4. Run the main program:

```
   python main.py
   ```

5. Show hand signs in front of your webcam, the system will speak the
recognised sign aloud.



-------------------

## Future Improvements

* Integrate with **ESP32-CAM** to make the system fully wearable and
embedded into smart glasses (hardware prototype already designed)
* Replace ESP32 with **Raspberry Pi** for faster processing and higher accuracy
* Use a **60fps camera** for better performance with fast hand movements
* Expand the parameter set beyond 20 for improved sign differentiation
* Extend functionality to assist **blind individuals** via environment detection


