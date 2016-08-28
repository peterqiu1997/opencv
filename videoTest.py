import numpy as np
import cv2

cap = cv2.VideoCapture(0)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(str(w) + ", " + str(h))
# Define the codec and create VideoWriter object
# -----fourcc = cv2.VideoWriter_fourcc(*'XVID') # Videowriter_fourcc does not exist?!?!
# fourcc = cv2.cv.CV_FOURCC(*'XVID') 
out = cv2.VideoWriter('output.avi', -1, 20.0, (1280,720))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:# boolean signifying a frame was captured
        frame = cv2.flip(frame, 180)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()



"""while(True):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
"""