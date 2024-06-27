import cv2
import face_recognition
import pickle

# dataset_paths = ['dataset/son/', 'dataset/tedy/']
# names = ['Son', 'Tedy']
dataset_paths = ['dataset/ji/']
names = ['Ji']
number_images = 3
image_type = '.jpg'
encoding_file = 'test_encodings.pickle'
model_method = 'hog'

knownEncodings = []
knownNames = []

for (i, dataset_path) in enumerate(dataset_paths):
    name = names[i]

    for idx in range(number_images):
        file_name = dataset_path + str(idx+1) + image_type

        image = cv2.imread(file_name)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb, model=model_method)

        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)
        
data = {"encodings": knownEncodings, "names": knownNames}
f = open(encoding_file, "wb")
f.write(pickle.dumps(data))
f.close()
