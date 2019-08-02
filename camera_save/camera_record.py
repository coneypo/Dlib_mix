import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('F', 'L', 'V', '1')
# fourcc = cv2.VideoWriter_fourcc('m', 'p', 'e', 'g')
# fourcc = cv2.VideoWriter_fourcc(*'mpeg')
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

fps = cap.get(cv2.CAP_PROP_FPS)

print(fps)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# out = cv2.VideoWriter('camera_test.avi', fourcc,10.0, size)
out = cv2.VideoWriter('acrn_test.flv', fourcc, 30.0, size, True)
while True:
    ret, frame = cap.read()
    # frame = cv2.flip(frame, 1)
    out.write(frame)
    cv2.putText(frame,
                "Press Q to save and quit",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0, 255, 0), 2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
