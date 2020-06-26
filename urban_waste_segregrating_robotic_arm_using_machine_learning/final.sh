raspistill -w 720 -h 640 -n -t 100 -q 10 -e jpg -th none -o image1.jpg
sleep 3
python pubb.py