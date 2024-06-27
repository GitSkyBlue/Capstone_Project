import cv2
import face_recognition
import pickle
import datetime

encoding_file = 'test_encodings.pickle'
unknown_name = 'Unknown'
model_method = 'hog'

cap = cv2.VideoCapture(1)
def getScreen():
    ret, frame = cap.read()

    return frame

def detectAndDisplay(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model=model_method)
    encodings = face_recognition.face_encodings(rgb, boxes)
    rgb = cv2.medianBlur(rgb, 3)

    names = []
    datas = []
    bye = []
 
    for encoding in encodings:
        data = pickle.loads(open(encoding_file, "rb").read())
        matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=0.35)
        name = unknown_name

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            name = max(counts, key=counts.get)

            datas.append(name)

            dt = datetime.datetime.now()
            if len(str(dt.month)) == 1:
                mon = "0"+str(dt.month)
            else:
                mon = str(dt.month)
            if len(str(dt.day)) == 1:
                day = "0"+str(dt.day)
            else:
                day = str(dt.day)
            if len(str(dt.hour)) == 1:
                hour = "0"+str(dt.hour)
            else:
                hour = str(dt.hour)
            if len(str(dt.minute)) == 1:
                mins = "0"+str(dt.minute)
            else:
                mins = str(dt.minute)
            datas.append(str(dt.year) + mon + day + hour + mins)
        
        names.append(name)

    for ((top, right, bottom, left), name) in zip(boxes, names):
        y = top - 15 if top - 15 > 15 else top + 15
        color = (0, 255, 0)
        line = 2
        if(name == unknown_name):
            color = (0, 0, 255)
            line = 2
            name = 'Unknown'
            
        cv2.rectangle(image, (left, top), (right, bottom), color, line)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(image, name, (left, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, line)       

    cv2.imwrite('img.png',image)
    
    for i in range(0, len(datas), 2):
        d = {}
        d["name"] = datas[i]
        d["time"] = datas[i + 1]
        bye.append(d)
        return d

    if len(bye) > 1:
        return bye[0]
    else:
        return bye
    
scr = getScreen()
detectAndDisplay(scr)

cv2.waitKey(0)
cv2.destroyAllWindows()
