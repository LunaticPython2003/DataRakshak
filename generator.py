import cv2
import torch
import mss
import numpy as np

def gen():
    sct = mss.mss()
    model = torch.hub.load('WongKinYiu/yolov7', 'custom', path_or_model='model/weight/best.pt')
    while True:
        sct_img = sct.grab(sct.monitors[1])
        frame = np.array(sct_img)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = model(frame_rgb)

        boxes = results.xyxy[0].numpy()

        for box in boxes:
            x1, y1, x2, y2 = box[:4].astype(int)

            frame[y1:y2, x1:x2] = cv2.GaussianBlur(frame[y1:y2, x1:x2], (51, 51), 0)

        frame_modified = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        ret, jpeg = cv2.imencode('.jpg', frame_modified)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')