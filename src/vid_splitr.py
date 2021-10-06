import os, sys
import math
import cv2

"""https://learnopencv.com/reading-and-writing-videos-using-opencv/"""

#input_video = '/path/to/project/video_split/input/3148_56041_1630792151_FishEye.mov'
output_dir = '/path/to/project/video_split/VideoClips/'

def video_split(input_video):
    vid_capture = cv2.VideoCapture(input_video)
    if (vid_capture.isOpened() == True):
        """
        available params instead of ints:
        https://docs.opencv.org/4.5.2/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        https://stackoverflow.com/questions/11420748/setting-camera-parameters-in-opencv-python
        """
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

    print('### opening and reading frames ###')
    while(vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        if ret == True:
            frame_pos = int(vid_capture.get(cv2.CAP_PROP_POS_FRAMES) - 1)
            frame_time_ms = vid_capture.get(cv2.CAP_PROP_POS_MSEC)
            print(f'Reading frame: {frame_pos} at the time mark: {frame_time_ms}')
            if frame_pos % (math.floor(frame_persec)*60) == 0:
                output_video = f'{output_dir}_{frame_pos}thFrame.mp4'
                print(f'Frame #:{frame_pos} | Output Dir: {output_video}')
                output = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc('X','V','I','D'), frame_persec, frame_size)
            output.write(frame)
            key = cv2.waitKey(20)
            if key == 113:
                break
        else:
            break

    vid_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        # add a usage() method with instructions
        os._exit(1)
    try:
        video_split(str(sys.argv[1]))
    except Exception as e:
        print(f'Encountered ERROR: {str(e)}')
        os._exit(1)