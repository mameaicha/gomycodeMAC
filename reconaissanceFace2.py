# Step 1: Import the required libraries
import cv2
import streamlit as st
from io import BytesIO
from PIL import Image

# Step 2: Load the face cascade classifier: pre-trained Viola-Jones face detection model
face_cascade = cv2.CascadeClassifier('C:/Users/user/Documents/GOMYCODE/detection faciale/haarcascade_frontalface_default.xml')

def detect_faces(image, scaleFactor, minNeighbors, rectangle_color):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), rectangle_color, 2)
    
    return image

def main():
    #st.title("Face Detection App")
    st.title("Face Detection using Viola-Jones Algorithm")
    st.write("The application captures frames from the webcam and uses the Viola-Jones algorithm to detect faces in the frames.It then draws rectangles around the detected faces and displays the frames in a window.")
    # Add instructions to the Streamlit app interface to guide the user on how to use the app.
    instructions = """
    **Instructions:**
    
    1. Use the sliders to adjust the parameters.
    2. Pick a rectangle color using the color picker.
    3. Click the 'Detect Faces' button to see the results.
    """
    st.sidebar.markdown(instructions)
    
    #st.markdown(" 1. Press the button below to start detecting faces from your webcam")
    #st.markdown(" 2. presses the 'q' key  to exits and releases the webcam and all windows")
    st.sidebar.header("Settings")
    
    
    scaleFactor = st.sidebar.slider("Scale Factor", 1.01, 2.0, 1.1)
    minNeighbors = st.sidebar.slider("Min Neighbors", 1, 10, 3)
    rectangle_color = st.sidebar.color_picker("Rectangle Color", "#00FF00")
    #rectangle_color = st.sidebar.color_picker("Choose rectangle color", "#FF0000")
        
    detect_button = st.sidebar.button("Detect Faces")
    if detect_button:
        # Initialize the webcam
        cap = cv2.VideoCapture(0)
        #while True:
        #    # Read the frames from the webcam
        #    ret, image = cap.read()
        #    result_image = detect_faces(image, scaleFactor, minNeighbors, rectangle_color)
        #    st.image(result_image, channels="BGR", caption="Detected Faces")
            
        #Display the frames
        #    cv2.imshow('Face Detection using Viola-Jones Algorithm', image)
        #    # Exit the loop when 'q' is pressed
        #    if cv2.waitKey(1) & 0xFF == ord('q'):
        #        break
            
        # Release the webcam and close all windows
        #cap.release()
        #cv2.destroyAllWindows()
        #save_button = st.sidebar.button("Save Image with Detected Faces")
        #if save_button:
        #        cv2.imwrite("detected_faces.jpg", result_image)
        #        st.sidebar.success("Image saved as 'detected_faces.jpg'")
         
        # Read the frames from the webcam
        ret, image = cap.read()    
        result_image = detect_faces(image, scaleFactor, minNeighbors, rectangle_color)
        st.image(result_image, channels="BGR", caption="Detected Faces")
            
        #Display the frames
        cv2.imshow('Face Detection using Viola-Jones Algorithm', image)
            
        # Release the webcam and close all windows
        cap.release()
        cv2.destroyAllWindows()
        
        save_button = st.sidebar.button("Save Image with Detected Faces")
        if save_button:
            cv2.imwrite("detected_faces.jpg", result_image)
            st.sidebar.success("Image saved as 'detected_faces.jpg'")   
if __name__ == "__main__":
    main()       
    
    