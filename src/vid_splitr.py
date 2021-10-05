"""
HC-20211002
py file based on following doc:
https://learnopencv.com/reading-and-writing-videos-using-opencv/
"""
import cv2

def vid_splitr(video_path):
    vid_capture = cv2.VideoCapture('/Users/hcadavid/Documents/projects/video_split/input/temp_vid2.mov')
    while(vid_capture.isOpened()):
        # available params instead of ints:
        # https://docs.opencv.org/4.5.2/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
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

        output = cv2.VideoWriter(f'/Users/hcadavid/Documents/projects/video_split/VideoClips/temp_frame.mp4'
                                , cv2.VideoWriter_fourcc('X','V','I','D'), frame_persec, frame_size)

        #for fr in range(0, int(frame_count) - 1):
        # vid_capture.read() methods returns a tuple, first element is a bool
        # and the second is frame
        ret, frame = vid_capture.read()
        if ret == True:
            print('reading frame:', frame)
            #cv2.imshow('Frame',frame)

            output.write(frame)
            # 20 is in milliseconds, try to increase the value, say 50 and observe
            # key = cv2.waitKey(1000)
            # if key == 113:
            #     break
        else:
            break

    vid_capture.release()
    cv2.destroyAllWindows()
    return