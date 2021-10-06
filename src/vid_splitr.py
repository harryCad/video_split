import os, sys
import math
import cv2

"""https://learnopencv.com/reading-and-writing-videos-using-opencv/"""
input_video = '/Users/hcadavid/Documents/projects/video_split/input/3148_56041_1630792151_FishEye.mov' #sample-mp4-file.mp4'
output_video = '/Users/hcadavid/Documents/projects/video_split/VideoClips/_frame.mp4'

vid_capture = cv2.VideoCapture(input_video)
if (vid_capture.isOpened() == True):
    # available params instead of ints:
    # https://docs.opencv.org/4.5.2/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    # https://stackoverflow.com/questions/11420748/setting-camera-parameters-in-opencv-python
    frame_persec = vid_capture.get(cv2.CAP_PROP_FPS) # .get(5)
    frame_count  = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT) # .get(7) 23116
    frame_width  = int(vid_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vid_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size   = (frame_width, frame_height)

    print(f"frame_persec = {frame_persec}")
    print(f"frame_count  = {frame_count}")
    print(f"frame_width  = {frame_width}")
    print(f"frame_height = {frame_height}")
    print(f"frame_size   = {frame_size}")
else:
    os.__exit(1)

# print('###initiating video writer###')
#output = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc('X','V','I','D'), frame_persec, frame_size)

print('###opening and reading frames###')
while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool
    # and the second is frame
    ret, frame = vid_capture.read()
    if ret == True:
        frame_pos = int(vid_capture.get(cv2.CAP_PROP_POS_FRAMES) - 1)
        frame_time_ms = vid_capture.get(cv2.CAP_PROP_POS_MSEC)
        print(f'reading frame: {frame_pos} at the time mark: {frame_time_ms}')
        #if frame_time_ms % 60000 == 0:
        """
        changed behavior from video time to frames per second due to following data never hitting 60,000:
        reading frame: 1799 at the time mark: 59986.66666666667
        reading frame: 1800 at the time mark: 60020.0
        """
        if frame_pos % (math.floor(frame_persec)*60) == 0:
            #print(f'reading frame: {frame_pos} at the time mark: {frame_time_ms}')
            print(frame_pos)
            output_video = f'/Users/hcadavid/Documents/projects/video_split/VideoClips/_{frame_pos}thFrame.mp4'
            print(output_video)
            output = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc('X','V','I','D'), frame_persec, frame_size)
        output.write(frame)
        key = cv2.waitKey(20)
        if key == 113:
            break
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()