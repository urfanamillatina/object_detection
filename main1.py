

# pip install opencv-contrib-python # some people ask the difference between this and opencv-python
                                    # and opencv-python contains the main packages wheras the other
                                    # contains both main modules and contrib/extra modules
# pip install cvlib # for object detection

# # pip install gtts
# # pip install playsound
# use `pip3 install PyObjC` if you want playsound to run more efficiently.
#YOLO
import cv2
import cvlib as cv
import os
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound
from food_facts import food_facts

# Print cvlib model directory
print("CVLIB YOLO DIR:", os.path.expanduser("~/.cvlib/object_detection"))

# Print all yolov3.cfg files in your system
import subprocess
print("\nSearching all yolov3.cfg files:")
subprocess.call("find $HOME -name yolov3.cfg", shell=True)


def speech(text):
    print("text=> ",text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./sounds/sound.mp3")
    print("file created => ")
    playsound(r'/Users/millatina/Documents/MU/Agentic AI/Assignments/CV/object_detection/sounds/sound.mp3')


video = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = video.read()
    # Bounding box.
    # the cvlib library has learned some basic objects using object learning
    # usually it takes around 800 images for it to learn what a phone is.
    bbox, label, conf = cv.detect_common_objects(frame, model = 'yolov3')

    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Detection", output_image)

    for item in label:
        if item in labels:
            print("item in labels => ", item)
            pass
        else:
            labels.append(item)
            print("labels.append(item) => ", item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

i = 0
new_sentence = []
for label in labels:
    print("for label in labels=> ", label)
    if i == 0:
        new_sentence.append(f"I found a {label}, and, ")
    else:
        new_sentence.append(f"a {label},")

    i += 1

print("new_sentence",new_sentence)
speech(" ".join(new_sentence))
speech("Here are the food facts i found for these items:")

for label in labels:
    try:
        print("labels loop")
        print(f"\n\t{label.title()}")
        food_facts(label)

    except:
        print("No food facts for this item") 