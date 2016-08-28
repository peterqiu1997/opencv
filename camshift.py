import numpy as np 
import cv2
import argparse

# initialize frame, selected roi (4 points), and whether or not inputMode
frame = None
roiPts = []
inputMode = False

def selectROI(event, x, y, flags, params): # all mouse event functions need these 5 params
	global frame, roiPts, inputMode

	if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4:
		roiPts.append((x,y))
		cv2.circle(frame, (x,y), 4, (0, 255, 0), 2)
		cv2.imshow("frame", frame)

def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("-v", "--video", help = "path to the optional video file", action = "store_true")
	args = vars(ap.parse_args())

	global frame, roiPts, inputMode

	# input video path later

	camera = cv2.VideoCapture(0)

	cv2.namedWindow("frame")
	cv2.setMouseCallback("frame", selectROI)

	termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
	roiBox = None

	while(1):
		grabbed, frame = camera.read()
		frame = cv2.flip(frame, 180)

		if roiBox is not None:
			# convert to HSV, do meanshift
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)

			#apply camshift 
			(r, roiBox) = cv2.CamShift(backProj, roiBox, termination)
			pts = np.int0(cv2.boxPoints(r))
			cv2.polylines(frame, [pts], True, (0,255,0), 2)

		cv2.imshow("frame", frame)
		key = cv2.waitKey(1) & 0xFF

		if key == ord("i") and len(roiPts) < 4:

			inputMode = True
			orig = frame.copy()
			# keep looping until 4 reference ROI points have
			# been selected; press any key to exit ROI selction
			# mode once 4 points have been selected
			while len(roiPts) < 4:
				cv2.imshow("frame", frame)
				cv2.waitKey(0)

			# determine the top-left and bottom-right points
			roiPts = np.array(roiPts)
			s = roiPts.sum(axis = 1)
			tl = roiPts[np.argmin(s)]
			br = roiPts[np.argmax(s)]

			print("Top left: " + str(tl) + ", " + "Bottom right: " + str(br))

			# grab the ROI for the bounding box and convert it
			# to the HSV color space
			# roi = orig[tl[0]:br[0], tl[1]:br[1]] # ROI selects y, then x (y,x) so this is not right 
			roi = orig[tl[1]:br[1], tl[0]:br[0]] # but this is 
			roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
			#roi = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)

			# compute a HSV histogram for the ROI and store the
			# bounding box
			roiHist = cv2.calcHist([roi], [0], None, [16], [0, 180])
			roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
			roiBox = (tl[0], tl[1], br[0], br[1])

		# if the 'q' key is pressed, stop the loop
		elif key == ord("q"):
			break

	# cleanup the camera and close any open windows
	camera.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()



















