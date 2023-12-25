import cv2


                             
def cv_video_images():
    vidcap = cv2.VideoCapture('./static/upload/alprVideo.mp4')
    success,image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite("./static/tmp/frame%d.jpg" % count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1