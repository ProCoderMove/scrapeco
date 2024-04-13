import cv2 as cv
import numpy as np

def detect(frame_path):   
    # Load the YOLOv3 model
    net = cv.dnn.readNet("D:/ewaste_price_detection/Ewaste_price_prediction/yolov3.weights", "D:/ewaste_price_detection/Ewaste_price_prediction/yolov3.cfg")

    # Load class names
    with open("D:/ewaste_price_detection/Ewaste_price_prediction/coco.names", 'r') as f:
        classes = f.read().strip().split('\n')

    # Read input image
    frame = cv.imread(frame_path)

    # Prepare the frame for object detection
    blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Get detections
    layer_names = net.getUnconnectedOutLayersNames()
    detections = net.forward(layer_names)

    # Process detections
    list_outputs = []
    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # If the confidence of the detected object is above a threshold
            if confidence > 0.65:  # Adjust this threshold as needed
                list_outputs.append((class_id, confidence))

    # Select the class with the highest confidence
    if list_outputs:
        class_id, confidence = max(list_outputs, key=lambda x: x[1])
        class_name = classes[class_id]
        return class_name
    else:
        return "No object detected"  # Return a default message if no object is detected

# Test the detect function with the provided image
print(detect('D:/ewaste_price_detection/Ewaste_price_prediction/image.png'))
