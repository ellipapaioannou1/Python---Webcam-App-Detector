import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


img = cv2.imread("news.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #turn the phot into b&w

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.05,
minNeighbors = 5)

for x, y, w, h in faces:
    img= cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0),3)


print(type(faces))
print(faces)

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
#show the image in a new window
cv2.imshow("Gray", img)  #put a name for the window
cv2.waitKey(0)
cv2.destroyAllWindows()
