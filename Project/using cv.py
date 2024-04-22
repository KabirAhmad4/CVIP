
import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
import easyocr

# Load EasyOCR model for better OCR accuracy
reader = easyocr.Reader(['en'])

# Load video
cap = cv2.VideoCapture('video.mp4')


while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter to reduce noise while preserving edges
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # Apply thresholding to get binary image
    edged = cv2.Canny(gray, 30, 200)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)

        # If contour has 4 vertices, it could be a license plate
        if len(approx) == 4:
            license_plate = cv2.boundingRect(approx)
            x, y, w, h = license_plate

            # Extract license plate region
            license_plate_img = gray[y:y + h, x:x + w]

            # Use EasyOCR to perform OCR on license plate region
            results = reader.readtext(license_plate_img, detail=0)

            if results:
                plate_number = results[0]
                print("License Plate Number:", plate_number)

                # Draw bounding box around license plate and annotate plate number
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, plate_number, (x - 50, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                break

    cv2_imshow(frame)  # Display frame

    # Wait for a short duration and check for key press
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
