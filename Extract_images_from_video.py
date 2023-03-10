# Importing all necessary libraries
import cv2
import os
  
# Read the video from specified path
cam = cv2.VideoCapture("/home/aureliencd/Téléchargements/Empi_HR.mp4")
  
os.makedirs('/home/aureliencd/Téléchargements/Images_HR')

savefolder = '/home/aureliencd/Téléchargements/Images_HR'

# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = str(savefolder) + '/frame' + str(currentframe) + '.png'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()





# Read the video from specified path
cam = cv2.VideoCapture("/home/aureliencd/Téléchargements/Empi_LR_buil.mp4")
  
os.makedirs('/home/aureliencd/Téléchargements/Images_LR_buil')

savefolder = '/home/aureliencd/Téléchargements/Images_LR_buil'

# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = str(savefolder) + '/frame' + str(currentframe) + '.png'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()