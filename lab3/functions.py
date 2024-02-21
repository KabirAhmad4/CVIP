import cv2
import time

from datetime import datetime
from random import randint



def capture_video(duration):
    cap = cv2.VideoCapture(0)  # Open the webcam
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for saving the video


    video_filename = f"captured_video_{2}.avi"
    out = cv2.VideoWriter(video_filename, fourcc, 20.0, (640, 480))  # Video writer object

    start_time = cv2.getTickCount()  # Get the initial time

    while(cap.isOpened()):
        ret, frame = cap.read()  # Read frame from the webcam
        if ret==True:
            out.write(frame)  # Write the frame to the video file

            # Display the frame
            cv2.imshow('frame',frame)

            # Check if 10 seconds have elapsed
            if (cv2.getTickCount() - start_time) / cv2.getTickFrequency() > duration:
                break

            # Exit when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()  # Release the webcam
    out.release()  # Release the video writer
    cv2.destroyAllWindows()  # Close all OpenCV windows
    return video_filename
    
# Duration of the video to be captured (in seconds)
print(capture_video(5))
