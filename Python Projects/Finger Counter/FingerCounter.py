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
#Display JS code in a notebook for browser interaction
#Executes the java function and return a capture from the webcam 
#Splits data string into metadata and base64-encoded image.
#Decodes the base64 string into raw image data
#Converts raw bytes into a image object
#Converts image into numpy array and returns it
def capture_frame():
    display(js) 
    data = eval_js("captureImage()") 
    _, encoded = data.split(',',1)   
    image_bytes = base64.b64decode(encoded) 
    image = PIL.Image.open(io.BytesIO(image_bytes))  
    return np.array(image)  

#Function to count fingers and thumb
#Defines the landmarks of the index, middle, ring, and pink fingers
#Initlizes  a counter for raised fingers
#Retrieves the hand landmark from the hand_landmarks object
#Loop through finger tips and check if the fingertip is above the base of the finger by comparing Y coordinates
def count_fingers(hand_landmarks):
    finger_tips = [8,12,16,20] 
    fingers_up = 0 
    landmarks = hand_landmarks.landmark 

    for tip in finger_tips:
        if landmarks[tip].y < landmarks[tip - 2].y: 
            fingers_up +=1
    return fingers_up

def detect_thumb(hand_landmarks):
    landmarks = hand_landmarks.landmark
    if landmarks[4].y < landmarks[1].y:
        return 1
    return 0

#Capture and process the image from webcam and return it as NumPy array
#Converts Image from RGB to BGR format for OpenCV processing
#Resizes the image to 640x480 pixels
# Processes the resized frame to detect hand landmarks using MediaPipe.
print("Please run the code and show your hand to the camera!")
frame = capture_frame()

frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
frame_resized = cv2.resize(frame,(640,480))
results = hands.process(cv2.cvtColor(frame_resized,cv2.COLOR_RGB2BGR))

#Function to Check for Hands & Counting Fingers
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_draw.draw_landmarks(frame_resized, hand_landmarks, mp_hands.HAND_CONNECTIONS) # Draw landmarks and connections for each hand on the frame
        fingers_up = count_fingers(hand_landmarks) 
        thumb_up = detect_thumb(hand_landmarks)

        #Display finger count on the frame
        cv2.putText(frame_resized, f'Fingers: {fingers_up}', (50,100), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
        if thumb_up == 1:
            cv2.putText(frame_resized, 'Thumb 1',(50,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

            
