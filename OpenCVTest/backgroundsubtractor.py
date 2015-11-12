import cv2


def background_subtractor_mog2():
    cap = cv2.VideoCapture("My_Movie.avi")
    fgbg = cv2.createBackgroundSubtractorMOG2()

    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output_MOG2.avi', codec, 20.0, (1920, 1080))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            fgmask = fgbg.apply(frame)
            frame = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
            out.write(frame)
            cv2.imshow('Background Subtraction', fgmask)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def background_subtractor_knn():
    cap = cv2.VideoCapture("My_Movie.avi")
    fgbg = cv2.createBackgroundSubtractorKNN()

    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output_KNN.avi', codec, 20.0, (1920, 1080))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            fgmask = fgbg.apply(frame)
            frame = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
            out.write(frame)
            cv2.imshow('Background Subtraction', fgmask)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    background_subtractor_mog2()
