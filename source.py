import cv2

face_cascade = cv2.CascadeClassifier(
    "E:/dowloads from chrome/inha/5s/DIP/Dataset/ISE4131-001-KBM/datasets/classifier/cascade.xml"
)

max_detected_width = 0
max_detected_height = 0
min_detectable_size = (30, 30)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_height, frame_width = frame.shape[:2]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=8, minSize=min_detectable_size
    )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if w > max_detected_width or h > max_detected_height:
            max_detected_width = w
            max_detected_height = h

        cv2.putText(
            frame,
            f"Min Size: {min_detectable_size[0]}x{min_detectable_size[1]}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            1,
        )

    cv2.putText(
        frame,
        f"Max Detected Size: {max_detected_width}x{max_detected_height}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2,
    )
    cv2.putText(
        frame,
        f"Frame Size: {frame_width}x{frame_height}",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Face Detection - Min/Max Size Analysis", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
