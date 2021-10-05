"""
HC-20211002
py file based on following doc:
https://learnopencv.com/reading-and-writing-videos-using-opencv/
"""
import os, sys
import cv2

input_video = '/Users/hcadavid/Documents/projects/video_split/input/sample-mp4-file.mp4'
output_video = '/Users/hcadavid/Documents/projects/video_split/VideoClips/temp_frame_2.mp4'

vid_capture = cv2.VideoCapture(input_video)
if (vid_capture.isOpened() == True):
    # available params instead of ints:
    # https://docs.opencv.org/4.5.2/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    # https://stackoverflow.com/questions/11420748/setting-camera-parameters-in-opencv-python
    frame_persec = vid_capture.get(cv2.CAP_PROP_FPS) # .get(5)
    frame_count  = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT) # .get(7)
    frame_width  = int(vid_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vid_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size   = (frame_width, frame_height)

    print(f"frame_persec = {frame_persec}")
    print(f"frame_count = {frame_count}")
    print(f"frame_width = {frame_width}")
    print(f"frame_height = {frame_height}")
    print(f"frame_size = {frame_size}")

    print('initiating video writer')
    output = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc('X','V','I','D'), frame_persec, frame_size)
else:
    os.__exit(1)

# pos_frame = vid_capture.get(cv2.CAP_PROP_POS_FRAMES)
# print(pos_frame)

print('opening and reading frames')
while(vid_capture.isOpened()):
    # for frameNum in range (0, frame_count-1):
    #     if frame >= frame_persec*60:
    #         pass

    # vid_capture.read() methods returns a tuple, first element is a bool
    # and the second is frame
    ret, frame = vid_capture.read()
    if ret == True:
        frame_pos = int(vid_capture.get(cv2.CAP_PROP_POS_FRAMES) - 1)
        frame_time_ms = vid_capture.get(cv2.CAP_PROP_POS_MSEC)
        print(f'reading frame: {frame_pos} at the time mark: {frame_time_ms}')
        if frame_time_ms % 6000 == 0:
            print('NEW VIDEO HERE!')
        #cv2.imshow('Frame',frame)
        #output.write(frame)
        key = cv2.waitKey(50)
        if key == 113:
            break
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()