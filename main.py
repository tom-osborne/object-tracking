import pafy
import cv2
from config import youtube_key

video_url = 'https://www.youtube.com/watch?v=Gr0HpDM8Ki8'

video = pafy.new(video_url)
video_best = video.getbest(preftype='mp4')

capture = cv2.VideoCapture(video_best.url)

while(capture.isOpened()):
    # Capture frame-by-frame
    ret, frame = capture.read()
    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame',frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break
    
# When everything done, release the video capture object
capture.release()
    
# Closes all the frames
cv2.destroyAllWindows()

