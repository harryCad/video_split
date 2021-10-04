"""
HC-20211002
py file based on following doc:
https://learnopencv.com/reading-and-writing-videos-using-opencv/
"""
import cv2

vid_capture = cv2.VideoCapture('/Users/hcadavid/Documents/projects/video_split/temp_vid2.mov')
if (vid_capture.isOpened() == False):
    print("Error opening the video file")
else:
    print("Success")
    # available params instead of ints:
    # https://www.geeksforgeeks.org/how-to-get-properties-of-python-cv2-videocapture-object/
    frame_persec = vid_capture.get(cv2.CAP_PROP_FPS) # .get(5)
    frame_count  = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT) # .get(7)
    # frame_height = vid_capture.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)
    # frame_width  = vid_capture.get(cv2.CV_CAP_PROP_FRAME_WIDTH)

while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool
    # and the second is frame
    ret, frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Frame',frame)
        # 20 is in milliseconds, try to increase the value, say 50 and observe
        key = cv2.waitKey(1000)
        if key == 113:
            break
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()