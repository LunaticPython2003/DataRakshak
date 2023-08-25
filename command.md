# Data Rakshak Commands

- Trained the Dataset with YOLOv7.pt weight file <bt>
`python train.py --img-size 640 --batch-size 6 --epochs 50 --data data.yaml --weights yolov7.pt`

- Generated the custom weight file

- Used the weight file to detect the object and blur the images using Gaussian Blur