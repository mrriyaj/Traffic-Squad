import cv2
import dlib
import math

def estimateSpeed(location1, location2):
    d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2) + math.pow(location2[1] - location1[1], 2))
    ppm = 8.8
    d_meters = d_pixels / ppm
    fps = 60
    speed = d_meters * fps * 3.6
    return speed

def start_speed_tracking():
    carCascade = cv2.CascadeClassifier('myhaar.xml')
    video = cv2.VideoCapture('cars.mp4')

    WIDTH = 1280
    HEIGHT = 720

    carTracker = {}
    carLocation1 = {}
    carLocation2 = {}
    speed = [None] * 1000

    while True:
        rc, image = video.read()
        if type(image) == type(None):
            break

        image = cv2.resize(image, (WIDTH, HEIGHT))
        resultImage = image.copy()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cars = carCascade.detectMultiScale(gray, 1.1, 13, 18, (24, 24))

        for (_x, _y, _w, _h) in cars:
            x = int(_x)
            y = int(_y)
            w = int(_w)
            h = int(_h)

            x_bar = x + 0.5 * w
            y_bar = y + 0.5 * h

            matchCarID = None

            for carID in carTracker.keys():
                trackedPosition = carTracker[carID].get_position()

                t_x = int(trackedPosition.left())
                t_y = int(trackedPosition.top())
                t_w = int(trackedPosition.width())
                t_h = int(trackedPosition.height())

                t_x_bar = t_x + 0.5 * t_w
                t_y_bar = t_y + 0.5 * t_h

                if ((t_x <= x_bar <= (t_x + t_w)) and (t_y <= y_bar <= (t_y + t_h)) and (x <= t_x_bar <= (x + w)) and (y <= t_y_bar <= (y + h))):
                    matchCarID = carID

            if matchCarID is None:
                tracker = dlib.correlation_tracker()
                tracker.start_track(image, dlib.rectangle(x, y, x + w, y + h))

                carTracker[currentCarID] = tracker
                carLocation1[currentCarID] = [x, y, w, h]

                currentCarID = currentCarID + 1

        for carID in carTracker.keys():
            trackedPosition = carTracker[carID].get_position()

            t_x = int(trackedPosition.left())
            t_y = int(trackedPosition.top())
            t_w = int(trackedPosition.width())
            t_h = int(trackedPosition.height())

            cv2.rectangle(resultImage, (t_x, t_y), (t_x + t_w, t_y + t_h), (0, 255, 0), 4)

            carLocation2[carID] = [t_x, t_y, t_w, t_h]

        for i in carLocation1.keys():
            [x1, y1, w1, h1] = carLocation1[i]
            [x2, y2, w2, h2] = carLocation2[i]
        if [x1, y1, w1, h1] != [x2, y2, w2, h2]:
                if (speed[i] is None or speed[i] == 0) and y1 >= 275 and y1 <= 285:
                    speed[i] = estimateSpeed([x1, y1, w1, h1], [x2, y2, w2, h2])

                if speed[i] is not None and y1 >= 180:
                    cv2.putText(resultImage, str(int(speed[i])) + " km/hr", (int(x1 + w1/2), int(y1-5)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        cv2.imshow('Speed Tracking', resultImage)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

