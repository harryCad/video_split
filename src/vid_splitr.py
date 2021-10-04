"""
HC-20211002
py file based on following doc:
https://learnopencv.com/reading-and-writing-videos-using-opencv/
"""
import cv2

vid_capture = cv2.VideoCapture('/Users/hcadavid/Documents/projects/video_split/input/temp_vid2.mov')
if (vid_capture.isOpened() == False):
    print("Error opening the video file")
else:
    print("Success")
    # available params instead of ints:
    # https://docs.opencv.org/4.5.2/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    frame_persec = vid_capture.get(cv2.CAP_PROP_FPS) # .get(5)
    frame_count  = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT) # .get(7)
    frame_width  = int(vid_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vid_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size   = (frame_width, frame_height)

print('initiating video writer')
#output = cv2.VideoWriter('Resources/output_video_from_file.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, frame_size)
output = cv2.VideoWriter('/Users/hcadavid/Documents/projects/video_split/output/temp_frame.mp4'
                        , cv2.VideoWriter_fourcc('X','V','I','D'), frame_persec, frame_size)

print('opening and reading frames')
while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool
    # and the second is frame
    ret, frame = vid_capture.read()
    if ret == True:
        print('reading frame:', frame)
        #cv2.imshow('Frame',frame)
        output.write(frame)
        # 20 is in milliseconds, try to increase the value, say 50 and observe
        key = cv2.waitKey(1000)
        if key == 113:
            break
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()