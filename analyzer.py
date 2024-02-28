import cv2
import face_recognition

# Load the known faces and their names
known_face_names = ["Person1", "Person2", "Person3"]
known_face_images = [face_recognition.load_image_file("person1.jpg"),
                     face_recognition.load_image_file("person2.jpg"),
                     face_recognition.load_image_file("person3.jpg")]

# Encode the known faces
known_face_encodings = [face_recognition.face_encodings(image)[0] for image in known_face_images]

video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2RGB)

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(col)
    face_encodings = face_recognition.face_encodings(col, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face encoding of the detected face with the known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Check if any face matches with the known faces
        for i in range(len(matches)):
            if matches[i]:
                name = known_face_names[i]
                break

        # Draw a rectangle and display the name of the face
        cv2.rectangle(video_data, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(video_data, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("video_live", video_data)

    if cv2.waitKey(10) == ord("z"):
        break

video_cap.release()
cv2.destroyAllWindows()
