from google.colab.output import eval_js
from IPython.display import display, Javascript
import cv2
import numpy as np
import PIL.Image
import io
import base64
from google.colab.patches import cv2_imshow
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

#Initialize Mediapipe Hand Detector

#create Hand Model
mp_hands = mp.solutions.hands #solutions.hands loads hand tracking model
mp_draw = mp.solutions.drawing_utils #Visualize hand landmarks
hands = mp_hands.Hands(static_image_mode = True, max_num_hands = 2, min_detection_confidence = 0.3) #Loads the hand model, image mode treats image as static, 
                                                                                                    #low detection confidence threashold

#Capture Image from Webcam, convert to Base 64 encoded JPEG using javascript
js = Javascript('''
    async function captureImage(){
            const video = document.createElement('video'); 
            const stream = await navigator.mediaDevices.getUserMedia({video: true}); 
            video.srcObject = stream;
            await new Promise((resolve) => video.onloadedmetadata = resolve);
            video.play();
            
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video,0,0);
            
            stream.getTracks().forEach(track => track.stop());
            video.remove();
                
            return canvas.toDataURL('image/jpeg');
        }
''')

#Convert image into a NumPy array.
def capture_frame():
    display(js) # Display JS code in a notebook for browser interaction
    data = eval_js("captureImage()") #Executes the java function and return a capture from the webcam 
    _, encoded = data.split(',',1)   # Splits data string into metadata and base64-encoded image.
    image_bytes = base64.b64decode(encoded) # Decodes the base64 string into raw image data
    image = PIL.Image.open(io.BytesIO(image_bytes))  # Converts raw bytes into a image object
    return np.array(image)  #Converts image into numpy array and returns it

#Function to count fingers and thumb
def count_fingers(hand_landmarks):
    finger_tips = [8,12,16,20] #Defines the landmarks of the index, middle, ring, and pink fingers
    fingers_up = 0 # Initlizes  a counter for raised fingers
    landmarks = hand_landmarks.landmark #Retrieves the hand landmark from the hand_landmarks object

            
