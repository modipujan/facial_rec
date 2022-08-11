import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImagesAttendance'
# Creating a list to store images
images = []
# Creating a list to store names
classNames = []
# Accessing the  file names
myList = os.listdir(path)
print(myList)

# Import images using file names
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    # Add image ot image list
    images.append(curImg)
    # Add name from file name
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


# Find encodings of all images at once
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Encoding face that we have detected
        encode = face_recognition.face_encodings(img)[0]
        print(encode)
        encodeList.append(encode)
    return encodeList


# returning just the encoding
def findOneEncodings(image):
    for img in image:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Encoding face that we have detected
        encode = face_recognition.face_encodings(img)[0]
    return encode


# Mark attendance
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


encodeListKnown = findEncodings(images)
print("Encoding Complete")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

        cv2.imshow('Webcam', img)
        cv2.waitKey(1)

# # Detecting face
# faceloc = face_recognition.face_locations(imgAs)[0]
#
# # Encding face that we have detected
# encodeAs = face_recognition.face_encodings(imgAs)[0]
#
# # To see where have detected faces (drawing rectangle on detected features)
# cv2.rectangle(imgAs, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 255), 2)
#
# # to check face is located or not
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
#
# results = face_recognition.compare_faces([encodeAs], encodeTest)
# faceDis = face_recognition.face_distance([encodeAs], encodeTest)
#
